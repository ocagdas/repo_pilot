"""Conformance tests for numeric versions, classifiers and workflow authorization."""

import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts import version, merged_pr


class VersioningTests(unittest.TestCase):
    def test_merge_policy_and_idempotency(self):
        self.assertEqual(version.plan("1.1.0", "1.1.0", merged=True)["mode"], "patch")
        self.assertEqual(version.plan("1.1.0", "1.1.0", merged=False)["mode"], "none")
        self.assertEqual(version.plan("1.1.0", "1.2.0", merged=False)["mode"], "tag")
        self.assertEqual(version.plan("1.1.0", "1.1.1", merged=True, tagged=True)["mode"], "none")
        with self.assertRaisesRegex(ValueError, "PR merge"):
            version.plan("1.1.0", "1.2.0", merged=True)
        with self.assertRaises(ValueError):
            version.plan("2.0.0", "1.1.0", merged=False)

    def test_strict_semver_and_bumps(self):
        for value in ("01.1.0", "1.2", "v1.2.3", "1.2.3rc1", "-1.0.0", " 1.2.3", 123):
            with self.assertRaises(ValueError):
                version.parse(value)
        for kind, expected in (("patch", "1.9.10"), ("minor", "1.10.0"), ("major", "2.0.0")):
            self.assertEqual(version.bump("1.9.9", kind), expected)

    def test_github_output_is_explicit_and_rejects_multiline(self):
        import tempfile

        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"GITHUB_OUTPUT": tmp + "/out"}):
            version.emit({"publish": False})
            self.assertFalse(Path(tmp, "out").exists())
            version.emit({"publish": False}, github_output=True)
            self.assertEqual(Path(tmp, "out").read_text(encoding="utf-8"), "publish=false\n")
            with self.assertRaises(ValueError):
                version.emit({"mode": "patch\ngo=true"}, github_output=True)

    def test_workflow_mutation_requires_successful_same_revision_trunk_push(self):
        import yaml

        def workflow(name):
            return yaml.load((ROOT / ".github/workflows" / name).read_text(encoding="utf-8"), Loader=yaml.BaseLoader)

        ci = workflow("ci.yml")
        job = ci["jobs"]["version"]
        self.assertEqual(job["needs"], ["quality-gate"])
        self.assertEqual(job["uses"], "./.github/workflows/version.yml")
        for guard in (
            "github.event_name == 'push'",
            "github.workflow == 'CI'",
            "github.event.repository.default_branch",
            "needs.quality-gate.result == 'success'",
            "needs.quality-gate.outputs.go == 'true'",
        ):
            self.assertIn(guard, job["if"])
        self.assertEqual(job["with"]["source"], "${{ github.sha }}")
        versioning = workflow("version.yml")
        self.assertEqual(set(versioning["on"]), {"workflow_call"})
        publisher = versioning["jobs"]["publish"]
        self.assertIn("github.sha == inputs.source", publisher["if"])
        self.assertIn("github.event_name == 'push'", publisher["if"])
        self.assertEqual(publisher["concurrency"]["cancel-in-progress"], "false")
        steps = publisher["steps"]
        detect = next(s["run"] for s in steps if s.get("name") == "Detect merged pull request")
        self.assertIn('scripts/merged_pr.py --source "$SOURCE" --trunk "$TRUNK"', detect)
        release = workflow("release.yml")
        self.assertEqual(release["permissions"]["pull-requests"], "read")
        self.assertIn("needs.checks.result == 'success'", release["jobs"]["release-candidate"]["if"])

    def test_merged_pr_detection_checks_all_pages_trunk_and_repository(self):
        def pr(trunk="release/next", repository="owner/repo", merged=True):
            return {"merged_at": "date" if merged else None, "base": {"ref": trunk, "repo": {"full_name": repository}}}

        wrong = [pr(trunk="main"), pr(repository="fork/repo"), pr(merged=False)]
        self.assertFalse(merged_pr.merged([wrong, []], "owner/repo", "release/next"))
        self.assertTrue(merged_pr.merged([wrong, [pr()]], "owner/repo", "release/next"))
        for malformed in ({}, [None], [[{}]], [[{"base": {}}]]):
            with self.assertRaises(ValueError):
                merged_pr.merged(malformed, "owner/repo", "main")
