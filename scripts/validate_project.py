"""Validate distribution metadata, source pins, schemas and workflow YAML."""

import json
from pathlib import Path
import tomllib

from jsonschema import Draft202012Validator
import yaml

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(root=ROOT):
    project = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))["project"]
    pin = json.loads((root / "upstream.lock.json").read_text(encoding="utf-8"))
    require(project["version"] == pin["package_version"], "Package versions differ")
    require(project["license"] == "MIT", "Package license metadata differs from LICENSE")
    expected = f"specify-cli @ git+{pin['upstream_repository']}.git@{pin['upstream_commit']}"
    requirements = [
        line
        for line in (root / "requirements.txt").read_text(encoding="utf-8").splitlines()
        if line and not line.startswith("#")
    ]
    require(requirements == [expected], "requirements.txt and upstream.lock.json differ")
    for path in root.glob("project/ai_workflow/**/*.json"):
        value = json.loads(path.read_text(encoding="utf-8"))
        if "$schema" in value:
            Draft202012Validator.check_schema(value)
    schema = json.loads((root / "project/ai_workflow/bootstrap.schema.json").read_text(encoding="utf-8"))
    Draft202012Validator(schema).validate(
        json.loads((root / "project/ai_workflow/bootstrap.json").read_text(encoding="utf-8"))
    )
    for folder in ("project", "preset", "extension", ".github"):
        for pattern in ("**/*.yml", "**/*.yaml"):
            for path in (root / folder).glob(pattern):
                list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
    for name in ("LICENSE", "NOTICE.md", "CONTRIBUTING.md", "SECURITY.md", "CODE_OF_CONDUCT.md", "SUPPORT.md", "CI.md"):
        require((root / name).is_file(), f"Missing community documentation: {name}")


if __name__ == "__main__":
    validate()
    print("Distribution contracts passed.")
