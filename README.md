# Frontier-first · Editorial Archive

Static site containing the Frontier-first newsletter archive — **26 editorial posts** as full-length web articles.

## Structure

```
/site
  ├── index.html          ← Archive landing page (grid of all 26 posts)
  ├── style.css           ← Shared brand stylesheet
  ├── site_generator.py   ← Python generator (re-run after editing POSTS)
  ├── assets/             ← 134 slide images at full resolution
  └── posts/              ← 26 individual article pages
```

Every page is a self-contained HTML file. No build step. No frameworks. Pure HTML/CSS, mobile-responsive, brand-consistent.

## All 26 Posts (chronological)

**April 2026:**
- Cerebras (IPO announcement)
- Deployed (Department of War / Pentagon AI deployment)
- Polymarket
- Reflection AI
- Aligned (Anthropic × SpaceX)
- Starship ($15B program)
- xAI / SPACEXai (xAI × SpaceX merger)
- Terafab
- Groq
- Diverged (Mag 7)
- Firehawk Aerospace
- The Book (Cerebras IPO update)
- Day One (Enhabit NYSE listing)
- Trophy Assets (Blue Owl)

**May 2026:**
- New Highs (April rebound)
- The Big Short 2.0 (Burry)
- Flight 12 (SpaceX V3)
- Physical AI (WEF Davos)
- The AI War (US-China decoupling)
- Agentic (Anthropic Wall Street)
- The Toolbox (Chatbot market)
- The Link (Neuralink)
- Arsenal (Anduril)
- American Made (Hadrian)
- Rare Earth (Vulcan Elements)
- The Orchestrator (NVIDIA)

## Deployment

**Recommended: Cloudflare Pages (free, fast)**
1. Push this folder to a GitHub repo
2. Connect Cloudflare Pages
3. No build command, output directory = `/`
4. Custom domain: `read.frontier-first.com` or similar
5. Update Instagram bio link

**Alternatives:** Vercel, GitHub Pages, Netlify — all identical workflow.

## Adding New Posts

1. Edit `site_generator.py` — append a new dict to the `POSTS` list
2. Drop the new slide PNGs into `/assets/`
3. Run `python3 site_generator.py`
4. Commit, push, deploy

## Brand System

All styling in `/style.css`. Single source of truth — edit there to update brand-wide.

- Display: Archivo Black
- Italic accents: Instrument Serif Italic
- Monospace metadata: JetBrains Mono
- Body: Archivo

Matches the Instagram carousel system exactly.

## Notes

- Byline reads "By KOCH CAPITAL" on every post
- Source links are live and open in new tabs
- Disclosures are baked into each post page
- Mobile-responsive
