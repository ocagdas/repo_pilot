# Spec Kit engineering package

This package adapts the official [GitHub Spec Kit](https://github.com/github/spec-kit) for embedded C and C++, Python and data science. It uses upstream v1.0.4 with a composable preset, an extension and project configuration. The official upstream remains unmodified. This custom package is not an official GitHub product.

## Start here

Follow [QUICKSTART.md](QUICKSTART.md) for a guided installation, project configuration and first feature workflow.

Read STATUS.md for what is ready and what remains unimplemented. Read ROADMAP.md for the proposed direction for personal overrides, portable knowledge, trunk snapshots and team sharing, and IMPLEMENTATION_PLAN.md for delivery work packages. Read INSTALLATION.md for native Python, venv, Conda and Docker instructions on Windows, Linux and macOS. Read REPOSITORY.md to push this distribution to your own Git repository.

For Linux or macOS, the shortest venv setup is:

```bash
python3 setup_tooling.py --mode venv --apply
python3 install.py /absolute/path/to/project --integration copilot --apply
```

For Windows PowerShell:

```powershell
py -3 setup_tooling.py --mode venv --apply
py -3 install.py C:\work\project --integration copilot --apply
```

Run from this tooling repository. Choose a Python 3.11 or newer installation and have Git on PATH. install.py discovers the local .venv CLI automatically. Omit --apply from either command to preview its work. Repeat --integration to select codex, cursor-agent and copilot together.

Setup installs machine tooling. install.py configures the target repository. Once target configuration is committed, another clone reuses it; it needs tooling but not regenerated documents. All methods use the same official Spec Kit source pin and engineering package.

## Configure the project

1. Fill in ai_workflow/project.yaml: project identity, domains, language versions, source documents and targets.
2. Replace CUSTOMISE commands in ai_workflow/commands.yaml with actual repository commands. Pure Python projects can use environment checks instead of a compilation target. Add domain specific commands and completion gates as needed.
3. Review .specify/memory/constitution.md and adapt its principles to the project. This is the sole philosophy document.
4. Adjust coding_style.md, build_test_deploy.md and documentation.md to reference existing authoritative project files.
5. Configure ai_workflow/bootstrap.json. Semantic mode defaults to auto; disabled remains fully supported. Matching branches default to the regular expression ^develop/.+$. Index query and update commands are deliberately unconfigured until a real backend is selected.
6. Review the generated changes and commit the agreed workflow files through your normal process. Generated local knowledge and migration backups are ignored by Git.

## Start a session

Open your agent at the repository root and say:

```text
Read AI_CONTEXT.md. Analyse the telemetry component and discuss the design options. Do not implement yet.
```

Or, after scope is agreed:

```text
Read AI_CONTEXT.md. Implement the agreed Spec Kit tasks. Run focused checks during development, then complete the final review and report remaining work.
```

The entry point maps ordinary language to the installed workflows. The agent must be able to read repository instructions. Markdown guidance alone does not enforce execution.

Logical commands include speckit.specify, speckit.plan, speckit.tasks, speckit.implement and speckit.converge. Our extension adds speckit.engineering.discuss, assess, bootstrap, test, review and report. The installed integration determines the invocation syntax; use its skill picker or ordinary language instructions rather than assuming one slash syntax works everywhere.

In this pinned release, generated skills are installed under .agents/skills for Codex, .cursor/skills for Cursor and .github/skills for Copilot. Copilot also receives .github/copilot-instructions.md pointing to AI_CONTEXT.md. Client settings and installed versions still determine whether these files are loaded. Tests verify generated files, not live model behaviour or subscription access.

## Branches and feature selection

Spec Kit owns feature artefacts such as specs/001-telemetry/spec.md, plan.md and tasks.md. Our branch cache rules do not dictate Spec Kit feature identity. Existing develop/* names can remain in use. If needed, identify the current feature explicitly before running upstream prerequisite scripts:

```bash
export SPECIFY_FEATURE_DIRECTORY=specs/001-telemetry
```

The upstream Python scripts also support .specify/feature.json. Do not point concurrent work at the same mutable feature state in one worktree. Use separate worktrees for concurrent writers. Independent review requires a separate reviewer or human; switching roles in one conversation remains self review.

## Completion

tasks.md is the sole task ledger. Use upstream T001 style task IDs and AC001 style acceptance criterion IDs in spec.md. The report command creates completion.json beside them. Validate it with:

```bash
python3 ai_workflow/tools/validate_completion.py specs/001-telemetry
```

The validator checks the bundled schema subset, task and acceptance coverage, checkbox agreement and evidence references for completed items. It does not execute commands, validate the truth of references or certify independence. Unavailable checks remain explicit. Existing CI and human approval rules remain necessary.

## Migrating version 6

For an unchanged version 6 template installation:

```bash
python3 install.py /absolute/path/to/repo --integration copilot --migrate-v6 --apply
```

Recognised legacy files are matched by content hash and moved to .ai_migration_backup before installing the new structure. Modified legacy files cause a stop before any target writes. Read MIGRATION.md to map customised policies and tasks deliberately. No active task information is silently converted or discarded.

## Package contents

preset contains composable domain additions to official templates and commands. extension contains six registered engineering commands. project contains the entry point, constitution seed, configuration, domain procedures and retained bootstrap utility. install.py stages and installs the selected integrations. upstream.lock.json records the official source. tests covers report validation and installer behaviour.

Do not copy the old actions.yaml, workflow.yaml or task schema into a migrated project. They would establish competing state and instructions.

## Validation and remaining work

See VALIDATION.md for checks actually performed. The pack does not include a compiler index engine, authenticated shared index publication, an automatic multi agent runner or a hardware test system. Optional adapters and real project commands still need configuration. The next pilot should use a representative C++ change and Python pipeline with two agent clients and real CI evidence.
