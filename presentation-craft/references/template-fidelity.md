# Template & brand fidelity

Score only when a corporate master, brand template or brand guidelines exist. The question: does the deck use the system correctly, or does it drift?

If the user can share the template file or brand guidelines, compare against them. If not, infer the system from the master layouts and the majority of slides, and flag deviations from that majority.

## Checks

- **Master usage**: slides built on the template's layouts, not on blank slides with manually recreated elements (check `deck_inventory.py` layout names — many "Blank" layouts in a templated deck is a signal).
- **Fonts**: only the brand fonts; no substitutions (e.g. Arial creeping in from pasted content). The inventory lists every family used.
- **Colors**: only palette colors; off-palette colors from pasted charts or images are a common drift. The inventory lists fill and text colors.
- **Logo & mandatory elements**: correct logo version, position and clear space; required footers, confidentiality labels, slide numbers, disclaimers present.
- **Chart styling**: charts use the brand chart palette and fonts, not Office defaults.
- **Imagery & iconography**: from the brand library or matching its style.
- **Tone of voice**: wording conventions (title case vs sentence case, terminology) followed.
- **Pasted-in content**: slides copied from other decks with a different look — a frequent consistency break.

Deliberate deviations (a client co-branded slide, a section that needs a different look) are fine if justified; accidental ones are findings.

## Score anchors

5 — indistinguishable from a brand-team-produced deck
4 — one or two small drifts
3 — several drifts (off-palette charts, a stray font, manual layouts)
2 — template used loosely; looks assembled from different sources
1 — template ignored or broken
