# Personal academic website

A small static site (plain HTML + CSS). No build step: what's in this folder is exactly what gets served.

## Structure

| Path | What it is |
|---|---|
| `index.html` | The whole site (one page): photo with education timeline, name with contact links (CV, LinkedIn, email), bio, working papers |
| `css/style.css` | All styling. Colors and fonts are set at the top in `:root` |
| `files/` | Public PDFs: `Mingjie_Cao_CV.pdf`, paper drafts, slides |
| `cv/` | CV source (`cv.tex`). Run `./cv/build.sh` to rebuild `files/Mingjie_Cao_CV.pdf` |
| `images/` | Portrait photo (`portrait.jpg`, 640×800, location data removed), talk photo below the papers (`talk.jpg`, 935×895, no metadata), "MC" tab icons, faint dotted world map (`world-map.svg`, built from public-domain coastline data), link-preview card (`share-v2.jpg`; rename it when the card changes so LinkedIn fetches the new one, 2400×1260, shown when the site is shared) |
| `favicon.ico` | Browser-tab icon ("MC" in Garamond on navy) |
| `CNAME` | Your custom domain (added when you set up hosting) |
| `.nojekyll` | Tells GitHub Pages to serve files as-is |

## Adding a working paper

In `index.html`, copy one `<article class="paper">…</article>` block under **Working Papers**, then edit the title, the short plain-language story, where it was presented, the PDF link, and the abstract. Drop the PDF into `files/`.

## Previewing locally

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Publishing

Hosted on GitHub Pages: push this folder to a GitHub repository, enable Pages (Settings → Pages → deploy from `main` branch, root folder), and add your domain. Changes go live a minute or so after each push.
