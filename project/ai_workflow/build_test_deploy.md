# Build, Test, and Deployment

Commands in this file must be runnable, repository relative, and free of developer specific absolute paths. Use scripts or build presets when a command is too complex to express reliably here.

Machine readable command identifiers and validation profiles live in `ai_workflow/commands.yaml`. This document explains how and when those commands are used. Keep the two consistent.

## Supported environments

`CUSTOMISE: Host operating systems, containers, toolchain versions, package sources, and environment setup.`

## Build variants and targets

`CUSTOMISE: Exact commands for host, simulator, emulator, and each supported hardware target.`

## Fast developer checks

`CUSTOMISE: Formatting, focused unit tests, compile checks, and other quick feedback commands.`

Focused checks should finish quickly enough to run after each coherent implementation slice. Document how to select a component, test case, suite, target, and changed file set without silently omitting affected dependencies.

## Required validation

`CUSTOMISE: Full compiler matrix, warnings policy, unit and integration tests, static analysis, sanitizers, coverage, size, stack, timing, and documentation checks.`

Define which checks are mandatory for ordinary implementation, which depend on change impact, and which require scarce hardware or human approval. Record expected duration, artefacts, acceptable baselines, and how failures are preserved.

## Hardware validation

`CUSTOMISE: Test rack selection, reservation, flashing procedure, hardware in loop commands, captured measurements, recovery, and human approval points.`

Host, mock, simulator, and emulator results must not be represented as physical hardware evidence.

## Packaging and artefacts

`CUSTOMISE: Reproducible packaging commands, versioning, checksums, signing boundaries, storage, and retention.`

## Deployment and rollback

`CUSTOMISE: Environments, promotion rules, deployment commands, rollback commands, health checks, and required approvals.`

An agent must not deploy, publish, sign, flash, merge, or release unless the current task explicitly authorises that exact action and the configured human gate has been satisfied.
