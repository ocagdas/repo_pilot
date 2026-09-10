"""Quality gates must fail closed and release manifests must cover exact artifacts."""

import contextlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts import check, run_tests, validate_project


class QualityGateTests(unittest.TestCase):
    def test_local_gate_overwrites_stale_go_and_stops_on_failure(self):
        with tempfile.TemporaryDirectory() as temporary:
            report = Path(temporary) / "gate.json"
            report.write_text('{"go": true}', encoding="utf-8")
            with (
                patch.object(check.subprocess, "run", return_value=SimpleNamespace(returncode=1)) as command,
                contextlib.redirect_stdout(io.StringIO()),
            ):
                self.assertEqual(check.main(["--report", str(report)]), 1)
            self.assertFalse(json.loads(report.read_text(encoding="utf-8"))["go"])
            self.assertEqual(command.call_count, 1)

    def test_full_test_profile_rejects_missing_prerequisites_and_writes_evidence(self):
        with tempfile.TemporaryDirectory() as temporary, patch.dict(os.environ, {}, clear=True):
            report = Path(temporary) / "tests.json"
            self.assertEqual(run_tests.main(["--full", "--report", str(report)]), 1)
            result = json.loads(report.read_text(encoding="utf-8"))
            self.assertFalse(result["passed"])
            self.assertIn("SPECIFY_BIN", result["error"])

    def test_full_test_profile_rejects_skips_unit_profile_discloses_them(self):
        class Skipped(unittest.TestCase):
            @unittest.skip("fixture unavailable")
            def test_fixture(self):
                pass

        def suite(*args, **kwargs):
            return unittest.TestSuite([Skipped("test_fixture")])

        environment = {key: "fixture" for key in ("SPECIFY_BIN", "SPECIFY_ALTERNATE_BIN", "SPECIFY_ALTERNATE_RECORD")}
        environment["REPO_PILOT_PACKAGE_TESTS"] = "1"
        with (
            patch.dict(os.environ, environment),
            patch.object(unittest.TestLoader, "discover", side_effect=suite),
            contextlib.redirect_stderr(io.StringIO()),
        ):
            self.assertTrue(run_tests.run(full=False)["passed"])
            report = run_tests.run(full=True)
        self.assertFalse(report["passed"])
        self.assertEqual(report["suites"][0]["skipped"][0]["reason"], "fixture unavailable")

    def test_distribution_contracts_and_license_metadata(self):
        validate_project.validate()

    def test_required_gate_and_release_dependency_are_present(self):
        import yaml

        workflow = yaml.load((ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
        gate = workflow["jobs"]["quality-gate"]
        self.assertEqual(set(gate["needs"]), {"quality", "unit", "integration", "artifacts"})
        self.assertEqual(gate["if"], "always()")
        self.assertIn("merge_group", workflow["on"])
        self.assertIn("workflow_call", workflow["on"])
        release = yaml.load(
            (ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8"), Loader=yaml.BaseLoader
        )
        self.assertEqual(release["jobs"]["release-candidate"]["needs"], "checks")
        self.assertIn("outputs.go == 'true'", release["jobs"]["release-candidate"]["if"])
