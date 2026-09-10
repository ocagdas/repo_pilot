"""Fail-closed integration decision from GitHub Actions dependency results."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

REQUIRED_JOBS = ("quality", "unit", "integration", "artifacts")


def evaluate(results: object) -> dict:
    if not isinstance(results, dict):
        results = {}
    checks = {}
    for name in dict.fromkeys((*REQUIRED_JOBS, *results)):
        job = results.get(name)
        result = job.get("result") if isinstance(job, dict) else None
        checks[name] = result if isinstance(result, str) else "missing"
    return {
        "schema_version": 1,
        "go": all(value == "success" for value in checks.values()),
        "checks": checks,
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results", type=Path, help="Job results JSON; otherwise use NEEDS_JSON")
    parser.add_argument("--report", type=Path, default=Path(".quality/ci-gate.json"), help="Decision JSON destination")
    args = parser.parse_args(argv)
    try:
        results = json.loads(
            args.results.read_text(encoding="utf-8") if args.results else os.getenv("NEEDS_JSON", "null")
        )
    except (OSError, UnicodeError, ValueError):
        results = None
    report = evaluate(results)
    report.update(commit=os.getenv("GITHUB_SHA"), run_id=os.getenv("GITHUB_RUN_ID"))
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    decision = "go" if report["go"] else "no-go"
    if output := os.getenv("GITHUB_OUTPUT"):
        with Path(output).open("a", encoding="utf-8") as stream:
            stream.write(f"go={str(report['go']).lower()}\n")
    if summary := os.getenv("GITHUB_STEP_SUMMARY"):
        with Path(summary).open("a", encoding="utf-8") as stream:
            stream.write(f"## Integration quality: {decision}\n\n")
            for name, result in report["checks"].items():
                # Results originate from Actions, but avoid rendering arbitrary input as Markdown.
                display = result if result in {"success", "failure", "cancelled", "skipped", "missing"} else "invalid"
                stream.write(f"- {name}: {display}\n")
    print(json.dumps(report, sort_keys=True))
    return 0 if decision == "go" else 1


if __name__ == "__main__":
    raise SystemExit(main())
