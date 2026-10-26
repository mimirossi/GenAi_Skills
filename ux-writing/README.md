---
name: UX Writing & Content Strategy
summary: Two skills for the words in a product — UX Writing for interface copy (microcopy, errors, empty states, CTAs) and Content Strategy for what content exists, how it is structured and who owns it.
area: [UX]
phase: [Define, Design]
format: [Skill, Guide]
topics: [ux-writing, microcopy, ux-copy, error-messages, empty-states, cta, confirmation-messages, onboarding, voice-and-tone, content-strategy, content-audit, content-model, content-governance, content-hierarchy, terminology, localization]
language: en
platform: Claude (one skill per subfolder); the text works as agent instructions on any platform
how_to_use: Install ux-writing/ for interface copy or content-strategy/ for content planning, each as its own skill. Then describe the screen, the user's situation and the product voice, and ask for copy or a content plan.
entry_point: README.md
maintainer: MC Dean (third party, MIT licence)
added: 2026-10-26
---

# UX Writing & Content Strategy

Two complementary skills. Content Strategy sets the framework — what content the product needs and how it is governed. UX Writing works at component level — the exact words on each screen.

| Skill | Use it when… | Covers |
|---|---|---|
| [UX Writing](ux-writing/SKILL.md) | the words are the deliverable | Button and form labels, tooltips, placeholders, error messages, empty states, confirmations, onboarding copy, CTAs, voice vs tone |
| [Content Strategy](content-strategy/SKILL.md) | the content itself is the problem | Content audit, content model, voice and tone, governance (who writes, reviews, retires content), content hierarchy, process |

## Use it

**Claude:** each subfolder is a separate skill. Download `ux-writing/` and/or `content-strategy/`, zip each one and upload it from the Skills section of Claude's settings. Upload the subfolder, not this whole folder.

**Other agents (ChatGPT, Copilot, enterprise platforms):** paste the content of the relevant `SKILL.md` into the agent's instructions, without the block between the `---` lines at the top.

**Give it context.** Say what the screen or product is, what the user is trying to do at that moment, and — if you have one — the product's voice. Example: "Write the empty state for the saved-searches page of a real-estate app: friendly, direct voice, the user has never saved a search."

## Pairs well with

- [Design Critique](../design-critique) — review a screen, then use UX Writing to fix the copy issues it finds.
- [Interface Design Checklists](../interface-design-checklists-agnostic) — the forms, inline validation and onboarding checklists flag where copy is missing or unclear.

The skills' descriptions mention plugin names from the original collection (`ux-strategy`, `designer-toolkit`) and an `information-architecture` skill. That skill is not in this library yet; it is available in the [original repository](https://github.com/Owl-Listener/designer-skills/tree/main/ux-strategy/skills/information-architecture).

## Source and licence

From MC Dean's [designer-skills](https://github.com/Owl-Listener/designer-skills) collection — `designer-toolkit/skills/ux-writing` and `ux-strategy/skills/content-strategy` — released under the MIT licence, © 2026 MC Dean. See [`LICENSE`](LICENSE).

Changes from the original: each skill moved into its own subfolder as `SKILL.md`, and this README added. The skills' content is unchanged.
