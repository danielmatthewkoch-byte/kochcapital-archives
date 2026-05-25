# Architecture & Deploy

## Hosting
- Repo: `github.com/danielmatthewkoch-byte/kochcapital-archives`
- Host: **Cloudflare** (Workers/Pages), auto-deploys on commit to the default branch.
- Live: **archives.kochcapital.io** (plural — "archives").
- Propagation: ~1–2 minutes after commit.

## Critical: the `/public/` structure
The site serves from the **`public/` subfolder**, NOT the repo root.

```
repo root/
  wrangler.jsonc          ← "assets": { "directory": "./public/", "not_found_handling": "404-page" }
  .git/                   ← lives at root, OUTSIDE /public/, so Cloudflare never scans it
  public/
    index.html            ← homepage (the list / table of contents)
    style.css             ← shared stylesheet for all posts
    assets/               ← all slide PNGs + logo.png + og-image.png
    posts/                ← one HTML file per post
```

**Why:** Cloudflare's asset scanner choked on `.git/objects/pack/*.pack` exceeding the 25 MiB asset limit (a known Cloudflare bug; `.assetsignore` was unreliable). Moving served files into `/public/` puts `.git` out of scope permanently. **Do not move the site back to repo root.**

## Adding a post (mechanics)
1. Slides → `public/assets/` (the PNGs).
2. Post page → `public/posts/<slug>.html`.
3. Homepage → edit `public/index.html`, add the `<li>` at the top of `<ul class="landing-list">`.

(Full step-by-step with the gotchas is in `CHECKLIST.md`.)

## GitHub web-UI gotchas (hard-won)
- **Drag files, not folders.** Dragging a folder into the upload box nests files (`assets/<folder>/x.png`) and breaks every image. Open the folder, Cmd+A the files, drag the files.
- **100 files per commit** max — split large asset batches.
- **Verify the breadcrumb** (`…/public/assets`) before uploading so files land in the right place.
- **Replace `index.html` wholesale** — select-all, delete, paste the full file. Pasting into the middle is error-prone and has failed before.
- Mac "Keep both" creates ` 2.png` duplicates — exclude them.
- HTML files preview inline instead of downloading — zip them to force a download. Don't "Save as PDF" for HTML. The iOS Claude app has no clean HTML save; use Safari or the Mac.

## Rendering notes (slides)
- Chromium is pre-installed at `/opt/pw-browsers`; set `PLAYWRIGHT_BROWSERS_PATH` before running Playwright.
- Google Fonts CDN is blocked in the sandbox — install via npm `@fontsource` and base64-inline as `@font-face`.
- Prefer surgical, slide-specific re-renders over full-deck re-renders.
- For valbox `.num` font sizes, ~152px max prevents `%` clipping within a ~480px valbox.

## Filename collisions
Before naming a post, check `public/posts/` for an existing file of the same name. If the new story is different, rename it (e.g. `polymarket-launch.html`) so the original isn't overwritten — and point the homepage link at the new name.

## If a deploy fails on `.pack` size
This is the bug the `/public/` structure already fixes. Confirm `wrangler.jsonc` still points `"directory": "./public/"` and that `.git` is at the repo root (outside `public/`).
