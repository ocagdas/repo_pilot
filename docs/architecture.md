# Architecture and ownership

Repo Pilot is a tooling distribution around official Spec Kit. Root Python modules implement the CLI, setup, installation, configuration, toolchain selection and optional knowledge adapters. The package maps this existing layout to repo_pilot; it is intentionally not moved to src/ as part of documentation standardization.

| Component | Responsibility and data ownership |
| --- | --- |
| cli.py, setup_tooling.py | Installed entry point and static/editable dependency-profile setup |
| configure.py, project/ai_workflow/tools/settings.py | Shared configuration hierarchy, scope/origin resolution and project settings |
| toolchains.py, upstream.lock.json, requirements.txt | Immutable official-tool selection and compatibility; package_version is a separate mirror |
| install.py, install_transaction.py | Staging, authored-file preservation, managed upgrade ledger, recoverable atomic installation |
| preset/, extension/ | Composable upstream additions and engineering commands |
| project/ | Consumer-installed instructions, defaults, schemas and bootstrap/completion utilities |
| knowledge.py | Optional CGC/Sourcegraph adapter commands, bounded retrieval and checked full-snapshot transfer |
| scripts/, .github/workflows/ | Distribution validation, numeric versions, atomic package tags and release artifacts |
| tests/, project/ai_workflow/tools/test_*.py | Distribution and installed-utility regression evidence |

Consumer state, graph caches, credentials, local overrides and install journals are not shared release source. Authored project guidance can be committed in the consumer repository; generated machine/checkout data uses documented ignored locations. Sourcegraph state is service-owned; CGC indexing/bundles use configured local storage. See the installed [backend guide](../project/ai_workflow/knowledge_backends.md).

Package build artifacts are disposable under .quality/ or an explicit output directory. Release CI owns commit/run-bound gate evidence and wheel/source validation. Package tag automation does not publish knowledge snapshots or public package releases. Proposed graph/base/overlay ownership is described in [knowledge design](development/knowledge-design.md).

Runtime code and CI are self-contained in this repository. Sibling projects inform shared conventions; none is imported at runtime.
