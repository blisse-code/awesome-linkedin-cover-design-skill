# Visual system

## Type

- **Golden-ratio scale** from the smallest size: 30 → 48.5 → 78.5 px on the 1584-wide canvas. The hook gets the top tier; supporting text the base tier; numbers or URLs the middle tier.
- **Minimum size:** 30px if the user wants mobile legibility; tell them it still renders ~7px on phones. If a layout forces a uniform scale-down, report the new smallest size.
- **Roles:** one display face for the hook, one clean sans for support, one mono for URLs if the URL is a hero. Ask the user; respect named fonts exactly and verify the downloaded file's family name before telling them a font "looks different".
- **Weight quirks:** some families widen sharply at heavy weights (Syne 800 is ~80% wider than 400). Show a weight specimen when choosing. If the family maxes out (Plus Jakarta Sans at 800) and the user wants bolder, a 1px same-colour stroke reads as Black without distortion.
- **Contrast:** brand golds and pastels often fail on light backgrounds. Darken the accent for light mode (for example #C9A84C → #8C6A1F on cream).

## Colour

Pull tokens from the user's website when they have one, so the click-through feels continuous. Offer light and dark when asked, and say which one matches their site.

## Patterns and textures

A pattern must mean something about the person, sit seamless and faded, and never compete with text.

| Pattern | Signals | Notes |
|---|---|---|
| Dot grid | designer's canvas | add one accent path through it |
| Fine layout grid | systems thinking | 8px rhythm gets busy; use 24–40px |
| Topographic contours | navigating complex terrain | elegant; one accent contour line |
| Isometric lattice | structure, architecture | very subtle; can disappear |
| Film grain + light leak | photography, cinema | texture only |

Placement options to offer: full bleed and faint, stronger at the edges and fading behind text, or framing the hero only. Draw patterns as vectors in code; do not generate them with an image model.

Rejected in real use: chaos-to-order diagrams, decision-tree trails, spec redlines plus token swatches all at once. Too many stories. Swatch columns read as documentation, not branding.

## Hero elements

- **Glass URL field:** a real 3D glass render with thickness, refraction and three specular highlights showing light direction (top-left corner, top-edge middle, exit at bottom-right) reads as premium; a flat drawn rectangle does not. Render the empty glass with an image model, then place text in code. Flat front-facing beats tilted text, which looks warped.
- **Cursor:** macOS pointer (black arrow, white keyline, soft shadow). Click ripple as flat 2D circles, never squashed ellipses.
- **Device mockup:** draw the device (bezel, notch, aluminium base) as vectors and place a real screenshot of the user's site, with their permission. It becomes illegible on mobile; that is acceptable as long as text stays clear.
- **Side graphics:** only if they carry meaning and look crisp. Generic AI isometric stacks were rejected as "absurd and indistinct".

## Image-model prompts for plates (initial drafts)

Always ask for 21:9 and crop the centre 4:1 band (a 16:9 crop discards 56% of pixels). Ask for no text, no cursor, empty glass. Template:

```
Ultra-wide premium banner background plate, no text. [Palette from brand tokens].
[Mode] canvas with a [pattern] at very low contrast. Hero: one empty, thick,
front-facing 3D frosted-glass input field with real thickness, refraction and
[accent]-gold specular highlights at the top-left corner, top-edge middle and
bottom-right corner; soft reflection below. Composition: the field spans
[x%]–[x%] of the width and [y%]–[y%] of the height; the left [n]% stays empty;
the area above the field stays clean for a headline. No text, letters, numbers,
logos, cursor or people. Photoreal, ray-traced, restrained.
```

For edits ("remove the grid", "remove the side graphic") pass the previous plate as a reference and list exactly what must stay identical.

## Motion versions

If asked for motion: LinkedIn covers are static, so motion is for Featured, posts or a site hero. High-end motion keeps objects still and moves light (specular sweeps, pulses) with a slow, subtle camera dolly added in post. Exploding parts, tilting cards and dips to black read as cheap. Pick a model that honours start and end frames for a clean loop, and composite text separately.
