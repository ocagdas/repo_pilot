# Validation record

This file records the latest qualification state and explicit evidence boundaries. Historical detail is intentionally condensed to reduce drift; use Git history for superseded entries.

## Follow-up qualification — 11 September 2026

Re-ran the pending CI fixes on 01f90b3 with the prepared default/alternate Spec Kit
installations and package tests enabled. `scripts/check.py --full` passed: **153 tests,
no skips, GO**, including installer preservation, writable Windows flush regression,
canonical paths, script imports and static/editable package qualification.
Log: /tmp/followup-rp-full.log. Shared conformance and actionlint passed.

The fixes remain local. Hosted run 34539845643 belongs to the old committed source;
Windows/macOS execution and actual integration-report upload still require the owner
to publish the reviewed revision and obtain its hosted Quality gate. No hosted green
status is inferred from this Linux run.

## Review fixes — 11 September 2026

The pending delta on 01f90b3 fixes installation planning/transaction races, writable
copy flushing for Windows, canonical root aliases, direct-script imports, platform
path assertions and explicit hidden integration-evidence uploads. New regressions
cover authored edits, writable flush handles and unrelated scripts namespaces.

- Full Linux gate: **153 tests passed, no skips** (121 repository + 32 bootstrap), GO.
  Command: `python scripts/check.py --full` with both pinned Spec Kit installations
  and REPO_PILOT_PACKAGE_TESTS=1. Log: /tmp/review-fixes-rp-full2.log.
- Formatting, lint, distribution/shared contracts and static/editable installation
  tests are included in that gate.

The old hosted run 34539845643 diagnosed real Windows flush, macOS path, Windows
import and integration upload failures. Code/fixture corrections are locally tested;
**new hosted Windows/macOS and evidence-upload runs have not occurred**.

## Consolidation evidence — 10 September 2026

- Full `scripts/check.py --full` with the provisioned toolchain environment: **149
tests passed, no skips** (117 repository + 32 consumer tests), full-profile GO.
Log: /tmp/rp-release-full.log.
- Real wheel/source build from a clean annotated-tag fixture, common provenance and
selected-tag/commit verification, isolated installed CLI/config inspection and
consumer-resource checks passed. Log: /tmp/rp-release-artifacts.log.
- Shared conformance, workflow actionlint and scoped formatting/lint checks passed in
local qualification.

No hosted CI/App publication, branch-rule changes, real tags, public/private releases,
Windows/macOS execution on the reviewed revision, live providers/media, or new token
benchmarks were performed in this consolidation checkpoint.

## Current qualification boundary

- Local Linux qualification is current.
- Hosted qualification for the reviewed revision remains outstanding.
- Versioning App publication for this repository remains unenabled pending setup.
- Public GitHub Release/PyPI publication remains disabled.

## Historical evidence

Older validation narrative from earlier checkpoints was intentionally condensed to keep
this file focused on current evidence. Use repository history when older run detail is
needed for audit or forensic review.
