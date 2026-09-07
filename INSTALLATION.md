# Installation on Windows, Linux and macOS

Use this repository as the tooling distribution. Keep it outside the software repository you want to configure. Machine setup installs official Spec Kit; install.py then installs the project files. The same tooling environment can serve multiple project clones.

The default is a Python virtual environment. Native Python, Conda and Docker are alternatives. None of these methods installs a coding assistant, compiler, board SDK, semantic index engine or model subscription.

## Prerequisites and validation scope

| Method | Windows | Linux | macOS | Prerequisites |
| --- | --- | --- | --- | --- |
| Native Python | PowerShell commands below | Shell commands below | Shell commands below | Python 3.11 or newer with pip; Git on PATH |
| venv | Scripts directory | bin directory | bin directory | Python with venv and pip; Git on PATH |
| Conda | Anaconda Prompt or initialised shell | Initialised shell | Initialised shell | Conda or Miniforge; environment includes Python, pip and Git |
| Docker | Docker Desktop using Linux containers | Docker Engine | Docker Desktop using Linux containers | Docker running; target directory exists and is shared with Docker |

These paths are supplied, but only Linux utility and integration execution has been tested here. Native dependency installation, Conda, Windows, macOS and Docker image execution are not claimed as tested. The supplied GitHub Actions workflow will exercise three operating systems and a Linux Docker build after you push it. It has not run remotely yet.

If Python, Git, Conda or Docker is missing, install it using your organisation's approved method first. Some Linux distributions package venv separately. Do not override an operating system managed Python restriction; use venv or Conda if native pip refuses installation.

## Recommended: venv

Linux and macOS, from this tooling repository:

```bash
python3 setup_tooling.py --mode venv --apply
python3 install.py /absolute/path/to/project --integration copilot
python3 install.py /absolute/path/to/project --integration copilot --apply
```

Windows PowerShell:

```powershell
py -3 setup_tooling.py --mode venv --apply
py -3 install.py C:\work\project --integration copilot
py -3 install.py C:\work\project --integration copilot --apply
```

Use a Python 3.11 or newer interpreter. The setup creates .venv beside install.py and installs the pinned official CLI. install.py detects .venv/bin/specify on Linux and macOS or .venv/Scripts/specify.exe on Windows. Activation is unnecessary. Omit --apply from setup_tooling.py to inspect the dependency installation commands without executing them.

To use a custom environment path:

```bash
python3 setup_tooling.py --mode venv --env-dir /path/to/toolenv --apply
python3 install.py /path/to/project --specify /path/to/toolenv/bin/specify --integration copilot --apply
```

On Windows, the equivalent executable is C:\path\to\toolenv\Scripts\specify.exe. Quote paths containing spaces. Virtual environments are recreated per machine and are never pushed to Git or copied between operating systems.

## Native Python

Linux and macOS:

```bash
python3 setup_tooling.py --mode native --apply
python3 install.py /path/to/project --specify /path/to/user/scripts/specify --integration copilot --apply
```

Windows:

```powershell
py -3 setup_tooling.py --mode native --apply
py -3 install.py C:\work\project --specify C:\path\to\Scripts\specify.exe --integration copilot --apply
```

Outside an active venv or Conda environment, this uses pip's user installation. Add that Python user scripts directory to PATH, or provide its full specify path as shown. Inside an active environment it installs into that environment. Replace the example paths with the location pip reports. A managed Python installation may reject native installation even with user scope.

## Conda or Miniforge

From this tooling repository in a Conda enabled shell on any supported OS:

```text
conda env create --file environment.yml
conda run -n spec_kit_engineering python install.py /path/to/project --integration copilot
conda run -n spec_kit_engineering python install.py /path/to/project --integration copilot --apply
```

Use a Windows path such as C:\work\project on Windows. Environment activation is optional because conda run selects the environment. To create a differently named environment, add --name YOUR_NAME to conda env create and use the same name with conda run.

The Python helper offers the equivalent creation path when Python and Conda are already available:

```text
python setup_tooling.py --mode conda --conda-name spec_kit_engineering --apply
```

Creation stops if the named environment already exists. Deliberate updates can use conda env update --file environment.yml. Review dependency changes before updating a shared team environment.

## Docker

Build the tooling image from this repository:

```text
docker build -t spec_kit_engineering:1.1 .
```

Linux example, preserving host file ownership:

```bash
docker run --rm --user "$(id -u):$(id -g)" --env XDG_CACHE_HOME=/tmp/cache --mount "type=bind,source=/absolute/path/to/project,target=/repo" spec_kit_engineering:1.1 /repo --integration copilot --apply
```

macOS example:

```bash
docker run --rm --mount "type=bind,source=/absolute/path/to/project,target=/repo" spec_kit_engineering:1.1 /repo --integration copilot --apply
```

Windows PowerShell example:

```powershell
docker run --rm --mount "type=bind,source=C:\work\project,target=/repo" spec_kit_engineering:1.1 /repo --integration copilot --apply
```

The target directory must already exist. Omit --apply to preview. Only the mounted target is installed into; source files and existing authored instructions are protected by installer conflict checks. This is a Linux tooling container on all three hosts, not a Windows container. It creates repository instructions; it does not run your IDE or agents. Local agent bootstrap later still needs Python and Git in the agent's execution environment.

The image downloads dependencies while building. Runtime project staging uses the official CLI's bundled assets. The Python image tag and transitive dependencies are not fully locked by digest; upstream.lock.json pins Spec Kit itself, not the entire operating system or dependency graph.

## Choose agents

Any installation method can select codex, cursor-agent or copilot. Repeat the integration option to prepare one project for all three:

```text
python install.py /path/to/project --integration codex --integration cursor-agent --integration copilot --apply
```

Replace python with python3 or py -3 where appropriate. The installer uses only the documented explicit upstream multiple integration option in disposable staging, renders customisations for each integration, then restores the first as default.

## Existing Spec Kit projects

The full installer is intentionally conservative and stops on differing existing files. It is not a general upgrade or merge tool. You can use the official CLI directly inside an existing project:

```text
specify extension add --dev /path/to/this/tooling/extension
specify preset add --dev /path/to/this/tooling/preset
```

Use Specify CLI 1.0.4. Compare and merge the relevant files from project/ into your project, especially AI_CONTEXT.md, domain configuration, utilities and the constitution. Preserve authored values. The extension and preset alone expect those companion files and are not a complete standalone installation. Installing them does not overwrite the live constitution with our seed.

For the recognised unchanged v6 baseline, use the --migrate-v6 option described in MIGRATION.md. For a new clone whose configuration is already committed, install machine tooling only; do not regenerate its repository files.

## Official references

[Spec Kit](https://github.com/github/spec-kit)

[Python virtual environments](https://docs.python.org/3/library/venv.html)

[Conda environment management](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html)

[Docker bind mounts](https://docs.docker.com/engine/storage/bind-mounts/)
