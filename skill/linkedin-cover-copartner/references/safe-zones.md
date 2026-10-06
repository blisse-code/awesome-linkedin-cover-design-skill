# Safe zones

All coordinates are in banner pixels on the 1584x396 canvas.

## Measured geometry (from real screenshots, October 2026)

LinkedIn changes its layout. Treat these as defaults and re-measure from the user's own screenshots whenever possible.

| View | Banner shown at | Profile photo (circle bbox incl. white ring) | UI icon over banner |
|---|---|---|---|
| Desktop profile | ~0.45x | x 60–459, y 156–555 | Edit pencil x 1456–1534, y 38–114 |
| Mobile app | ~0.24x, **full width** | x 76–634, y 76–634 | Gear x 1386–1521, y 76–211 |
| Side panel / feed card | ~0.12x | x 141–904, y 356+ (mostly below) | none |

Key consequences:
- Mobile shows the whole banner, not a centre crop, but the photo is huge. For text, the usable area below y 76 starts around x 640 (the circle edge curves, so lines higher up can start a little further left; check with the simulator).
- Above y 76 the full width is clear on all views (good for an eyebrow line).
- The right edge must avoid the desktop pencil and the mobile gear. Users often accept a device mockup being partly covered on mobile; never text.
- Mobile renders at ~0.24x: 30px becomes ~7px, 48px ~11.5px, 78px ~19px. Only the hook and a large URL truly read on phones.

## Generic advice to treat with caution

Articles commonly say "keep the bottom-left quarter empty" and "mobile crops to the centre 60%". The first is roughly right for desktop; the second was wrong on the measured profile. Always prefer the user's screenshot.

## Re-measuring

1. Ask for desktop and mobile screenshots of the profile with the banner live.
2. Run `scripts/measure_from_screenshot.py` with the banner's left/right x in the screenshot and the photo circle's left, right and top in screenshot pixels. It prints banner-space coordinates.
3. Update the geometry passed to `scripts/simulate_views.py`.

## Vertical balance

Measure the real ink extents of the text block (top of the eyebrow caps to the bottom of the last descender) and centre that span on y 198. Do the same check for the device / URL group and report both.
