"""Release artifact completeness and integrity contracts."""

import hashlib
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts import build_release


class BuildReleaseTests(unittest.TestCase):
    def test_release_manifest_rejects_tampering_and_incomplete_sets(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            wheel = output / "fixture.whl"
            source = output / "fixture.tar.gz"
            wheel.write_bytes(b"wheel")
            source.write_bytes(b"source")
            build_release.write_provenance(output, version="1.1.0", commit="a" * 40)
            (output / "SHA256SUMS").write_text(
                "".join(
                    hashlib.sha256(path.read_bytes()).hexdigest() + "  " + path.name + "\n"
                    for path in (wheel, source, output / "provenance.json")
                ),
                encoding="utf-8",
            )
            build_release.verify_manifest(output)
            wheel.write_bytes(b"changed")
            with self.assertRaisesRegex(ValueError, "Checksum mismatch"):
                build_release.verify_manifest(output)
            source.unlink()
            with self.assertRaisesRegex(ValueError, "exactly one wheel"):
                build_release.verify_manifest(output)

    def test_portable_manifest_and_complete_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            wheel, source = folder / "fixture.whl", folder / "fixture.tar.gz"
            wheel.write_bytes(b"wheel")
            source.write_bytes(b"source")
            manifest = folder / "SHA256SUMS"
            build_release.write_provenance(folder, version="1.1.0", commit="a" * 40)
            original = "".join(
                hashlib.sha256(p.read_bytes()).hexdigest() + "  " + p.name + "\n"
                for p in (wheel, source, folder / "provenance.json")
            )
            manifest.write_text(original, encoding="utf-8")
            build_release.verify_manifest(folder)
            extra = folder / "unexpected.txt"
            extra.write_text("not validated", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Unexpected files"):
                build_release.verify_manifest(folder)
            extra.unlink()
            for invalid in (
                original + original.splitlines()[0] + "\n",
                original.replace("fixture.whl", "../fixture.whl"),
                original.replace("fixture.whl", "..\\fixture.whl"),
                original.replace("fixture.whl", "C:fixture.whl"),
                original.replace(original[:64], "0" * 63),
            ):
                manifest.write_text(invalid, encoding="utf-8")
                with self.assertRaises(ValueError):
                    build_release.verify_manifest(folder)
            manifest.write_text(original, encoding="utf-8")
            extra.mkdir()
            with self.assertRaisesRegex(ValueError, "regular files"):
                build_release.verify_manifest(folder)

    def test_provenance_rejects_false_release_and_mismatched_digests(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            (folder / "fixture.whl").write_bytes(b"wheel")
            value = build_release.write_provenance(folder, version="1.1.0", commit="a" * 40)
            build_release.verify_provenance(value, value["artifacts"])
            for updates in (
                {"tag": "v1.1.0"},
                {"source_commit": "bad"},
                {"schema_version": True},
                {"build_kind": "release", "tag": "v1.1.0", "version_commit": "a" * 40, "dirty": True},
            ):
                with self.assertRaises(ValueError):
                    build_release.verify_provenance(value | updates, value["artifacts"])
            with self.assertRaises(ValueError):
                build_release.verify_provenance(value, {"other.whl": "0" * 64})
