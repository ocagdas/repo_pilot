---
description: Report using project engineering requirements
---

Read AI_CONTEXT.md first.

## User request

$ARGUMENTS

## Procedure

Read the active spec.md, plan.md, tasks.md and real check results. Write completion.json in that feature directory using ai_workflow/completion_report.schema.json. Include every canonical task ID and acceptance criterion. Classify completed, incomplete and untouched honestly. Evidence entries must identify actual commands or review records, code snapshot and target or dataset context. Check the report with python3 ai_workflow/tools/validate_completion.py PATH_TO_FEATURE. Passing schema validation proves structure only.
