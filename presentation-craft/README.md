---
name: Presentation Craft
summary: Skill to build, review and fix slide decks against one quality standard — storyline, narrative structure by deck type, action titles, text density, data visualization, hierarchy, visual craft, originality, brand fidelity and accessibility — with a scored report and slide-by-slide fixes.
area: [UX, UI, Research]
phase: [Define, Design, Test, Handoff]
format: [Skill, Checklist, Guide]
topics: [presentations, slides, slide-deck, pitch-deck, storytelling, storyline, narrative, action-titles, client-proposal, consulting-deliverable, stakeholder-presentation, research-readout, design-review, portfolio, keynote, workshop, data-visualization, charts, text-density, visual-hierarchy, typography, visual-design, originality, brand-fidelity, templates, accessibility, deck-review, pptx]
language: en
platform: Claude (skill); reviewing .pptx files at full depth needs a session that can run Python. The framework works as agent instructions on any platform.
how_to_use: Install this folder as a skill. To build, describe the audience, the goal and what they should decide, and attach your material. To review, attach the deck (.pptx, PDF, screenshots or a Figma/Canva link) and ask for a review.
entry_point: SKILL.md
maintainer: mimirossi
added: 2026-10-28
---

# Presentation Craft

One quality standard for slide decks, used in three ways:

| Mode | Ask for… | You get |
|---|---|---|
| **Create** | "Make a pitch deck from these notes" · "Turn this research into slides for the client" | A storyline (one action title per slide) to approve, then the deck — self-reviewed before delivery |
| **Review** | "Review my deck" · "Is this proposal good?" · "Rivedi queste slide" | A score out of 100, the single most damaging problem, findings by slide (critical / major / minor) with concrete fixes, rewritten titles, and the questions the audience is likely to ask |
| **Revise** | "Improve this deck" · "Fix these slides" | The review, then the fixes applied in the deck's own format |

## What makes it different

**The rules change with the deck type.** A consulting deliverable, an investor pitch and a portfolio are judged differently: each type has its own narrative skeleton and its own scoring weights.

| Type | Examples |
|---|---|
| Consulting · Status | Client deliverable, steering committee, business case, project update |
| Investor pitch · Client pitch · Elevator | Fundraising, sales or freelance proposal, short intro |
| Keynote | Talk, conference, workshop, teaching |
| Creative | Portfolio, brand presentation, concept or design review |

**It checks nine dimensions:** storyline and structure, slide focus and text density, data visualization, visual hierarchy and layout, visual quality and craft, originality, template and brand fidelity, accessibility, motion.

**Without a template, it asks for visual references** — decks, sites, brands or designers whose look you want to approach — and uses them as the visual brief.

**It never invents data.** Missing numbers, clients or quotes become marked placeholders (`[X% — to confirm]`) for you to fill.

## For designers

- **Stakeholder and client presentations** — consulting profile: the argument must be readable from the titles alone and end on a clear decision.
- **Research readouts** — consulting or keynote profile, depending on whether the deck is sent or presented.
- **Design reviews and portfolios** — creative profile: visual craft and originality weigh most.

## Install

**Claude:** download this folder, zip it and upload it from the Skills section of Claude's settings. Keep the folder whole — `references/` and `scripts/` are part of the skill.

**Other agents (ChatGPT, Copilot, enterprise platforms):** paste `SKILL.md` into the agent's instructions, without the block between the `---` lines at the top, and upload the files in `references/` as knowledge. The `.pptx` analysis script won't run there: the agent will review from slide images or PDF only.

## Get a better result

Say in your request:

1. **What kind of deck** it is (e.g. client proposal, research readout, portfolio).
2. **Presented or read** — whether you'll speak over it or send it ahead.
3. **Who the audience is and what they should decide** afterwards.
4. **Template or not** — attach it, or share 2–3 visual references.
5. **Language** of the deck.

Example: *"Review this research readout for the client's product team. I'll present it live, 20 minutes, company template. They need to decide which three features go into the next release. Deck in English, report in Italian."*

## What's in the folder

```
presentation-craft/
├── SKILL.md                 ← instructions: modes, profile, scoring, report format
├── references/              ← the standard, one file per dimension
│   ├── narrative-frameworks.md   skeletons for each deck type
│   ├── storyline.md              action titles and argument flow
│   ├── density.md                text limits by delivery mode
│   ├── data-viz.md               choosing and labelling charts
│   ├── hierarchy-layout.md
│   ├── visual-quality.md         craft when there is no template
│   ├── originality.md            clichés to avoid
│   ├── template-fidelity.md
│   └── accessibility.md          contrast, sizes, alt text, motion
└── scripts/
    └── deck_inventory.py    ← reads a .pptx and lists fonts, sizes, word counts,
                               colours, images, charts, alt text (read-only)
```

The script only reads the file you give it. It needs Python and the `python-pptx` package.

## Pairs well with

- [Design Critique](../design-critique) — for reviewing the screens you show in the deck.
- [UX Writing & Content Strategy](../ux-writing) — for the copy on product slides.

## Version

v1 — October 2026. Later versions replace these files; the repository history keeps every earlier version.
