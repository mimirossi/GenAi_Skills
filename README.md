# GenAi_Skills

A shared library of AI skills and working material for designers — UX, UI and research — organised by the phase of work where it helps.

## What's inside

| Resource | Area | Phase | Format |
|---|---|---|---|
| [Interface Design Checklists](interface-design-checklists-agnostic) | UX, UI | Design, Test | Skill, Checklist, Knowledge base |
| [Find Skills](Find_Skill) | All | All | Skill (+ CLI source) |
| [Design Library Finder](design-library-finder) | All | All | Skill |

The full, searchable list lives in [`catalog.json`](catalog.json).

## How to find material

**Ask Claude.** Install the [Design Library Finder](design-library-finder) skill, then ask things like:

- "Find UX material for usability testing"
- "Is there a checklist for reviewing forms?"
- "Cosa c'è per la fase di discovery?"

It reads the live catalogue, so new resources show up as soon as they are added.

**Browse by hand.** Open `catalog.json` and filter by:

- **Area** — UX · UI · Research
- **Phase** — Discovery · Define · Ideate · Design · Test · Handoff
- **Format** — Skill · Template · Checklist · Guide · Knowledge base

## Installing a skill in Claude

1. Download the skill's folder (or its `SKILL.md`) from this repository.
2. Zip the folder and upload it from the Skills section of Claude's settings.

Each resource's README explains platform-specific setup.

## Adding material

Read [CONTRIBUTING.md](CONTRIBUTING.md). In short: one folder per resource, a README with standard fields, and an entry in `catalog.json`.

**This repository is public — never add client material, internal documents or anything under NDA.**

## Licences

Each resource keeps its own licence. `Find_Skill` is © Vercel, Inc., MIT licence — see [Find_Skill/LICENSE](Find_Skill/LICENSE).
