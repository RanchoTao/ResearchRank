# MVP roadmap

## Current foundation

v0 provides schemas and examples, Python models, strict local validation, transparent group scoring, CLI discovery, exports, tests, and architectural/curation policy. It intentionally omits production rankings, scraping, a database/API, automatic identity resolution, scheduled refresh, authentication, and a web interface.

## Next five development steps

1. **Evidence and provenance:** add observation/source schemas, `as_of` timestamps, licenses, confidence, and score-policy versions.
2. **Relationship integrity:** validate cross-file IDs, add Institution and DatasetBenchmark persistence, and introduce temporal affiliations/memberships.
3. **Cohort score policies:** define field-reviewed normalization, missing-data handling, scholar/paper scorecards, uncertainty, and sensitivity tests.
4. **Thin ingestion adapters:** implement one rate-limited primary API connector (likely OpenAlex) plus GitHub snapshots, retaining raw responses and requiring reconciliation review.
5. **Read API prototype:** move reviewed snapshots to PostgreSQL behind FastAPI, then validate the model with a minimal topic/radar view before committing to Next.js, graph, or vector-search infrastructure.

## Exit criteria before public ranking

A public pilot requires documented cohort definitions, evidence coverage and freshness indicators, identity-review workflows, reproducible policy-versioned calculations, correction/dispute handling, bias review, and multiple field experts approving representative samples.
