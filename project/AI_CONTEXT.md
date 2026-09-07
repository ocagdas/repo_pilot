# AI context

This repository uses official GitHub Spec Kit with the engineering preset and extension. Read `.specify/memory/constitution.md` and `ai_workflow/project.yaml` first. Runtime permissions and current user instructions remain authoritative.

Spec Kit feature directories own spec.md, plan.md and tasks.md. Do not create an independent task YAML or workflow state machine. Identify the active feature explicitly; when the branch name is not a Spec Kit feature identifier, use the documented SPECIFY_FEATURE_DIRECTORY environment variable pointing to the existing feature directory. Do not rename a develop/* branch merely to satisfy discovery.

Use `ai_workflow/action_map.md` for shorthand requests. Read only the relevant domain sections, source documents and feature artefacts. Conceptual discussion needs no bootstrap or source edits. Strictly read only work must not write caches. When code work permits local cache writes, run `python3 ai_workflow/tools/repo_bootstrap.py prepare --pretty`. Read semantic status even when action_required is none, and follow bootstrap_analysis.md when analysis is requested. Required semantic mode blocks dependent code work if unavailable. Auto and disabled modes permit current source inspection. Commands declared in bootstrap configuration are not executed by the utility.

Read current source and the configured build system. A new inventory is a map, not proof of exhaustive understanding. Expand analysis to affected dependencies, callers, tests and configurations. Preserve base, committed branch and dirty worktree separation. Semantic adapters are optional and not bundled.

During implementation, use the engineering lifecycle in `ai_workflow/lifecycle.md`. At completion, report every task and acceptance criterion as completed, incomplete or untouched with actual evidence. A self review is not independent review. Do not claim unavailable checks passed. Existing user authorisation counts; request decisions only for unresolved scope or actions outside it.

On Windows, use the available Python 3.11 or newer interpreter, such as `py -3` or `python`, in place of `python3` in procedural examples. Within a venv or Conda session, use that environment interpreter. Never assume a command name means the tool is installed.
