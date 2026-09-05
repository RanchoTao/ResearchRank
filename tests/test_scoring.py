import pytest

from researchrank.scoring import score_group


def test_group_score_is_transparent_and_weighted():
    result = score_group({"open_source_score": 80, "growth_score": 60})
    assert result.total_score == 21
    assert result.score_breakdown["open_source_score"] == {
        "value": 80.0, "weight": 0.15, "weighted_score": 12.0
    }
    assert set(result.score_breakdown) == {
        "top_venue_papers_recent", "representative_paper_score", "open_source_score",
        "benchmark_score", "student_pipeline_score", "industry_adoption_score",
        "growth_score", "curator_adjustment",
    }


def test_group_score_rejects_out_of_range_values():
    with pytest.raises(ValueError, match="between 0 and 100"):
        score_group({"growth_score": 101})


def test_group_score_rejects_unknown_components():
    with pytest.raises(ValueError, match="Unknown score components"):
        score_group({"prestige": 100})
