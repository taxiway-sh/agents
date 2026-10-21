#!/usr/bin/env python3
"""Validate heartbeats, machine queue items and deployed.json.

The schemas come from Taxiway main.
Usage: check-status.py ROOT STATUS_SCHEMA QUEUE_SCHEMA
"""
import json
import pathlib
import sys

from jsonschema import Draft202012Validator, FormatChecker

root = pathlib.Path(sys.argv[1])
schema = json.loads(pathlib.Path(sys.argv[2]).read_text())
validator = Draft202012Validator(schema, format_checker=FormatChecker())
queue_schema = json.loads(pathlib.Path(sys.argv[3]).read_text())
queue_validator = Draft202012Validator(queue_schema, format_checker=FormatChecker())
errors = []
for path in sorted((root / "status").glob("*.json")):
    try:
        data = json.loads(path.read_text())
    except ValueError as err:
        errors.append(f"{path.name}: invalid JSON: {err}")
        continue
    for error in validator.iter_errors(data):
        errors.append(f"{path.name}: {error.message}")
    if isinstance(data, dict) and data.get("id") != path.stem:
        errors.append(f"{path.name}: id must be {path.stem!r}")
for path in sorted((root / "queue" / "machine").glob("*.json")):
    try:
        data = json.loads(path.read_text())
    except ValueError as err:
        errors.append(f"queue/machine/{path.name}: invalid JSON: {err}")
        continue
    for error in queue_validator.iter_errors(data):
        errors.append(f"queue/machine/{path.name}: {error.message}")
    if isinstance(data, dict) and data.get("id") != path.stem:
        errors.append(f"queue/machine/{path.name}: id must be {path.stem!r}")
deployed = json.loads((root / "deployed.json").read_text())
if not isinstance(deployed.get("agents"), dict):
    errors.append("deployed.json: agents must be an object")
for error in errors:
    print(f"FAIL: {error}", file=sys.stderr)
sys.exit(1 if errors else 0)
