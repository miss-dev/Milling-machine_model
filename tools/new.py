#!/usr/bin/env python3
"""Create a new project document from a template.

Fills in the ID, date and author, puts the file in the right folder and,
where there is one, adds a row to that folder's index table.

Examples:
  python tools/new.py log "Ada Lovelace"
  python tools/new.py meeting mentor
  python tools/new.py experiment "Sleep current"
  python tools/new.py decision "Use MQTT for telemetry"
  python tools/new.py trade-study "Which microcontroller?"
  python tools/new.py subsystem "Sensing"
  python tools/new.py dataset "Field images"
  python tools/new.py model "Fault classifier"
  python tools/new.py review 2

Needs Python 3.8+ and nothing else.
"""

import argparse
import datetime
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates"
DOCS = ROOT / "docs"

INDEX_MARKER = "<!-- index: new rows are added above this line -->"

PHASES = {
    1: ("Define", "Concept Review", "define"),
    2: ("Design", "Design Review", "design"),
    3: ("Build & Integrate", "Integration Review", "build-integrate"),
    4: ("Test & Validate", "Validation Demo", "test-validate"),
    5: ("Deliver", "Final Submission", "deliver"),
}

MEETING_TYPES = ("team", "mentor", "standup", "other")


def slugify(text):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "untitled"


def git_user():
    try:
        result = subprocess.run(
            ["git", "config", "user.name"], capture_output=True, text=True, cwd=ROOT
        )
        return result.stdout.strip()
    except OSError:
        return ""


def next_number(folder, prefix):
    numbers = []
    for path in folder.glob(f"{prefix}-*.md"):
        match = re.match(rf"{prefix}-(\d+)", path.name)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers, default=0) + 1


def render(template_name, dest, values):
    if dest.exists():
        sys.exit(f"Error: {dest.relative_to(ROOT)} already exists. Nothing was created.")
    text = (TEMPLATES / template_name).read_text(encoding="utf-8")
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8")
    print(f"Created {dest.relative_to(ROOT).as_posix()}")


def add_index_row(index_file, row):
    rel = index_file.relative_to(ROOT).as_posix()
    text = index_file.read_text(encoding="utf-8") if index_file.exists() else ""
    if INDEX_MARKER not in text:
        print(f"Reminder: add this document to the index in {rel}")
        return
    index_file.write_text(text.replace(INDEX_MARKER, f"{row}\n{INDEX_MARKER}", 1), encoding="utf-8")
    print(f"Added a row to {rel}")


def cmd_log(args, today, author):
    name = args.name
    folder = DOCS / "06-reports" / "progress-logs" / slugify(name)
    doc_id = f"LOG-{next_number(folder, 'LOG'):02d}"
    render("progress-log.md", folder / f"{doc_id}.md",
           {"ID": doc_id, "DATE": today, "AUTHOR": name})


def cmd_meeting(args, today, author):
    folder = DOCS / "07-meetings"
    dest = folder / f"{today}-{args.type}.md"
    n = 2
    while dest.exists():
        dest = folder / f"{today}-{args.type}-{n}.md"
        n += 1
    render("meeting-notes.md", dest, {"DATE": today, "TYPE": args.type, "AUTHOR": author})


def cmd_experiment(args, today, author):
    folder = DOCS / "04-testing" / "experiments"
    doc_id = f"EXP-{today}-{slugify(args.title)}"
    values = {"ID": doc_id, "TITLE": args.title, "DATE": today, "AUTHOR": author}
    render("experiment.md", folder / f"{doc_id}.md", values)
    data_readme = ROOT / "data" / doc_id / "README.md"
    if not data_readme.exists():
        render("data-readme.md", data_readme, values)
    add_index_row(folder / "README.md",
                  f"| [{doc_id}]({doc_id}.md) | {args.title} | TODO | TODO | TODO | {author} |")


def cmd_decision(args, today, author):
    folder = DOCS / "02-design" / "decisions"
    doc_id = f"DDR-{next_number(folder, 'DDR'):03d}"
    filename = f"{doc_id}-{slugify(args.title)}.md"
    render("design-decision.md", folder / filename,
           {"ID": doc_id, "TITLE": args.title, "DATE": today, "AUTHOR": author})
    add_index_row(folder / "README.md",
                  f"| [{doc_id}]({filename}) | {args.title} | Proposed | {today} |")


def cmd_trade_study(args, today, author):
    folder = DOCS / "02-design" / "trade-studies"
    doc_id = f"TS-{next_number(folder, 'TS'):03d}"
    filename = f"{doc_id}-{slugify(args.title)}.md"
    render("trade-study.md", folder / filename,
           {"ID": doc_id, "TITLE": args.title, "DATE": today, "AUTHOR": author})
    add_index_row(folder / "README.md",
                  f"| [{doc_id}]({filename}) | {args.title} | TODO | TODO | {today} |")


def cmd_subsystem(args, today, author):
    folder = DOCS / "03-subsystems"
    slug = slugify(args.name)
    render("subsystem.md", folder / slug / "README.md",
           {"TITLE": args.name, "DATE": today, "AUTHOR": author})
    add_index_row(folder / "README.md",
                  f"| [{args.name}]({slug}/README.md) | TODO | Not started | TODO | |")


def cmd_dataset(args, today, author):
    folder = ROOT / "data"
    slug = slugify(args.name)
    render("dataset.md", folder / slug / "README.md",
           {"TITLE": args.name, "DATE": today, "AUTHOR": author})
    add_index_row(folder / "README.md",
                  f"| [{args.name}]({slug}/README.md) | v1 | TODO | {author} |")


def cmd_model(args, today, author):
    folder = DOCS / "02-design" / "ml-models"
    slug = slugify(args.name)
    render("model-card.md", folder / f"{slug}.md",
           {"TITLE": args.name, "DATE": today, "AUTHOR": author})
    add_index_row(folder / "README.md",
                  f"| [{args.name}]({slug}.md) | v1 | TODO | TODO | {author} |")


def cmd_review(args, today, author):
    name, gate, slug = PHASES[args.phase]
    folder = DOCS / "06-reports" / "phase-reviews"
    filename = f"phase-{args.phase}-{slug}.md"
    render("phase-review.md", folder / filename,
           {"PHASE_NUM": str(args.phase), "PHASE_NAME": name, "GATE": gate,
            "DATE": today, "AUTHOR": author})
    add_index_row(folder / "README.md",
                  f"| [Phase {args.phase}: {name}]({filename}) | {gate} | TODO | TODO |")


def main():
    parser = argparse.ArgumentParser(
        description="Create a new project document from a template.",
        epilog="Run 'python tools/new.py <command> --help' for details on a command.",
    )
    parser.add_argument("--author", help="author name (default: your git user.name)")
    parser.add_argument("--date", help="date as YYYY-MM-DD (default: today)")
    sub = parser.add_subparsers(dest="command", metavar="<command>")
    sub.required = True

    p = sub.add_parser("log", help="your next progress log")
    p.add_argument("name", help='your name, e.g. "Ada Lovelace"')
    p.set_defaults(func=cmd_log)

    p = sub.add_parser("meeting", help="meeting notes for today")
    p.add_argument("type", nargs="?", default="team", choices=MEETING_TYPES)
    p.set_defaults(func=cmd_meeting)

    p = sub.add_parser("experiment", help="an experiment record and its data folder")
    p.add_argument("title", help='short title, e.g. "Sleep current"')
    p.set_defaults(func=cmd_experiment)

    p = sub.add_parser("decision", help="a design decision record (DDR)")
    p.add_argument("title", help='the decision, e.g. "Use MQTT for telemetry"')
    p.set_defaults(func=cmd_decision)

    p = sub.add_parser("trade-study", help="a trade study (TS)")
    p.add_argument("title", help='the question, e.g. "Which microcontroller?"')
    p.set_defaults(func=cmd_trade_study)

    p = sub.add_parser("subsystem", help="a subsystem document")
    p.add_argument("name", help='subsystem name, e.g. "Sensing"')
    p.set_defaults(func=cmd_subsystem)

    p = sub.add_parser("dataset", help="a dataset card in data/<name>/")
    p.add_argument("name", help='dataset name, e.g. "Field images"')
    p.set_defaults(func=cmd_dataset)

    p = sub.add_parser("model", help="a model card for a machine learning model")
    p.add_argument("name", help='model name, e.g. "Fault classifier"')
    p.set_defaults(func=cmd_model)

    p = sub.add_parser("review", help="a phase review (1-5)")
    p.add_argument("phase", type=int, choices=sorted(PHASES),
                   help="1 Define, 2 Design, 3 Build & Integrate, 4 Test & Validate, 5 Deliver")
    p.set_defaults(func=cmd_review)

    args = parser.parse_args()

    if args.date:
        try:
            datetime.date.fromisoformat(args.date)
        except ValueError:
            parser.error("--date must be YYYY-MM-DD")
        today = args.date
    else:
        today = datetime.date.today().isoformat()

    author = args.author or git_user() or "TODO: author"
    args.func(args, today, author)


if __name__ == "__main__":
    main()
