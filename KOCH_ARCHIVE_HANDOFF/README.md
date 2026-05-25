# Koch Capital Archives — Handoff Package

**Snapshot: May 24, 2026.** This package is the source of truth for the Frontier-first archive site. If anything here disagrees with memory or an old file, **this package wins.**

## What this is

A public-facing archive of Frontier-first Instagram carousel posts, rendered as web pages.

- **Live site:** https://archives.kochcapital.io
- **Repo:** `github.com/danielmatthewkoch-byte/kochcapital-archives`
- **Deploy:** auto-deploys from the repo's `/public/` folder via Cloudflare Workers (~1–2 min after commit).
- **Main site** (`kochcapital.io`) is a separate Wix site — not in this repo.
- **Current size:** 52 posts (see `ARCHIVE_MANIFEST.md`).

## Files in this package

| File | What it covers |
|------|----------------|
| `README.md` | This overview |
| `CHECKLIST.md` | **The add-a-post runbook** — start here when publishing |
| `BRAND_SPEC.md` | Frontier-first visual system (fonts, layout, slide specs) |
| `ARCHITECTURE.md` | Repo structure, Cloudflare deploy, GitHub upload mechanics, rendering notes |
| `DISCLOSURE_RULES.md` | 1789 holdings list + exact disclosure/caption language |
| `_TEMPLATE.html` | Blank post page, pre-wired with the four date fields tagged |
| `ARCHIVE_MANIFEST.md` | All 52 live posts with verified dates |

## The one rule that matters most

Every post carries a date in **four** places that must all match the **slide's build date** (top-right of the hero slide):

1. Slide top-right (`ISSUE №026 · MM.DD.26`) — the master
2. Post brand-bar (top-right of page)
3. Post eyebrow (dot line under brand-bar)
4. Post byline ("blog date" under the title)
5. Homepage list entry

The byline is the one that drifts. `CHECKLIST.md` and `_TEMPLATE.html` exist to keep these locked. This was the source of a full date-audit in May 2026 that corrected 11 posts.

## Recent corrections logged in this snapshot

- Migrated repo to serve from `/public/` (fixes a Cloudflare `.git` pack-size build failure).
- Added 14 posts (Claude → Starship, May 18–22).
- Renamed a colliding `polymarket.html` → `polymarket-launch.html` (preserves the original May 7 Polymarket post).
- Full date audit: corrected 11 early posts so homepage, brand-bar, eyebrow, and byline all match the slide date; re-sorted the homepage to stay reverse-chronological.
