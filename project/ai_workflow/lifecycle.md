# Engineering lifecycle

The constitution, feature specification, plan and tasks are authoritative. Select active domains and applicable gates from project.yaml, domain_profiles.md and quality_gates.yaml. CUSTOMISE is an unconfigured command, not a passing check. Reuse existing user authorisation for the agreed task.

## Development

Implement one coherent slice, format the affected files, build the relevant component when applicable, run focused behaviour and regression tests, then inspect the diff for correctness and test adequacy. Fix issues before expanding the change. Record actual command results. Checkpoint reviews include code and test changes. Select tests by risk and dependency impact; tests for trivial reversible documentation changes are unnecessary.

## Final validation

Run the selected complete checks. Review the complete change against the agreed specification and plan. Use a separate reviewer or human when independent review is required. The reviewer and tester must assess the same immutable commit or explicitly hashed snapshot including dirty files. Parallel execution is optional and requires suitable runtime support and isolated outputs. One agent may work sequentially, but must label self review honestly.

Resolve actionable findings, rerun affected checks and repeat final review after changes. Evidence becomes stale when its relevant source, target configuration, toolchain or data inputs change. Do not automatically merge, deploy, release or flash hardware based on an agent review result.

## Closure

Create completion.json beside the active tasks.md using the extension report command. Cover every canonical task ID and acceptance criterion. Completed means supported by required evidence; incomplete means attempted but unfinished; untouched means no work performed. Link evidence, changed files, review findings and resolutions, limitations, residual risks and excluded scope. The report is a derived view, not another task ledger. Uncheck task boxes if required evidence no longer supports completion.

Validate report structure with `python3 ai_workflow/tools/validate_completion.py PATH_TO_FEATURE`. Structural validation cannot establish truth or independence. Human review and CI remain responsible for their respective checks.
