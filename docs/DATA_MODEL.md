# Data model

Entities use stable slug IDs; relationship fields contain IDs rather than embedded objects. JSON Schemas define current persisted seed contracts, while Python dataclasses support application use.

- **Topic:** parent coarse field, aliases and relations, key entities, trend label, and optional overcrowding/opportunity hypotheses.
- **Scholar:** identity aliases and external IDs, affiliation, role/career stage, topics, work, and groups.
- **ResearchGroup:** institution and geography, people, topics, representative artifacts, qualitative strengths/limitations, and score inputs.
- **Institution:** departments, groups, and scholars. It is modeled in Python but persistence/schema is deferred because it is not a requested v0 seed collection.
- **Paper:** bibliographic identifiers, authorship, links, nullable sourced metrics, topics, contribution type, and rank signals.
- **Repository:** owner/link, nullable snapshot metrics, license/activity metadata, related entities, and integrations.
- **DatasetBenchmark:** creator, task/field, paper, users, and leaderboard. Like Institution, storage is deferred in v0.

## Conventions

Empty strings/lists mean “not supplied”; `null` is used for unknown numeric observations and must not be interpreted as zero. Dates use ISO 8601. Topic relationships should use IDs in canonical data; the group CLI currently accepts human topic labels because the examples demonstrate user-facing filtering.

## Evolution required

Before real ranking, add an `EvidenceObservation` with source, observed value, retrieval time, method, license, confidence, and supersession history. Add aliases/identity claims, membership date ranges, field cohorts, scoring policy versions, and curator decisions. Many-to-many relations should then become temporal join records. Migrations must preserve source snapshots and distinguish corrections from metric refreshes.
