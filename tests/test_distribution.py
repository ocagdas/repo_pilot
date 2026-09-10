"""Installation semantics: build actual packages in disposable environments."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]


class DistributionTests(unittest.TestCase):
    def test_setup_profiles_preview_and_aliases(self):
        for mode in ('native', 'venv', 'conda'):
            for install_mode in ('static', 'editable'):
                output = subprocess.check_output([sys.executable, str(ROOT/'setup_tooling.py'),
                    '--mode', mode, '--'+install_mode, '--extras', 'sourcegraph'], text=True, encoding='utf-8')
                plan = json.loads(output)
                command = plan['commands'][-1]
                self.assertEqual('--editable' in command, install_mode == 'editable')
                self.assertTrue(command[-1].endswith('[sourcegraph]'))
                self.assertEqual(plan['extras'], 'sourcegraph')
                self.assertFalse(plan['apply'])
        default = json.loads(subprocess.check_output([sys.executable, str(ROOT/'setup_tooling.py')], text=True, encoding='utf-8'))
        self.assertEqual((default['extras'], default['install_mode']), ('minimal', 'static'))

    def test_dependency_profiles_and_version_match_distribution(self):
        data = tomllib.loads((ROOT/'pyproject.toml').read_text(encoding='utf-8'))['project']
        self.assertEqual(data['version'], json.loads((ROOT/'upstream.lock.json').read_text(encoding='utf-8'))['package_version'])
        self.assertEqual(data['dependencies'], [])
        self.assertEqual(data['optional-dependencies']['sourcegraph'], ['mcp==1.30.0'])
        requirements = [line for line in (ROOT/'requirements-knowledge.txt').read_text(encoding='utf-8').splitlines() if line and not line.startswith('#')]
        self.assertEqual(set(data['optional-dependencies']['all']), set(requirements))

    @unittest.skipUnless(os.environ.get('REPO_PILOT_PACKAGE_TESTS'), 'Set REPO_PILOT_PACKAGE_TESTS=1 to build/install static and editable distributions')
    def test_static_and_editable_launchers_and_payload(self):
        with tempfile.TemporaryDirectory(prefix='repo-pilot packaging ') as temp:
            base = Path(temp); source = base/'source checkout'; source.mkdir()
            for file in list(ROOT.glob('*.py')) + [ROOT/name for name in (
                    'pyproject.toml','README.md','upstream.lock.json','legacy_v6_files.json',
                    'requirements.txt','requirements-knowledge.txt','environment.yml')]:
                shutil.copy2(file, source/file.name)
            for name in ('project','preset','extension'):
                shutil.copytree(ROOT/name, source/name, ignore=shutil.ignore_patterns('__pycache__'))
            launchers = {}
            locations = {}
            for mode in ('static','editable'):
                env = base/mode
                subprocess.run([sys.executable,'-m','venv',str(env)],check=True,capture_output=True)
                python = env/('Scripts/python.exe' if os.name=='nt' else 'bin/python')
                args = [str(python),'-m','pip','install','--no-deps']
                if mode=='editable': args.append('--editable')
                subprocess.run(args+[str(source)],check=True,capture_output=True,text=True,encoding='utf-8')
                launcher = env/('Scripts/repo-pilot.exe' if os.name=='nt' else 'bin/repo-pilot')
                launchers[mode] = launcher
                info = json.loads(subprocess.check_output([str(launcher),'--version'],cwd=base,text=True,encoding='utf-8'))
                self.assertEqual(info['install_mode'],mode)
                locations[mode] = Path(info['code_path'])
                for name in ('project/.specify/memory/constitution.md','project/.github/copilot-instructions.md',
                             'project/.cursor/rules/engineering.mdc','project/ai_workflow/tools/knowledge_backend.py',
                             'preset/preset.yml','extension/extension.yml','legacy_v6_files.json'):
                    self.assertTrue((locations[mode]/name).is_file(), name)
                self.assertEqual(json.loads(subprocess.check_output([str(launcher),'configure','inspect',
                    '--user-config',str(base/'missing.json')],cwd=base,text=True,encoding='utf-8'))['settings']['knowledge']['backend'],'off')
            code = source/'cli.py'
            code.write_text(code.read_text(encoding='utf-8').replace('Usage: repo-pilot','Changed usage: repo-pilot'),encoding='utf-8')
            payload = source/'project/AI_CONTEXT.md'
            payload.write_text(payload.read_text(encoding='utf-8')+'\nEDITABLE-PAYLOAD-MARKER\n',encoding='utf-8')
            for mode, launcher in launchers.items():
                output = subprocess.check_output([str(launcher),'--help'],cwd=base,text=True,encoding='utf-8')
                self.assertEqual('Changed usage' in output,mode=='editable')
                self.assertEqual('EDITABLE-PAYLOAD-MARKER' in (locations[mode]/'project/AI_CONTEXT.md').read_text(encoding='utf-8'),mode=='editable')
            source.rename(base/'moved source')
            if os.environ.get('SPECIFY_ALTERNATE_BIN') and os.environ.get('SPECIFY_ALTERNATE_RECORD'):
                env = dict(os.environ, PATH=str(Path(os.environ['SPECIFY_ALTERNATE_BIN']).parent) + os.pathsep + os.environ['PATH'])
                selected = subprocess.run([str(launchers['static']), 'install', str(base/'alternate-consumer'),
                    '--toolchain-record', os.environ['SPECIFY_ALTERNATE_RECORD']], env=env,
                    cwd=base, capture_output=True, text=True, encoding='utf-8')
                self.assertEqual(selected.returncode, 0, selected.stdout + selected.stderr)
                self.assertEqual(json.loads(selected.stdout)['compatibility']['source_verification'], 'verified_commit')
            subprocess.run([str(launchers['static']),'--version'],cwd=base,check=True,capture_output=True)
            if os.environ.get('SPECIFY_BIN'):
                target = base/'consumer';target.mkdir()
                authored = target/'AI_CONTEXT.md'
                installed = subprocess.run([str(launchers['static']),'install',str(target),'--specify',os.environ['SPECIFY_BIN'],
                    '--apply'],cwd=base,capture_output=True,text=True,encoding='utf-8')
                self.assertEqual(installed.returncode, 0, installed.stdout + installed.stderr)
                authored.write_text('User instructions\n',encoding='utf-8')
                upgraded = subprocess.run([str(launchers['static']), 'install', str(target),
                    '--specify', os.environ['SPECIFY_BIN'], '--upgrade', '--apply'], cwd=base,
                    capture_output=True, text=True, encoding='utf-8')
                self.assertEqual(upgraded.returncode, 0, upgraded.stdout + upgraded.stderr)
                self.assertEqual(authored.read_text(encoding='utf-8'),'User instructions\n')
                self.assertTrue((target/'ai_workflow/tools/knowledge_backend.py').is_file())
