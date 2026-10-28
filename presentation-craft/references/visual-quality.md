# Visual quality & craft

This is the dimension that matters most when there is **no template**: nobody else made the design decisions, so every decision is the author's. The question is not "is it pretty" but "does it look intentionally designed, by someone who controls type, color, space and image?"

With a template, score this lighter: focus on how well content was placed *within* the system (image quality, chart styling, spacing discipline), since the system itself was given.

Evaluate from the slide images, not from extracted data.

## 1. Typography

- **Pairing**: a clear role for each family (display / text / data). Two families is a sensible default for business decks; a third (e.g. mono for data) is fine if it has a role. More families without roles is a finding. `deck_inventory.py` lists families in use.
- **Not only "sans-serif"**: serif display faces, condensed or expressive type are legitimate — especially in `creative`, `keynote` and `pitch` decks. Judge whether the choice suits the content and is executed well, not the category.
- **Type scale**: a limited set of sizes with clear steps (e.g. 72 / 40 / 24 / 18 / 12). Many near-identical sizes (20, 21, 22, 24) = no system.
- **Craft details**: line length (roughly 45–75 characters for body), line spacing (≈1.1–1.3 for body, tighter for big display), no widows/orphans in titles, no faux bold/italic, no stretched or squashed text, consistent case for titles, proper quotes and dashes, tracking adjusted on all-caps.
- **Default fonts** (Calibri, Arial, Aptos, Helvetica-by-default) aren't wrong, but in a no-template deck they signal no typographic decision was made — note it under Originality, not here, unless execution is also weak.

## 2. Color

- **Palette discipline**: a small, defined palette (typically 1 primary, 1 accent, neutrals, plus semantic colors if data needs them). Colors used by role, not decoration.
- **Harmony**: colors belong together (shared temperature, saturation logic); no clashing saturated pairs side by side unless intentional.
- **Neutrals**: greys/off-whites chosen, not default `#808080`; text not pure black on pure white if the palette is warm/soft (and vice versa — judge coherence).
- **Consistency**: the same color means the same thing on every slide.
- **Backgrounds**: dark/light switching has a logic (e.g. section breaks), not random.

## 3. Imagery & graphics

- **Resolution**: no pixelated, upscaled or compressed images; no visible watermarks.
- **Cropping & placement**: intentional crops; faces/subjects not cut awkwardly; full-bleed images reach the edge cleanly.
- **Coherent style**: photos share a treatment (light, color grade, framing); illustrations share a style; icons come from one set with the same stroke weight, corner style and size.
- **Relevance**: images carry meaning. Generic stock (handshakes, puzzle pieces, people pointing at screens, lightbulbs) is decoration → also an Originality finding.
- **Distortion**: no stretched logos or images (aspect ratio broken).
- **Logos**: correct version, clear space respected, not on a busy background.

## 4. Composition

- **Grid**: a visible underlying structure (columns, margins) used consistently; occasional deliberate breaks are fine.
- **Scale contrast**: confident size differences (a big number, a big image) create interest; everything medium-sized looks timid.
- **Negative space**: used as a design element, not leftover.
- **Rhythm across the deck**: a variety of layouts (statement, image, data, comparison) within one system — monotony (every slide identical) and chaos (every slide different) are both findings.

## 5. Finish & polish

- Consistent corner radii, stroke weights, shadows (ideally none or one style).
- No leftover placeholder text, lorem ipsum, "Click to add title", default theme artifacts, misaligned text boxes, broken master elements.
- Slide numbers, footers and sources styled consistently.
- Exported PDF renders fonts correctly (no fallback font substitutions — check the rendered images for odd faces).

## Score anchors

5 — looks professionally designed: controlled type, palette and imagery; nothing to clean up
4 — strong system with a few unpolished spots
3 — competent but generic or inconsistent in places (mixed icon styles, loose type scale, a few low-res images)
2 — visibly amateur: default styling with errors, clashing colors, distorted images
1 — visual execution actively undermines credibility
