"""Deterministic exports suitable for downstream APIs or review."""

import json
from pathlib import Path
from typing import Any


def export_json(data: dict[str, list[dict[str, Any]]], output: Path | None = None) -> str:
    rendered = json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if output:
        output.write_text(rendered)
    return rendered


def export_markdown(data: dict[str, list[dict[str, Any]]], output: Path | None = None) -> str:
    lines = ["# ResearchRank Seed Catalog", "", "> Examples only; not authoritative rankings.", ""]
    for collection, records in data.items():
        lines.extend([f"## {collection.title()}", ""])
        for record in records:
            label = record.get("name") or record.get("title") or record["id"]
            lines.append(f"- **{label}** (`{record['id']}`)")
        lines.append("")
    rendered = "\n".join(lines)
    if output:
        output.write_text(rendered)
    return rendered
