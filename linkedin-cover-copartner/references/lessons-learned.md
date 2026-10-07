# Lessons learned (from a real 23-version engagement)

Each item cost at least one revision. Read before Phase 3.

## Process
- **Restate before building on ambiguity.** A dark block in a user wireframe was a crop of an earlier draft, used as a placeholder. Building it as a design element wasted a round.
- **Keep approved elements fixed.** Moving and shrinking an approved laptop + URL group to make room for a bigger hook was rejected. Solve within constraints, or ask.
- **Ask permission for expensive or irreversible directions** (new layout system, new plate generation) and state credit cost.
- **Do not proceed when the user says not to.** If a deliverable can only be partly met (for example "layered SVG" when the glass is a raster render), explain exactly what is and is not possible and wait.
- **Show, don't describe, when checking understanding.** A quick schematic sketch confirmed a pattern plan faster than paragraphs.

## Copy
- Job titles are not hooks. Values statements are not hooks. Transactions are.
- Delivery menus ("Case studies · Audits · Mentoring") lower perceived seniority.
- "Systems Architecture" reads as software engineering to executives; "Agentic Workflows" implies building agents. Match words to what the person can defend in an interview.
- Banner numbers must match resume, headline and website. Catch mismatches (13+ vs 14+ years, 60+ vs 100+ launches) before publishing.
- Hands-on vs management: if both matter, say it in plain first person ("I lead design teams and still ship the work.").

## Layout and safe zones
- Real mobile view showed the full banner width with a huge photo; the "centre 60%" rule was wrong.
- Right-aligning the text block against a device mockup lets shorter lines step away from the photo circle.
- After removing elements, re-centre the block vertically by measured ink extents, not by baselines.
- Give at least ~50px between the text block and a device mockup; 24px read as cramped.
- Avoid UI icons: desktop edit pencil (top right), mobile gear (right, upper middle).

## Visuals
- Flat code-drawn glass looked fake; a rendered 3D glass with clear light direction worked.
- Perspective-warped URL text looked ugly; keep the field and URL front-facing.
- Generic AI side graphics looked absurd. Decorative token swatches were rejected. Chaos-to-order diagrams were rejected as busy.
- Patterns were requested as "seamless faded" and meaningful; topographic contours from the user's chosen plate worked.
- Squashed-ellipse click ripples read as warped; use flat circles.
- macOS cursor was preferred over a generic white arrow.

## Production
- Composite all text in code. Image models misspell and warp.
- Generate plates at 21:9, crop to 4:1.
- Keep a 2x export (3168x792) for crisp upload.
- Verify every candidate with simulated desktop, mobile and side-panel views, and ask for real screenshots after upload.
