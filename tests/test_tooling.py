import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('setup_tooling', ROOT/'setup_tooling.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class ToolingTests(unittest.TestCase):
    def test_venv_refuses_non_environment_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            directory=Path(temp)
            (directory/'important.txt').write_text('preserve')
            with self.assertRaises(ValueError): module.commands('venv',directory,'engineering')
            self.assertEqual((directory/'important.txt').read_text(),'preserve')
    def test_venv_paths_with_spaces_are_single_arguments(self):
        with tempfile.TemporaryDirectory() as temp:
            directory=Path(temp)/'tools with spaces'
            plan=module.commands('venv',directory,'engineering')
            self.assertEqual(plan[0][-1],str(directory))
            self.assertIn('tools with spaces',plan[1][0])
            self.assertFalse(directory.exists())
    def test_conda_name_rejects_option_injection(self):
        with self.assertRaises(ValueError): module.commands('conda',Path('.'),'--prefix')
    def test_official_pin_consistency(self):
        import json
        lock=json.loads((ROOT/'upstream.lock.json').read_text())
        self.assertIn('https://github.com/github/spec-kit.git@'+lock['upstream_commit'],(ROOT/'requirements.txt').read_text())

if __name__=='__main__':unittest.main()
