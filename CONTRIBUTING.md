# Maintaining the tooling package

Set up official Spec Kit using INSTALLATION.md, then run the bootstrap and package tests. SPECIFY_BIN should identify the CLI in the chosen environment.

Linux or macOS with the default venv:

```bash
SPECIFY_BIN="$PWD/.venv/bin/specify" python3 -m unittest discover -s tests -v
python3 -m unittest discover -s project/ai_workflow/tools -p 'test_*.py'
```

Windows PowerShell:

```powershell
$env:SPECIFY_BIN = "$PWD\.venv\Scripts\specify.exe"
$env:PYTHONUTF8 = "1"
py -3 -m unittest discover -s tests -v
py -3 -m unittest discover -s project/ai_workflow/tools -p "test_*.py"
```

Without SPECIFY_BIN the installation tests skip deliberately; report that omission. Test modified environment modes with actual tools before marking them verified. Keep CI and local evidence distinct.

The preset composes with upstream templates and commands. The extension supplies additional procedures. Companion project files supply policy, configuration and local utilities. Avoid maintaining a second specification or task ledger alongside Spec Kit.

Before a release, update STATUS.md, VALIDATION.md and the package version in upstream.lock.json. A change to the official CLI pin must also update requirements.txt and manifest compatibility constraints. No upstream fork is maintained.

## Version override regression tests

The optional live version tests need both the pinned CLI and an alternate CLI plus its exported source record. They skip explicitly when these are absent. Use the paths produced by setup_tooling.py:

```bash
SPECIFY_BIN=/path/to/default/bin/specify \
SPECIFY_ALTERNATE_BIN=/path/to/alternate/bin/specify \
SPECIFY_ALTERNATE_RECORD=/path/to/alternate-record.json \
python3 -m unittest discover -s tests -v
```

In PowerShell set the same three environment variables before using the selected Python interpreter to run unittest. Do not infer cross-platform support from a Linux run. Alternate manifests are adapted only in disposable staging; the committed pin and manifest constraints remain the distribution baseline.

## Optional backend checks

Install requirements-knowledge.txt in a disposable environment and run tests/test_knowledge.py through unittest discovery. Without MCP, the Sourcegraph protocol test skips explicitly; it uses a fixture, not a production Sourcegraph instance. For real CGC validation, follow the index/export/import/query sequence in project/ai_workflow/knowledge_backends.md on two disposable clean clones and verify returned paths exist in the receiving clone. Do not infer cross-machine or large-codebase results from that check.

## Installed distribution checks

Set `REPO_PILOT_PACKAGE_TESTS=1` to include actual static/editable pip installations in the unittest suite. These build in disposable environments and may need network access for the build backend. With SPECIFY_BIN set, the packaging test also exercises a static installed launcher after its source checkout is moved, then verifies consumer installation and preservation on upgrade. Keep pyproject.toml's version consistent with upstream.lock.json and its optional dependency profiles consistent with requirements-knowledge.txt. Hidden integration payload files must remain present in wheels.

## Baseline and CI status

No repository regression workflow is currently included. Run the checks above locally; adding CI is tracked in IMPLEMENTATION_PLAN.md separately from future knowledge-artifact publication. A pushed commit is not evidence that remote tests ran.

Before recording a baseline, reconcile ROADMAP.md and IMPLEMENTATION_PLAN.md with the code, label partial deliveries, and distinguish historical validation from the current run. Include the optional packaging and alternate-version checks when validating those parts of a pending change, and report every skip. Keep claims about generated integration files separate from live agent results.
