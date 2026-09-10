"""Shared quality schema and fail-closed required/additional job handling."""

import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts import ci_gate


class GateTests(unittest.TestCase):
    def test_missing_failed_skipped_cancelled_and_extra_jobs(self):
        good = {name: {"result": "success"} for name in ci_gate.REQUIRED_JOBS}
        self.assertTrue(ci_gate.evaluate(good)["go"])
        self.assertTrue(ci_gate.evaluate(good | {"extra": {"result": "success"}})["go"])
        for status in ("failure", "cancelled", "skipped", None):
            for name in ("unit", "extra"):
                self.assertFalse(ci_gate.evaluate(good | {name: {"result": status}})["go"])
        self.assertFalse(ci_gate.evaluate({k: v for k, v in good.items() if k != "unit"})["go"])
        for invalid in (None, [], {}, {"unit": "success"}):
            self.assertFalse(ci_gate.evaluate(invalid)["go"])

    def test_report_schema_revision_and_explicit_results_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            results = folder / "results.json"
            report = folder / "ci-gate.json"
            output = folder / "output"
            results.write_text(
                json.dumps({name: {"result": "success"} for name in ci_gate.REQUIRED_JOBS}), encoding="utf-8"
            )
            with patch.dict(os.environ, {"GITHUB_SHA": "abc", "GITHUB_RUN_ID": "123", "GITHUB_OUTPUT": str(output)}):
                self.assertEqual(ci_gate.main(["--results", str(results), "--report", str(report)]), 0)
            value = json.loads(report.read_text(encoding="utf-8"))
            self.assertEqual(
                value,
                {
                    "schema_version": 1,
                    "go": True,
                    "commit": "abc",
                    "run_id": "123",
                    "checks": {name: "success" for name in ci_gate.REQUIRED_JOBS},
                },
            )
            self.assertEqual(output.read_text(encoding="utf-8"), "go=true\n")
            results.write_text("{malformed", encoding="utf-8")
            self.assertEqual(ci_gate.main(["--results", str(results), "--report", str(report)]), 1)
            self.assertFalse(json.loads(report.read_text(encoding="utf-8"))["go"])
