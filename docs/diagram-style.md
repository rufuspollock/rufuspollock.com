---
title: Diagram Style
created: 2026-11-12
---

# Diagram Style

How we draw explanatory diagrams for essays: technical, a little isometric, after [makingsoftware.com](https://makingsoftware.com). First used in [[The Mug, the Doughnut and the DAO]]. The script that draws its figures is [`diagrams/the-mug-the-doughnut-and-the-dao.py`](diagrams/the-mug-the-doughnut-and-the-dao.py): copy it as a starting point.

## Look

- **Palette.** Cobalt ink `#1F3FD1` on a pale blue-white `#F6F8FD` with a dot grid `#C8D2EC`. Faces in three tints: `#FFFFFF` (top), `#E4EAFC` and `#C3D0F7` (sides), `#9DB1F1` for shadowed insides. One accent, orange `#FF5A1F`, used only for the thing the figure is about (the hole, the fee). Secondary labels in a soft blue `#7D93E6`.
- **Type.** Monospace, upper case, letter-spaced. Title top left as `FIG. N — CLAIM`, with a rule under it. Labels have a background-coloured halo (`paint-order="stroke"`) so they stay legible over lines.
- **Isometric.** Objects are simple boxes, cylinders and prisms in a standard isometric projection; top face lightest, one side mid, the other darker. Flows (money, goods) are arrows drawn on the ground plane.
- **Labels with leader lines.** A dotted line and a dot from the object up to its label, rather than labels sitting on the drawing.
- **Attribution.** Bottom right, small and soft: `CC-BY Rufus Pollock · rufuspollock.com` (plus `openrevolution.net` where relevant). No logo, no copyright line.

## Content

- **One claim per figure, stated in the title.** "Airbnb is a market square", not "Marketplaces".
- **Draw the structure, not the decoration.** Put what owns what in the geometry: the owner stands outside the ground they own, and what sits on the platform is what trades on it. Decorative objects (a fountain) invite the wrong reading.
- **Side-by-side comparisons use identical geometry**, so the eye sees the sameness. Put the comparison detail in a small table under the drawing rather than crowding labels onto it.
- **Captions** go in the essay, in italics directly below: `*Fig. 1. …*`.

## Files

- SVG is the source and what the page shows. Also export a 2x PNG next to it for Substack, email and social cards; PNGs keep the font exact.
- Store both in `images/<page-slug>/`; generate them with a script in `docs/diagrams/` so they can be re-drawn.
- Check the render as an image (not just in a browser tab) before publishing: labels overlap more often than you expect.
