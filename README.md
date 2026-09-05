# ResearchRank

ResearchRank is an early-stage, local-first foundation for **field-specific research intelligence**. It models scholars, groups, papers, repositories, and topics, then exposes auditable scorecards within a coherent topic—not a universal league table. Publication cultures and citation dynamics differ too much to compare unrelated fields responsibly.

> **Data status:** everything under `data/seed/` is an illustrative, incomplete seed example. Names do not imply rank or endorsement; placeholder score inputs are for exercising the software.

## MVP capabilities

- YAML-compatible JSON seed records checked against JSON Schema contracts.
- Python dataclass domain models with explicit relationships.
- A group scorecard returning both a total and component-level calculation.
- Local filtering and deterministic JSON/Markdown exports.
- An architecture path toward evidence snapshots, provenance, APIs, and an opportunity radar.

## Quick start

```bash
python -m pip install -e .
pytest
researchrank validate
researchrank list-topics
researchrank list-groups --topic "Efficient LLM/VLM Inference"
researchrank score-group mit-han-lab
researchrank export-json --output catalog.json
researchrank export-markdown --output catalog.md
```

Without `--output`, export commands print to standard output. Commands resolve bundled seed data independent of the current directory.

## Repository map

- `src/researchrank/`: models, loaders, scorecard, exporters, and CLI.
- `data/seed/`: curator-maintained examples; `data/processed/` is reserved for generated snapshots.
- `schemas/`: strict JSON Schemas for the five MVP seed collections.
- `docs/`: vision, architecture, model, scoring, taxonomy, curation, and roadmap decisions.
- `tests/`: model/schema and scoring behavior.

## Boundaries

v0 has no scraper, database, API, identity resolution, live metric refresh, production ranking, or web UI. See [the roadmap](docs/MVP_ROADMAP.md), [scoring contract](docs/SCORING.md), and [curation guide](docs/CURATION_GUIDE.md).
