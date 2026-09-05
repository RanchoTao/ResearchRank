# Architecture

## v0: local, inspectable pipeline

```text
curated YAML -> JSON Schema validation -> dataclass models
             -> topic filtering / scorecards -> JSON or Markdown exports
```

`loaders.py` owns file access and schema validation. `models.py` defines domain boundaries without persistence concerns. `scoring.py` is a pure calculation layer. `export.py` creates deterministic interchange and review formats; `cli.py` is the thin composition layer. Stable string IDs provide relationships between records. Raw evidence must eventually be represented separately from derived scores.

The architecture favors boring files and pure functions: seed changes are reviewable in Git, schema evolution is explicit, calculations can be reproduced, and a database is not required to explore the model.

## Connector boundary

Future connectors for arXiv, OpenAlex, Semantic Scholar, DBLP, OpenReview, Papers With Code, GitHub, Hugging Face, proceedings, labs, and institutions should emit normalized observations with source URL, retrieval time, license, and raw snapshot reference. They must not write directly into curated canonical records. Google Scholar data should enter only through legal access or documented manual curation.

A reconciliation stage will match observations to identities, surface ambiguity, and require review before publishing corrections. Generated data belongs outside `data/seed/`.

## Future service shape

A compatible evolution is PostgreSQL for canonical and temporal observations, background ingestion workers, and a FastAPI read/curation API. A Next.js client could add field/topic, scholar, group, and paper pages; graph visualization; vector search over papers and curator notes; and an opportunity-radar dashboard. The CLI and export formats remain useful for reproducibility and bulk review.

## Quality and security boundaries

Validate at ingestion, preserve raw provenance, use allowlisted connector behavior, rate limits, secrets outside the repository, and role-based review for edits. Derived outputs need a scoring-policy version and `as_of` time. Caches and APIs should never make stale metrics appear current.
