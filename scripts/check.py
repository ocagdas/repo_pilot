"""Portable local/CI quality gate. Exit zero and go=true only when every check passes."""

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def initialize_reports(directory=ROOT / ".quality"):
    """Leave honest failure evidence if dependency/toolchain setup prevents the gate running."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    records = {
        "gate.json": {
            "schema_version": "1.0",
            "profile": "full",
            "go": False,
            "checks": [],
            "error": "Integration setup did not reach the quality gate; see job logs.",
        },
        "tests.json": {
            "schema_version": "1.0",
            "profile": "full",
            "passed": False,
            "suites": [],
            "error": "Tests have not run; see integration setup and quality gate logs.",
        },
    }
    for name, record in records.items():
        (directory / name).write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--full", action="store_true", help="Require integration prerequisites and reject every skipped test"
    )
    parser.add_argument("--report", type=Path, default=ROOT / ".quality/gate.json")
    args = parser.parse_args(argv)
    steps = [
        ("format", [sys.executable, "-m", "ruff", "format", "--check", "."]),
        ("lint", [sys.executable, "-m", "ruff", "check", "."]),
        ("contracts", [sys.executable, "scripts/validate_project.py"]),
        ("repository-standard", [sys.executable, "scripts/check_repository_standard.py"]),
        (
            "tests",
            [
                sys.executable,
                "scripts/run_tests.py",
                *(["--full"] if args.full else []),
                "--report",
                str(args.report.with_name("tests.json")),
            ],
        ),
    ]
    report = {"schema_version": "1.0", "profile": "full" if args.full else "unit", "go": False, "checks": []}
    try:
        for name, command in steps:
            started = time.monotonic()
            result = subprocess.run(command, cwd=ROOT, check=False)
            report["checks"].append(
                {"name": name, "exit_code": result.returncode, "seconds": round(time.monotonic() - started, 3)}
            )
            if result.returncode:
                break
        report["go"] = len(report["checks"]) == len(steps) and all(item["exit_code"] == 0 for item in report["checks"])
    except (OSError, KeyboardInterrupt) as error:
        report["error"] = type(error).__name__
    finally:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        if os.environ.get("GITHUB_OUTPUT"):
            with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as handle:
                handle.write("go=" + str(report["go"]).lower() + "\n")
    print("Quality gate: " + ("GO" if report["go"] else "NO-GO"))
    return 0 if report["go"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
