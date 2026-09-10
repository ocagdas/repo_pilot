"""Fail closed unless every required CI job succeeded; emit a machine-readable flag."""

import argparse
import json
import os
from pathlib import Path


def decision(results, required=("quality", "unit", "integration", "artifacts")):
    return (
        isinstance(results, dict)
        and bool(results)
        and set(results) == set(required)
        and all(isinstance(results[name], dict) and results[name].get("result") == "success" for name in required)
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, default=Path(".quality/ci-gate.json"))
    args = parser.parse_args()
    try:
        results = json.loads(os.environ.get("NEEDS_JSON", "{}"))
        go = decision(results)
    except (ValueError, TypeError):
        results, go = {}, False
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        json.dumps({"schema_version": "1.0", "go": go, "jobs": results}, indent=2) + "\n", encoding="utf-8"
    )
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as handle:
            handle.write("go=" + str(go).lower() + "\n")
    print("GO" if go else "NO-GO")
    return 0 if go else 1


if __name__ == "__main__":
    raise SystemExit(main())
