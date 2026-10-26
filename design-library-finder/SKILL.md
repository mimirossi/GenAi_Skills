---
name: design-library-finder
description: Finds design resources (skills, templates, checklists, guides, knowledge bases) in the GenAi_Skills library by area (UX, UI, Research), work phase and topic. Use when a designer asks what material exists for a task, phase or topic — e.g. "find UX material for usability testing", "is there a checklist for forms?", "cosa c'è per la discovery?".
---

# Design Library Finder

Searches the shared design library at https://github.com/mimirossi/GenAi_Skills and tells the designer which resources fit their task, where they are, and how to use them.

The library's single source of truth is its catalogue:

- Catalogue (raw): `https://raw.githubusercontent.com/mimirossi/GenAi_Skills/main/catalog.json`
- Resource link pattern: `https://github.com/mimirossi/GenAi_Skills/tree/main/<path>`
- File link pattern: `https://github.com/mimirossi/GenAi_Skills/blob/main/<entry_point>`

Never answer from memory of what the library contains — always read the current catalogue, because people add material over time.

## Step 1 — Understand the request

Extract three things from the message:

| Field | Allowed values |
|---|---|
| **Area** | UX, UI, Research |
| **Phase** | Discovery, Define, Ideate, Design, Test, Handoff |
| **Topic** | free text (e.g. forms, accessibility, interviews, design system) |

Map everyday wording to these values. Examples:

- "user interviews", "personas", "desk research", "interviste" → Research, Discovery
- "journey map", "problem statement", "requisiti" → UX, Define
- "brainstorming", "concept", "workshop" → Ideate
- "wireframe", "mockup", "componente", "UI kit" → Design
- "usability test", "review", "audit", "heuristic evaluation", "rivedere un design" → Test
- "specs for developers", "consegna agli sviluppatori", "annotations" → Handoff

If neither area, phase nor topic can be inferred, ask **one** short question, e.g.: "What are you working on — and in which phase (discovery, design, test…)?". If at least one is clear, search straight away.

## Step 2 — Read the catalogue

Fetch the raw `catalog.json` URL above. If fetching fails, tell the user the library could not be reached and give them the repository link — do not guess the content.

## Step 3 — Match and rank

For each resource in `resources`:

1. **Filter** by area and phase when the user gave them (a resource matches if its list contains the value).
2. **Score** topic relevance by comparing the user's topic (and its synonyms, in English and Italian) against `topics`, `name` and `summary`. A direct tag match beats a match only in the summary.
3. Drop resources with no meaningful topic relevance when a topic was given. Generic resources (e.g. ones tagged for every phase, like tooling) only appear if nothing more specific matches, or if the user asks for tools.

Return at most 5 results, best first.

## Step 4 — Answer

Reply in the user's language. For each result:

- **Name** — linked to the resource folder
- One line on why it fits *this* request (not the generic summary)
- **How to use:** from `how_to_use`, adapted to the request, with a link to the `entry_point`
- Language and platform notes when relevant (e.g. "the material is in Italian", "needs Node.js")

If the best result contains several sub-items (e.g. one file per interface pattern), point to the specific file(s) for the request when the catalogue or the resource's README makes them identifiable. You may open the resource's `entry_point` to find them.

## When nothing matches

Say so plainly: "The library doesn't have material on <topic> yet." Do not stretch a weakly related resource to fill the gap. Then suggest the closest resource only if it is genuinely useful, and mention that anyone can add material by following `CONTRIBUTING.md` in the repository.

## Example

User: "Do we have anything to review a checkout form?"

→ Area: UX/UI · Phase: Test · Topic: forms, checkout
→ Result: **Interface Design Checklists** — has dedicated question sets for web forms and inline validation; use them in analysis mode on the checkout screens. Entry: `knowledge-base/web-forms.md` and `inline-validation.md` (material in Italian).
