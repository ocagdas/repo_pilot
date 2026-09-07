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
