import json
import os
from pathlib import Path

import pytest

from researchrank import cli
from researchrank.export import export_json, export_markdown


@pytest.fixture
def unicode_catalog():
    return {
        "scholars": [{"name": "李明 / Zoë 🚀", "id": "unicode-scholar"}],
        "papers": [{"title": "Δοκιμή — 日本語", "id": "unicode-paper"}],
    }


def expected_file_bytes(content):
    # Preserve the exporters' existing platform-native newline behavior.
    return content.replace("\n", os.linesep).encode("utf-8")


def test_json_unicode_roundtrip_and_deterministic_utf8_bytes(tmp_path, unicode_catalog):
    output = tmp_path / "catalog.json"
    rendered = export_json(unicode_catalog, output)
    expected = (
        '{\n  "papers": [\n    {\n      "id": "unicode-paper",\n'
        '      "title": "Δοκιμή — 日本語"\n    }\n  ],\n'
        '  "scholars": [\n    {\n      "id": "unicode-scholar",\n'
        '      "name": "李明 / Zoë 🚀"\n    }\n  ]\n}\n'
    )
    assert rendered == expected
    assert output.read_bytes() == expected_file_bytes(expected)
    assert json.loads(output.read_text(encoding="utf-8")) == unicode_catalog

    repeated = tmp_path / "repeated.json"
    assert export_json(unicode_catalog, repeated) == rendered
    assert export_json(unicode_catalog) == rendered
    assert repeated.read_bytes() == output.read_bytes()


def test_markdown_unicode_content_and_deterministic_utf8_bytes(tmp_path, unicode_catalog):
    output = tmp_path / "catalog.md"
    rendered = export_markdown(unicode_catalog, output)
    expected = (
        "# ResearchRank Seed Catalog\n\n"
        "> Examples only; not authoritative rankings.\n\n"
        "## Scholars\n\n- **李明 / Zoë 🚀** (`unicode-scholar`)\n\n"
        "## Papers\n\n- **Δοκιμή — 日本語** (`unicode-paper`)\n"
    )
    assert rendered == expected
    assert output.read_bytes() == expected_file_bytes(expected)
    assert output.read_text(encoding="utf-8") == rendered

    repeated = tmp_path / "repeated.md"
    assert export_markdown(unicode_catalog, repeated) == rendered
    assert export_markdown(unicode_catalog) == rendered
    assert repeated.read_bytes() == output.read_bytes()


@pytest.mark.parametrize("exporter", [export_json, export_markdown])
def test_exports_use_utf8_with_a_non_utf8_default(
    tmp_path, monkeypatch, unicode_catalog, exporter
):
    original_write_text = Path.write_text
    encodings = []

    def write_with_windows_default(path, content, encoding=None, **kwargs):
        encodings.append(encoding)
        return original_write_text(path, content, encoding=encoding or "cp1252", **kwargs)

    monkeypatch.setattr(Path, "write_text", write_with_windows_default)
    output = tmp_path / "catalog.txt"
    rendered = exporter(unicode_catalog, output)

    assert encodings == ["utf-8"]
    assert output.read_bytes() == expected_file_bytes(rendered)


@pytest.mark.parametrize(
    ("command", "filename"),
    [("export-json", "catalog.json"), ("export-markdown", "catalog.md")],
)
def test_cli_unicode_stdout_matches_file(
    tmp_path, monkeypatch, capsys, unicode_catalog, command, filename
):
    monkeypatch.setattr(cli, "load_all", lambda: unicode_catalog)
    assert cli.main([command]) == 0
    stdout = capsys.readouterr()
    assert stdout.err == ""

    output = tmp_path / filename
    assert cli.main([command, "--output", str(output)]) == 0
    file_run = capsys.readouterr()
    assert file_run.out == file_run.err == ""
    assert output.read_text(encoding="utf-8") == stdout.out
    assert output.read_bytes() == expected_file_bytes(stdout.out)
