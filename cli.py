"""Installed Repo Pilot command; static wheels and editable checkouts share this entry point."""

import importlib.metadata
import json
from pathlib import Path
import importlib
import sys

ROOT = Path(__file__).resolve().parent
COMMANDS = {
    "install": "install",
    "configure": "project.ai_workflow.tools.settings",
    "knowledge": "project.ai_workflow.tools.knowledge_backend",
    "bootstrap": "project.ai_workflow.tools.repo_bootstrap",
}


def main(argv=None):
    args = sys.argv[1:] if argv is None else list(argv)
    if args == ["--version"]:
        distribution = importlib.metadata.distribution("repo-pilot")
        origin = json.loads(distribution.read_text("direct_url.json") or "{}")
        print(
            json.dumps(
                {
                    "version": distribution.version,
                    "install_mode": "editable" if origin.get("dir_info", {}).get("editable") else "static",
                    "code_path": str(ROOT),
                },
                indent=2,
            )
        )
        return 0
    if not args or args[0] in ("-h", "--help"):
        print(
            "Usage: repo-pilot {install,configure,knowledge,bootstrap} [arguments]\n"
            "       repo-pilot --version\nUse repo-pilot COMMAND --help for command options."
        )
        return 0
    if args[0] not in COMMANDS:
        print("Unknown command: " + args[0], file=sys.stderr)
        return 2
    name = COMMANDS[args[0]]
    module = importlib.import_module("." + name, __package__) if __package__ else importlib.import_module(name)
    return module.main(args[1:])
