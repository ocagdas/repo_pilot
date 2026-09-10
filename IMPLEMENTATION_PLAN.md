# Implementation plan

Status: reconciled with the working tree, 8 September 2026. Companion to ROADMAP.md. This is a delivery plan for the tooling distribution, not a consumer project's task ledger. Work packages 1 (settings foundation) and 2 (local version overrides) are implemented; see project/ai_workflow/settings.md and VALIDATION.md. Work packages 3, 4 and 6 have partial deliveries. Pilot selection and the full semantic artifact/backend contract remain open. Current evidence remains in VALIDATION.md.

## Delivery status and next actions

| Work package | Current status | Remaining milestone |
| --- | --- | --- |
| 1: configuration | Implemented | Maintain documented precedence and preservation guarantees |
| 2: Spec Kit selection | Implemented | Broaden evidence only for platforms actually exercised |
| 3: artifact/backend contract | Partial: CGC identity/revision/checksum sidecar and two adapters | Select pilot; define build context, coverage, exact bases and invalidation |
| 4: local knowledge | Partial: bounded clean-revision retrieval and source-fallback reporting | Measure correctness/tokens; add semantic updates and richer queries |
| 5: trunks/cache | Planned | Ancestor snapshot selection, exact-base overlays and immutable shared cache |
| 6: bundles | Partial: matching-revision CGC full snapshots | Overlay/base contracts, build compatibility and actual two-machine transfer |
| 7: publication | Planned | Authenticated artifact discovery, publication, fetch and retention |
| 8: scaling | Planned | Prioritise bottlenecks demonstrated by the pilot |

Static/editable packaging, the repo-pilot launcher and optional dependency profiles are additional delivered work; see INSTALL_MODES.md. Delivery status includes pending working-tree changes and is not a release or commit claim.

Next: select the pilot repository, record its languages/build variants/trunks and run repeatable source-only versus assisted tasks with actual agent clients. Use those results to finish work package 3 and prioritise work package 4 before semantic branch composition.

Repository CI delivered: .github/workflows/ci.yml and release.yml run quality gates, pinned default/alternate integration tests and distribution validation. CI.md documents local equivalents, JSON go/no-go evidence and administrator setup. Remote runs and required branch checks are not yet established. This maintenance workflow is separate from work package 7's knowledge-artifact publication.

## Delivery approach

Implement small, reviewable increments in the order below. Preserve the current installation and source-analysis paths throughout. Do not change the official upstream pin as part of configuration work. Each increment updates documentation and readiness only for capabilities actually delivered and tested.

The implemented configuration precedence is: distribution defaults → user defaults → shared project → personal project → checkout-local → invocation. It remains explicit and reviewable rather than inferred differently by each command.

## Work package 1: configuration foundation

Implemented 8 September 2026 using schema 1.0 JSON settings and a shared resolver. The requirements below describe the delivered foundation.

Dependencies: none.

- Inventory settings in project.yaml, bootstrap.json, setup_tooling.py and install.py; map each to its owner and whether it is overridable.
- Define a versioned schema and final user/project/local file locations, including OS conventions and stable repository identity.
- Implement one resolver usable by machine setup, installation and installed project tools. Account for setup running before a consumer project exists: accept an explicit project scope and otherwise use distribution/user settings.
- Implement recursive mapping merges, list/scalar replacement, schema-defined reset semantics, unknown-key diagnostics and paths relative to the declaring file.
- Add effective-configuration inspection with origins, redaction and a compatibility-relevant fingerprint.
- Preserve existing files through a previewable migration. Do not leave two authoritative copies of the same setting. Install ignore rules without replacing existing target content.

Acceptance: exercise every precedence boundary, missing/invalid files, list replacement, relative paths and personal project reuse across clones. Verify checkout isolation and unchanged defaults. Verify personal settings do not silently waive mandatory checks or execution permissions.

Deliverable: working configuration resolver and documented migration contract. No semantic backend required.

## Work package 2: effective Spec Kit selection

Implemented 8 September 2026. See TOOLCHAIN_VERSIONS.md for supported behaviour and VALIDATION.md for executed checks.

Dependencies: work package 1.

- Route setup and installer pin checks through the same effective toolchain selection.
- Resolve official tags/commits to immutable identities and produce a local resolved-toolchain record.
- Keep upstream.lock.json and requirements.txt unchanged and consistent as distribution defaults.
- Isolate environments by selected identity; distinguish an explicitly supplied CLI from the desired CLI and diagnose mismatches.
- Validate preset, extension and integration compatibility in disposable staging before target writes.
- Provide upgrade preview/apply and reproducibility export/import without silently regenerating existing project instructions.

Acceptance: run actual installations for the default and one selected alternative; verify incompatible selections fail before mutation and customised target files survive. Verify selecting one project's version does not replace another's environment. Record precise local evidence without claiming unexecuted platform or live-agent coverage.

Deliverable: local version overrides usable without modifying or contributing changes to the distribution repository.

## Work package 3: artifact and backend contract

Partial: CGC sidecars identify repository, exact revision, backend version and checksum. Two adapters exist; pilot selection, build/input compatibility, coverage and overlay semantics remain open.

Dependencies: work package 1; can precede completion of work package 2.

- Choose the pilot repository and record scale, languages, build variants and trunk history.
- Define repository identity, artifact identity, exact overlay-base references, relative paths, coverage and provenance.
- Extend the existing manifest contract for checksums and relevant generator/build/input compatibility. Do not treat declared trust as verified authenticity.
- Define backend operations for build, incremental update, bounded query, compatibility inspection and export/import.
- Specify node/edge replacement, tombstones, dependency invalidation, partial coverage and source fallback behaviour.
- Evaluate a backend against the pilot before committing to a storage engine or graph database. Record capability gaps and portability limitations.

Acceptance: fixtures cover same revision with different targets, incompatible generators, missing bases and partial extraction. Backend selection includes evidence for update and query semantics, not only successful parsing.

Deliverable: versioned contract and a documented backend decision.

## Work package 4: local knowledge workflow

Partial: explicit CGC full rebuilds, bounded retrieval and source-fallback reporting are implemented. Bootstrap reports backend selection without launching it. The retrieval adapter rejects dirty worktrees; semantic updates and measured accuracy/token results remain open.

Dependencies: work packages 1 and 3.

- Integrate the selected backend behind the contract; execute configured operations through validated tooling rather than relying on the LLM to compose shell commands.
- Implement source/index/auto retrieval, origin selection, update/fetch policy and query limits.
- Connect bootstrap to real refresh and query status while preserving source fallback and read-only behaviour.
- Provide definitions, references, dependencies and change queries with revision/evidence information.
- Implement branch/worktree updates and affected-dependency invalidation. Keep mutable state isolated and writes atomic.
- Add concise project orientation and evidence-linked summaries with freshness rules where they improve the pilot.

Acceptance: compare queries against source/build evidence and a fresh index. Cover renamed/deleted files, changed headers/build inputs, dirty reversions and concurrent worktree isolation. Verify source mode performs no graph retrieval and disabled updates do not write caches.

Deliverable: useful local retrieval with a measured source-only comparison. Measure cold generation, warm startup, incremental refresh, result accuracy and actual agent token use; set performance targets from this baseline.

## Work package 5: trunk selection and reusable snapshots

Planned. Existing bootstrap inventories and branch deltas do not implement semantic composition.

Dependencies: work package 4.

- Add explicit trunk configuration, per-branch override and recorded selection with evidence.
- Implement ancestry inference with ambiguity reporting; handle shallow history, missing refs and detached HEAD.
- Select a compatible published ancestor snapshot independently of logical trunk association.
- Compute overlays from the exact selected snapshot to HEAD, then apply worktree changes.
- Revalidate association and overlays after switches, merges, rebases and history rewrites.
- Add an immutable machine cache shared across clones, locking and retention protecting referenced bases.

Acceptance: exercise release and RC histories with separate feature branches and advancing trunk tips. Compare composed results to a full current-checkout index. Verify trunk-only changes absent from the branch cannot leak into the result. Demonstrate clone reuse without repeating base generation.

Deliverable: correct multi-trunk local reuse. Arbitrary non-ancestor transformations remain deferred.

## Work package 6: portable bundles

Partial: full CGC snapshots transfer between matching clean revisions with identity/version/checksum checks and clone path rebasing. This initial capability does not depend on work package 5; the overlay/base-aware scope below does. Two-machine validation remains open.

Dependencies: work package 5 for overlay/base-aware bundles.

- Add compact overlay and self-contained exports using one versioned bundle format.
- Validate integrity, compatibility and base dependencies before atomic import/activation; reject unsafe archive paths and do not execute bundled commands.
- Keep code transport separate: require matching source for current-checkout activation or expose imported knowledge as another revision.
- Make dirty worktree inclusion explicit and report included paths/content categories.
- Document machine transfer and developer-to-developer exchange.

Acceptance: demonstrate transfer between two actual machines, including different clone paths, missing base recovery and build-context mismatch. Test corrupt/incomplete bundles and unavailable source. Record the platforms actually used.

Deliverable: manual sharing independent of a central server.

## Work package 7: CI publication and consumption

Planned; no automated knowledge publication or fetching is implemented.

Dependencies: work package 6; requires selection of artifact host, credentials, cadence and retention budget.

- Add a reusable pipeline template for configured trunk/build variants.
- Generate and validate immutable snapshots, then atomically publish an artifact catalog entry.
- Implement authenticated discovery/fetch, checksum verification and publisher verification appropriate to the chosen host.
- Support interrupted downloads, offline reuse, historical snapshots and retention protecting active dependencies.
- Use the same artifact contract as manual exchange and obey effective personal fetch/update policy.

Acceptance: run a real remote pipeline and have a second developer consume its snapshot and compute only the required overlay. Exercise offline use, interrupted fetch, invalid artifacts and historical-base retention. Keep local and remote CI evidence distinct.

Deliverable: working team distribution for the pilot, with operational instructions.

## Work package 8: scaling and additional adapters

Planned; no measured token-saving or large-repository performance target has been established.

Dependencies: pilot evidence from work packages 4–7.

Prioritise measured bottlenecks: incremental CI generation, deduplication across trunks, dependency invalidation precision, summary reuse, retention and additional languages. Add provider/session hooks only where actual integrations can be exercised. Consider non-ancestor reuse only if its expected benefit justifies the correctness burden.

Acceptance: repeatable benchmarks covering correctness, time, storage, transfer and tokens. No token-saving or platform-support claims without measurements.

## Verification and release discipline

Use the current Python interpreter in tests and UTF8 text I/O. Run focused checks for each implementation increment and the repository's required regression checks when affected. Keep installer preservation tests in scope for configuration, version and migration changes. Consult CONTRIBUTING.md for the official CLI test setup.

Update STATUS.md when a capability is delivered and VALIDATION.md when checks actually execute. Update the package version at release according to CONTRIBUTING.md. An intentional default upstream change must update both lock and requirements plus compatibility constraints; personal overrides must not do so.

## Decisions required before dependent implementation

Configuration and initial adapters are already implemented. Before committing to the broader backend contract, settle the pilot repository and build variants. Before hosted publication, settle the artifact service and authentication model. Before declaring performance success, agree numerical targets using the pilot baseline. No hosting, deployment or version change is performed by writing this plan.

## CGC / Sourcegraph retrieval pilot

Implemented: default-off backend selection through settings and CLI, isolated CGC indexing/MCP queries, Sourcegraph revision-scoped MCP keyword queries, bounded output, and checked CGC bundle export/import with clone path rebasing. Next: backend accuracy/token benchmark, real Sourcegraph deployment validation, then immutable trunk manifests and dependency-aware branch composition.
