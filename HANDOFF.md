# Maintaining Repo Pilot safely

Start with [README.md](README.md), [PURPOSE.md](PURPOSE.md), [STATUS.md](STATUS.md), [TODO.md](TODO.md) and the latest evidence in [VALIDATION.md](VALIDATION.md). Inspect Git status before editing; preserve unrelated staged and unstaged changes. This file owns resumption conventions, not a session diary or task backlog.

`project/` is the consumer-installed payload. Its AI_CONTEXT.md and AGENTS.md instruct work in consumer repositories, not maintenance of this distribution. Keep runtime prompts, default settings, schemas and installed documentation at their loader-defined paths. [Architecture](docs/architecture.md) describes those boundaries.

Keep the package version in pyproject.toml and upstream.lock.json synchronized through scripts/version.py. The official Spec Kit commit/tag, requirements.txt and preset/extension compatibility are a separate pin; change them together only for an intentional upstream update. Preserve consumer-authored content and test installation/upgrade recovery when those paths change.

Use the current Python interpreter for child commands and UTF-8 text I/O. Run [CI.md](CI.md)'s appropriate gate with its declared integration dependencies; a skipped test is not a pass. Record actual commands, revision and scope in VALIDATION.md. Local fixtures and Linux runs do not qualify Windows, macOS, hosted CI, production Sourcegraph or live agents.

[REPOSITORY_STRUCTURE.md](REPOSITORY_STRUCTURE.md) owns common helper interfaces and documentation roles. [VERSIONING.md](VERSIONING.md) owns package release policy and credentials. Never import sibling checkouts at runtime or in CI. Do not infer permission to publish or alter hosted rules from local workflow work.

Remove completed items from TODO.md and update STATUS.md and VALIDATION.md. Keep ROADMAP.md at milestone/acceptance level and detailed design in docs/development; avoid competing checklists. Preserve approved legal notices and reporting procedures.
