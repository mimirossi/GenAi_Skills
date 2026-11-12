---
name: typography-audit
description: >-
  Audits a typography design system — tokens, text styles, roles, scale, responsive behavior, accessibility, handoff to code, and AI-readiness — against a 42-checkpoint framework across 7 blocks, producing per-block scores, a maturity rating, and a clear priority (the weakest block, not just the total). Also exposes 5 standalone diagnostic prompts run individually — trace the token chain, find values off the scale, test whether roles carry meaning, check behaviour across breakpoints, write the context file AI reads. Use whenever the user asks to audit, review, evaluate, grade, or score a typography system, type scale, text styles, heading/body hierarchy, or design tokens — even without saying "audit". Trigger on "review our type system", "are our text styles accessible", "check if our tokens are AI-ready", "trace this token chain", "find values off scale", or when the user shares token/CSS/SCSS files, a Figma typography library, or describes their type styles wanting feedback.
---

# Typography Audit

A structured framework for auditing a typography design system as it actually exists today — not as it was intended, documented in a spec nobody follows, or planned for later. The audit is built on one idea: **score only what you can verify.** Anything partial, undocumented, or merely planned scores zero. This keeps the result honest even when it's uncomfortable.

The framework has two things you can run:

1. **The full audit** — walk all 7 blocks (42 checkpoints), score them, and report a maturity level.
2. **One of 5 standalone diagnostic prompts** — narrower, single-purpose checks the user can ask for directly ("trace this token chain", "check accessibility across our breakpoints") without running the whole audit.

Both modes are diagnostic, not corrective. Neither one should turn into a redesign or a list of fixes unless the user explicitly asks for that as a separate next step — the value of this audit is a trustworthy picture of the current state, and that value collapses if findings get mixed with opinions about what to change.

## Before you start: gather sources

This audit is not tied to any framework, file format, or tool. It works from whatever the user has:

- Design token files (JSON, YAML, CSS custom properties, SCSS variables, etc.)
- Theme/style-dictionary configs
- Component code that consumes typography (React, Swift, Android XML, etc.)
- A Figma file or library (use the Figma MCP tools if connected — `get_design_context`, `get_variable_defs`, etc. — to pull text styles and variables directly)
- Screenshots or a plain-text/verbal description of the type system, when no files exist

If it's unclear what's available, ask before assuming a tech stack or file format. Don't guess at a format the user hasn't shown you — this audit is only as honest as its inputs, and guessing defeats that.

It's fine — expected, even — for sources to be incomplete. Missing rules are findings, not blockers. A checkpoint with no verifiable evidence scores 0 and gets a one-line reason why; the audit doesn't stall waiting for a document that doesn't exist.

## Scoring rule (applies to every checkpoint, in both modes)

Each checkpoint is binary:

- **1** — confirmed and verifiable in the sources provided right now
- **0** — partial, undocumented, inconsistent, contradicted elsewhere in the sources, or merely planned/intended

Never score from what the user *says* the system does — score from what you can actually see. If a token file defines a scale but three components ignore it, the checkpoint about sizes coming from the scale scores 0, with the counterexamples named. Being asked to trust stated intent over evidence is exactly the failure mode this audit exists to catch.

---

## Mode 1: Full audit (7 blocks, 42 checkpoints)

Work through each block in order. For every checkpoint, state pass/fail and a one-line reason pointing at the actual evidence (a file, token name, or component) — not a restatement of the checkpoint text. Keep it terse and checkpoint-style, not prose.

### Architecture (raw values → semantic tokens → text styles)
1. Layers are separated — raw values, semantic tokens, and text styles remain distinct (no text style hardcodes a raw value directly)
2. Styles are bound — text styles reference tokens rather than hardcoded values
3. Semantics reference source tokens — semantic tokens resolve to documented primitive/raw values
4. Properties are complete — required typography properties (size, line-height, weight, at minimum) are defined consistently across styles
5. References resolve — no token points to a missing, renamed, or deleted target
6. Naming is consistent — tokens follow one documented naming pattern, not several ad hoc ones

### Roles (styles named by purpose, not appearance)
1. Roles carry meaning — styles are named by content purpose (e.g. Display, Headline, Body), not by size or look (e.g. "24px", "big-bold")
2. Role boundaries are clear — each role has a distinct, documented purpose
3. Role levels are distinct — hierarchy levels don't overlap without a stated reason
4. Reading roles are distinct — primary reading content and supporting/secondary content use separate roles
5. Interface text has defined roles — controls, labels, and navigation use documented interface roles, not reading roles repurposed
6. Emphasis preserves hierarchy — emphasis (bold, larger, etc.) doesn't require switching to a higher-level role to get visual weight

### Scale (documented sizes, line-heights, weights, tracking)
1. Sizes come from the scale — typography sizes use documented scale steps, not one-off values
2. The scale is documented — the available steps and how they map to use are written down somewhere
3. Line-height follows rules — line-height values follow a documented system (e.g. tied to size, or a fixed set of ratios)
4. Weight usage is defined — each supported font weight has a clear, documented purpose
5. Variants stay aligned — emphasis/variant styles preserve the role's core typography properties (they don't quietly change size or line-height too)
6. Letter-spacing is systematic — tracking uses documented values, not local per-instance adjustments

### Responsive (breakpoint behaviour controlled centrally)
1. Responsive rules are centralised — breakpoint behaviour is controlled from one shared source, not scattered
2. Styles are not duplicated — responsive changes don't require a separate copy of each style per breakpoint
3. Breakpoints are documented — the viewport ranges where typography changes are written down
4. Role behaviour is defined — the system states which roles resize at breakpoints and how
5. Reading text stays readable — responsive changes preserve comfortable reading sizes (body text doesn't shrink into illegibility)
6. Hierarchy survives compression — smaller viewports still preserve clear differences between roles

### Accessibility (contrast, spacing, scaling)
1. Text classes are known — styles are correctly classified for the contrast requirements they trigger (e.g. WCAG large-text vs normal-text thresholds)
2. Contrast is validated in every mode — checked across breakpoints, themes (light/dark), and the backgrounds text actually appears on
3. Small text has a defined floor — the system documents how small text is allowed to become
4. Text spacing remains adjustable — custom letter/line/paragraph spacing overrides (e.g. WCAG 1.4.12) don't break content or functionality
5. Line-height supports reading — reading roles use spacing appropriate for sustained reading, not tightened for visual density
6. Text is resizable — text can scale to 200% without losing content or functionality

### Handoff (design → code without interpretation)
1. Components use semantics — components reference semantic typography tokens, not raw values
2. Responsive rules map to code — breakpoint behaviour has a documented code implementation, not just a design-side description
3. Naming maps to code — token names follow a predictable, documented mapping into code identifiers
4. Handoff is written — implementation rules exist somewhere durable, not only in meetings or verbal explanation
5. Usage is documented — roles include explicit guidance on when to use them (and, ideally, when not to)
6. Changes are traceable — a typography decision can be followed from its design source through to the code that implements it

### AI-ready (tokens and rules a model can apply without guessing)
1. AI can load the system — tokens and rules exist in a format a model can actually read (not locked in a raster image or inaccessible tool)
2. Rules are machine-usable — guidance is written as explicit constraints, not implied intent a human would have to infer
3. Invariants are declared — the system states what must never change, and why
4. Role logic is explicit — which role to use can be derived from documented purpose, not inferred from visual size
5. Context is complete — a model can get the rules it needs for a task without reconstructing the whole system first
6. Context is versioned — AI-facing context can be matched to the version of the system it describes

### Scoring and output

Sum each block out of 6, then total out of 42. But the raw scoring is only half the job — the audit is worthless to the person reading it if they have to decode a checklist to find out what it means for them. Write the report so a stakeholder who has never seen this framework before can read the top of it and immediately understand where they stand and what to do first, then go as deep into the evidence as they want.

Structure the report in this order, and translate every score into plain language — not just "Roles: 2/6" but what a 2/6 on Roles actually costs the team day to day:

```
# Typography System Audit

## The short version
[3-5 plain-language sentences: overall state in everyday terms (not "8/42" as the opening fact —
lead with what that means, e.g. "your typography is still decided component-by-component rather
than by a shared system"), the maturity level and what it practically implies, and the one thing
to fix first and why it matters more than the others.]

## Scores at a glance
| Block | Score | What this tells you |
|---|---|---|
| Architecture | x/6 | [one plain sentence: what's solid or fragile here, in consequences not jargon] |
| Roles | x/6 | [same] |
| Scale | x/6 | [same] |
| Responsive | x/6 | [same] |
| Accessibility | x/6 | [same] |
| Handoff | x/6 | [same] |
| AI-ready | x/6 | [same] |
| **Total** | **x/42** | |

## Maturity: [level name]
[the level's description, expanded into 1-2 sentences of what it means for THIS system specifically,
not the generic definition alone]

## Where to start: [weakest block(s)]
[why this block, specifically — grounded in the concrete evidence, told as a small story: what's
happening now, why it will get worse if left alone, and what changes once it's fixed. Not a generic
"improve everything" statement, and not just a restatement of the checkpoint failures.]

## Patterns worth knowing about
[any concrete instances of the 6 common failure patterns, explained in one or two sentences each —
what's happening, where, and why it's the kind of thing that gets worse quietly. Omit this section
if none are found; don't force a match.]

## The evidence
[pass/fail + one-line reason for every one of the 42 checkpoints, grouped by block — this is the
appendix a technical reader or a future audit will want, not the part most people will read first]
```

The "short version" and "Scores at a glance" sections are what most readers will actually absorb — write them for someone who cares about the outcome, not the framework. The checkpoint-by-checkpoint evidence still needs to exist in full underneath it, both because it's what makes each finding verifiable and because it's what a follow-up audit will diff against — just don't lead with it.

Maturity levels — assign strictly by total score, but always lead with the weakest block in "Where to start," since **the weakest block describes the system more accurately than the total does**. A 30/42 built on one collapsed block and six near-perfect ones is a different problem than a 30/42 spread evenly thin.

| Score | Level | What it means |
|---|---|---|
| 36–42 | System-grade | Change is absorbed by the system. Remaining gaps are contained fixes, not structural problems. |
| 25–35 | Structured but leaking | Behaves like a system until the first real pressure (a new breakpoint, a new theme, an edge-case component) — then gaps compound. |
| 13–24 | Style sheet | Consistency is maintained by hand, not by structure. The move is to restructure the layer, not add more rules on top of it. |
| 0–12 | No system | Typography is decided per screen. There's little structure worth preserving, so rebuilding from a clear foundation is usually faster than repairing what's there. |

### Common failure patterns to watch for

These are specific, recurring ways typography systems break under real use — actively look for them while scoring, and call out concrete instances (don't just list the pattern names):

- **Contrast checked only on desktop** — contrast requirements change with text size (e.g. 24px regular needs 3:1, but 22px needs 4.5:1), so a check done once at one breakpoint doesn't cover smaller sizes elsewhere
- **Per-breakpoint style duplicates** — copies that started identical and have since diverged, multiplying the number of styles to keep in sync
- **Size reduced, line-height left behind** — reading ratios drift because size and line-height were changed independently instead of together
- **One detached style** — a style that stopped receiving token updates but still renders correctly for now, so nobody notices until the underlying values change
- **Caption replacing Body** — primary reading content sitting at a support role's size and contrast, because it reads fine to the person who set it up
- **A hardcoded fallback value** — a component or a model returns a fixed value because the alias chain it should follow was never defined as an actual constraint

---

## Mode 2: Standalone diagnostic prompts

Run these when the user wants a narrow check instead of the full audit — or wants to go deeper on one finding from the full audit. Each has a required input, an exact procedure, and explicit boundaries. The boundaries matter as much as the procedure: these are deliberately scoped to describe what's true, not to propose what to change. Don't drift into suggesting fixes even when the fix seems obvious — that's a different, separate ask.

### 1. Trace the token chain
**Requires:** text styles, tokens, scale steps, optional code mappings
**Do:** Trace each text style through semantic tokens, primitives, and scale steps. Flag hardcoded values, skipped layers, broken references, duplicate aliases, and any chain that cannot be resolved. If code mappings are supplied, continue the trace into code.
**Do not:** reconstruct missing links, or suggest fixes.
**Use for:** running before changing values — it shows where the structure breaks, not how to repair it.

### 2. Find values that are off the scale
**Requires:** text styles, scale steps, role rules
**Do:** Review text styles against scale steps and role rules. Flag any size, line-height, letter-spacing, or weight outside the documented system, plus styles using values not allowed for their role. Trace each issue to the exact style and rule it violates. Mark missing or ambiguous rules as unresolved (not as violations).
**Do not:** suggest replacement values.
**Use for:** separating actual drift from places where the system simply has no documented rule yet — these need different responses.

### 3. Test whether roles carry meaning
**Requires:** role definitions and one real screen
**Do:** Review every text element on the screen against the role definitions. Assign a role only when its purpose clearly matches a supplied definition. Return the current style, the proposed role, and the rule that justifies it. If multiple roles fit, or none does, mark it unresolved.
**Do not:** choose by visual size, and do not invent roles that weren't defined.
**Use for:** a direct test of the role definitions themselves — if a model can't choose without looking at how big the text is, the definitions describe appearance, not purpose, and need to be rewritten.

### 4. Check behaviour across breakpoints
**Requires:** styles, responsive rules, accessibility rules
**Do:** Compare styles across every supplied breakpoint. Flag duplicated breakpoint-specific styles, values that break the responsive rules, roles that resize unexpectedly, and text whose accessibility classification changes as it shrinks (see the contrast-threshold pattern above).
**Do not:** infer missing rules or thresholds that weren't supplied.
**Use for:** finding where responsive behaviour stops being controlled by the system and starts being handled locally, breakpoint by breakpoint.

### 5. Write the context file AI reads
**Requires:** tokens, roles, usage rules, invariants
**Do:** Build a structured context file from the system's sources. Include token structure, role purposes, allowed scale relationships, usage rules, responsive behaviour, and documented invariants. Preserve the source's own terminology rather than translating it. Write "Not defined" for anything missing and collect those under a "Context gaps" section.
**Do not:** resolve contradictions in the sources, or promote common practice into stated system guidance — if it's not written down as a rule, it doesn't become one just because it's consistently done.
**Use for:** producing a file the user can hand to any AI tool so it applies the system's actual rules instead of guessing. Note in the output that it should be versioned alongside the sources it was built from — complete-but-outdated context still causes a model to apply the wrong rules with full confidence.

---

## Delivering the full audit report

A 42-checkpoint audit read as a wall of markdown checkboxes is technically complete and practically useless — the person who asked for it usually needs to act on it or share it with people who weren't in this conversation, and a raw `.md` dump in chat doesn't survive that trip well. Once the full audit (Mode 1) is complete, deliver it as an actual document rather than just pasting the markdown into the reply:

- If the current session can publish a formatted artifact, page, or document (an Artifacts tool, a docs/document-creation skill, a `.docx`/PDF generator, or similar), use it to produce a clean, readable report — headings that read as headings, a real table, the executive summary visually distinct from the checkpoint appendix — and hand the user that document.
- If nothing like that is available, at minimum make the chat response itself read like a finished report someone could forward as-is: strong visual hierarchy through headings and short paragraphs, the "short version" genuinely short, and the 42-item evidence appendix clearly separated (e.g. behind a heading or a collapsible-feeling structure) so it doesn't drown the summary above it.

Either way, the goal is the same: a design lead, a PM, or an engineer who's never seen this framework should be able to open the result and immediately understand where the system stands — not have to parse a checklist to find out.

The 5 standalone diagnostic prompts (Mode 2) are usually a narrower, more technical ask made mid-workflow — a plain, well-organized chat response is normally the right fit for those unless the user asks for a document explicitly.

## A note on tone

Plain language and evidence-based rigor aren't in tension — use both, in the right place. The executive summary and the "what this tells you" column exist to be read by someone without the framework in their head, so write them the way you'd explain the finding out loud to that person: concretely, in terms of consequences, no unexplained jargon. The checkpoint-by-checkpoint evidence underneath is for verification, not persuasion — there, match the source material's directness: state pass/fail as fact with a pointer to evidence, not softened with hedges ("it seems like...", "you might want to..."), one line per checkpoint. Save discussion and nuance for when the user follows up on a specific finding.
