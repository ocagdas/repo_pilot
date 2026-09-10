# Knowledge reuse design

This document records design constraints for the roadmap. It is not a delivery ledger: [TODO.md](../../TODO.md) owns open actions, [ROADMAP.md](../../ROADMAP.md) owns dependencies and acceptance, and [STATUS.md](../../STATUS.md) owns delivered behavior.

## Configuration and tooling boundary

The existing precedence is distribution defaults → user defaults → shared project → personal project → checkout-local → invocation. Mapping merges, list/scalar replacement, reset behavior, origin-relative paths and fingerprints are one shared resolver contract. Personal settings cannot waive required checks or execution permissions. Initial setup may have user settings before a consumer repository exists.

Official release/commit selection resolves to immutable identities and isolated environments. Portable toolchain records reproduce selection. Installer staging checks compatibility and preserves authored content; package versions and personal toolchain overrides do not silently change the distribution's upstream pin.

## Artifact and backend boundary

A semantic artifact identifies repository, source revision, generator, build/input compatibility, coverage, checksums and provenance. An overlay references one exact base artifact. Relative paths permit clone relocation; declared publisher identity alone does not authenticate content. Same revision with different targets or extraction coverage can require different artifacts.

Backend operations include build, incremental update, bounded query, compatibility inspection and export/import. Node/edge replacement, tombstones, dependency invalidation and partial coverage must have explicit semantics. Bootstrap's existing file inventory/delta is distinct from a compiler or semantic graph. Current CGC full clean-revision transfer does not imply semantic branch composition.

## Local retrieval and branch composition

Queries need revision/evidence information and source fallback. Definitions, references, dependencies and changes must be checked against source/build results. Mutable worktree state remains isolated and writes atomic. Reversions, removed untracked files, renamed files, headers and build-input changes all affect invalidation; a full rebuild is the comparison baseline.

Logical trunk association and reusable snapshot selection are separate. An explicit release/RC trunk or inferred ancestor does not imply that its latest snapshot belongs in a feature branch. Choose a compatible ancestor artifact and apply the exact base-to-HEAD overlay, then dirty changes. Ambiguous ancestry, shallow history, missing refs, detached HEAD and rebases require explicit handling. Never leak newer trunk-only changes into an older branch.

An immutable machine cache can reuse bases across clones; locks protect writers and retention must protect referenced bases. Arbitrary non-ancestor transformations are deferred until evidence justifies their complexity.

## Transport and publication

Manual compact overlays and self-contained bundles share a format with hosted snapshots. Validate complete dependencies, integrity and build compatibility before atomic activation. Reject unsafe paths and never execute bundled commands. Source transport is separate: activation requires matching source or explicit access as another revision. Dirty inclusion must describe exactly what it exports.

Hosted publication adds authenticated catalogs/fetching, immutable identity, interrupted-download recovery, offline use and historical retention. Host, credentials, cadence and cost/retention decisions precede implementation. Package release automation is unrelated to knowledge-artifact publication.

## Evaluation boundary

The pilot compares source-only and assisted tasks with real agent clients on representative C++ and Python work. Measure correctness, cold generation, warm startup, refresh time, transfer/storage and actual tokens. Set targets from evidence; do not infer token savings from successful indexing. Two local clones, a protocol fixture, or generated client files do not establish two-machine, production-service or live-model behavior.
