"""Load and validate local seed data."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SEED_DIR = PROJECT_ROOT / "data" / "seed"
SCHEMA_DIR = PROJECT_ROOT / "schemas"
COLLECTIONS = ("topics", "groups", "scholars", "papers", "repositories")


def load_collection(name: str, seed_dir: Path = SEED_DIR) -> list[dict[str, Any]]:
    if name not in COLLECTIONS:
        raise ValueError(f"Unknown collection: {name}")
    # JSON is a strict subset of YAML, keeping seed files YAML-compatible while
    # allowing the foundation to install without a runtime parser dependency.
    payload = json.loads((seed_dir / f"{name}.yaml").read_text())
    records = payload.get(name)
    if not isinstance(records, list):
        raise ValueError(f"{name}.yaml must contain a '{name}' list")
    return records


def load_all(seed_dir: Path = SEED_DIR) -> dict[str, list[dict[str, Any]]]:
    return {name: load_collection(name, seed_dir) for name in COLLECTIONS}


def validate_all(seed_dir: Path = SEED_DIR, schema_dir: Path = SCHEMA_DIR) -> list[str]:
    errors = []
    for name in COLLECTIONS:
        schema_name = {"groups": "group", "repositories": "repository"}.get(
            name, name.removesuffix("s")
        )
        schema = json.loads((schema_dir / f"{schema_name}.schema.json").read_text())
        for index, record in enumerate(load_collection(name, seed_dir)):
            prefix = f"{name}[{index}]"
            missing = set(schema["required"]) - set(record)
            unknown = set(record) - set(schema["properties"])
            errors.extend(f"{prefix} missing required property '{key}'" for key in sorted(missing))
            errors.extend(f"{prefix} unknown property '{key}'" for key in sorted(unknown))
            for key, value in record.items():
                rule = schema["properties"].get(key, {})
                expected = rule.get("type")
                expected = expected if isinstance(expected, list) else [expected]
                matches = (
                    ("null" in expected and value is None)
                    or ("string" in expected and isinstance(value, str))
                    or ("array" in expected and isinstance(value, list))
                    or ("object" in expected and isinstance(value, dict))
                    or ("integer" in expected and isinstance(value, int) and not isinstance(value, bool))
                    or ("number" in expected and isinstance(value, (int, float)) and not isinstance(value, bool))
                )
                if expected != [None] and not matches:
                    errors.append(f"{prefix}.{key} has invalid type")
    return errors
