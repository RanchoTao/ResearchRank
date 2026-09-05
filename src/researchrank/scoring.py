"""Explicit scorecards; totals are meaningful only inside a topic/field cohort."""

from dataclasses import dataclass
from typing import Mapping

GROUP_WEIGHTS = {
    "top_venue_papers_recent": 0.15,
    "representative_paper_score": 0.20,
    "open_source_score": 0.15,
    "benchmark_score": 0.10,
    "student_pipeline_score": 0.10,
    "industry_adoption_score": 0.10,
    "growth_score": 0.15,
    "curator_adjustment": 0.05,
}


@dataclass(frozen=True)
class ScoreResult:
    total_score: float
    score_breakdown: dict[str, dict[str, float]]

    def as_dict(self) -> dict:
        return {"total_score": self.total_score, "score_breakdown": self.score_breakdown}


def score_group(inputs: Mapping[str, float], weights: Mapping[str, float] = GROUP_WEIGHTS) -> ScoreResult:
    """Return a weighted 0–100 score and every auditable component."""
    unexpected = set(inputs) - set(weights)
    if unexpected:
        raise ValueError(f"Unknown score components: {sorted(unexpected)}")
    breakdown = {}
    for component, weight in weights.items():
        value = float(inputs.get(component, 0))
        if not 0 <= value <= 100:
            raise ValueError(f"{component} must be between 0 and 100")
        breakdown[component] = {
            "value": value,
            "weight": float(weight),
            "weighted_score": round(value * weight, 3),
        }
    return ScoreResult(round(sum(item["weighted_score"] for item in breakdown.values()), 3), breakdown)
