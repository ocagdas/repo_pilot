import importlib.util
from pathlib import Path
import json
import tempfile
import unittest

root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("completion", root / "project/ai_workflow/tools/validate_completion.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class CompletionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.feature = Path(self.temp.name)
        (self.feature / "tasks.md").write_text("- [x] T001 Implement\n- [ ] T002 Review\n")
        (self.feature / "spec.md").write_text("AC001: Correct behaviour\n")
        self.report = {
            "schema_version": "1.0",
            "source_revision": "abc",
            "snapshot": "abc:clean",
            "tasks": [
                {"id": "T001", "status": "completed", "evidence": ["test.log"], "remaining_work": ""},
                {"id": "T002", "status": "untouched", "evidence": [], "remaining_work": "Independent review"},
            ],
            "acceptance_criteria": [
                {"id": "AC001", "status": "completed", "evidence": ["test.log"], "remaining_work": ""}
            ],
            "checks": [],
            "review": {"kind": "none", "result": "pending", "evidence": ""},
            "changed_files": [],
            "limitations": ["Review pending"],
        }

    def tearDown(self):
        self.temp.cleanup()

    def run_report(self):
        (self.feature / "completion.json").write_text(json.dumps(self.report))
        module.validate(self.feature)

    def test_valid_partial_report(self):
        self.run_report()

    def test_missing_task(self):
        self.report["tasks"].pop()
        with self.assertRaises(ValueError):
            self.run_report()

    def test_missing_criterion(self):
        self.report["acceptance_criteria"] = []
        with self.assertRaises(ValueError):
            self.run_report()

    def test_unsupported_completion(self):
        self.report["tasks"][0]["evidence"] = []
        with self.assertRaises(ValueError):
            self.run_report()

    def test_checkbox_disagreement(self):
        self.report["tasks"][1]["status"] = "completed"
        self.report["tasks"][1]["evidence"] = ["review.log"]
        with self.assertRaises(ValueError):
            self.run_report()

    def test_bad_schema(self):
        self.report["review"] = "passed"
        with self.assertRaises(ValueError):
            self.run_report()


if __name__ == "__main__":
    unittest.main()
