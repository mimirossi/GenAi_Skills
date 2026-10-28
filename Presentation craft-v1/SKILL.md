---
name: presentation-craft
description: Create or review slide decks and presentations with a quality standard covering storyline, narrative structure by deck type (investor pitch, client/freelance proposal, elevator pitch, consulting deliverable, status update, keynote/workshop, portfolio/brand/concept review), action titles, text density, data visualization, visual hierarchy, visual quality and craft (especially without a template), originality, brand/template fidelity and accessibility. Use it to BUILD a new deck ("make a pitch deck", "fammi una presentazione", "slides for my talk", "turn this report into a deck") and to AUDIT an existing one (.pptx, PDF, Keynote/Google Slides export, Figma, Canva, screenshots) with a scored report and slide-by-slide fixes ("review my deck", "is this pitch good?", "rivedi queste slide", "what's wrong with this presentation?"). Use it whenever slides, decks, pitches or presentations are being made, improved or judged, even if the user doesn't mention quality.
---

# Presentation Craft

One quality standard, three modes:

- **Create** — build a deck that would pass this skill's own review.
- **Review** — audit an existing deck and return a scored report with fixes.
- **Revise** — review first, then apply the fixes.

Decide the mode from the request. "Make / build / turn into / prepare" → Create. "Review / check / is it good / what's wrong / feedback" → Review. "Improve / fix / redo this deck" → Revise. If a deck is attached and the request is ambiguous, ask once: review only, or review and rework?

## Step 1 — Establish the profile (all modes)

The rules for a good deck depend on what kind of deck it is. Infer these from the request and material and ask only what you can't infer, gathering all questions into one short message. Visual references (when there's no template) and language are the two items to ask for explicitly unless the user already gave them.

1. **Deck type** — selects the narrative skeleton (`references/narrative-frameworks.md`) and the scoring weights (Step R4)

   | Type | Examples | Weight profile |
   |---|---|---|
   | `investor-pitch` | fundraising, accelerator, startup competition | pitch |
   | `client-pitch` | sales deck, new business, freelance proposal | pitch |
   | `elevator` | 1–3 min pitch, intro slides | pitch |
   | `consulting` | client deliverable, steerco, business case, board pack | consulting |
   | `status` | internal update, project review | consulting |
   | `keynote` | talk, conference, workshop, teaching, event | keynote |
   | `creative` | portfolio, brand presentation, concept/design review, moodboard | creative |

2. **Delivery mode** — `presented` (a voice carries it), `read` (sent ahead, must stand alone), or `hybrid` (judge storyline as read, density as presented)
3. **Template status** — `template` (corporate/brand master) or `no template` (designed from scratch).
   **If there is no template, ask for visual references** before building or judging the visual side: decks, websites, brand assets, moodboards, images or named designers/studios whose look the user wants to approach (or avoid). References replace the template as the visual brief.
   - Create: use them to define the visual system in Step C4. If the user has none, say so in the output and propose 2–3 named directions in one line each before building.
   - Review: use them to judge whether the visual choices match the intended direction; without references, judge craft and originality on their own terms and state that the direction couldn't be checked.
4. **Language** — ask which language the deck (Create) or the report (Review) should be in, unless the request already makes it clear. Content and slide text may need a different language from the conversation (e.g. a conversation in Italian, a deck for an international client in English). In Review, also check the deck's own language for consistency: mixed languages across slides, untranslated chart labels, inconsistent terminology.
5. **Audience, goal and ask** — who is in the room and what they should decide or do afterwards. In Create mode this is the most important input: no ask, no deck.
6. **Constraints** (Create) — duration or slide count, deadline, brand, mandatory content.

State the profile at the top of the output so the user can correct it.

---

# CREATE MODE

## Step C1 — Gather the material

Collect the substance before thinking about layout: notes, documents, data, product screenshots, brand assets, prior decks. Note what the skeleton needs that is missing (an investor pitch without a "why now", a proposal without pricing). Ask for missing essentials once; if the user isn't available, use clearly marked placeholders (`[X% — to confirm]`). Never invent numbers, quotes, clients or results.

## Step C2 — Build the storyline first

Read `references/narrative-frameworks.md` and pick the skeleton for the deck type. Adapt it, don't apply it mechanically: drop beats that don't serve this audience (the mapping table at the end of that file says which), reorder to lead with the strongest card, merge beats when slide count is tight.

Then write the **title sequence**: one action title per slide (`references/storyline.md`). Read the titles in order — they must tell the whole argument and end on the ask. Fix the sequence now; it's far cheaper than fixing slides.

For decks over ~8 slides, or when the material is ambiguous, show the user the title sequence before building and invite changes. For short or clearly specified decks, proceed and show the storyline alongside the result.

## Step C3 — Plan each slide

For each slide decide its one idea, the one dominant element that proves it (chart, big number, image, diagram, short statement), and what goes to speaker notes or appendix. Apply:
- density thresholds for the delivery mode (`references/density.md`)
- the right chart for each data relationship, with the takeaway highlighted (`references/data-viz.md`)
- a variety of slide archetypes within one system: statement, big number, chart + takeaway, image-led, comparison, process, proof/quote, section divider, ask

## Step C4 — Set the visual direction

- **With a template**: use its layouts, fonts and palette strictly (`references/template-fidelity.md`). Originality goes into framing, data angles and diagram invention.
- **Without a template**: start from the user's references (Step 1, point 3) — extract what they share (type voice, palette mood, image treatment, density, composition) and translate it into the deck, without copying any specific design. Then define a compact system before building — type pairing and scale, palette with roles, grid and margins, image treatment, one graphic motif — following `references/visual-quality.md`. Aim for a visual concept specific to the topic and audience; avoid the clichés in `references/originality.md` (stock handshakes and rockets, default themes, the purple-gradient AI look).
- Accessibility from the start: contrast and minimum sizes in `references/accessibility.md`.

## Step C5 — Build

Choose the output by what the session offers and what the user asked for:
- If the session offers a slide-deck artifact type (e.g. a Slides type) and the user didn't name a file format, build there.
- If the user asked for PowerPoint/.pptx, load the `pptx` skill and build the file.
- If the user named a connected tool (Figma Slides, Canva, Google Slides), build there with its skill/tools.

Add speaker notes for `presented` decks (what to say, the transition to the next slide). Put backup slides in an appendix for the questions the audience is most likely to ask — the weakest points of the model, risks, assumptions, methodology.

## Step C6 — Self-review before delivering

Render the slides and run Review mode Steps R2–R3 on your own deck. Fix every critical and major finding before handing it over. Deliver with the profile, the storyline (titles in order), and the open points the user must fill or confirm.

---

# REVIEW MODE

## Step R1 — Ingest the deck

Always look at the slides as images; most visual problems are invisible in extracted text.

- **.pptx**: run `python scripts/deck_inventory.py file.pptx` for facts (fonts, sizes, word counts, colors, image resolution, charts, 3D, alt text, animations). Render: `soffice --headless --convert-to pdf file.pptx`, then `pdftoppm -png -r 80 file.pdf slide`. View every slide image.
- **.pdf**: `pdftoppm -png -r 80`, plus `pdftotext -layout` for word counts.
- **Figma / Canva / Google Slides**: use the connected tools for screenshots and text/style data.
- **Images**: view directly.

For decks over ~40 slides, scan all at low resolution, then zoom into flagged slides. Use inventory facts as evidence; don't report them raw.

## Step R2 — Check the narrative skeleton

Compare the deck with the skeleton for its type in `references/narrative-frameworks.md`: which required beats are present, missing, weak or misplaced. For pitches, check the review flags in that file (only-TAM markets, missing "why now", "no competitors", projections without assumptions, no amount or use of funds). A missing ask is always at least a major finding.

## Step R3 — Evaluate each dimension

Read the reference for each dimension you score.

| # | Dimension | Reference | Scored when |
|---|---|---|---|
| 1 | Storyline & structure | `storyline.md` + `narrative-frameworks.md` | always |
| 2 | Slide focus & text density | `density.md` | always |
| 3 | Data visualization | `data-viz.md` | deck has charts, tables or numbers |
| 4 | Visual hierarchy & layout | `hierarchy-layout.md` | always |
| 5 | Visual quality & craft | `visual-quality.md` | always; full weight without template |
| 6 | Originality | `originality.md` | always |
| 7 | Template & brand fidelity | `template-fidelity.md` | template or brand guidelines exist |
| 8 | Accessibility | `accessibility.md` | always |
| 9 | Motion & animation | `accessibility.md` (Motion) | animations/transitions present, else N/A |

Score 1–5 with the anchors in each file (5 = passes a senior reviewer unchanged · 4 = minor polish · 3 = visible problems a client would notice · 2 = weakens message or credibility · 1 = undermines the deck).

Some dimensions pull against each other — **consistency vs originality**, **density vs standalone readability**. Resolve through the profile, not by averaging: a consulting deck earns originality through sharp framing, not decoration; a creative deck that is consistent but generic should not score high.

## Step R4 — Weight and total

`sum(score × weight) / (5 × sum(weights)) × 100`. Drop N/A dimensions and renormalize. Without a template, move the fidelity weight onto Visual quality.

| Dimension | consulting | pitch | keynote | creative |
|---|---:|---:|---:|---:|
| Storyline & structure | 25 | 20 | 15 | 10 |
| Slide focus & density | 15 | 15 | 15 | 10 |
| Data visualization | 15 | 10 | 5 | 5 |
| Hierarchy & layout | 10 | 10 | 15 | 15 |
| Visual quality & craft | 10 | 15 | 15 | 20 |
| Originality | 5 | 10 | 15 | 25 |
| Template & brand fidelity | 10 | 10 | 5 | 5 |
| Accessibility | 10 | 10 | 15 | 10 |

Bands: 85+ ready · 70–84 ready after fixes · 50–69 needs a revision pass · <50 needs restructuring. One **critical** finding (wrong number on a key slide, missing ask on a pitch, unreadable key content) caps the verdict at "needs a revision pass".

## Step R5 — Write the report

Lead with the verdict and the most damaging problem.

```
# Presentation review — [deck name]

**Profile:** [type] · [delivery] · [template / no template + references] · language: [deck / report] · audience: [who] · ask: [what]
**Score:** [NN]/100 — [band]
**Fix first:** [the single most damaging issue, one sentence]

## Scorecard
| Dimension | Score | Weight | One-line reason |

## Storyline check
[Titles in order; whether they form an argument on their own.
Skeleton beats for this deck type: present / missing / weak / misplaced.]

## Findings
### Critical — breaks the message, credibility or accessibility
### Major    — visibly weakens the deck
### Minor    — polish

- **Slide N — [issue]**
  What: [concrete observation]
  Why it matters: [effect on the audience]
  Fix: [specific action; rewrite the title or text when that's the fix]

## What works
[2–4 specific strengths worth keeping; skip if none.]

## Rewrite suggestions
[Before/after action titles for the weakest 3–5 slides; missing beats drafted as slide outlines.]

## Likely questions
[Pitches and consulting decks: the 3–5 hardest questions this audience will ask, and whether the deck or appendix answers them.]
```

Group repeated issues ("Slides 4, 7, 9–12 — legend instead of direct labels"). Cap Minor findings at ~10. Offer to render the report as an HTML page or doc if it will be shared, and offer to apply the fixes.

## Revise mode

Run R1–R5, show the report briefly, then fix in priority order: storyline and missing beats, then density and charts, then visual quality. Edit the deck in its own format (.pptx stays .pptx). Finish with a before/after score and what still needs the user's input.

---

## Principles

- **Evidence over taste.** Every finding points to a slide and something observable.
- **Frameworks are skeletons, not scripts.** Adapt beats to the deck type and audience; a beat that doesn't serve this audience is cut, not forced.
- **Rules are defaults.** Thresholds describe typical good practice. A deliberate, well-executed break is fine; an accidental one is a finding.
- **Never invent substance.** No made-up numbers, market sizes, clients, quotes or traction — use marked placeholders.
- **Rewrite, don't just criticize.** Write the better title, name the right chart, draft the missing slide.
- **Don't invent problems.** If a dimension is strong, say so in one line and move on.
