# Scoring

Scores are **topic- and cohort-specific scorecards**, never universal measures of quality. v0 demonstrates a group calculation only. Inputs are normalized to 0–100 by a future, versioned field policy; absent values currently contribute zero and therefore mean “no credited evidence,” not proven lack of impact.

## v0 group formula

| Component | Weight |
|---|---:|
| Recent top-venue papers | 0.15 |
| Representative paper score | 0.20 |
| Open-source score | 0.15 |
| Benchmark score | 0.10 |
| Student pipeline score | 0.10 |
| Industry adoption score | 0.10 |
| Growth score | 0.15 |
| Curator adjustment | 0.05 |

`total_score = Σ(component value × component weight)`. The API returns `total_score` plus each value, weight, and weighted score. Inputs outside 0–100 and unknown components fail rather than being silently clipped. Placeholder seed inputs test mechanics only.

## Planned scorecards

Scholar dimensions include recent output, representative work, citations, authorship contribution, open source, datasets/benchmarks, topic definition, collaboration, growth, and curator adjustment. Paper dimensions include citations, venue context, problem definition, originality, datasets/benchmarks, open-source adoption, downstream influence, and adjustment. Group scorecards later add topic definition and field centrality.

## Guardrails

Every published calculation needs a topic/cohort, observation window, `as_of` date, policy version, source links, uncertainty/missingness, and complete breakdown. Field curators should calibrate normalization and venue context. Adjustments require a rationale and review trail. Rankings should support sensitivity views and never use a total to conceal disputed components.
