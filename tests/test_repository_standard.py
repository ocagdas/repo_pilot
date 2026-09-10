"""Shared schemas and same-run quality authorization reject ambiguous evidence."""

import copy
import json
from pathlib import Path
import sys
import unittest
import tempfile
from unittest.mock import patch

from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts import check_repository_standard, verify_quality_evidence, verify_release


class RepositoryStandardTests(unittest.TestCase):
    def test_shared_schemas_are_valid(self):
        for path in (ROOT / "standards/repository/v1").glob("*.schema.json"):
            Draft202012Validator.check_schema(json.loads(path.read_text(encoding="utf-8")))

    def test_quality_identity_and_types_fail_closed(self):
        value = {"schema_version": 1, "go": True, "commit": "a" * 40, "run_id": "7", "checks": {"unit": "success"}}

        def verify(data):
            verify_quality_evidence.verify(data, commit="a" * 40, run_id="7", required=["unit"])

        verify(value)
        for changes in (
            {"go": "true"},
            {"schema_version": True},
            {"schema_version": 2},
            {"commit": "b" * 40},
            {"run_id": "8"},
            {"checks": {}},
            {"checks": {"unit": "success", "extra": "failure"}},
            {"checks": {"unit": "skipped"}},
        ):
            with self.assertRaises(ValueError):
                verify(value | changes)

    def test_publication_requires_identity_and_release_fields(self):
        value = {"schema_version": 1, "status": "unchanged", "source_commit": "a" * 40}
        check_repository_standard.validate("publication", value)
        for change in ({"schema_version": "1"}, {"source_commit": "unknown"}, {"status": "published"}):
            with self.assertRaises(ValidationError):
                check_repository_standard.validate("publication", value | change)
        published = value | {"status": "published", "version": "1.2.3", "tag": "v1.2.3", "version_commit": "b" * 40}
        check_repository_standard.validate("publication", published)

    def test_release_schema_always_requires_boolean_intent(self):
        value = {"schema_version": 1, "version": "1.2.3", "tag": "v1.2.3", "source_commit": "a" * 40, "publish": False}
        check_repository_standard.validate("release-plan", value)
        broken = copy.deepcopy(value)
        broken.pop("schema_version")
        with self.assertRaises(ValidationError):
            check_repository_standard.validate("release-plan", broken)


class DownloadedReleaseTests(unittest.TestCase):
    def test_selected_identity_is_required_after_manifest_validation(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            value = {
                "build_kind": "release",
                "tag": "v1.2.3",
                "source_commit": "a" * 40,
                "version_commit": "a" * 40,
                "artifacts": {"payload": "b" * 64},
            }
            metadata = directory / "provenance.json"
            with patch.object(verify_release.subprocess, "run") as checked:
                metadata.write_text(json.dumps(value), encoding="utf-8")
                result = verify_release.verify(directory, "v1.2.3", "a" * 40)
                self.assertEqual(result["checks"], {"downloaded_artifacts": "success"})
                checked.assert_called_once()
                for changes in (
                    {"build_kind": "candidate"},
                    {"tag": "v1.2.4"},
                    {"source_commit": "c" * 40},
                    {"version_commit": "c" * 40},
                ):
                    metadata.write_text(json.dumps(value | changes), encoding="utf-8")
                    with self.assertRaises(ValueError):
                        verify_release.verify(directory, "v1.2.3", "a" * 40)
