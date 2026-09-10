#!/usr/bin/env python3
"""Distribution entry point for knowledge_backend."""

if __package__:
    from .project.ai_workflow.tools.knowledge_backend import main
else:
    from project.ai_workflow.tools.knowledge_backend import main

if __name__ == "__main__":
    raise SystemExit(main())
