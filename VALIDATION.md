# Validation record

Date: 6 September 2026.

Official upstream: github/spec-kit v1.0.4 at cb610277fdea781fcfa83d20522c2db37c94068d. The checkout remained unmodified. The official CLI was installed into an isolated local Python environment.

## Passed checks

1. Twenty retained bootstrap regression tests, including Python source selection, branch separation, dirty reversions, deletion, configuration invalidation and optional semantic mode behaviour.
2. Six completion tests covering valid partial reporting, missing tasks, missing acceptance criteria, missing evidence, checkbox disagreement and invalid structure.
3. Seven installation tests covering each integration, combined installation, preview without target writes, preservation of customised entry instructions, and archival of a recognised legacy file.
4. Package JSON and YAML parsing. Upstream extension and preset installation accepted the manifests. Generated implementation instructions contained both upstream content and the engineering addition.

Installation tests executed the official CLI for Codex, Cursor and Copilot. Combined installation uses the explicit upstream multiple integration option in disposable staging and activates each integration through the official public CLI to apply registered presets. The selected first integration is restored as default.

These checks validate installation output, document composition and local utilities. They do not establish live model compliance, independent review quality, client subscription access, hardware correctness or performance on a large repository. Semantic indexing and shared publication adapters remain unconfigured. Actual project build and test commands remain project configuration work.

## Reproduce

From the package directory, with the pinned CLI available:

```bash
python3 -m unittest discover -s project/ai_workflow/tools -p 'test_*.py'
SPECIFY_BIN=/absolute/path/to/specify python3 -m unittest discover -s tests
```

The completion validator uses only the standard library and supports the keywords in its bundled schema. It is not a general JSON Schema implementation. The installer requires the official Specify CLI and its dependencies.

## Version 1.1 update

7 September 2026: all 37 tests passed locally on Linux: 20 bootstrap, 6 completion, 7 installation and 4 tooling setup tests. The three machine setup modes produced valid preview commands without target writes. Installer tests used an existing isolated environment containing the pinned official CLI. Fresh native or Conda dependency installation and Docker image execution were not run. Windows and macOS were not available.

Added explicit UTF8 subprocess handling, platform neutral migration path keys, current interpreter test commands, and exact CLI version checking. Added native, venv and Conda setup planning plus Docker build instructions. JSON and YAML parsed successfully. The GitHub Actions matrix is supplied but has not run remotely.

## Conda setup guidance update

7 September 2026: five tooling tests passed locally using `python3 -m unittest discover -s tests -p test_tooling.py -v`. The new subprocess regression test uses the current Python interpreter and verifies that `--conda-name my_spec_tools` reaches the creation command in preview without installing an environment. Documentation links, code fences and diff whitespace were checked.

The existing environment-name option now has CLI help, and successful Conda setup prints activation guidance. Actual Conda creation, post-install activation and Windows/macOS shell behaviour were not executed for this change. The full installation suite was not rerun for this focused setup/documentation update.
