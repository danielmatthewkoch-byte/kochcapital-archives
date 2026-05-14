# Koch Capital Archives

Source for **[archives.kochcapital.io](https://archives.kochcapital.io)** — the public archive of frontier-first posts from Koch Capital.

Auto-deployed via **Cloudflare Pages** from the `main` branch. Any commit triggers a re-deploy within ~30 seconds.

---

## Repo Structure

```
.
├── index.html              # Homepage at archives.kochcapital.io
├── README.md               # This file
├── assets/
│   ├── logo.png            # Koch Capital logo (used in index header)
│   └── og-image.png        # Social share image (optional)
└── posts/
    └── YYYY-MM-DD-slug.html  # Individual HTML carousel posts
```

---

## Daily Workflow — How to Add a New Post

### Step 1 — Save the new post HTML

Filename convention: `YYYY-MM-DD-slug.html`

- **Date** in ISO format (sorts naturally in file lists)
- **Slug** = short kebab-case description of the topic
- Examples:
  - `2026-05-14-vulcan-elements.html`
  - `2026-05-15-defense-tech-thesis.html`
  - `2026-05-16-rare-earths-supply-chain.html`

### Step 2 — Upload the HTML file to GitHub

1. Open this repo on github.com
2. Navigate to the `posts/` folder
3. Click **Add file** → **Upload files**
4. Drag your HTML file in
5. Scroll down, click **Commit changes**

### Step 3 — Add the post to the homepage list

1. In the repo root, open `index.html` and click the pencil ✏️ icon to edit
2. Find the section marked `ADD NEW POSTS BELOW THIS LINE`
3. Just above the `POSTS GO ABOVE THIS LINE` marker, paste this block (newest at the top):

   ```html
   <li class="post">
     <a href="posts/YYYY-MM-DD-slug.html">
       <span class="post-date">Month DD, YYYY</span>
       <span class="post-title">Your Post Title Here</span>
     </a>
   </li>
   ```

4. Fill in the date, filename, and title to match the new post
5. If this is the first post you're adding, also **delete the `<li class="empty-state">Archive coming soon</li>` line** below the markers
6. Scroll down, click **Commit changes**

### Step 4 — Verify

- Cloudflare Pages will auto-deploy within ~30 seconds
- Visit `https://archives.kochcapital.io` to confirm the new post appears in the list
- Click the link to verify the individual post renders correctly

---

## Branding Notes

- **Display font:** Archivo Black (via Google Fonts)
- **Body font:** Inter (via Google Fonts)
- **Color palette:** Pure black `#000000` on pure white `#ffffff`. No greys in the brand color system (light greys used only for secondary metadata text)
- **Sectors:** AI · Minerals · Aerospace · Defense-Tech · Energy · Sports
- **Tagline:** "Frontier-first commentary"
- **Sign-off:** "— Frontier-first."

---

## Disclaimers (Standing)

> Personal commentary. Not investment advice. Not an offer or solicitation.

### When a post references Vulcan Elements or 1789 Capital, append:

> *Disclosure: The author is an early-stage investor in Vulcan Elements and an LP in 1789 Capital, which also holds a position.*

### Confirmed 1789 Capital portfolio (for disclosure purposes):

Anduril, Cerebras, Crusoe, Databricks, Deel, Groq, Hadrian, Neuralink, Plaid, Polymarket, Ramp, Reflection AI, SpaceX, Substack, Vulcan Elements, X, xAI, Perplexity, Firehawk Aerospace.

(1789 Capital does **NOT** hold Anthropic.)

---

## Hosting

- **Host:** Cloudflare Pages (connected to this repo)
- **Branch:** `main`
- **Custom domain:** `archives.kochcapital.io`
- **DNS:** Managed via Cloudflare (root `kochcapital.io` Wix site is unaffected by archive deploys)
