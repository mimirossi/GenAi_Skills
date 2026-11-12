---
name: Figma Design System Variables
summary: Skill that builds a design system's variables in Figma — brand primitives with OKLCH tonal scales, semantic aliases, Light/Dark component mapping, responsive typography and spacing, elevation, motion with reduced-motion, scopes, code syntax — then validates the whole set and delivers a report.
area: [UI]
phase: [Design, Handoff]
format: [Skill, Guide]
topics: [figma, figma-variables, variables, design-tokens, tokens, design-system, color-scales, tonal-scales, oklch, dark-mode, light-dark, theming, typography, type-scale, text-styles, spacing, component-spacing, responsive, breakpoints, grid, elevation, shadows, effect-styles, motion, reduced-motion, naming-convention, scopes, code-syntax, dev-mode, accessibility, wcag, contrast, handoff]
language: it
platform: Claude with the Figma connector (builds the variables in the file); without it, the skill outputs the full specification as tables to import
how_to_use: Install this folder as a skill and connect Figma. Then share the Figma file link, the brand colours, the fonts, breakpoints and grid, and your Figma plan, and ask it to build the variables.
entry_point: SKILL.md
maintainer: mimirossi
added: 2026-11-12
---

# Figma Design System Variables

Builds a complete, consistent set of design system variables directly in a Figma file, following written rules for every scale, and checks the result before handing it over. Works for any kind of product — digital products, dashboards, brand sites, editorial: where a rule depends on the product type, the skill asks or infers it and says which choice it made.

**The skill is written in Italian.** It replies in the language you write in; variable names are always in English.

## What it builds

Five collections, each referring only to the one below it, so no raw value lives outside `Brand`:

| Collection | Holds | Modes |
|---|---|---|
| `Brand` | Raw values: tonal colour scales, 4px size grid, fonts, shadow colours, durations, easing | — |
| `Alias` | Semantic categories (primary, error, success…), radius, border width, elevation levels | — |
| `Mapped` | Component colours for text, icon, surface, border; shadow colour per level | Light · Dark |
| `Responsive` | Typography per role, generic and component spacing, breakpoints, grid | Desktop · Tablet · Mobile |
| `Motion` | Animation roles: enter, exit, expand, move, feedback, stagger | Default · Reduced |

On top of the variables it creates **text styles** and **elevation effect styles** with every field bound to a variable, sets **scopes**, **Web code syntax** and a **description** on each variable.

## What makes it reliable

- **Colour scales on perceived lightness (OKLCH)**, never on opacity, with the brand colour kept exact on `500`.
- **Dark mode refined beyond inversion:** raised surfaces get lighter, brand and feedback colours adjusted where they fail contrast, off-white body text.
- **Component spacing named by relationship** (`spacing/card/header-content`, `spacing/button/inset-vertical`), not by size — changing a component's density is one variable.
- **Typography by function**, with a type scale chosen by product type and the reason stated.
- **Accessibility built in:** WCAG contrast checked for every text and UI pair in Light and Dark, minimum text sizes, 44px touch targets on Mobile, reduced-motion mode.
- **No invented values.** If a required input is missing, the skill stops and asks.

The final report lists errors found and fixed, the rules applied, values raised to minimums, a typography score, a CSS block for `prefers-reduced-motion`, and a `typography-context.md` file for developers and AI tools.

## Before you start

Have these ready — the skill asks for anything missing:

| Input | Required | Where from |
|---|---|---|
| Brand colours (HEX or RGB) | Yes | Figma styles or variables, brand guidelines, or pasted |
| Font family, styles and weights | Yes | Figma text styles or a list |
| Breakpoints and grid (columns, margins, container, baseline) | Yes | Frame layout grids or values |
| **Your Figma plan** | Yes | It decides how many modes a collection can have |
| Product type | No — inferred | Sets the type scale factor |
| Type sizes, components to cover | No — generated | Existing auto layout in the file is read to find real spacing |

**On the Starter plan** collections can't have modes: the skill creates Light, Desktop and Default values only, and puts Dark, Tablet, Mobile and Reduced in the report, ready to add if the plan changes.

## Install

**Claude:** download this folder, zip it and upload it from the Skills section of Claude's settings. Connect **Figma** from Claude's connectors so it can write in the file. Without the connector the skill still works, but produces the variable tables for you to import instead of building them.

**Other agents (ChatGPT, Copilot, enterprise platforms):** paste `SKILL.md` into the agent's instructions, without the block between the `---` lines at the top. Unless the agent can edit Figma files, you get the specification, not the built variables.

## Try it

*"Crea le variabili del design system in questo file Figma: [link]. Colori brand #3366CC e #FF7A45, font Inter (Regular, Medium, Bold), breakpoint 1440 / 768 / 375 con griglia 12/8/4 colonne. È una web app, piano Professional."*

## Limits to know

- **Prototype transitions can't be bound to variables in Figma** (to be rechecked as Figma changes): Motion variables are the specification for code and Dev Mode, and the values are applied to prototypes by hand.
- **Letter spacing in Figma variables is pixels only**: the skill converts its percentage rules to pixels per role and mode.
- Plan limits on modes are stated as known at the time of writing; the skill rechecks them.

## Pairs well with

- [Design Systems](../design-systems) — `design-token`, `naming-convention` and `theming-system` for planning the system; this skill builds it in Figma.
- [Design Critique](../design-critique) — check that screens actually use the system consistently.

The skill refers to a `typography-audit` skill for its typography checkpoints. That skill is not in this library yet; the rules this skill needs are written into it.

## Version

v1 — November 2026. Later versions replace these files; the repository history keeps earlier versions.
