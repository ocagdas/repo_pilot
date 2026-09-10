"""Publish a tested trunk version and immutable tag in one atomic Git push.

Use a disposable CI checkout with an authorized GitHub App token already configured.
The workflow grants permission; this helper additionally checks revision identity,
cleanliness and the remote tip. It never rebases or force-pushes.
"""

from __future__ import annotations

import argparse
import subprocess
import sys

if __package__:
    from . import version
else:
    import version


def publish(source: str, trunk: str, *, merged: bool = False) -> dict:
    return version.shared.publish(
        source,
        trunk,
        git=version.git,
        current=version.current,
        classify=version.ci_plan,
        write=version.write_version,
        tag=version.create_tag,
        files=version.VERSION_FILES,
        merged=merged,
    )


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
