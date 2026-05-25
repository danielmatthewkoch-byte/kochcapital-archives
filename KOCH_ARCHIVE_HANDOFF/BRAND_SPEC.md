# Frontier-first — Brand Spec

The visual system for Koch Capital's Frontier-first content (Instagram carousels + archive web posts).

## Typography
- **Display / headlines:** Archivo Black
- **Accents / emphasis:** Instrument Serif, italic
- **Labels / mono data:** JetBrains Mono
- Body (web posts): Archivo

Headlines are **single word + period** — `CLAUDE.` `QUANTUM.` `STARGATE.` Section headers may pair roman + italic: **THE** *TRAJECTORY.*

## Color & layout
- Pure **white** background, pure **black** text.
- 1.5px borders/rules.
- High contrast, editorial, lots of negative space.

## Slides
- Render at **1080 × 1350**, `device_scale_factor=2`.
- Masthead top-right every slide: `ISSUE №026 · NN / NN` then `CATEGORY · MM.DD.26`.
- **Issue №026** is used throughout all of 2026.
- Hero (slide 01): masthead, eyebrow (`● CATEGORY · HEADLINE · MM.DD.26`), giant headline, dek (serif italic mix), a black stat box, and a footer strip with a kicker stat.
- Final slide is "THE READ" — a pull quote with attribution and a source line.
- Each inner slide carries a `SOURCE · …` line bottom-left.

## Dates on slides (important)
- **Top-right masthead date = the build date** (the day the slide was made / the "post date").
- An **event date** may appear in the eyebrow or body (e.g., a deal announced earlier). That's allowed and lives only in eyebrow/body/captions.
- The build date is what every downstream field keys off of. See `CHECKLIST.md`.

## Sign-off & voice
- Sign-off: **"— Frontier-first."**
- Voice: spare, momentum-forward, declarative. "Less is more."
- Firm name stays **anonymous in captions** — never "Koch Capital" in a caption; use the sign-off.

## Web post structure
Post pages reuse the shared `public/style.css`. Structure (top to bottom):
`brand-bar` → `eyebrow` → `title` → `dek` → `byline` → `body` (slides as `figure.slide` + prose) → `blockquote.pull` (+ italic full quote) → final quote `figure` → `disclosure` (if applicable) → `sources` → `post-footer` (`— Frontier-first.`).

See `_TEMPLATE.html` for the exact markup.

## Do / Don't
- **Do** keep all header dates equal to the slide build date.
- **Do** link posts to `../style.css` (shared stylesheet), not inline CSS.
- **Don't** put the firm name in captions.
- **Don't** use the "Frontier-first" tagline on **KOCH SEATTLE** material — that's a separate brand (Cinzel / Cormorant / Jost, forest/cobalt/cream). Frontier-first and KOCH SEATTLE never mix.
