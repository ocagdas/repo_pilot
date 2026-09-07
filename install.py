#!/usr/bin/env python3
"""Stage official Spec Kit and engineering additions; protect existing files."""
import argparse
import os
import re
import sys
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import datetime

ROOT = Path(__file__).resolve().parent

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def run(argv, cwd):
    env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
    proc = subprocess.run(argv, cwd=cwd, text=True, encoding="utf-8", errors="replace", env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if proc.returncode:
        raise RuntimeError(proc.stdout)
    return proc.stdout

def files(root):
    return [p for p in root.rglob('*') if p.is_file() and '.git' not in p.relative_to(root).parts and '__pycache__' not in p.parts]

def install(args):
    target = args.repo.resolve()
    integrations = list(dict.fromkeys(args.integration or ['codex']))
    local_cli = ROOT / '.venv' / ('Scripts/specify.exe' if os.name == 'nt' else 'bin/specify')
    specify = shutil.which(args.specify) if args.specify else (str(local_cli) if local_cli.is_file() else shutil.which('specify'))
    if not specify:
        raise RuntimeError('Install the pinned official Specify CLI first; see README.md')
    version = run([specify, 'version'], ROOT)
    expected_version = json.loads((ROOT / 'upstream.lock.json').read_text(encoding='utf-8'))['specify_cli_version']
    plain_version = re.sub(r'\x1b\[[0-9;]*m', '', version)
    if not re.search(r'CLI Version\s+' + re.escape(expected_version) + r'(?![\w.])', plain_version):
        raise RuntimeError('This package is validated with Specify CLI 1.0.4 only')
    # Stage all upstream changes before considering the target.
    with tempfile.TemporaryDirectory(prefix='engineering_stage_') as temp:
        stage = Path(temp) / 'project'
        run([specify, 'init', str(stage), '--integration', integrations[0],
             '--script', 'py', '--ignore-agent-tools', '--non-interactive'], ROOT)
        run([specify, 'extension', 'add', '--dev', str(ROOT / 'extension')], stage)
        run([specify, 'preset', 'add', '--dev', str(ROOT / 'preset')], stage)
        # Explicit opt in to the requested combination, in disposable staging only.
        # Upstream does not mark every supported integration as multi install safe.
        for integration in integrations[1:]:
            run([specify, 'integration', 'install', integration, '--script', 'py', '--force'], stage)
        # Upstream registers presets for the active integration. Activate each
        # through its public API, then restore the requested default.
        for integration in [*integrations[1:], integrations[0]]:
            run([specify, 'integration', 'use', integration], stage)
        for source in files(ROOT / 'project'):
            dest = stage / source.relative_to(ROOT / 'project')
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, dest)
        incoming = {p.relative_to(stage).as_posix(): p for p in files(stage)}
        legacy = json.loads((ROOT / 'legacy_v6_files.json').read_text(encoding='utf-8'))
        retirement = []
        conflicts = []
        if args.migrate_v6:
            for relative, expected in legacy.items():
                path = target / relative
                if path.exists():
                    if path.is_symlink() or not path.is_file() or digest(path) != expected:
                        conflicts.append(relative + ' (modified legacy file; map custom values manually)')
                    else:
                        retirement.append(relative)
        for relative, source in incoming.items():
            dest = target / relative
            if any(parent.is_symlink() for parent in [dest, *dest.parents] if parent != Path('/')):
                conflicts.append(relative + ' (symlink in destination)')
            elif dest.exists() and relative not in retirement:
                if not dest.is_file() or digest(dest) != digest(source):
                    conflicts.append(relative)
        ignore_target = target / ".gitignore"
        if ignore_target.is_symlink() or (ignore_target.exists() and not ignore_target.is_file()):
            conflicts.append(".gitignore (not a regular file)")
        if conflicts:
            raise RuntimeError('No target writes made. Resolve these collisions:\n' + '\n'.join(sorted(set(conflicts))))
        plan = {'target':str(target),'integrations':integrations,'files_to_install':len(incoming),
                'legacy_files_to_archive':len(retirement),'apply':args.apply}
        print(json.dumps(plan, indent=2))
        if not args.apply:
            return
        target.mkdir(parents=True, exist_ok=True)
        backup = target / '.ai_migration_backup' / datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%f')
        for relative in retirement:
            dest = backup / relative
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(target / relative), dest)
        for relative, source in incoming.items():
            dest = target / relative
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, dest)
        ignore = target / '.gitignore'
        existing = ignore.read_text(encoding='utf-8') if ignore.exists() else ''
        exclusions = ['.ai_cache/', '.ai_migration_backup/']
        missing = [line for line in exclusions if line not in existing.splitlines()]
        if missing:
            ignore.write_text(existing.rstrip('\n') + '\n' + '\n'.join(missing) + '\n', encoding='utf-8')
        print('Installed official Spec Kit plus engineering customisations. Configure project commands before implementation.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('repo', type=Path)
    parser.add_argument('--integration', action='append', choices=['codex','cursor-agent','copilot'])
    parser.add_argument('--specify', default=None)
    parser.add_argument('--apply', action='store_true', help='Apply the validated staging plan')
    parser.add_argument('--migrate-v6', action='store_true', help='Archive only recognised unchanged v6 template files')
    args = parser.parse_args()
    try:
        install(args)
    except (RuntimeError, OSError) as error:
        parser.exit(1, str(error) + '\n')
