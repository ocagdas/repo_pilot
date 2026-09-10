#!/usr/bin/env python3
"""Distribution entry point for settings."""

if __package__:
    from .project.ai_workflow.tools.settings import main
else:
    from project.ai_workflow.tools.settings import main

if __name__ == "__main__":
    raise SystemExit(main())
