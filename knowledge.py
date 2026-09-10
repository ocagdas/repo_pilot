#!/usr/bin/env python3
"""Distribution entry point for optional knowledge backends."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent / 'project/ai_workflow/tools'))
from knowledge_backend import main

if __name__ == '__main__':
    raise SystemExit(main())
