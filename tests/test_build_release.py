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
            (output / "SHA256SUMS").write_text(
                "".join(
                    hashlib.sha256(path.read_bytes()).hexdigest() + "  " + path.name + "\n" for path in (wheel, source)
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
            original = "".join(
                hashlib.sha256(p.read_bytes()).hexdigest() + "  " + p.name + "\n" for p in (wheel, source)
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
