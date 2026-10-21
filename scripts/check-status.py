#!/usr/bin/env python3
"""Validate heartbeats, machine queue items and deployed.json.

The schemas come from Taxiway main.
Usage: check-status.py ROOT STATUS_SCHEMA QUEUE_SCHEMA
"""
import json
import pathlib
import sys

from jsonschema import Draft202012Validator, FormatChecker

if len(sys.argv) != 4:
    sys.exit("usage: check-status.py ROOT STATUS_SCHEMA QUEUE_SCHEMA")
root = pathlib.Path(sys.argv[1])
errors = []


def validate(folder, schema_path):
    """Validate every JSON file in ROOT/folder and check its id matches its name."""
    schema = json.loads(pathlib.Path(schema_path).read_text())
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for path in sorted((root / folder).glob("*.json")):
        name = f"{folder}/{path.name}"
        try:
            data = json.loads(path.read_text())
        except ValueError as err:
            errors.append(f"{name}: invalid JSON: {err}")
            continue
        for error in validator.iter_errors(data):
            errors.append(f"{name}: {error.message}")
        if isinstance(data, dict) and data.get("id") != path.stem:
            errors.append(f"{name}: id must be {path.stem!r}")


validate("status", sys.argv[2])
validate("queue/machine", sys.argv[3])
deployed = json.loads((root / "deployed.json").read_text())
if not isinstance(deployed.get("agents"), dict):
    errors.append("deployed.json: agents must be an object")
for error in errors:
    print(f"FAIL: {error}", file=sys.stderr)
sys.exit(1 if errors else 0)
