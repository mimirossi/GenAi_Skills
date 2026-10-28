#!/usr/bin/env python3
"""Build catalog.json (and the table in README.md) from each resource folder's metadata.

Every top-level folder is a resource. Its metadata is the frontmatter block at the
top of LIBRARY.md if present, otherwise README.md:

    ---
    name: Usability Test Script
    summary: One sentence on what it is.
    area: [UX, Research]
    phase: [Test]
    format: [Template]
    topics: [usability-testing, moderation]
    ---

Usage:
    python3 .github/scripts/build_catalog.py           # write catalog.json + README table
    python3 .github/scripts/build_catalog.py --check   # validate only, exit 1 on errors

No third-party dependencies, so it runs on any GitHub runner as-is.
"""

import datetime
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REPO_URL = "https://github.com/mimirossi/GenAi_Skills"

TAXONOMY = {
    "area": ["UX", "UI", "Research"],
    "phase": ["Discovery", "Define", "Ideate", "Design", "Test", "Handoff"],
    "format": ["Skill", "Template", "Checklist", "Guide", "Knowledge base"],
}
REQUIRED = ["name", "summary", "area", "phase", "format", "topics"]
LIST_FIELDS = ["area", "phase", "format", "topics"]
FIELD_ORDER = [
    "id", "name", "path", "summary", "area", "phase", "format", "topics",
    "language", "platform", "how_to_use", "entry_point", "maintainer", "added", "files",
]
METADATA_FILES = ["LIBRARY.md", "README.md"]
IGNORED_DIRS = {"node_modules"}
SYSTEM_DIRS = {".git", ".github"}
RAW_BASE = "https://raw.githubusercontent.com/mimirossi/GenAi_Skills/main/"
TEXT_EXTENSIONS = {".md", ".txt", ".csv", ".json", ".html"}
MAX_FILES = 80

TABLE_START = "<!-- catalog:start -->"
TABLE_END = "<!-- catalog:end -->"


def parse_value(raw):
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        return [item.strip().strip("'\"") for item in raw[1:-1].split(",") if item.strip()]
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "'\"":
        return raw[1:-1]
    return raw


def read_frontmatter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read().lstrip("﻿")
    match = re.match(r"^---\s*\n(.*?)\n---\s*(\n|$)", text, re.S)
    if not match:
        return None
    data = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"line is not 'key: value' → {line.strip()!r}")
        key, value = line.split(":", 1)
        data[key.strip()] = parse_value(value)
    return data


def resource_dirs():
    for name in sorted(os.listdir(ROOT), key=str.lower):
        full = os.path.join(ROOT, name)
        if os.path.isdir(full) and not name.startswith(".") and name not in IGNORED_DIRS:
            yield name


def hidden_folder_errors():
    """Folders starting with '.' are hidden on GitHub and macOS — almost always a naming slip."""
    return [
        f"{name}/: folder names must not start with '.' — it hides the folder. "
        f"Rename it, e.g. to '{name.lstrip('.').strip().lower().replace(' ', '-')}'"
        for name in sorted(os.listdir(ROOT))
        if name.startswith(".") and name not in SYSTEM_DIRS and os.path.isdir(os.path.join(ROOT, name))
    ]


def readable_files(folder):
    """Text files an agent may need to open, as repo-relative paths.

    Agents read these through RAW_BASE + path: GitHub's HTML pages (tree/blob)
    are often unreadable to web-fetch tools, and raw URLs can't list a folder,
    so the catalogue carries the exact paths.
    """
    found = []
    for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT, folder)):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith(".") and d not in IGNORED_DIRS)
        for name in sorted(filenames):
            if os.path.splitext(name)[1].lower() in TEXT_EXTENSIONS:
                found.append(os.path.relpath(os.path.join(dirpath, name), ROOT).replace(os.sep, "/"))
    return found[:MAX_FILES]


def build():
    resources, errors = [], hidden_folder_errors()
    for folder in resource_dirs():
        meta_file = next(
            (f for f in METADATA_FILES if os.path.isfile(os.path.join(ROOT, folder, f))), None
        )
        if not meta_file:
            errors.append(f"{folder}/: no README.md or LIBRARY.md with the metadata block")
            continue
        rel = f"{folder}/{meta_file}"
        try:
            meta = read_frontmatter(os.path.join(ROOT, folder, meta_file))
        except ValueError as exc:
            errors.append(f"{rel}: {exc}")
            continue
        if meta is None:
            errors.append(f"{rel}: missing the metadata block between --- lines at the top")
            continue

        problems = [f"missing '{k}'" for k in REQUIRED if not meta.get(k)]
        for key in LIST_FIELDS:
            if key in meta and not isinstance(meta[key], list):
                meta[key] = [meta[key]]
        for key, allowed in TAXONOMY.items():
            for value in meta.get(key, []):
                if value not in allowed:
                    problems.append(f"{key} '{value}' is not one of: {', '.join(allowed)}")
        entry = meta.get("entry_point")
        if entry and not os.path.exists(os.path.join(ROOT, folder, entry)):
            problems.append(f"entry_point '{entry}' does not exist inside {folder}/")
        if problems:
            errors.extend(f"{rel}: {p}" for p in problems)
            continue

        meta["files"] = readable_files(folder)
        meta["topics"] = [t.lower() for t in meta["topics"]]
        meta["id"] = meta.get("id") or folder.lower()
        meta["path"] = folder
        meta["entry_point"] = f"{folder}/{entry}" if entry else rel
        ordered = {k: meta[k] for k in FIELD_ORDER if k in meta}
        ordered.update({k: v for k, v in meta.items() if k not in ordered})
        resources.append(ordered)

    resources.sort(key=lambda r: r["name"].lower())
    return resources, errors


def readme_table(resources):
    rows = ["| Resource | Area | Phase | Format |", "|---|---|---|---|"]
    for r in resources:
        rows.append(
            f"| [{r['name']}]({r['path']}) | {', '.join(r['area'])} | "
            f"{', '.join(r['phase'])} | {', '.join(r['format'])} |"
        )
    return "\n".join(rows)


def write_outputs(resources):
    catalog_path = os.path.join(ROOT, "catalog.json")
    previous = {}
    if os.path.exists(catalog_path):
        with open(catalog_path, encoding="utf-8") as f:
            previous = json.load(f)

    catalog = {
        "name": "GenAi_Skills — Design resource library",
        "repository": REPO_URL,
        "raw_base": RAW_BASE,
        "reading_files": "To read a file, fetch raw_base + its path from a resource's files list. "
        "Never fetch github.com/.../tree or /blob pages: they are for linking people, not for reading.",
        "schema_version": "1.2",
        "generated": "Automatically from each folder's README.md/LIBRARY.md — do not edit by hand.",
        "updated": previous.get("updated", ""),
        "taxonomy": {**TAXONOMY, "topics": "Free lowercase tags in English"},
        "resources": resources,
    }
    # Only bump the date when the content actually changes, so no-op runs create no commit.
    if {k: v for k, v in catalog.items() if k != "updated"} != {
        k: v for k, v in previous.items() if k != "updated"
    }:
        catalog["updated"] = datetime.date.today().isoformat()
    with open(catalog_path, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
        f.write("\n")

    readme_path = os.path.join(ROOT, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, encoding="utf-8") as f:
            readme = f.read()
        pattern = re.compile(re.escape(TABLE_START) + ".*?" + re.escape(TABLE_END), re.S)
        if pattern.search(readme):
            block = f"{TABLE_START}\n{readme_table(resources)}\n{TABLE_END}"
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(pattern.sub(lambda _: block, readme))


def main():
    check_only = "--check" in sys.argv
    resources, errors = build()
    for r in resources:
        print(f"ok    {r['path']}")
    for e in errors:
        print(f"ERROR {e}")
    if errors:
        print(f"\n{len(errors)} problem(s). See CONTRIBUTING.md for the metadata format.")
        sys.exit(1)
    if not check_only:
        write_outputs(resources)
        print(f"\ncatalog.json written with {len(resources)} resource(s).")


if __name__ == "__main__":
    main()
