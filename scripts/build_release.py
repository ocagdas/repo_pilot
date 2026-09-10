"""Build, validate and smoke-test release artifacts without publishing anything."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import tomllib
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def verify_manifest(directory):
    manifest = directory / "SHA256SUMS"
    entries = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        digest, name = line.split("  ", 1)
        if Path(name).name != name or name in entries:
            raise ValueError("Invalid checksum manifest entry")
        entries[name] = digest
    artifacts = {p.name for p in directory.glob("*.whl")} | {p.name for p in directory.glob("*.tar.gz")}
    if len(artifacts) != 2 or set(entries) != artifacts:
        raise ValueError("Expected exactly one wheel and one source distribution in manifest")
    if len(list(directory.glob("*.whl"))) != 1 or len(list(directory.glob("*.tar.gz"))) != 1:
        raise ValueError("Release artifact types are incomplete")
    for name, expected in entries.items():
        if hashlib.sha256((directory / name).read_bytes()).hexdigest() != expected:
            raise ValueError(f"Checksum mismatch: {name}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / ".quality/release")
    parser.add_argument("--tag", help="Require vVERSION to match both package version files")
    parser.add_argument("--verify-only", action="store_true")
    args = parser.parse_args(argv)
    output = args.output.resolve()
    if args.verify_only:
        verify_manifest(output)
        return 0
    version = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]["version"]
    pin = json.loads((ROOT / "upstream.lock.json").read_text(encoding="utf-8"))
    if pin["package_version"] != version or (args.tag and args.tag != "v" + version):
        raise ValueError("Tag and package version files must agree")
    if output.exists() and any(output.iterdir()):
        raise ValueError("Artifact output must be empty; choose a new directory or remove old artifacts explicitly")
    output.mkdir(parents=True, exist_ok=True)
    subprocess.run([sys.executable, "-m", "build", "--outdir", str(output)], cwd=ROOT, check=True, timeout=600)
    wheels = list(output.glob("*.whl"))
    sources = list(output.glob("*.tar.gz"))
    if len(wheels) != 1 or len(sources) != 1:
        raise ValueError("Build must produce exactly one wheel and one source distribution")
    subprocess.run(
        [sys.executable, "-m", "twine", "check", "--strict", str(wheels[0]), str(sources[0])], check=True, timeout=120
    )
    with zipfile.ZipFile(wheels[0]) as archive:
        names = archive.namelist()
        if not any(name.endswith("/licenses/LICENSE") for name in names) or not any(
            name.endswith("/licenses/NOTICE.md") for name in names
        ):
            raise ValueError("Wheel is missing licensing notices")
        if not any(name.endswith("/tools/knowledge_state.py") for name in names):
            raise ValueError("Wheel is missing required consumer payload")
    with tempfile.TemporaryDirectory(prefix="repo-pilot-release-") as temporary:
        environment = Path(temporary) / "environment"
        subprocess.run([sys.executable, "-m", "venv", str(environment)], check=True, timeout=120)
        binary = environment / ("Scripts" if os.name == "nt" else "bin")
        python = binary / ("python.exe" if os.name == "nt" else "python")
        subprocess.run([str(python), "-m", "pip", "install", "--no-deps", str(wheels[0])], check=True, timeout=120)
        launcher = binary / ("repo-pilot.exe" if os.name == "nt" else "repo-pilot")
        result = subprocess.run(
            [str(launcher), "--version"], cwd=temporary, check=True, capture_output=True, text=True, encoding="utf-8"
        )
        if json.loads(result.stdout)["version"] != version:
            raise ValueError("Installed wheel version does not match release")
        subprocess.run(
            [str(launcher), "configure", "inspect", "--user-config", str(Path(temporary) / "absent.json")],
            cwd=temporary,
            check=True,
            capture_output=True,
            timeout=60,
        )
    manifest = "".join(
        hashlib.sha256(path.read_bytes()).hexdigest() + "  " + path.name + "\n" for path in sorted(wheels + sources)
    )
    (output / "SHA256SUMS").write_text(manifest, encoding="utf-8")
    verify_manifest(output)
    print(f"Validated release artifacts in {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
