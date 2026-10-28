# Slide focus & text density

An audience cannot read and listen at the same time. When a presented slide is a wall of text, people read it and stop listening. A read-ahead deck has the opposite problem: too little text and it can't stand on its own. Judge density against the delivery mode.

## Thresholds (body words per slide, excluding title, footnotes, source lines)

| Density | `presented` | `read` |
|---|---|---|
| < 20 words | ideal for most slides | fine for visual/data slides; check the slide still makes sense alone |
| 20–50 | acceptable for context or process slides if well structured | normal |
| 50–80 | finding (major if recurrent) | acceptable if structured with hierarchy |
| > 80 | major | finding — consider a memo/doc instead of a slide |

`deck_inventory.py` reports words per slide; use it.

**About the "5-5-5 rule"** (≤5 lines, ≤5 words per line, ≤5 minutes per slide): treat it as a heuristic for `presented` keynote-style decks only. The "5 words per line" part contradicts action titles (a good action title is often 10–15 words) and is unrealistic for consulting decks. Don't cite it as a standard.

## Checks

- **Focus**: one dominant element per slide (a chart, a statement, an image). Multiple competing charts on a presented slide is a finding.
- **Cramming**: content edge to edge, margins violated, font shrunk to fit. Slide real estate is cheap — five points can be five slides.
- **Bullets**: more than ~6 bullets, or bullets nested 3 levels deep, signals a document pasted into slides.
- **Full sentences vs phrases**: for `presented`, phrases; for `read`, full sentences are fine where they carry logic.
- **White space**: is there breathing room around the key element? White space is how the main point gets isolated, not wasted area.
- **Speaker-notes test** (`presented`): is text on the slide that should be said instead of shown?
- **Repetition**: title and body saying the same thing.

## How to cut (use in fixes)

paragraph → bullets → diagram · sentence → headline phrase · detail → speaker notes or appendix · five points on one slide → build or split

## Score anchors

5 — every slide has one clear focus; density fits the delivery mode
4 — 1–2 slides over-dense
3 — recurring over-density or several slides without a clear focus
2 — most slides are text blocks or cluttered composites
1 — document pasted into slides; unreadable when presented
