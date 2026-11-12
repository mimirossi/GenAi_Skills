---
name: Typography Audit
summary: Skill that audits a typography system against 42 binary checkpoints in 7 blocks — architecture, roles, scale, responsive, accessibility, handoff, AI-readiness — and returns a maturity level and the weakest block to fix first, plus 5 standalone diagnostics such as tracing a token chain or writing the context file AI tools read.
area: [UI, UX]
phase: [Design, Test, Handoff]
format: [Skill, Checklist]
topics: [typography, typography-audit, type-scale, text-styles, type-roles, type-hierarchy, design-tokens, tokens, design-system, design-system-audit, responsive, breakpoints, line-height, letter-spacing, font-weight, accessibility, wcag, contrast, text-resize, text-spacing, handoff, code-mapping, ai-ready, ai-context, figma, css]
language: en
platform: Claude (skill; reads Figma files when the Figma connector is on); the framework works as agent instructions on any platform
how_to_use: Install this folder as a skill. Share what your type system lives in — a Figma library link, token or CSS files, or screenshots — and ask for a full typography audit, or for one diagnostic such as "trace this token chain".
entry_point: SKILL.md
maintainer: mimirossi
added: 2026-11-12
---

# Typography Audit

Gives an honest picture of a typography system **as it actually exists today** — not as the spec says, not as it was planned. Every checkpoint scores 1 only if it can be verified in the sources you share; anything partial, undocumented or merely intended scores 0. The audit describes the current state and does not propose fixes unless you ask for them afterwards.

## Two ways to use it

| You ask for… | You get |
|---|---|
| **A full audit** — "Audit our type system" · "Are our text styles accessible?" | 42 checkpoints scored, a score per block, a maturity level, the weakest block to start from, recurring failure patterns found, and the evidence for every checkpoint — delivered as a readable document |
| **One diagnostic** — narrower, mid-workflow checks | A focused answer in chat |

### The 7 blocks (6 checkpoints each)

| Block | Checks that… |
|---|---|
| Architecture | Raw values, semantic tokens and text styles are separate layers, and every reference resolves |
| Roles | Styles are named by purpose (Body, Headline), not by look (24px, big-bold) |
| Scale | Sizes, line-heights, weights and tracking come from a documented system |
| Responsive | Breakpoint behaviour is controlled centrally, without duplicated styles |
| Accessibility | Contrast is checked in every mode and breakpoint; text can be resized and re-spaced |
| Handoff | Design decisions map to code without interpretation |
| AI-ready | Rules are written so an AI tool can apply them without guessing |

### Maturity levels

| Score | Level |
|---|---|
| 36–42 | System-grade |
| 25–35 | Structured but leaking |
| 13–24 | Style sheet |
| 0–12 | No system |

The report always leads with the **weakest block**, because it describes the system better than the total does.

### The 5 diagnostics

1. **Trace the token chain** — follow each text style through tokens to raw values (and into code if supplied); flag hardcoded values and broken links.
2. **Find values off the scale** — separate real drift from places where no rule exists yet.
3. **Test whether roles carry meaning** — assign roles to every text on a real screen using only the written definitions.
4. **Check behaviour across breakpoints** — find where responsive behaviour stops being systemic, including text whose contrast requirement changes as it shrinks.
5. **Write the context file AI reads** — a structured file of tokens, roles, rules and invariants to give any AI tool, with gaps marked "Not defined".

## What to share

It works from whatever you have — the more you share, the more checkpoints can pass:

- a **Figma library or file** (link; the Figma connector lets it read text styles and variables directly)
- **token files** (JSON, YAML), **CSS/SCSS** variables, theme configs
- **component code** that uses typography
- **screenshots** or a written description, if nothing else exists

Missing material isn't a blocker: what can't be verified scores 0, with the reason written next to it.

## Install

**Claude:** download this folder, zip it and upload it from the Skills section of Claude's settings. Connect **Figma** to audit a library straight from its link.

**Other agents (ChatGPT, Copilot, enterprise platforms):** paste `SKILL.md` into the agent's instructions, without the block between the `---` lines at the top, and attach token files or screenshots to the chat.

## Try it

- *"Audit the typography in this Figma library: [link]. Tokens are in the attached JSON."*
- *"Trace the token chain for our heading styles."*
- *"Write the AI context file for our type system."*

## Pairs well with

- [Figma Design System Variables](../figma-design-system-variables) — builds typography variables and text styles designed to pass this audit (target 40/40: all checkpoints except the two Handoff ones that need code). Build with that skill, verify with this one.
- [Design Systems](../design-systems) — `design-token` and `naming-convention` to plan the token layer the audit checks.
- [Design Critique](../design-critique) — reviews how type reads on real screens; this audit reviews the system behind them.

## Version

v1 — November 2026. Later versions replace these files; the repository history keeps earlier versions.
