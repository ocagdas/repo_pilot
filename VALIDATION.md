# Validation record

## Final branch and consolidation review — 10 September 2026

Full quality gate passed: 149 tests, no skips (117 repository + 32 consumer). Log: /tmp/unified-policy-rp-full.log.

Final shared conformance, including master trunk selection and wrong-target rejection,
passed in all three repositories. Workflow actionlint and git diff whitespace checks
passed. The shared bundle is byte-identical; digest: `ad0044680cd3883efef6b358b8aa294554aa95a74f8016d4154d9339a9a28279`.
Aiplane's clean runner preserves real profiles and cleans temporary directories;
workflow regression tests cover failed PR lookup and per-artifact attestation loops.

GitHub readback confirms main/main/master trunks, active Quality gate and immutable
version-tag rules plus squash-only merges in Repo Pilot/aiplane. ACF remains private
on master; its plan denies private rulesets and repository-settings changes require
owner/admin access. Versioning is enabled only for aiplane; Repo Pilot/ACF need App
setup before enabling it. This supersedes earlier statements that no hosted settings
were changed. No real commits, pushes, branch renames, tags, secrets or releases were
created by this work. Current-candidate hosted CI, live App publication and hosted
attestation qualification remain outstanding. See docs/development/github-policy-setup.md.

## Current release consolidation evidence — 10 September 2026

Pending local working-tree delta. Real repository versions and refs were unchanged;
commits/tags/pushes in tests targeted disposable local fixtures only. Shared code,
provenance, conformance and post-publication verification are now integrated in all
three repositories; this supersedes earlier statements about pending adapter migration.

- Full `scripts/check.py --full` with the provisioned toolchain environment: **149
  tests passed, no skips** (117 repository + 32 consumer tests), full-profile GO.
  Log: /tmp/rp-release-full.log.
- Real wheel/source build from a clean annotated-tag fixture, common provenance and
  selected-tag/commit verification, isolated installed CLI/config inspection and
  consumer-resource checks passed. Log: /tmp/rp-release-artifacts.log.

All three pass shared conformance (including immutable bundle hashes, failed/skipped/
missing gate cases, classification, reruns and advanced-tip publication), actionlint
1.7.12 workflow structure/expression checks, and scoped formatting/lint. Documentation
and final gate wiring were checked after the artifact builds. Installed release assets
were local fixtures; no actual hosted download, attestation, App mutation, ruleset,
Windows/macOS run or release publication occurred. Hosted qualification remains open.

Earlier evidence below retains its original scope and does not supersede this entry.

## Current snapshot: shared contract and community alignment, 10 September 2026

Pending working-tree delta on e61036d13fba04a4b5a3ac252db42fad4e6e6702. Package version
remains 1.1.0 and the official Spec Kit pin remains v1.0.4. The shared bundle is
reviewed-copy material, not a committed release or a sibling runtime dependency.

Executed on Linux with /tmp/repo-pilot-graph-validation/bin/python:

- `scripts/check.py --full`, with .quality/toolchains/environment.json: **148 tests
  passed, no skips** (116 repository and 32 consumer bootstrap tests), full-profile
  GO. Includes Ruff formatting/analysis, document contracts and common conformance.
  Log: /tmp/repo-pilot-shared-final.log.
- Common conformance passed bundle integrity, schema/CLI/gate cases, context-independent
  classification, tagged reruns and atomic publication/advanced-tip behavior in disposable
  local Git fixtures. Schema and evidence tests reject ambiguous types and wrong identities.
- Explicit candidate and clean annotated-tag wheel/source builds passed Twine, payload
  and source inclusions, clean wheel installation, common provenance schema and complete
  checksum membership. Tags were created only in the disposable fixture. Artifacts:
  /tmp/repo-pilot-contract-final-candidate and /tmp/repo-pilot-contract-final-release;
  log: /tmp/repo-pilot-contract-final-builds.log. Subsequent documentation-only evidence
  updates do not change the qualified build implementation.
- All three repositories passed canonical document presence, exact shared GitHub/conduct
  parity, maintained Markdown local-link checks, actionlint 1.7.12 structural/expression
  checks and git diff --check. Aiplane's affected documentation contract suite passed
  **38 tests**; its full product suite was not rerun. ACF focused build/gate/version/
  publication tests passed **61 tests** in its provisioned environment; a disposable
  metadata build verified proprietary license expression and license/notice inclusion,
  without claiming standalone wheel runtime qualification.

See [the tree/content audit](docs/development/repository-standard-audit.md) for retained
product differences and [the design](docs/development/repository-standard-design.md)
for the frozen common interface. The replacement parent handoff specifies remaining
sibling adapter migration; these checks do not certify that migration as complete.
No hosted CI/App publication, branch-rule changes, real tags, public/private releases,
Windows/macOS execution, live providers/media or new token benchmarks were performed.

## Previous snapshot: initial repository standardization, 10 September 2026

Tested the working-tree standardization delta on base commit `89947a155de6c2f81f76bf51bbc397233e184871`; this is not a committed release revision. Read the sibling handoff and AI Content Factory's shared contract/reference helpers. The reference checkout was at `e5ab754f2e26470ca1ce68dd0eaa8c4c92efee01` with staged standardization changes, so that commit alone does not identify the borrowed working-tree implementation. Repo Pilot contains local adapters, not a dependency on sibling paths, and no sibling migration/hosted success is asserted.

Executed on Linux with `/tmp/repo-pilot-graph-validation/bin/python`:

- `scripts/check.py --full`, using `.quality/toolchains/environment.json`: **143 tests passed, no skips** (111 repository tests and 32 consumer bootstrap tests). `.quality/gate.json` reports full-profile GO. Log: `/tmp/repo-pilot-standard-full.log`.
- Version/publication tests cover mirror synchronization, strict numeric versions, dry runs, PR merge-base handling, same-commit reruns, wrong source rejection, tag collisions, dirty trees, stale remote tips and atomic server rejection against disposable bare remotes. A non-main `release/next` trunk was actually published locally. Canonical JSON modes/statuses and explicit GitHub outputs are checked; classify-release returns publish=false.
- Paginated PR fixtures cover later-page matches, other trunks/repositories, unmerged PRs and malformed responses. No live GitHub PR association call is claimed. Quality tests cover missing/failed/skipped/cancelled jobs, successful extra jobs and failing extra dependencies, plus integer schema version, boolean GO and commit/run identity.
- `scripts/build_release.py --output /tmp/repo-pilot-standard-release --tag v1.1.0` built wheel/source artifacts, passed strict Twine metadata checks, verified required source guides/helpers, inspected wheel payload/licenses, installed and smoke-tested the wheel in a clean venv, and verified SHA256SUMS. Log: `/tmp/repo-pilot-standard-build.log`.
- Manifest tests reject changed bytes, incomplete/duplicate sets, portable unsafe names, invalid hashes, unexpected files and non-file entries. Moved guides are included through MANIFEST.in. Maintained root/docs Markdown links and required documents pass `scripts/validate_project.py`.
- Ruff formatting/analysis, pinned actionlint 1.7.7 and `git diff --check` passed. Version check remains 1.1.0; patch dry-run proposes 1.1.1 without modifying package metadata.

Retained adapters: root runtime layout, installed project/ payload, wheel/source qualification, optional/toolchain integration tests, existing App variable/secret names and approved legal/security policies. Root quickstart/installation remain because package/setup references use them. Detailed guides moved under docs; TODO owns open actions, the former implementation backlog became focused knowledge design, and the unreleased manual changelog was consolidated into capability/evidence documentation.

No hosted CI, App push, ruleset change, public release/PyPI upload, Windows/macOS execution or new live-agent/backend/token benchmark was performed. Pending hosted qualification and product work are tracked only in TODO.md. Versioning is behind the gated reusable version.yml; the selected trunk defaults to GitHub's repository default branch with REPO_PILOT_VERSIONING_TRUNK override.

## Historical evidence

The entries below retain their original run scope and may reference previous document/interface names. They are not the current validation snapshot.

Date: 6 September 2026.

Official upstream: github/spec-kit v1.0.4 at cb610277fdea781fcfa83d20522c2db37c94068d. The checkout remained unmodified. The official CLI was installed into an isolated local Python environment.

## Passed checks

1. Twenty retained bootstrap regression tests, including Python source selection, branch separation, dirty reversions, deletion, configuration invalidation and optional semantic mode behaviour.
2. Six completion tests covering valid partial reporting, missing tasks, missing acceptance criteria, missing evidence, checkbox disagreement and invalid structure.
3. Seven installation tests covering each integration, combined installation, preview without target writes, preservation of customised entry instructions, and archival of a recognised legacy file.
4. Package JSON and YAML parsing. Upstream extension and preset installation accepted the manifests. Generated implementation instructions contained both upstream content and the engineering addition.

Installation tests executed the official CLI for Codex, Cursor and Copilot. Combined installation uses the explicit upstream multiple integration option in disposable staging and activates each integration through the official public CLI to apply registered presets. The selected first integration is restored as default.

These checks validate installation output, document composition and local utilities. They do not establish live model compliance, independent review quality, client subscription access, hardware correctness or performance on a large repository. Semantic indexing and shared publication adapters remain unconfigured. Actual project build and test commands remain project configuration work.

## Reproduce

From the package directory, with the pinned CLI available:

```bash
python3 -m unittest discover -s project/ai_workflow/tools -p 'test_*.py'
SPECIFY_BIN=/absolute/path/to/specify python3 -m unittest discover -s tests
```

The completion validator uses only the standard library and supports the keywords in its bundled schema. It is not a general JSON Schema implementation. The installer requires the official Specify CLI and its dependencies.

## Version 1.1 update

7 September 2026: all 37 tests passed locally on Linux: 20 bootstrap, 6 completion, 7 installation and 4 tooling setup tests. The three machine setup modes produced valid preview commands without target writes. Installer tests used an existing isolated environment containing the pinned official CLI. Fresh native or Conda dependency installation and Docker image execution were not run. Windows and macOS were not available.

Added explicit UTF8 subprocess handling, platform neutral migration path keys, current interpreter test commands, and exact CLI version checking. Added native, venv and Conda setup planning plus Docker build instructions. JSON and YAML parsed successfully. Correction recorded 8 September 2026: no GitHub Actions workflow is present in the current checkout; the earlier claim that a matrix was supplied was incorrect. No remote run is established.

## Conda setup guidance update

7 September 2026: five tooling tests passed locally using `python3 -m unittest discover -s tests -p test_tooling.py -v`. The new subprocess regression test uses the current Python interpreter and verifies that `--conda-name my_spec_tools` reaches the creation command in preview without installing an environment. Documentation links, code fences and diff whitespace were checked.

The existing environment-name option now has CLI help, and successful Conda setup prints activation guidance. Actual Conda creation, post-install activation and Windows/macOS shell behaviour were not executed for this change. The full installation suite was not rerun for this focused setup/documentation update.

## Configuration foundation

8 September 2026: 52 tests passed locally on Linux: 30 package tests (6 completion, 9 installation, 10 settings, 5 tooling) and 22 bootstrap tests. Installed the exact requirements.txt Spec Kit commit into a fresh disposable venv at /tmp/repo-pilot-config-validation for the installer checks; the distribution lock and requirement were unchanged.

Commands executed:

```bash
SPECIFY_BIN=/tmp/repo-pilot-config-validation/bin/specify python3 -m unittest discover -s tests -v
python3 -m unittest discover -s project/ai_workflow/tools -p 'test_*.py'
```

The bootstrap suite was rerun after adding the final ignored-settings invalidation regression. Settings coverage includes all precedence boundaries, list replacement/null reset, relative paths, two-directory clone identity reuse and checkout isolation, invalid settings, read-only inspection, conservative migration, and setup CLI overrides. Real installer tests exercise settings-selected integration, preservation of authored local settings, installation of the resolver, ignore rules, and rejection of invalid settings before target writes. Bootstrap tests exercise source/index override precedence and configuration invalidation of completed and pending analysis. Settings schema JSON parsing, documentation links/code fences and diff whitespace checks passed.

The two-clone settings tests ran on one Linux machine; this is not a cross-machine artifact-sharing test. No alternate Spec Kit version, Conda activation, Windows/macOS execution, Docker build, remote CI, live model behaviour or semantic backend was tested in this update.

## Settings command naming

8 September 2026: renamed the settings creation command to `configure`, retaining `migrate` as a deprecated CLI alias. All 11 settings tests passed using `python3 -m unittest discover -s tests -p test_settings.py -v`, including both preview command paths and preservation checks. Diff whitespace checks passed. The full installation suite was not rerun for this command naming change.

## Local Spec Kit versions and backend research

8 September 2026: implemented official release/full-commit overrides, isolated environments, source records, staging compatibility checks, conservative upgrade previews and managed-file updates. The committed default lock, requirements and preset/extension compatibility constraints remain unchanged.

All 66 Python tests passed on Linux: 44 package tests (6 completion, 9 installation, 11 settings, 13 toolchain/version tests, 5 tooling) and 22 bootstrap tests. Commands used the current Python interpreter, with these live-version inputs:

```bash
SPECIFY_BIN=/tmp/repo-pilot-config-validation/bin/specify \
SPECIFY_ALTERNATE_BIN=/tmp/repo-pilot-version-pilot-speckit-6906bc582230bb752776e23287ee97990c1af743/bin/specify \
SPECIFY_ALTERNATE_RECORD=/tmp/repo-pilot-v1.0.3.json \
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s project/ai_workflow/tools -p 'test_*.py'
```

The alternate was actually installed from official tag v1.0.3, resolved to 6906bc582230bb752776e23287ee97990c1af743. Setup exported a checked record. Both 1.0.4 and 1.0.3 ran actual public CLI staging commands. Tests exercised all three integrations on the alternate, exact installed commit verification, mismatched CLI rejection before target writes, offline record import, invalid-source rejection, and upgrade from 1.0.3 to 1.0.4 while preserving custom AI_CONTEXT.md. Upgrade preview made no target writes. Token/graph backends were not part of these executable tests.

Additional environment checks actually executed:

- Created the alternate Conda environment under /tmp/repo-pilot-conda-version-check using conda-forge and Python 3.12. Setup compatibility checks passed. Automatic environment discovery supported preview and installation into a disposable consumer project. Activation and ordinary python/specify commands passed in a child Bash session; this does not mean setup can activate its parent shell.
- Built Docker images for default 1.0.4 and alternate 1.0.3 with the new SPEC_KIT_REF build argument. Non-root mounted-project preview/apply passed for both, with host file ownership and personal settings preserved. Tested a mounted project whose host tooling preference is Conda; the container correctly used its built CLI. The initial non-root test found an unreadable image source record; setting that non-secret record to mode 0644 fixed the issue. Added a dedicated container entry point to isolate image CLI selection from host setup preferences.
- JSON schema parsing, documentation links/fences and diff whitespace checks passed. The Docker wrapper was validated through the container runs after the Python suite completed.

Host native installation and Windows/macOS execution were not run. Native override isolation was verified in preview; its companion environment uses the exercised venv path. No remote CI, live coding agent behaviour, arbitrary-version certification, graph generation, cross-machine graph transfer or token reduction is claimed. Records pin Spec Kit source, not all transitive dependencies. The alternate compatibility result covers local staging of this engineering package, not distribution-wide certification.

Online research is recorded in KNOWLEDGE_SOLUTIONS.md with primary-source links, a licensing distinction for GitNexus, and a proposed correctness/token-cost pilot. No candidate was installed or benchmarked, and no numerical token-saving claim was established.

## Optional CGC and Sourcegraph adapters

8 September 2026: validated on Linux with Python 3.13, CodeGraphContext 0.6.13, Kuzu 0.11.3 and MCP SDK 1.30.0 in a disposable venv. Default-off operation works without that optional environment. No Spec Kit pin or baseline requirement changed.

The adapter suite has 14 tests covering default-off behavior, precedence/source policy, malformed settings, explicit runtime database isolation, missing/dirty/wrong-clone snapshots, revision-scoped literal Sourcegraph queries, locks, stderr version probing, failed-index invalidation, bundle identity/revision/checksum rejection, preserved existing databases, imported-path mapping, output limits, checkout races and redacted transport failures. Its Sourcegraph test executes the real MCP SDK handshake and tool request through an HTTP protocol fixture with authentication and redirects disabled; it is not a live Sourcegraph deployment test.

Actual CGC execution indexed a small Python Git repository, queried it over stdio MCP, exported a .cgc bundle plus provenance sidecar, imported into a differently named second clone with the same canonical origin/commit, and queried that imported graph without reparsing. Assertions checked that returned paths identify existing files in the receiving clone. Import uses a fresh database, preserves existing ones, and maps CGC's bundle-name-suffixed graph root to the clone. Both clones were on the same Linux machine; cross-machine transfer was not exercised.

Live checks caught and fixed CGC context selection overriding KUZUDB_PATH (now explicit --db-path and runtime overrides), version output on stderr, and the import destination's extra bundle-name component. Initial indexing also generated .cgcignore; after reviewing and committing it in the disposable fixture, the clean-revision check passed. No generated exclusion file in a consumer repository is automatically committed.

Reproduction environment and commands:

```bash
python -m pip install -r requirements-knowledge.txt
SPECIFY_BIN=/tmp/repo-pilot-config-validation/bin/specify \
SPECIFY_ALTERNATE_BIN=/tmp/repo-pilot-version-pilot-speckit-6906bc582230bb752776e23287ee97990c1af743/bin/specify \
SPECIFY_ALTERNATE_RECORD=/tmp/repo-pilot-v1.0.3.json \
/tmp/repo-pilot-graph-validation/bin/python -m unittest discover -s tests -v
/tmp/repo-pilot-graph-validation/bin/python -m unittest discover -s project/ai_workflow/tools -p 'test_*.py'
```

All 81 tests passed: 58 package tests (including all 14 backend tests and real default/alternate Spec Kit installation checks) and 23 bootstrap tests. No tests skipped in these final runs. Schema JSON, documentation code fences, default-off status and diff whitespace were checked. Live Sourcegraph, Windows/macOS, graph execution under Conda/Docker, large-repository performance, C/C++ compiler accuracy, cross-machine bundle portability, automatic CI publication, branch semantic composition and token savings remain unverified or unimplemented. Earlier Spec Kit environment evidence does not establish graph backend support on those environments.

## Static/editable installation and optional dependencies

8 September 2026: added an installable repo-pilot console command, static (default) and editable setup modes, and minimal (default), CGC, Sourcegraph and all dependency profiles. The selected official Spec Kit source remains provisioned separately by setup_tooling.py, preserving version override isolation. Direct pip installation manages Repo Pilot and its extras only. The upstream pin and requirements.txt remain unchanged.

Actual Linux checks built and installed static and editable distributions in disposable Python environments. The tests changed both launcher source and project payload: the editable installation saw the changes on its next invocation, while the static installation retained its original copies. The static launcher still worked after moving its source checkout. Installed wheels contained the hidden Codex/Copilot/Cursor-related payload resources, manifests and knowledge utilities; static consumer installation and authored-file preservation through upgrade were exercised with the real pinned Specify CLI.

Complete setup was executed in a fresh venv using static/minimal, then repeated in that environment using editable/Sourcegraph. Both passed compatibility staging. The installed command reported its source mode/location, and pip check found no broken dependencies. CGC/all extras were checked against the previously exercised pinned requirements; this update did not reinstall or benchmark CGC.

Final regression commands:

```bash
REPO_PILOT_PACKAGE_TESTS=1 \
SPECIFY_BIN=/tmp/repo-pilot-config-validation/bin/specify \
SPECIFY_ALTERNATE_BIN=/tmp/repo-pilot-version-pilot-speckit-6906bc582230bb752776e23287ee97990c1af743/bin/specify \
SPECIFY_ALTERNATE_RECORD=/tmp/repo-pilot-v1.0.3.json \
/tmp/repo-pilot-graph-validation/bin/python -m unittest discover -s tests -v
/tmp/repo-pilot-graph-validation/bin/python -m unittest discover -s project/ai_workflow/tools -p 'test_*.py'
```

New native/Conda profile commands were tested in preview; fresh native/Conda installations with the new launcher were not run. Windows/macOS remain unverified. Static mode here freezes Repo Pilot code/payload, not all transitive dependencies or already installed consumer files. Editable mode requires the source checkout to remain available and still needs reinstalling for dependency/entry-point changes.

All 84 tests passed in the final run: 61 package tests and 23 bootstrap tests, with no skips. Static/minimal and editable/minimal Docker images built successfully. Container runs verified static package location, next-run editable source-mount changes, static isolation from those changes, and default static non-root consumer installation. These Docker checks used the default Spec Kit version; alternate image versions and optional graph execution in these new image modes were not rerun. Documentation links/fences, TOML parsing and diff whitespace checks passed.

## Baseline reconciliation

8 September 2026: reviewed the pending installation, toolchain, settings, packaging, bootstrap and retrieval changes against the roadmap and readiness documentation. This pass changed documentation only. It did not commit or release the pending implementation.

ROADMAP.md and IMPLEMENTATION_PLAN.md now distinguish delivered configuration/tooling, partial retrieval/full-snapshot sharing, and planned semantic composition/publication. Corrected obsolete YAML settings paths, upgrade guidance and backend-research wording. Expanded the settings reference to match the resolver. Repository inspection found no .github/workflows/validate.yml or other tracked workflow; corrected the included-CI claims in STATUS.md, INSTALLATION.md, REPOSITORY.md and the earlier validation entry. Adding regression CI is explicitly tracked as follow-up work.

Fresh checks ran on Linux with Python 3.13.14 using the existing validation environments:

```bash
REPO_PILOT_PACKAGE_TESTS=1 \
SPECIFY_BIN=/tmp/repo-pilot-config-validation/bin/specify \
SPECIFY_ALTERNATE_BIN=/tmp/repo-pilot-version-pilot-speckit-6906bc582230bb752776e23287ee97990c1af743/bin/specify \
SPECIFY_ALTERNATE_RECORD=/tmp/repo-pilot-v1.0.3.json \
/tmp/repo-pilot-graph-validation/bin/python -m unittest discover -s tests -v
/tmp/repo-pilot-graph-validation/bin/python -m unittest discover -s project/ai_workflow/tools -p 'test_*.py'
git diff --check
```

All 84 tests passed with no skips: 61 package tests and 23 bootstrap tests. This includes actual default/alternate Spec Kit staging, installer preservation, disposable static/editable package installation and the Sourcegraph MCP protocol fixture. Existing tests use their running interpreter for child Python processes. JSON/YAML/TOML parsing, Python syntax, local inline Markdown file links, code fences and package/upstream pin consistency checks passed. Package version 1.1.0 and the upstream v1.0.4 source pin remain unchanged and consistent with requirements.txt.

No fresh Docker/Conda execution, real CGC indexing, live Sourcegraph deployment, Windows/macOS, remote CI, live agent or token benchmark ran in this reconciliation. Earlier environment and graph evidence above remains historical evidence with its original scope. The next product milestone is the representative repository pilot described in IMPLEMENTATION_PLAN.md.

## Review fixes — 10 September 2026

Corrected project bootstrap configuration resolution for prepare/complete/status, including the installed launcher. All three share one helper; explicit --config wins, project configuration is next, and the bundled fallback is used only when no project configuration exists. Malformed project configuration fails rather than silently falling back.

CLI discovery now checks configured locations, the current interpreter's scripts directory and executable candidates across PATH, validating selected version and alternate source commit before accepting them. This includes a matching alternate behind the launcher's mismatched default CLI on PATH. Explicit --specify is not substituted. Native setup verifies the user scripts directory when it installs with --user, or the current interpreter's scripts directory otherwise, without choosing an unrelated executable from PATH.

CGC import staging is enclosed in a temporary-directory context covering metadata parsing, database construction and closing. Tests inject failures at all three boundaries and assert that no staging directory or installed database remains. A real CGC import of the existing fixture and a subsequent MCP query also passed on Linux; returned paths existed in the receiving clone and no staging directory remained. The graph was reused, not freshly parsed in this run.

The settings schema now uses one $defs/settings definition for both global settings and per-project user settings. The real Draft 2020-12 validator accepted representative values and rejected invalid backend values in both scopes. Bootstrap's duplicated configuration-loading blocks were removed.

The review's command reproductions now pass: implicit and explicit project bootstrap both preserve disabled semantic mode and the custom cache root; selecting the alternate source record succeeds without --specify, as well as with it. Native user/active-environment path selection was regression-tested with simulated schemes; no bare-host native installation, Windows/macOS, Docker or Conda run is claimed for this change.

Final result: all 91 tests passed with no skips (66 package tests, 25 bootstrap tests). The package run used REPO_PILOT_PACKAGE_TESTS=1 and the same default/alternate CLI and record paths documented above, with /tmp/repo-pilot-graph-validation/bin/python. It included real static/editable builds, a static launcher after moving its source checkout, verified alternate discovery without --specify, and the existing preservation/upgrade checks. Sourcegraph coverage remains a protocol fixture. Syntax, schema validation, documentation links/fences, pin consistency and diff whitespace checks passed.

## Structural review fixes — 10 September 2026

Installation now uses per-file atomic replacement and a pre-write recovery journal containing original snapshots and expected hashes. Focused regressions cover partial-copy failure, multi-file rollback and successful retry, simulated process interruption, refusal to overwrite subsequent authored edits, live-owner protection, damaged backups, completed-journal cleanup and preserved executable mode. Legacy migration and real upgrade/preservation tests also passed. Recovery is designed for serialized installation and process/I/O failures; power-loss durability and concurrent external writers are not certified.

Incremental inventories retain dirty-path provenance and reuse unchanged records. In a real 100-file temporary Git repository, one edit caused one candidate file-record read and its reversion caused one; the resulting inventory matched the original. Additional tests compare incremental and full results after committed rename/deletion and a POSIX symlink addition. Old indices without provenance receive a full refresh. This is correctness and instrumentation evidence, not a large-codebase throughput or LLM token benchmark.

Bootstrap configuration validation is independent of the editable defaults, uses a bundled structural schema, and reports file/field errors. Schema/default validation passed with Draft 2020-12. Malformed optional semantic manifests still permit source fallback. Command handlers accept argument lists without launcher mutations of sys.argv, sys.path or PATH; static and editable installed launchers executed bootstrap successfully with the new validator/schema payload. Companion CLI discovery remains explicit in the toolchain/backend adapters.

Toolchain/setup execution shares bounded subprocess handling: configurable 15-second probes and 600-second commands, with POSIX process-group termination on timeout. A real sleeping Python subprocess hit the probe deadline; a separate test verified discovery proceeds after a timed-out candidate. Backend diagnostics distinguish invalid state, query failures and unexpected operation failures without exposing private exception messages from query transport.

Final Linux regression run: **107 tests passed, no skips** — 81 package/integration tests and 26 bootstrap tests. The package run used REPO_PILOT_PACKAGE_TESTS=1, the default/alternate CLI and alternate record paths documented above, and /tmp/repo-pilot-graph-validation/bin/python. It included actual static/editable builds, installation after moving the source checkout, all integration targets, default/alternate staging and Sourcegraph protocol fixtures. The final small callable-installer return adjustment was followed by the 15 focused regressions. Python syntax, bootstrap schema/defaults, package/upstream pin consistency and git diff whitespace checks passed.

No new bare-host native installation, Conda/Docker execution, real CGC indexing, live Sourcegraph deployment, Windows/macOS run, live agent run or remote CI execution is claimed for this change. Existing evidence remains historical with its original scope.

## Recovery and bootstrap integrity follow-up — 10 September 2026

Installation ownership now uses an OS file lock, with no PID probing or signaling. POSIX uses flock; Windows uses a nonblocking byte-range lock. The lock inode persists and OS ownership ends when the handle closes or the process dies. Earlier PID-based journals are rejected for manual reconciliation rather than guessing whether their writer remains alive.

The version 2 transaction manifest records prepared, committed and rolled_back phases. Terminal journals are atomically renamed out of the active recovery location before recursive deletion. A cleanup failure is reported and retried during a later installation. Tests cover partial deletion of retired metadata, a subsequent successful installation, and preservation of existing recovery checks. An actual Linux child process was killed after replacing a destination: its OS lock blocked a second installer while alive, was released by process death, and recovery restored the original snapshot. Windows byte-lock calls were exercised using a simulated msvcrt module; this does not establish a Windows execution result.

Bootstrap paths now come from a shared layout definition used by validation and writers. Validation rejects reserved state/candidate collisions, case aliases, nested output destinations, overlapping storage roots and semantic/inventory collisions before cache creation. Preparation binds canonical candidate contents to a digest in the request; completion verifies the digest, revision, worktree fingerprint and configured paths before promotion. Completed state retains an index digest for subsequent freshness/incremental checks. Altered and stale candidates, old requests without integrity metadata, path substitution and saved-index corruption are regression-tested. Existing caches without integrity metadata refresh once; damaged file indices can be rebuilt with --force-full.

Validation: 84 package/integration tests and 29 bootstrap tests passed on Linux with no skips (113 total). The package run used REPO_PILOT_PACKAGE_TESTS=1 and the documented default/alternate Specify executables and alternate record, with /tmp/repo-pilot-graph-validation/bin/python. It exercised real static/editable builds and installations, default/alternate toolchains, all integration targets and the Sourcegraph fixture. The 29 bootstrap tests were rerun after the final metadata validation tightening. Syntax, schema/default validation, package/upstream pin consistency and git diff whitespace checks also passed.

No live Windows/macOS, new Conda/Docker/native installation, real CGC indexing, production Sourcegraph, live agent, remote CI or large-repository/token benchmark ran for this follow-up. Process-death recovery does not certify power-loss durability or safety against concurrent external file edits.

## Cancellation, planning and object-format follow-up — 10 September 2026

Toolchain timeout and cancellation paths now share process cleanup. A real Linux test sent SIGINT to the caller while its command and a descendant were running; cancellation returned after cleanup, and the descendant did not perform its delayed write. A separate test checks cleanup before KeyboardInterrupt propagation. This preserves setup's ordering: subprocess cleanup finishes before its environment-lock finally block runs. Windows descendant-tree cancellation was not executed or certified.

Bootstrap now decides full-rebuild conditions before inspecting a cache for reuse. Tests change the configured index filename after completed analysis and successfully prepare, complete and reuse the new index without --force-full. A separate test verifies a configuration change bypasses an obsolete corrupt index. Integrity rejection remains active for otherwise reusable caches.

Atomic JSON/text persistence and state/request/index contracts moved into knowledge_state.py. The module is included in actual static/editable package payload checks. Repository revision validation now uses git rev-parse --show-object-format: a real SHA-256 repository passed full analysis, completion, fresh status, unchanged preparation and incremental completion. SHA-1 lifecycle coverage remains in the existing suite. Tests reject mismatched local object formats and confirm that the official Spec Kit source-ref validator still rejects 64-character pins.

The focused cancellation/recovery suite passed all 21 tests; the bootstrap suite passed all 32 tests. Syntax, schema/default consistency, package/upstream pin consistency and whitespace checks passed. No fresh Conda/Docker/native install, Windows/macOS run, real CGC indexing, production Sourcegraph, live agent, remote CI or large-repository/token benchmark ran for this follow-up.

Final full result: **119 tests passed with no skips** — 87 package/integration tests and 32 bootstrap tests. The package run used REPO_PILOT_PACKAGE_TESTS=1, the documented default/alternate Specify paths and alternate source record, and /tmp/repo-pilot-graph-validation/bin/python. It included real static/editable builds, installed bootstrap execution with the extracted persistence module, all integration targets, default/alternate staging and the Sourcegraph protocol fixture.

## Open-source and CI readiness — 10 September 2026

The existing MIT license is now reflected in package metadata and NOTICE.md; license and attribution files are also included with the installed consumer payload. Added security/conduct/support policies, contributor/CI guidance, changelog, code ownership, issue forms and a pull-request template. No private contact address was invented; private vulnerability reporting and branch protections require repository-administrator setup.

Development dependencies pin Ruff, build, Twine, JSON Schema and YAML tooling. The codebase was formatted with Ruff 0.12.0, and static analysis passed after removing unused imports and consolidating setup imports. Local gate scripts emit JSON evidence and exit nonzero on failed checks. Full mode rejects missing integration prerequisites and every skip. Gate regressions cover failed/cancelled/skipped/missing upstream jobs, stale GO reports, missing test prerequisites and artifact tampering.

The new integration setup script actually created fresh default and alternate Specify environments under ignored .quality/toolchains and emitted its environment/record files. Using those environments, `python scripts/check.py --full` returned GO: **126 tests passed with no skips** (94 package/integration and 32 bootstrap tests). The package suite included actual static/editable installs with license metadata, all integration targets, default/alternate versions and the Sourcegraph protocol fixture. Seven focused gate tests also passed after the final contract-check tightening.

A checksum-verified official actionlint 1.7.7 binary accepted both workflow definitions, including their expressions and job dependencies. Action release tags were resolved to immutable upstream commits. CI includes the same workflow linter, Python formatting/analysis/contracts, Linux/macOS/Windows unit matrices, strict Linux integration and artifact validation; a final Quality gate fails closed and exports a reusable go flag. No remote Actions execution or Windows/macOS runtime result is claimed.

The release builder actually produced a wheel and source distribution, passed Twine's strict metadata checks, verified wheel license/payload files, installed and smoke-tested the wheel in a clean environment, and generated/verified SHA256SUMS. Release-readiness automation only prepares artifacts after the full gate; it does not publish to GitHub/PyPI or deploy. No branch rules, repository visibility, private reporting settings or remote release were changed. Syntax, schema/defaults, package/upstream pins and diff whitespace checks passed. Production backends, live agents and token savings remain outside this rehearsal.

## 10 September 2026: automatic package versions and tags

Inspected the neighboring aiplane `scripts/version.py`, CI workflow and release workflow. Adapted its main-merge patch policy, explicit maintainer increases, PR version restriction and authenticated App loop guard to Repo Pilot's `pyproject.toml` / `upstream.lock.json`. The publisher uses a single atomic branch/tag push and declines a superseded source commit instead of rebasing onto an untested tip. VERSIONING.md documents the behavioral difference and activation requirements.

Executed on Linux with `/tmp/repo-pilot-graph-validation/bin/python`:

- Full `scripts/check.py --full`, with the prepared default/alternate Spec Kit environment from `.quality/toolchains/environment.json`: **138 tests passed, no skips** (106 repository tests, 32 consumer bootstrap tests). `.quality/gate.json` reports `profile=full`, `go=true`; log `/tmp/repo-pilot-version-full.log`.
- Final focused `unittest discover -s tests -p test_version.py -v`: **12 tests passed**, including the final reusable-workflow permission assertion; log `/tmp/repo-pilot-version-focused.log`.
- Real disposable local bare Git remotes exercised patch publication, annotated tag identity, explicit minor tagging, reruns, stale source rejection, conflicting tags, and server update-hook rejection without advancing the remote branch. Source-pin values remained unchanged during package version updates. Policy tests cover merged/squashed/rebased PR classification, actor-based loop prevention, monotonic numeric versions and PR merge-base comparison.
- Final Ruff format and lint checks, `scripts/validate_project.py` in the development environment, pinned actionlint 1.7.7, and `git diff --check` passed. A separate contract-check attempt with the ambient interpreter lacked jsonschema; the correctly provisioned development environment passed.
- `scripts/version.py check` reported 1.1.0; `patch --dry-run` proposed 1.1.1 without changing the real package metadata. No real repository version commit, tag or remote push was made.

The App ID/private-key settings, authenticated hosted publication, GitHub ruleset behavior and resulting tag-triggered release-readiness runs have not been exercised. No new macOS/Windows execution or public release/PyPI upload is claimed. Repository setup and recovery steps are in VERSIONING.md.
