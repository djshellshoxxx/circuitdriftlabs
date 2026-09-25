# Circuit Drift Lab website

A static website for GitHub Pages. The working brand name is **Circuit Drift Lab**. Everything loads from this folder: no package manager, framework, build step, tracking, or stock images.

## Preview on your computer

Open `index.html` in a browser, or serve it locally with `python -m http.server 8000` and open `http://localhost:8000`.

## Publish with GitHub Pages

For a site at `https://djshellshoxxx.github.io/`, copy the **contents** of this folder to a new public repository named `djshellshoxxx.github.io`. On your Windows PC, after extracting the ZIP and opening PowerShell inside the extracted folder:

```powershell
git init -b main
git add .
git commit -m "Build Circuit Drift Lab website"
gh repo create djshellshoxxx.github.io --public --source=. --remote=origin --push
```

Then open the repository's **Settings → Pages**. Choose **Deploy from a branch**, select **main** and **/(root)**, then save. GitHub will show the live address on that page after deployment. If a repository with that name already exists, use a different repository name and follow the same Pages settings; all asset paths are relative and will work under a project URL.

## Add plugins later

Edit `products.js`. Uncomment the sample and add one object per published plugin with `name`, `type`, `description`, and a public `url`. The release section only appears when it has entries. There are no invented product names, release dates, prices, compatibility claims, or download links in this version.

Change the brand name and company copy directly in `index.html`; the palette and layout are in `styles.css`. Run `python tools/generate_art.py` to regenerate the SVG drawings if you edit their source. The artworks use the colors and flat technical style from `theme.md`.

## Files

- `index.html` — page structure and copy
- `styles.css` — responsive design
- `site.js`, `products.js` — optional release cards
- `assets/*.svg` — original vector drawings
- `tools/generate_art.py` — reproducible vector art source
- `.nojekyll` — serves the static files directly on GitHub Pages

The chosen name is a working title. Before using it commercially, check domain and trademark availability for your markets.
