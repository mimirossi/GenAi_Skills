# Accessibility (and motion)

Accessible slides are clearer for everyone: the back row of a room, a laptop screen in a hybrid meeting, a phone, a colorblind reviewer, a screen-reader user receiving the PDF.

## Thresholds

| Check | Standard |
|---|---|
| Text contrast | ≥ 4.5:1 for body text; ≥ 3:1 for large text (≥ 24px / ~18pt regular or ~14pt bold) — WCAG 2.x AA |
| Non-text contrast | chart marks, icons, key lines ≥ 3:1 against background |
| Body size, `presented` | ≥ 18pt (≥ 24pt for large rooms) |
| Title size, `presented` | ≥ 28pt |
| Body size, `read` (screen) | ≥ 12pt; footnotes/sources ≥ 9–10pt |
| Color dependency | meaning never carried by color alone (add labels, icons, patterns) |
| Alt text | charts and meaningful images have alt text in decks shared digitally |
| Reading order | logical order in the file (matters for screen readers and PDF export) |

`deck_inventory.py` reports the minimum font size per slide and text/background color pairs where detectable; verify contrast on the rendered images for text over images or gradients — that's where most failures hide.

## Checks

- Light grey text on white, white text on light photos, text over busy images without an overlay.
- Red/green as the only positive/negative signal.
- Thin fonts at small sizes; long all-caps passages; justified text with rivers.
- Dense charts with tiny labels.
- Video without captions; audio without transcript.
- Fast flashing or strobe effects (seizure risk) — **critical**.

## Motion & animation

Score as a separate dimension only if the deck uses animation or transitions; otherwise N/A.

Purposeful uses: revealing points one at a time while speaking, highlighting the bar being discussed, building a diagram step by step, marking a section change.

Findings: objects flying in from different directions, spinning/bouncing text, a different transition on every slide, animation that delays content the audience needs, animation that hides content in the PDF/read version (builds that stack elements on top of each other when printed).

When in doubt, a static slide beats a poorly animated one. Respect reduced-motion needs: no large parallax or zoom effects without reason.

Motion anchors: 5 none or purposeful only · 3 some gratuitous effects · 1 distracting or hides content.

## Score anchors (accessibility)

5 — meets all thresholds; works for colorblind and screen-reader users
4 — one or two contrast or size misses on secondary text
3 — recurring small text or contrast issues
2 — key content fails contrast or size; color-only meaning
1 — large parts unreadable for many viewers
