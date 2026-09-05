"""Command-line interface for the local MVP."""

import argparse
import json
from pathlib import Path

from .export import export_json, export_markdown
from .loaders import load_all, load_collection, validate_all
from .scoring import score_group


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="researchrank")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("validate")
    commands.add_parser("list-topics")
    groups = commands.add_parser("list-groups")
    groups.add_argument("--topic")
    score = commands.add_parser("score-group")
    score.add_argument("group_id")
    for command in ("export-json", "export-markdown"):
        export = commands.add_parser(command)
        export.add_argument("--output", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "validate":
        errors = validate_all()
        if errors:
            print("\n".join(errors))
            return 1
        print("All seed records are valid.")
    elif args.command == "list-topics":
        for topic in load_collection("topics"):
            print(f"{topic['id']}\t{topic['name']}\t[{topic['parent_field']}]")
    elif args.command == "list-groups":
        groups = load_collection("groups")
        for group in groups:
            if not args.topic or args.topic.casefold() in {item.casefold() for item in group["topics"]}:
                print(f"{group['id']}\t{group['name']}")
    elif args.command == "score-group":
        group = next((item for item in load_collection("groups") if item["id"] == args.group_id), None)
        if group is None:
            build_parser().error(f"unknown group id: {args.group_id}")
        print(json.dumps(score_group(group.get("score_inputs", {})).as_dict(), indent=2))
    else:
        data = load_all()
        render = export_json if args.command == "export-json" else export_markdown
        content = render(data, args.output)
        if not args.output:
            print(content, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
