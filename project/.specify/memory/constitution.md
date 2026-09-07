# Engineering constitution

Version: 1.0.0. Initial template adoption: 6 September 2026. Replace project specific settings in ai_workflow/project.yaml before implementation.

## Scope and truth

Implement the agreed requirements with the smallest correct coherent change. Preserve documented behaviour and protected interfaces. State assumptions and uncertainties. Specifications, plans and tasks live in Spec Kit feature directories. This constitution is the single project philosophy authority.

## Engineering evidence

Use actual configured build, formatting and test tools. Record commands, results and source context. Missing tools, hardware or data are missing evidence. Documentation and a model judgement are not proof of correct behaviour. Apply risk appropriate focused checks during development and complete checks before claiming completion.

## Domain constraints

Read only the relevant sections of ai_workflow/domain_profiles.md. Embedded targets require explicit compiler and hardware context, concurrency and lifetime review, and applicable memory and timing constraints. Python requires an identified environment and dependency configuration. Data science requires versioned inputs, a fixed evaluation protocol, leakage checks and honest uncertainty. Do not invent numerical limits or apply unselected coding standards.

## Review and closure

Follow ai_workflow/lifecycle.md. Correct findings and refresh affected evidence. Clearly distinguish independent review from self review. Report completed, incomplete and untouched tasks against the canonical tasks.md. Never describe an unverified item as complete.

## Authority and access

Runtime rules, organisational controls and current user instructions remain authoritative. Reuse existing authorisation for the agreed scope. Actions outside that scope require a decision. Merge, release, production deployment and hardware modification require applicable explicit authorisation. Avoid redundant approval requests.

## Knowledge

Current source and measured evidence take precedence over generated summaries. Optional semantic tooling may aid navigation. Preserve base, branch and worktree separation. Required index mode blocks dependent work when unavailable; optional mode allows direct analysis. Do not treat manifest declarations as authenticated trust.

## Amendments

Amend this document deliberately, record the reason and version, and propagate changes to affected specifications and validation expectations. Preset installation must not silently replace an authored constitution.
