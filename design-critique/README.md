---
name: Design Critique
summary: Skill that gives structured feedback on a design — first impression, usability, visual hierarchy, consistency and accessibility — with severity ratings and prioritised fixes.
area: [UX, UI]
phase: [Ideate, Design, Test]
format: [Skill]
topics: [design-critique, design-review, feedback, usability, visual-hierarchy, consistency, design-system, accessibility, typography, figma]
language: en
platform: Claude (skill or slash command); the framework works as agent instructions on any platform
how_to_use: Install this folder as a skill, then share a Figma link, screenshot or description with its context and stage (exploration, refinement, final) and ask for a critique.
entry_point: SKILL.md
maintainer: Anthropic (third party, Apache 2.0 licence)
added: 2026-10-26
---

# Design Critique

Structured feedback on a screen, flow or mockup at any stage, from early exploration to final polish. It reviews five dimensions and returns a ready-to-share report.

| Dimension | What it checks |
|---|---|
| First impression | What draws the eye first, whether the purpose is immediately clear |
| Usability | Whether the user can reach their goal, intuitive navigation, unnecessary steps |
| Visual hierarchy | Reading order, emphasis, whitespace, typographic hierarchy |
| Consistency | Adherence to the design system, spacing, colour and type, behaviour of similar elements |
| Accessibility | Colour contrast, touch target size, readability, alternative text |

The report lists findings with a severity (critical, moderate, minor), what already works, and the three highest-impact recommendations.

## Use it

**Claude:** download this folder, zip it and upload it from the Skills section of Claude's settings. Then share the design and ask for a critique, e.g. "Critique this checkout screen — it's for a B2B SaaS, refinement stage, focus on mobile."

**Other agents (ChatGPT, Copilot, enterprise platforms):** paste the content of `SKILL.md` into the agent's instructions, without the block between the `---` lines at the top. The parts about connectors only apply when the agent is connected to tools such as Figma.

**Give it context.** Results are much more useful when you say what the design is, who it's for and which stage it's at.

## Pairs well with

[Interface Design Checklists](../interface-design-checklists-agnostic) — Design Critique gives a broad review across five dimensions; the checklists go deep on a specific pattern (forms, tables, date pickers…). Use the critique first to find where the problems are, then the relevant checklist to fix them thoroughly.

## Source and licence

From the `design` plugin in Anthropic's [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) repository (`design/skills/design-critique`), released under the Apache License 2.0 — see [`LICENSE`](LICENSE).

Changes from the original:

- `CONNECTORS.md` copied from the plugin's root into this folder, and the link to it in `SKILL.md` updated so it works here.
- This README added.

The skill's content is otherwise unchanged.
