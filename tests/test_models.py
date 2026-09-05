from researchrank.loaders import load_all, validate_all
from researchrank.models import ResearchGroup, Topic


def test_seed_data_validates():
    assert validate_all() == []


def test_models_construct_from_seed_records():
    data = load_all()
    topic = Topic.from_dict(data["topics"][0])
    group = ResearchGroup.from_dict(data["groups"][0])
    assert topic.name == "Efficient LLM/VLM Inference"
    assert topic.id in group.topics or topic.name in group.topics


def test_model_rejects_unknown_fields():
    try:
        Topic.from_dict({"id": "x", "name": "X", "surprise": True})
    except ValueError as error:
        assert "surprise" in str(error)
    else:
        raise AssertionError("unknown fields must be rejected")
