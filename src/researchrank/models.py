"""Small, dependency-free domain models for curated ResearchRank records."""

from __future__ import annotations

from dataclasses import dataclass, field as model_field, fields
from typing import Any, TypeVar

T = TypeVar("T", bound="Record")


@dataclass
class Record:
    id: str
    name: str
    notes: str = ""

    @classmethod
    def from_dict(cls: type[T], data: dict[str, Any]) -> T:
        allowed = {item.name for item in fields(cls)}
        unknown = set(data) - allowed
        if unknown:
            raise ValueError(f"Unknown {cls.__name__} fields: {sorted(unknown)}")
        return cls(**data)


@dataclass
class Topic(Record):
    parent_field: str = ""
    aliases: list[str] = model_field(default_factory=list)
    description: str = ""
    related_topics: list[str] = model_field(default_factory=list)
    key_papers: list[str] = model_field(default_factory=list)
    key_groups: list[str] = model_field(default_factory=list)
    key_scholars: list[str] = model_field(default_factory=list)
    key_repositories: list[str] = model_field(default_factory=list)
    trend_status: str = "unknown"
    overcrowding_score: float | None = None
    opportunity_score: float | None = None


@dataclass
class Scholar(Record):
    aliases: list[str] = model_field(default_factory=list)
    current_affiliation: str = ""
    homepage_url: str = ""
    google_scholar_url: str = ""
    semantic_scholar_id: str = ""
    openalex_id: str = ""
    dblp_url: str = ""
    github_username: str = ""
    x_twitter_url: str = ""
    role: str = ""
    career_stage: str = ""
    topics: list[str] = model_field(default_factory=list)
    representative_papers: list[str] = model_field(default_factory=list)
    affiliated_groups: list[str] = model_field(default_factory=list)
    created_at: str = ""
    updated_at: str = ""


@dataclass
class ResearchGroup(Record):
    aliases: list[str] = model_field(default_factory=list)
    institution: str = ""
    country_or_region: str = ""
    homepage_url: str = ""
    pi_scholars: list[str] = model_field(default_factory=list)
    members: list[str] = model_field(default_factory=list)
    alumni: list[str] = model_field(default_factory=list)
    topics: list[str] = model_field(default_factory=list)
    representative_papers: list[str] = model_field(default_factory=list)
    representative_repositories: list[str] = model_field(default_factory=list)
    representative_datasets: list[str] = model_field(default_factory=list)
    representative_benchmarks: list[str] = model_field(default_factory=list)
    strengths: list[str] = model_field(default_factory=list)
    limitations: list[str] = model_field(default_factory=list)
    score_inputs: dict[str, float] = model_field(default_factory=dict)
    created_at: str = ""
    updated_at: str = ""


@dataclass
class Institution(Record):
    aliases: list[str] = model_field(default_factory=list)
    country_or_region: str = ""
    homepage_url: str = ""
    type: str = ""
    departments: list[str] = model_field(default_factory=list)
    groups: list[str] = model_field(default_factory=list)
    scholars: list[str] = model_field(default_factory=list)


@dataclass
class Paper(Record):
    title: str = ""
    authors: list[str] = model_field(default_factory=list)
    year: int | None = None
    venue: str = ""
    arxiv_id: str = ""
    doi: str = ""
    openreview_url: str = ""
    semantic_scholar_id: str = ""
    openalex_id: str = ""
    code_urls: list[str] = model_field(default_factory=list)
    project_url: str = ""
    dataset_urls: list[str] = model_field(default_factory=list)
    benchmark_urls: list[str] = model_field(default_factory=list)
    citation_count: int | None = None
    influential_citation_count: int | None = None
    topics: list[str] = model_field(default_factory=list)
    contribution_type: str = ""
    rank_signals: dict[str, float] = model_field(default_factory=dict)


@dataclass
class Repository(Record):
    owner: str = ""
    github_url: str = ""
    stars: int | None = None
    forks: int | None = None
    watchers: int | None = None
    license: str = ""
    last_commit_at: str = ""
    created_at: str = ""
    related_papers: list[str] = model_field(default_factory=list)
    related_groups: list[str] = model_field(default_factory=list)
    related_scholars: list[str] = model_field(default_factory=list)
    package_or_framework_integrations: list[str] = model_field(default_factory=list)


@dataclass
class DatasetBenchmark(Record):
    type: str = ""
    homepage_url: str = ""
    paper: str = ""
    task: str = ""
    field: str = ""
    created_by: list[str] = model_field(default_factory=list)
    used_by_papers: list[str] = model_field(default_factory=list)
    leaderboard_url: str = ""
