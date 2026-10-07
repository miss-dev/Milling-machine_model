#!/usr/bin/env python3
"""Check the documentation for broken links and unfilled placeholders.

  python tools/check_docs.py            fail if any relative link or image is broken
  python tools/check_docs.py --todo     also list files that still contain TODO / EXAMPLE
  python tools/check_docs.py --strict   like --todo, but leftover placeholders also fail
                                        (use this before the final submission)

Links inside code blocks, inline code and HTML comments are ignored, and so is
the templates/ folder (its placeholders and links only make sense once a
document has been created from it).

Needs Python 3.8+ and nothing else.
"""

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent

SKIP_DIRS = {".git", "templates", "node_modules", ".venv", "venv", ".pio",
             "build", "install", "log"}
PLACEHOLDER_SUFFIXES = {".md", ".csv"}

LINK_RE = re.compile(r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+[\"'][^\"']*[\"'])?\s*\)")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
TODO_RE = re.compile(r"\bTODO\b")
EXAMPLE_RE = re.compile(r"\bEXAMPLE\b")


def project_files(suffixes):
    for path in sorted(ROOT.rglob("*")):
        rel_parts = path.relative_to(ROOT).parts
        if path.is_file() and path.suffix in suffixes and not SKIP_DIRS.intersection(rel_parts):
            yield path


def strip_non_prose(text):
    """Remove HTML comments, fenced code blocks and inline code."""
    text = COMMENT_RE.sub("", text)
    lines, in_fence = [], False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            lines.append("")
            continue
        lines.append("" if in_fence else INLINE_CODE_RE.sub("", line))
    return "\n".join(lines)


def broken_links(path, prose):
    problems = []
    for lineno, line in enumerate(prose.splitlines(), start=1):
        for target in LINK_RE.findall(line):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue  # external URL, mailto:, or same-page anchor
            target_path = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target_path:
                continue
            base = ROOT if target_path.startswith("/") else path.parent
            if not (base / target_path.lstrip("/")).exists():
                problems.append((lineno, target))
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--todo", action="store_true", help="list leftover TODO / EXAMPLE placeholders")
    parser.add_argument("--strict", action="store_true", help="fail on leftover placeholders too")
    args = parser.parse_args()

    failed = False

    link_problems = 0
    for path in project_files({".md"}):
        prose = strip_non_prose(path.read_text(encoding="utf-8"))
        for lineno, target in broken_links(path, prose):
            print(f"BROKEN LINK  {path.relative_to(ROOT).as_posix()}:{lineno}  ->  {target}")
            link_problems += 1
    if link_problems:
        failed = True
        print(f"\n{link_problems} broken link(s).\n")
    else:
        print("Links: OK")

    if args.todo or args.strict:
        rows = []
        for path in project_files(PLACEHOLDER_SUFFIXES):
            text = path.read_text(encoding="utf-8")
            prose = strip_non_prose(text) if path.suffix == ".md" else text
            todos, examples = len(TODO_RE.findall(prose)), len(EXAMPLE_RE.findall(prose))
            if todos or examples:
                rows.append((path.relative_to(ROOT).as_posix(), todos, examples))
        if rows:
            width = max(len(r[0]) for r in rows)
            print(f"\n{'File'.ljust(width)}  TODO  EXAMPLE")
            for name, todos, examples in rows:
                print(f"{name.ljust(width)}  {todos:>4}  {examples:>7}")
            total_t, total_e = sum(r[1] for r in rows), sum(r[2] for r in rows)
            print(f"{'Total'.ljust(width)}  {total_t:>4}  {total_e:>7}")
            if args.strict:
                failed = True
        else:
            print("Placeholders: none left")

    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
