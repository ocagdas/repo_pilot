# Current validation

Policy and check commands belong to [CI.md](CI.md); current capabilities belong to
[STATUS.md](STATUS.md). This file records the latest qualification only. Superseded
results remain in Git history; they do not qualify this delta.

## Qualified scope

Validated on Linux with Python 3.13.14 against the uncommitted source-layout, recovery-fixture, resource-detection,
documentation and workflow-pin delta over `33822ba7e889452d5d2c676a2462dcdae549d164`. Package version remains 1.1.0;
requirements.txt and upstream.lock.json were not changed.

| Check | Result |
|---|---|
| Strict `python scripts/check.py --full` | GO; 164 tests, no skips (132 distribution + 32 bootstrap) |
| Default and alternate Spec Kit integration | Passed with the prepared pinned CLI environments and exported alternate record |
| Actual static/editable package installation | Passed; live code/payload updates, stale-build exclusion, source relocation, consumer preservation and unrelated parent project metadata |
| `python scripts/build_release.py --candidate --output /tmp/merge-ready-rp-artifacts` | Wheel and sdist built, Twine/checksum/provenance checks and isolated wheel installation passed |
| Workflow pin consistency and actionlint | Passed, including drift/unpinned-version regression cases |
| Documentation links and shared conformance | Passed |

The full gate used `SPECIFY_BIN`, `SPECIFY_ALTERNATE_BIN`,
`SPECIFY_ALTERNATE_RECORD` and `REPO_PILOT_PACKAGE_TESTS=1` as described in CI.md.
Logs: `/tmp/yaml-pins-rp-full.log`, `/tmp/merge-ready-rp-release.log`. These are local session artifacts, not published evidence.

The source distribution includes its payload and build helper. The wheel contains
runtime and hidden consumer resources and excludes consumer tests, local settings and
bytecode. Runtime code is in `src/repo_pilot`; authored payloads remain at root.

## Unverified scope

The updated revision has not run in hosted CI, Windows/macOS, Docker or Conda.
Docker imports were updated and source launchers were tested on Linux; no container
execution is claimed. Production Sourcegraph, live agents and token savings were not
tested. The Sourcegraph integration here uses a protocol fixture. GitHub App/tag/public
release activation remains separate from local build qualification; consult the
[hosted setup guide](docs/development/github-policy-setup.md).

Versioning App publication remains disabled pending setup. Public GitHub Release/PyPI
publication remains disabled. These local checks do not establish hosted qualification.

The YAML-based workflow-pin validator now rejects the original inline-action bypass.
Regression coverage includes flow mappings, quoted keys, aliases, reusable workflows,
duplicate keys and shell-script text. The strict full gate passed after this change;
workflow linting and shared bundle consistency passed across all three repositories.
The previously built release artifact entry above predates this maintenance-script fix.

The subsequent aiplane-consolidation delta shares its safe version-mirror containment
and trunk-specific publication tracking ref. Shared conformance, workflow linting and
15 focused version/publication tests passed (`/tmp/divergence-rp-release-tests.log`).
The earlier full-product run above predates this shared-helper delta. All managed
files and bundle manifests are identical across the three repositories; the aiplane
runner also passes conformance against this repository. Hosted qualification of the
new helper revision remains pending.
