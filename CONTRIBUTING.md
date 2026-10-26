# Contributing to the library

Anyone can propose material. The library only stays searchable if every resource follows the same three rules.

## 1. One folder per resource

- Put everything for one resource in its own folder at the repository root.
- Name it in English, lowercase, with hyphens: `usability-test-script`, `design-tokens-guide`.
- Do not include client material, internal company documents, personal data or anything under NDA. **This repository is public.**
- If the material is someone else's work, keep its licence file and credit the author.

## 2. A README in the folder

Every folder needs a `README.md` that starts with this block, followed by any explanation you like:

```markdown
---
name: Usability Test Script
area: [UX, Research]
phase: [Test]
format: [Template]
topics: [usability-testing, moderation, tasks]
language: en
---

What it is, when to use it, and how.
```

## 3. An entry in `catalog.json`

Add an object to the `resources` list. This is what the search skill reads — a folder without an entry will never be found.

```json
{
  "id": "usability-test-script",
  "name": "Usability Test Script",
  "path": "usability-test-script",
  "summary": "One sentence: what it is and what it helps you do.",
  "area": ["UX", "Research"],
  "phase": ["Test"],
  "format": ["Template"],
  "topics": ["usability-testing", "moderation", "tasks"],
  "language": "en",
  "platform": "Where it works (any, Claude, Figma, Miro…)",
  "how_to_use": "Concrete first step for someone opening it for the first time.",
  "entry_point": "usability-test-script/README.md",
  "maintainer": "your-github-username",
  "added": "YYYY-MM-DD"
}
```

### Allowed values

| Field | Values |
|---|---|
| `area` | `UX`, `UI`, `Research` |
| `phase` | `Discovery`, `Define`, `Ideate`, `Design`, `Test`, `Handoff` |
| `format` | `Skill`, `Template`, `Checklist`, `Guide`, `Knowledge base` |
| `topics` | Free tags, lowercase English with hyphens. Reuse existing tags before inventing new ones. |

Use only the phases where the resource genuinely helps — tagging everything with every phase makes search worse for everyone.

## How to submit

- **Collaborators:** commit directly to `main`.
- **Everyone else:** fork the repository, add your folder and catalogue entry, and open a pull request. The maintainer reviews it before merging.

Before submitting, check that `catalog.json` is still valid JSON (paste it into any JSON validator).
