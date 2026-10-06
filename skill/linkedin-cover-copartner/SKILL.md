---
name: linkedin-cover-copartner
description: Co-design a LinkedIn profile cover / banner (1584x396) with the user as a creative partner, not a template machine. Use whenever someone asks to create, redesign, critique, or improve a LinkedIn banner, cover image, background photo, profile header, or "billboard" for their personal brand, including requests that mention hooks, taglines, CTAs, safe zones, profile-photo overlap, mobile cropping, glassmorphism, mockups, or AI image prompts for a banner. Also use for X/Twitter headers or YouTube channel art when the user wants the same guided process. The skill forces a structured intake (goal, audience, proof, offer, contact path, taste references, brand assets, real profile screenshots), synthesizes the user's inspirations, proposes options with scores, iterates one change at a time, and verifies every draft against measured desktop, mobile and side-panel views before delivery.
---

# LinkedIn Cover Co-Partner

A banner is a billboard that gets about one second. This skill exists because the fastest way to a bad banner is to skip the person: their goal, their proof, their taste, and how their profile actually renders. Every step below either gathers what only the user knows or shows them options to react to. Do not jump to a finished design.

## Operating principles

1. **Ask before you make.** Never produce a visual draft until the intake gates (Phase 0) are passed. If the user says "just make something", run a 3-question minimum intake (goal, audience, one reference) and state your assumptions in writing.
2. **References before taste.** The user's inspirations define the target. Analyse them out loud (what each one does, what to borrow, what to avoid) before proposing anything.
3. **Options, scored.** Offer 2 to 3 directions at each decision point with a short scoring table. Recommend one. Let the user choose.
4. **One change per round.** When refining, change only what was asked plus what that change forces. Say what moved and why. Unrequested moves of approved elements erode trust fast.
5. **Restate before big moves.** If an instruction is ambiguous (for example a wireframe element that might be a placeholder), restate your understanding in plain words, ideally with a quick sketch, and ask for confirmation.
6. **Verify on the real thing.** Simulate desktop, mobile and side-panel views using measured geometry, and ask the user for real screenshots after they upload. Their screenshot beats any article.
7. **Honesty over polish.** Flag claims the user cannot defend, numbers that conflict across their materials, and trade-offs you made. Never invent credentials, logos, testimonials or metrics.

## Workflow

### Phase 0. Intake (mandatory gates)

Ask in small batches (max 3 questions per message; use the tappable-options tool when available). Do not move on until each gate is answered or explicitly waived. Full question bank with option sets: `references/intake-questions.md`.

- **Gate A. Goal and audience:** primary goal (get hired, win clients, partners, mentees, speaking), primary audience to self-identify, the one action wanted from a visitor.
- **Gate B. Substance:** what they help with, the result they deliver, verifiable credentials (years, launches, clients served, recognitions, mentoring hours), and where to send people (URL on the banner vs "see Featured").
- **Gate C. Taste:** at least 2 reference banners or images they like and why, anything they dislike, brand assets (website URL, palette, fonts, logo, photography), light vs dark vs both.
- **Gate D. Reality:** a screenshot of their current profile on desktop and on mobile (or permission to work from default geometry and verify later), and their profile photo colours so the banner complements it.

If the user cannot share references, offer 3 contrasting mini moodboards in words and let them pick.

### Phase 1. Research and synthesis

- Analyse each reference: message, background, pattern, proof, CTA, and the one lesson it teaches. Use a compact table.
- If they have a website, pull its colour tokens and fonts so the banner is cohesive.
- State the design brief back in 5 to 7 lines and get a yes.
- Best-practice frameworks to apply (and their tensions) are in `references/copy-framework.md`.

### Phase 2. Copy first

Banners fail on words more often than on visuals. Draft 2 to 3 copy sets covering: who it is for, the value (hook), how they help, a credential, and the contact path. Run the persona test (hiring manager, client or founder, student, partner) from `references/copy-framework.md` and show the table. Get the copy locked before layout.

### Phase 3. Structure

- Propose 2 to 3 layout directions (for example Bold Authority, Textured Minimalist, Portfolio Showcase) or accept the user's wireframe.
- Treat wireframes as structure. Crops of earlier drafts inside a wireframe are usually placeholders, not instructions. Ask if unsure.
- Place everything inside the measured safe zones: `references/safe-zones.md`.

### Phase 4. Visual drafts

- Build at 1584x396 plus a 2x export. Use the visual system in `references/visual-system.md` (golden-ratio type scale, patterns that mean something, colour from their brand, glass and cursor details, device mockups with their real site).
- Generated imagery is for plates and materials only (glass, light, texture). Always composite text yourself so it is pixel-sharp; image models warp letters.
- Deliver at most 3 variations per round with a scoring table (`references/copy-framework.md` has the rubric) and a recommendation.

### Phase 5. Refinement loop

- Apply the requested change, keep approved elements fixed, report exact before and after values (sizes, positions, gaps).
- If a request conflicts with an earlier rule (minimum text size, safe zone), say so and offer the two options instead of silently breaking one.
- Keep a short running decision log in the conversation so nothing approved gets lost.

### Phase 6. Verification

- Run `scripts/simulate_views.py` on every candidate to produce desktop, mobile and side-panel previews with the profile photo and UI icons overlaid.
- After the user uploads, ask for fresh screenshots and re-measure with `scripts/measure_from_screenshot.py` if anything is covered.

### Phase 7. Delivery

Deliver PNGs (1584x396 and 3168x792), light and dark if requested, plus the view-simulation sheet. Remind them of any consistency fixes (for example the same years-of-experience number on banner, headline and resume). Offer one next move, not a menu.

## Hard don'ts (each one cost a round in real use)

Full list with reasons: `references/lessons-learned.md`.

- Do not trust generic "centre 60% on mobile" advice over a real screenshot. On the profile this skill was built from, mobile showed the full width with a much larger photo.
- Do not add generic AI-looking graphics or decorative widgets that say nothing about the person. Every pattern needs a meaning.
- Do not stack five ideas. One message, very large. Proof and CTA quiet.
- Do not put links people must type as the only path when a Featured section is one tap away. Offer both as variants.
- Do not use emoji or "click below" on a banner; it is not clickable.
- Do not move or rescale elements the user approved unless asked.
- Do not ship a claim the user cannot prove on request.
