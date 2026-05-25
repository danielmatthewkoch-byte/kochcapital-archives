# Koch Capital Archives — Add-a-Post Runbook

Repo: `danielmatthewkoch-byte/kochcapital-archives` → auto-deploys to **archives.kochcapital.io** via Cloudflare (~1–2 min).
Site serves from the **`/public/`** folder. Everything below lives under `public/`.

---

## THE GOLDEN RULE: one date, four places

The **slide's build date** (top-right of the hero slide: `ISSUE №026 · MM.DD.26`) is the single source of truth. That exact date must appear in **all four** places. If they ever drift, the slide wins.

- [ ] **1. Slide top-right** — `MM.DD.26` (this is the master date)
- [ ] **2. Post brand-bar** (top-right of page) — `Issue №026 · MM.DD.26`
- [ ] **3. Post eyebrow** (the dot line under the brand bar) — `… · MM.DD.26`
- [ ] **4. Post byline** ("blog date" under the title) — `Month D, 2026`
- [ ] **5. Homepage entry** (`index.html` list) — `Month D, 2026`

> The byline is the one that silently drifts — it's hand-typed and easy to forget. Check it every time.
> Note: the eyebrow may carry a separate **event** date in the body/caption; that's fine. The header dates (1–5) all use the **build** date.

---

## Publishing steps

### A. Slides → `public/assets/`
- [ ] Render at 1080×1350, device_scale_factor=2.
- [ ] Add file → Upload files → navigate INTO `public/assets` (check breadcrumb: `…/public/assets`).
- [ ] Open the folder on your Mac, **Cmd+A to select the PNG files**, drag the **files** — never the folder. (Dragging a folder nests them as `assets/<foldername>/x.png` and breaks every image.)
- [ ] Upload preview should show individual filename rows, not one folder row.
- [ ] More than 100 files? Split into batches (100/commit limit).
- [ ] Exclude any ` 2.png` "Keep both" duplicates from Mac.

### B. Post page → `public/posts/`
- [ ] Filename is lowercase-hyphen, e.g. `my-post.html`.
- [ ] **Check for a name collision first** — if `posts/<name>.html` already exists and it's a different story, rename the new one (e.g. `polymarket-launch.html`). Don't overwrite.
- [ ] Confirm all 4 header dates match the slide (see Golden Rule).
- [ ] Disclosure block present if a 1789 holding is the subject or is named (see list below); omit if not.
- [ ] Sources list filled in.
- [ ] Upload the `.html` file the same way (files, not folder).

### C. Homepage → `public/index.html`
- [ ] **Replace the whole file** — don't paste into the middle. (Pasting mid-file is what failed before.)
- [ ] New `<li class="landing-list-item">` goes at the **top** of `<ul class="landing-list">`, newest first.
- [ ] Entry date (`landing-list-date`) = the slide date, `Month D, 2026`.
- [ ] List stays in reverse-chronological order top to bottom.

### D. Verify after deploy (~1–2 min)
- [ ] Homepage shows the new entry at the right spot with the right date.
- [ ] Click it: page opens, **brand-bar + eyebrow + byline all match** the homepage date.
- [ ] All slides load (no broken images → if broken, check for the nested-folder bug in A).

---

## Disclosure rules (the author = "The author")

- Caption/post sign-off: **"— Frontier-first."** Never the firm name in captions.
- Use **"The author is a Limited Partner in 1789 Capital, which holds a position in [X]."** (or "positions in X, Y, and Z").
- Always add: **"Personal commentary and editorial analysis. Not investment advice, not an offer or solicitation."**
- Disclose only when the subject (or a named company) is a **1789 holding**.

**1789 holdings (disclose):** Anduril, Cerebras, Crusoe, Databricks, Deel, Groq, Hadrian, Neuralink, Plaid, Polymarket, Ramp, Reflection AI, SpaceX, Substack, Vulcan Elements, X, xAI, Perplexity, Firehawk Aerospace, PsiQuantum.

**Do NOT disclose / not held:** Anthropic (Claude), OpenAI, Google/Gemini, NVIDIA, Thinking Machines, CoreWeave, and any company not on the list above.

- Vulcan Elements posts add: *early-stage investor in Vulcan Elements and LP in 1789 Capital, which also holds a position.*

---

## Brand quick-reference

- Fonts: Archivo Black (display), Instrument Serif italic (accents), JetBrains Mono (labels).
- White background, pure black text. Single-word + period headlines.
- **Issue №026** throughout 2026.
- Post pages link to the shared `../style.css`; don't inline post CSS.

---

## If something breaks

- **New entries don't show on homepage** → the `index.html` edit didn't take. Replace the whole file again.
- **Images broken on a post** → nested-folder upload bug. Delete the stray subfolder in `public/assets`, re-upload the files directly.
- **A new post 404s** → file didn't land in `public/posts`, or the homepage link points to the wrong filename (check rename, e.g. `-launch`).
- **Cloudflare build fails on `.pack` size** → already solved by the `/public/` structure; `.git` lives outside `/public/` so it's never scanned. Don't move the site back to repo root.
