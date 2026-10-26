# Contributing to the library

Anyone can propose material. There is **one rule**: every resource is a folder whose `README.md` starts with a metadata block. The catalogue (`catalog.json`) and the table in the main README are rebuilt automatically from those blocks — never edit them by hand.

## 1. Create a folder

- One folder per resource, at the repository root.
- Name it in English, lowercase, with hyphens: `usability-test-script`, `design-tokens-guide`.
- **This repository is public.** No client material, internal company documents, personal data or anything under NDA.
- If the material is someone else's work, keep its licence file and credit the author.

## 2. Start its README with the metadata block

Copy this to the very top of `README.md` (the `---` lines included), fill it in, then write whatever explanation you like below it:

```markdown
---
name: Usability Test Script
summary: Moderated test script with warm-up, five task templates and debrief questions.
area: [UX, Research]
phase: [Test]
format: [Template]
topics: [usability-testing, moderation, tasks]
language: en
platform: Any — a Word/Docs template
how_to_use: Duplicate the template, replace the tasks with your product's key flows, and run a pilot session first.
entry_point: README.md
maintainer: your-github-username
added: 2026-10-26
---

# Usability Test Script

What it is, when to use it, and how.
```

### Fields

| Field | Required | What to write |
|---|---|---|
| `name` | yes | Readable title |
| `summary` | yes | One sentence: what it is and what it helps you do |
| `area` | yes | One or more of `UX`, `UI`, `Research` |
| `phase` | yes | One or more of `Discovery`, `Define`, `Ideate`, `Design`, `Test`, `Handoff` — only those where it genuinely helps |
| `format` | yes | One or more of `Skill`, `Template`, `Checklist`, `Guide`, `Knowledge base` |
| `topics` | yes | Free tags, lowercase English with hyphens. Reuse existing tags from `catalog.json` before inventing new ones |
| `language` | no | `en`, `it`, … |
| `platform` | no | Where it works (any, Claude, Figma, Miro…) |
| `how_to_use` | no | The concrete first step for someone opening it for the first time |
| `entry_point` | no | File to open first, relative to the folder (default: the README) |
| `maintainer` | no | Your GitHub username |
| `added` | no | Date, `YYYY-MM-DD` |

Format rules: one field per line, lists in square brackets separated by commas, each value on a single line.

**Third-party folders** whose README you shouldn't change: put the same block in a `LIBRARY.md` file in the folder instead. It takes priority over the README.

## 3. Submit

- **Collaborators:** commit to `main`. Within a minute the catalogue updates itself.
- **Everyone else:** fork the repository, add your folder, open a pull request. An automatic check validates the metadata and shows any problem on the pull request; the maintainer merges once it passes.

If the automatic check fails, open the failed run in the **Actions** tab: each problem is listed with the file and the field to fix.
