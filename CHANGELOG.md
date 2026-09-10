# Changelog

## Unreleased

- Added open-source community policies, issue/PR templates, package license metadata and license notices in the consumer payload.
- Added local formatting/static-analysis/contract/test gates, GitHub Actions matrices, strict integration evidence and release-candidate validation with checksums.
- Added recoverable installation transactions, OS-owned locks and deferred cleanup of completed journals.
- Added candidate/index integrity checks, output-layout validation and reusable incremental file records.
- Fixed cancellation cleanup, configuration-change invalidation and SHA-256 Git repository bootstrap.
- Replaced script dispatch with callable command handlers and separated persistence contracts from bootstrap orchestration.

- Added synchronized package version commands and quality-gated automatic main patch versions and annotated tags, with GitHub App configuration, immutable tags and atomic publication.

These entries describe pending repository changes, not a published release. Package versions and upstream pins are recorded in `pyproject.toml` and `upstream.lock.json`; execution evidence and platform limits are in [VALIDATION.md](VALIDATION.md).
