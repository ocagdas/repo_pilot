# Readiness

Package version: 1.1.0. Date: 8 September 2026. Official Spec Kit remains pinned to v1.0.4.

See ROADMAP.md for proposed delivery phases covering hierarchical settings, local Spec Kit version overrides, reusable semantic knowledge and shared trunk publication. The settings foundation is now implemented as described below; local version overrides are also implemented; manual CGC bundle sharing is implemented; automated sharing remains planned.

## Ready for a project pilot

1. Official Spec Kit installation and composable engineering preset and extension.
2. Codex, Cursor and Copilot integration, separately or together.
3. Project entry point and embedded, Python and data science guidance.
4. Focused testing and review instructions, final correction cycle and derived completion report validation.
5. Local Git inventories and branch deltas, with optional semantic availability detection and source fallback.
6. Conservative initial installation and unchanged v6 migration with archived original files.
7. Machine setup helper for native Python, venv and Conda; Dockerfile; operating system specific instructions.
8. A repository layout and local regression tests suitable for your own Git host. GitHub Actions CI and release-readiness workflows now provide formatting, static analysis, unit/integration tests and validated distribution artifacts; hosted results and branch-protection enforcement still require a real remote run and administrator setup.
9. Hierarchical JSON preferences shared by setup, installation and bootstrap, effective-setting inspection, stable project identity and conservative project configuration. See project/ai_workflow/settings.md.
10. Official release/commit overrides, isolated environments, portable source records, staging compatibility checks and conservative upgrade preview/apply. See TOOLCHAIN_VERSIONS.md.
11. Installable repo-pilot command, static/editable source modes and minimal/CGC/Sourcegraph/all dependency profiles. See INSTALL_MODES.md.

## Requires your project values

Compiler and interpreter versions, board and target details, format and build commands, tests, applicable quality gates, authoritative documentation, data identities and evaluation criteria. The default CUSTOMISE values are deliberately incomplete and cannot count as passing checks.

## Not implemented

Shared Clang or semantic graph publication, authenticated index fetching, branch aware semantic graph composition, a general arbitrary task migration engine, automatic concurrent agent orchestration, automatic cache retention and guaranteed runtime enforcement of every Markdown instruction.

The current inventory overlays are real file records. They are not a compiler dependency graph. CGC and Sourcegraph now have optional default-off retrieval adapters; CGC also supports checked bundle export/import. Full semantic branch composition remains unimplemented. See project/ai_workflow/knowledge_backends.md.

## Validation scope

Static/editable launcher and payload behavior was verified on Linux, including complete venv setup, Sourcegraph optional dependency installation and both Docker source modes. See INSTALL_MODES.md and VALIDATION.md.

Linux execution with pinned Spec Kit 1.0.4 and alternate 1.0.3 is tested. Conda creation/activation and default/alternate Docker builds with non-root project installation were also exercised on Linux. The graph pilot also ran actual CGC indexing, MCP queries and bundle reuse between two local clones, plus a Sourcegraph MCP protocol fixture. Live Sourcegraph, host native installation, Windows/macOS and live agents remain unverified; no remote CI success is claimed. See VALIDATION.md for exact evidence and test commands.

## Reconciled baseline

8 September 2026: the current working tree was reviewed against the roadmap, and all 84 existing tests passed on Linux with no skips. See the baseline reconciliation entry in VALIDATION.md for the precise scope. IMPLEMENTATION_PLAN.md now lists delivered, partial and planned work together. These statements include pending changes and do not imply a release.

Next: choose the representative pilot and measure correctness and agent token use with the existing adapters. Repository regression CI is implemented locally; remote execution and enforcement remain to be configured; semantic branch reuse and knowledge publication remain later milestones.

10 September 2026 review fixes: installed bootstrap respects consumer configuration, alternate CLI discovery handles installed launchers and PATH shadowing, native verification follows pip's installation scheme, and failed CGC imports clean up staging. See VALIDATION.md for current regression evidence.

10 September 2026 structural review follow-up: added recoverable atomic installation writes, bounded toolchain/setup commands, incremental inventory record reuse with dirty-path provenance, bootstrap contract validation, callable CLI handlers and operation-specific backend diagnostics. Validation evidence and limitations are recorded in VALIDATION.md.

10 September 2026 recovery/integrity follow-up: OS-owned installation locks replace PID checks, journal retirement makes cleanup retryable, and bootstrap binds requests to candidate contents and checks output-path collisions using one layout definition. Linux process-death tests and Windows locking simulations are distinguished in VALIDATION.md.

10 September 2026 cancellation/planning follow-up: toolchain cancellation shares timeout cleanup; bootstrap invalidation precedes cache-reuse integrity checks; SHA-1 and SHA-256 repository revisions are supported. Atomic persistence and state/request/index contracts now live in the consumer payload's knowledge_state.py module. See VALIDATION.md for execution evidence.

10 September 2026 open-source/CI readiness: MIT metadata and notices are reconciled; community policies, contribution templates, code ownership and changelog are supplied. CI checks formatting, static analysis, workflow validity, distribution contracts, cross-platform unit matrices, strict Linux integration and release artifacts. Local rehearsal evidence is in VALIDATION.md; no hosted run, branch-protection change or public release is claimed.
