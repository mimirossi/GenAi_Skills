---
name: Design Systems
summary: Eleven skills and three commands to build, document and maintain a design system — tokens, component specs, naming, theming, motion, icons, localization, accessibility audits and governance.
area: [UI, UX]
phase: [Define, Design, Test, Handoff]
format: [Skill, Template, Guide]
topics: [design-system, design-tokens, tokens, component-spec, components, naming-convention, theming, dark-mode, multi-brand, motion, icons, iconography, localization, rtl, accessibility, wcag, accessibility-audit, documentation, pattern-library, governance, versioning, design-system-audit]
language: en
platform: Claude (one skill per subfolder in skills/, or the whole plugin in Claude Code); the text works as agent instructions on any platform
how_to_use: Pick the skill for your task from the list below (e.g. skills/design-token for the token layer, skills/component-spec for a component) and install that subfolder as a skill. Then describe your product, brand and existing system and ask for the deliverable.
entry_point: README.md
maintainer: MC Dean (third party, MIT licence)
added: 2026-10-26
---

# design-systems
Build, document, and maintain scalable design systems — from tokens and components to accessibility and theming.
## Skills (11)
- **accessibility-audit** — Audit an existing interface against WCAG, producing findings with severity ratings and remediation steps. Use when you have a design or build to assess now. Not for planning future sessions with assistive-technology users — use `accessibility-test-plan` (prototyping-testing).
- **component-spec** — Specify one component — props, states, variants, accessibility, and usage rules. Use when defining a library component. For the reusable doc scaffold use `documentation-template`; for a problem-solution pattern use `pattern-library`.
- **design-system-governance** — Define how the system evolves — contribution model, versioning, deprecation, and change management. Use when multiple teams contribute. For driving uptake use `design-system-adoption` (designer-toolkit); for design file history use `version-control-strategy` (design-ops).
- **design-token** — Define and organise tokens for colour, spacing, type, and elevation with naming and usage rules. Use when establishing the token layer. For auditing existing usage use `design-token-audit` (designer-toolkit); for multi-brand mapping use `theming-system`.
- **documentation-template** — Generate a reusable documentation scaffold for components, patterns, or guidelines. Use when standardising how the system is documented. For the content of one component's spec, use `component-spec`.
- **icon-system** — Specify an icon system — grid, sizing, stroke weight, naming, categories, and implementation. Use when standardising iconography. For broader illustration, use `illustration-style` (ui-design).
- **localization-design** — Design for multiple languages, writing directions, and cultural contexts — text expansion, RTL mirroring, and locale formats. Use when shipping beyond one locale. For the words themselves, use `ux-writing` (designer-toolkit).
- **motion-system** — Define motion tokens — durations, easing vocabulary, and reduced-motion handling — for consistency product-wide. Use when standardising motion across a system. For crafting one specific animation, use `animation-principles` (interaction-design).
- **naming-convention** — Establish naming rules for components, tokens, and layers with patterns and worked examples. Use when names are inconsistent or being set. For what the tokens actually contain, use `design-token`.
- **pattern-library** — Structure a pattern entry — problem context, solution, usage examples, and related patterns. Use when documenting a recurring solution rather than a component. For a single component's API, use `component-spec`.
- **theming-system** — Design theming architecture — brand variants, dark mode, and high-contrast — mapped through token layers. Use when one system must serve multiple themes. For a single palette use `color-system` (ui-design); for dark mode craft use `dark-mode-design` (ui-design).

## Commands (3)
- `/audit-system` — Run a comprehensive audit of an existing design system for consistency, completeness, and accessibility.
- `/create-component` — Scaffold a full component specification end to end — props, states, variants, accessibility, and documentation.
- `/tokenize` — Extract tokens from an existing design or stylesheet and organise them — naming, structure, and theme mapping.

## Use it

**Claude:** each folder in `skills/` is a separate skill. Download only the ones you need, zip each folder and upload it from the Skills section of Claude's settings — upload the single skill folder, not the whole `design-systems` folder.

**Commands** (`commands/`) are slash commands for Claude Code. In a normal Claude chat or another agent you can still use them: paste the content of the `.md` file as instructions, without the block between the `---` lines at the top.

**Claude Code:** install the whole plugin from the original collection with `/plugin marketplace add Owl-Listener/designer-skills`, then `/plugin install design-systems@designer-skills`.

**Other agents (ChatGPT, Copilot, enterprise platforms):** paste the content of the relevant `SKILL.md` into the agent's instructions, without the block between the `---` lines.

**Which one do I need?**

| If you want to… | Use |
|---|---|
| Set up colours, spacing, type as tokens | `design-token`, then `naming-convention` |
| Turn an existing design or CSS into tokens | `/tokenize` |
| Spec a new component for the library | `component-spec` or `/create-component` |
| Support dark mode or several brands | `theming-system` |
| Check an existing system for gaps | `/audit-system` |
| Check a screen against WCAG | `accessibility-audit` |
| Decide who can change the system and how | `design-system-governance` |

Several skills refer to skills from other collections (`ui-design`, `interaction-design`, `prototyping-testing`, `designer-toolkit`, `design-ops`). Only `ux-writing` is in this library ([UX Writing & Content Strategy](../ux-writing)); the others are in the [original repository](https://github.com/Owl-Listener/designer-skills).

## Pairs well with

- [Design Critique](../design-critique) — its consistency check tells you where the system isn't being followed.
- [Interface Design Checklists](../interface-design-checklists-agnostic) — pattern-level questions to include in a component spec.

## Source and licence

The `design-systems` plugin from MC Dean's [designer-skills](https://github.com/Owl-Listener/designer-skills) collection, released under the MIT licence, © 2026 MC Dean. See [`LICENSE`](LICENSE).

Changes from the original: the metadata block at the top and the sections from "Use it" onward added to this README. Skills and commands are unchanged.
