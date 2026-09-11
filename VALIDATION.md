# Current validation

[CI.md](CI.md) owns check commands and [STATUS.md](STATUS.md) owns capabilities.
Use Git history for superseded evidence.

## Verified locally

The CI dependency/evidence fixes passed the strict full gate on Linux/Python 3.13.14:
**165 tests, no skips, GO** (133 distribution tests and 32 consumer bootstrap tests).
Default and alternate Spec Kit integrations and actual static/editable package tests
were enabled. Log: `/tmp/rp-ci-evidence-full.log`.

A fresh `pip install --dry-run --ignore-installed -e '.[dev,all]'` resolved successfully:
MCP 1.30.0, CodeGraphContext 0.6.13 and Kuzu 0.11.3. Resolver evidence is in
`/tmp/rp-compatible-dependencies.json`; this verifies resolution, not installation of
that entire fresh environment. Package metadata and requirements retain the same MCP pin.

Regression coverage checks uploadable NO-GO/test-not-run reports before dependency
setup, replacement after gate execution, and consistent optional dependency profiles.
Workflow linting, pin checks, shared conformance in all three repositories and patch
whitespace checks passed. The shared Dependabot policy excludes MCP >=2 until the
backend is compatible; its managed hashes were synchronized across all three repos.

## Hosted diagnosis and remaining scope

Run 34655522395 failed because its MCP 2.2.0 update conflicted with CodeGraphContext's
MCP <2 requirement. Installation stopped before the old workflow generated reports;
the artifact-upload failure was downstream. Unit tests separately failed an obsolete
literal MCP-version assertion. Expected negative-test GO=false output was not the cause.

These fixes require a fresh hosted run. Existing failed runs are not qualified by local
checks. No new hosted Windows/macOS run, actual artifact upload, public release, App
publication, Docker/Conda execution, production backend or live-agent validation is
claimed. No commits, pushes or releases were performed by this fix task.
