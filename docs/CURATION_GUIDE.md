# Curation guide

## Source priority

Prefer primary, durable sources: paper landing pages/DOIs and proceedings; arXiv/OpenReview; OpenAlex or Semantic Scholar snapshots; official repository APIs; official dataset, benchmark, lab, and institution pages. DBLP is valuable for bibliography. Record Papers With Code and Hugging Face as ecosystem evidence. Treat personal pages as identity evidence and use Google Scholar only manually or through legal access.

## Workflow

1. Choose a narrowly defined topic and inclusion window.
2. Create or match stable IDs; record aliases rather than duplicating entities.
3. Capture the source URL, retrieval date, metric definition, and evidence supporting each claim (the evidence object is a planned schema addition).
4. Leave unknown values null/empty; never invent citations, membership, or scores.
5. Run `researchrank validate`, inspect relationship IDs, and request topical review.
6. Explain corrections and curator adjustments in notes; preserve superseded evidence in history once that layer exists.

## Style and disputes

Use neutral descriptions, distinguish affiliations by date, and avoid superlatives unsupported by cohort evidence. Seed examples and provisional hypotheses must be labeled. A contested record should remain visible with its evidence and curator note; corrections should be reviewable pull requests. Conflicts of interest should be disclosed.

## Limitations

Coverage and English-language/source availability can bias results. Citations mature at different rates and can be gamed; stars are volatile; author order differs by field; group boundaries and affiliations change. Entity resolution produces ambiguity. Opportunity and overcrowding scores are hypotheses, not forecasts. UI and exports must communicate freshness, missingness, and uncertainty.
