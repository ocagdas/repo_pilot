"""Publish a tested trunk version and immutable tag in one atomic Git push.

Use a disposable CI checkout with an authorized GitHub App token already configured.
The workflow grants permission; this helper additionally checks revision identity,
cleanliness and the remote tip. It never rebases or force-pushes.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys

if __package__:
    from . import version
else:
    import version


def publish(source: str, trunk: str, *, merged: bool = False) -> dict:
    git = version.git
    git("check-ref-format", f"refs/heads/{trunk}")
    if git("status", "--porcelain"):
        raise ValueError("Publication requires a clean disposable checkout")
    if git("rev-parse", "HEAD") != source or os.getenv("GITHUB_SHA") != source:
        raise ValueError("Checkout and GITHUB_SHA must match the tested source commit")
    # Explicit remote tracking ref avoids ambiguous FETCH_HEAD when tags are fetched too.
    remote = "refs/remotes/origin/release-trunk"
    git("fetch", "origin", f"refs/heads/{trunk}:{remote}", "--tags")
    if git("rev-parse", remote) != source:
        return {"schema_version": 1, "status": "superseded", "source_commit": source}
    plan = version.ci_plan(merged)
    if plan["mode"] == "none":
        return {"schema_version": 1, "status": "unchanged", "source_commit": source}
    if plan["mode"] == "patch":
        version.write_version(plan["version"])
        git("add", "--", *version.VERSION_FILES)
        git("commit", "-m", f"chore(release): {plan['tag']}")
    tag = version.create_tag()
    git("push", "--atomic", "origin", f"HEAD:refs/heads/{trunk}", f"refs/tags/{tag}")
    return {
        "schema_version": 1,
        "status": "published",
        "version": version.current(),
        "tag": tag,
        "source_commit": source,
        "version_commit": git("rev-parse", "HEAD"),
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True)
    parser.add_argument("--trunk", required=True)
    parser.add_argument("--merged", action="store_true")
    parser.add_argument("--github-output", action="store_true")
    args = parser.parse_args(argv)
    try:
        version.emit(publish(args.source, args.trunk, merged=args.merged), github_output=args.github_output)
        return 0
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        print(f"Version publication error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
