# Quality gates and release readiness

The same Python commands run locally and in GitHub Actions. No Make installation is required; the Makefile provides convenience aliases. Use Python 3.11 or newer and Git with `--show-object-format` support.

## Local checks

```bash
python -m pip install -e '.[dev]'
python scripts/check.py
```

The gate checks Ruff formatting, Ruff static analysis, distribution contracts and both unittest suites. It exits nonzero on failure and writes `.quality/gate.json` with `go: true` only if every stage passed. `.quality/tests.json` lists test counts, failures and explicit skips. `make check` is equivalent. Fix formatting with `python -m ruff format .`; do not bypass a failing check to obtain a green result.

The default unit profile permits the existing optional integration skips and reports them. It is not the release gate. For all integration tests, install optional dependencies and prepare both pinned toolchains:

```bash
python -m pip install -e '.[dev,all]'
python scripts/prepare_integration.py
```

The helper writes `.quality/toolchains/environment.json`. Set its four values in your shell: `SPECIFY_BIN`, `SPECIFY_ALTERNATE_BIN`, `SPECIFY_ALTERNATE_RECORD`, and `REPO_PILOT_PACKAGE_TESTS=1`. Then run:

```bash
python scripts/check.py --full
```

Full mode fails if prerequisites are absent or any test is skipped. It covers default and alternate Spec Kit installation, static/editable distributions and backend protocol fixtures. Run the strict profile on Linux; POSIX-only tests are explicitly skipped on Windows. Test results do not certify production Sourcegraph, real agent behavior or token savings.

## Hosted checks and go/no-go integration

`.github/workflows/ci.yml` runs for pull requests, branch pushes, merge queues and manual dispatch. It is also reusable through `workflow_call`. Jobs cover:

- formatting, static analysis, contract validation and checksum-pinned actionlint workflow validation;
- unit tests on Linux/Python 3.11–3.13 and macOS/Windows/Python 3.13;
- complete Linux integration tests with no skips;
- wheel/sdist build, metadata validation, checksums and clean-environment wheel smoke tests.

The final **Quality gate** job requires all four job groups to succeed. Failed, cancelled, skipped or missing prerequisites produce NO-GO. It publishes `go=true|false` as a job output, a reusable-workflow output and `.quality/ci-gate.json`. Evidence is uploaded as Actions artifacts. CI uses read-only repository permissions, immutable action commits and no repository secrets; it does not execute untrusted PR code with a privileged `pull_request_target` event.

Repository administrators must enable Actions and configure the default branch/release trunks to require **Quality gate**, require up-to-date checks or a merge queue, prevent force pushes, and require review appropriate to the team. A workflow file alone cannot enforce branch protection. Add the check after its first real run so GitHub can discover its name. Do not exempt documentation-only changes: they can affect package metadata, workflows or installed guidance.

A downstream deployment workflow can call `ci.yml`, depend on that job, and require `needs.checks.outputs.go == 'true'`. Also use a protected deployment environment for publication credentials and approvals. Never consume a previous run's green flag as evidence for a different commit.

## Release candidates

```bash
python scripts/build_release.py --tag v1.1.0
python scripts/build_release.py --verify-only
```

The build command requires empty output, verifies tag/version consistency when a tag is supplied, builds one wheel and one source distribution, validates metadata with Twine, checks wheel licenses/payload, installs the wheel in a disposable environment, and writes `SHA256SUMS`. Build defaults to `.quality/release`; choose another directory with `--output`. A manifest detects changed bytes; it does not authenticate an arbitrary publisher.

The **Release readiness** workflow runs on version tags or manual dispatch, reuses the entire CI gate and uploads a validated release candidate only after GO. It prepares distribution artifacts; it does not create public releases, upload to PyPI, change versions, move tags or deploy automatically. Publication can consume these artifacts behind the team's protected environment. Tag names must match both `pyproject.toml` and `upstream.lock.json`.

## Maintainer setup

Enable GitHub private vulnerability reporting so the route in SECURITY.md works. Confirm a private maintainer contact for conduct reports, and configure notification/review ownership. Dependabot proposes weekly action and Python updates; each update must pass the same gate. Optional backend pins must stay consistent with `requirements-knowledge.txt`; default Spec Kit pins must stay consistent with `requirements.txt` and manifest compatibility constraints.

See VALIDATION.md for what actually ran. A workflow committed locally is readiness evidence, not a successful remote CI run or verified Windows/macOS support.
