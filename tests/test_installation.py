import sys
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
BIN=os.environ.get('SPECIFY_BIN')

@unittest.skipUnless(BIN, 'Set SPECIFY_BIN to the pinned official CLI')
class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.repo=Path(self.temp.name)/'project'
    def tearDown(self): self.temp.cleanup()
    def install(self, *extra):
        return subprocess.run([sys.executable,str(ROOT/'install.py'),str(self.repo),'--specify',BIN,*extra],capture_output=True,text=True)
    def test_dry_run_leaves_target_absent(self):
        result=self.install()
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertFalse(self.repo.exists())
    def test_custom_entry_is_preserved(self):
        self.repo.mkdir()
        entry=self.repo/'AI_CONTEXT.md'
        entry.write_text('Our existing policy')
        result=self.install('--apply')
        self.assertNotEqual(result.returncode,0)
        self.assertEqual(entry.read_text(),'Our existing policy')
        self.assertFalse((self.repo/'.specify').exists())
    def test_codex_composes_core_and_engineering(self):
        result=self.install('--apply')
        self.assertEqual(result.returncode,0,result.stderr)
        command=self.repo/'.agents/skills/speckit-implement/SKILL.md'
        content=command.read_text()
        self.assertIn('Engineering integration',content)
        self.assertIn('Pre-Execution Checks',content)
        self.assertTrue((self.repo/'.specify/extensions/engineering/extension.yml').exists())
        self.assertFalse((self.repo/'ai_workflow/task.schema.json').exists())
    def test_cursor_composes_core_and_engineering(self):
        result=self.install('--integration','cursor-agent','--apply')
        self.assertEqual(result.returncode,0,result.stderr)
        commands=list((self.repo/'.cursor/skills/speckit-implement').rglob('*.md'))
        self.assertTrue(commands)
        self.assertTrue(any('Engineering integration' in p.read_text() for p in commands))
    def test_copilot_composes_core_and_engineering(self):
        result=self.install('--integration','copilot','--apply')
        self.assertEqual(result.returncode,0,result.stderr)
        commands=list((self.repo/'.github/skills/speckit-implement').rglob('*.md'))
        self.assertTrue(commands)
        self.assertTrue(any(p.is_file() and 'Engineering integration' in p.read_text() for p in commands))
        self.assertIn('AI_CONTEXT.md',(self.repo/'.github/copilot-instructions.md').read_text())
    def test_three_integrations_share_workflow(self):
        result=self.install('--integration','codex','--integration','cursor-agent','--integration','copilot','--apply')
        self.assertEqual(result.returncode,0,result.stderr)
        for relative in ['.agents/skills','.cursor/skills','.github/skills']:
            text=(self.repo/relative/'speckit-implement/SKILL.md').read_text()
            self.assertIn('Engineering integration',text)
            self.assertIn('Pre-Execution Checks',text)
    def test_known_legacy_file_is_archived(self):
        self.repo.mkdir()
        # The unchanged v6 entry point is reconstructed from the sibling baseline.
        baseline=ROOT/'tests/fixtures/v6_AI_CONTEXT.md'
        (self.repo/'AI_CONTEXT.md').write_bytes(baseline.read_bytes())
        result=self.install('--migrate-v6','--apply')
        self.assertEqual(result.returncode,0,result.stderr)
        backups=list((self.repo/'.ai_migration_backup').rglob('AI_CONTEXT.md'))
        self.assertEqual(len(backups),1)
        self.assertEqual(backups[0].read_bytes(),baseline.read_bytes())

if __name__=='__main__': unittest.main()
