# Use this as your tooling repository

Extract the archive, open the spec_kit_engineering directory and push its contents as the root of a new repository. Keep project/, preset/, extension/, tests/, the installation files and documentation. Do not push .venv, caches or credentials; ignore rules are included.

Example initialisation, after substituting your actual Git remote:

```text
git init -b main
git add .
git commit -m "Add Spec Kit engineering package"
git remote add origin YOUR_GIT_REMOTE
git push -u origin main
```

No remote has been created or pushed by this task. Choose a licence and ownership notice before publishing the custom material publicly. The included NOTICE.md identifies official upstream; the custom package is not an official GitHub product.

This tooling repository is distinct from your firmware, service or data science repository. Install it into those repositories with install.py. Commit the agreed generated project instructions there so every clone receives the same workflow version.

The included .github/workflows/validate.yml runs utility and installation checks on Linux, Windows and macOS, plus a Linux Docker build. These jobs install the pinned official Spec Kit dependency. They do not install a coding agent or require an LLM subscription. You will see the first actual remote platform results after pushing to GitHub.

Keep upstream.lock.json and requirements.txt in agreement. Retest a new official Spec Kit version before changing the pin. The preset and extension compatibility requirements must change in the same review. Initial installation checks reject a different CLI version.

Retain existing project commands and authored documents when upgrading. Current install.py intentionally rejects conflicts rather than guessing how to merge them. A general upgrade manager is future work.
