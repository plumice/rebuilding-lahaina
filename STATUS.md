# Rebuilding Lahaina — Thesis Website Status

**Last updated:** 2026-04-03
**Repo:** https://github.com/plumice/rebuilding-lahaina
**Live:** https://rebuildinglahaina.org (behind Cloudflare Access)
**Stack:** Astro 5.x, Tailwind CSS 3.x, Pagefind, Leaflet, GitHub Pages + Cloudflare
**Node:** v22.14.0 | `export PATH="/c/Program Files/nodejs:$PATH"` before npm commands

---

## Project Stats

| Metric | Count |
|--------|-------|
| Total pages | 186 |
| Content files | 184 |
| Sections (thesis text) | 29 |
| Drawings | 60 |
| Sources (bibliography) | 48 |
| Terms (glossary) | 21 |
| Timeline events | 9 |
| Topics | 11 |
| Scales | 5 |
| Maps (interactive) | 1 |
| GIS features | 238 (50 streams + 188 ditches) |
| Searchable words | 3,544 |

---

## Project Structure

```
thesis-website/
├── astro.config.mjs          # Astro config (static, Tailwind, sitemap)
├── tailwind.config.mjs        # Design tokens (light theme)
├── package.json               # Dependencies + postbuild (Pagefind)
├── tsconfig.json              # TypeScript strict
├── STATUS.md                  # This file
├── thesis_source.txt          # Extracted thesis text for reference
│
├── .github/workflows/
│   ├── deploy.yml             # GitHub Pages deploy on push
│   └── fetch-news.yml         # News feed cron (every 6 hours)
│
├── scripts/
│   └── fetch-news.mjs         # Google News RSS fetcher
│
├── public/
│   ├── favicon.svg
│   ├── CNAME                  # rebuildinglahaina.org
│   ├── robots.txt             # Sitemap reference
│   ├── downloads/
│   │   └── final_as_thesis.pdf  # (gitignored, 204MB)
│   ├── data/
│   │   ├── news.json          # Static news feed (auto-updated)
│   │   └── geojson/
│   │       ├── streams.geojson  # 50 features from Hawaii DLNR/DAR
│   │       └── ditches.geojson  # 188 features from CWRM
│   ├── icons/topics/          # 11 topic icon PNGs
│   └── images/drawings/
│       ├── cover_hero.jpg     # High-res hero (3990x2250)
│       ├── complete_ppt/      # 69 slides from COMPLETE PPTX
│       └── updated_*.jpg      # Latest map images
│
├── src/
│   ├── content.config.ts       # Zod schemas for all 8 collections
│   ├── content/
│   │   ├── sections/    (29)   # Verbatim thesis text
│   │   ├── drawings/    (60)   # Drawing metadata + image refs
│   │   ├── sources/     (48)   # Bibliography with thesis discussion
│   │   ├── terms/       (21)   # Full definitions + relatedSections
│   │   ├── timeline/     (9)   # Historical events with body text
│   │   ├── maps/         (1)   # Interactive map configs
│   │   ├── topics/      (11)   # Topic page intros
│   │   └── scales/       (5)   # Scale page intros
│   │
│   ├── layouts/
│   │   ├── BaseLayout.astro    # Global shell (header, nav, footer, meta)
│   │   ├── SectionLayout.astro # Thesis section pages
│   │   └── DrawingLayout.astro # Drawing detail pages
│   │
│   ├── pages/
│   │   ├── index.astro         # Homepage (hero + news + entry points)
│   │   ├── read/               # Narrative path (chapter-by-chapter)
│   │   ├── topic/              # Topic explorer with icons
│   │   ├── scale/              # Scale navigator
│   │   ├── drawing/            # Drawing index + detail
│   │   ├── source/             # Bibliography index + detail
│   │   ├── term/               # Glossary index + detail
│   │   ├── map/                # Interactive GIS maps
│   │   ├── timeline.astro      # Historical timeline
│   │   ├── search.astro        # Pagefind search
│   │   └── 404.astro           # Custom 404
│   │
│   ├── components/
│   │   ├── Nav.astro           # Mobile hamburger + desktop nav + aria-current
│   │   ├── Footer.astro        # Attribution + source/glossary links
│   │   ├── NewsBulletin.astro  # Static news feed (safe DOM, no innerHTML)
│   │   ├── TopicIcon.astro     # Topic icon component (3 sizes)
│   │   ├── TagPills.astro      # Tag display with icons + Pagefind filters
│   │   ├── ContentCard.astro   # Reusable content card
│   │   ├── Breadcrumbs.astro   # Navigation breadcrumbs
│   │   ├── DrawingViewer.astro # Zoomable image (keyboard accessible)
│   │   ├── MapViewer.astro     # Leaflet interactive map
│   │   ├── Sidebar.astro       # Related content sidebar
│   │   ├── PrevNext.astro      # Section navigation
│   │   ├── ScaleNav.astro      # Scale level selector
│   │   └── Timeline.astro      # Timeline visualization
│   │
│   └── styles/
│       ├── global.css          # Design tokens + base styles
│       └── fonts.css           # Self-hosted Inter + EB Garamond (preloaded)
│
└── docs/superpowers/
    └── specs/                  # Design specs (iconography)
```

---

## Content by Chapter

### Ch1: Introduction (3 sections)
- Dedication & Acknowledgements, Abstract, Research Questions & Hypothesis

### Ch2: Overview (4 sections)
- Key Terms & Definitions, Resilience Drivers, Community Anchors, Literature & Methodology

### Ch3: Analysis (8 sections)
- History of Lahaina, Environmental Analysis, Zoning & Land Use, The Water Crisis, Pioneer Mill Water Infrastructure, Fire Analysis, Disaster Gentrification, Cultural Heritage

### Ch4: Principles (5 sections)
- Multi-Scalar Diagnostic, Buffer Framework, Water/Green/Mobility Systems, Street-by-Street Mobility, Water System Zones

### Ch5: Design (9 sections)
- Redensification & Hubs, Design Interventions, Module System, School Design Detail, Module Assembly Rules, District Typologies, Hub Operations, Results & Discussion, Contribution

---

## What's Done

- Full site scaffold (Astro 5.x + Tailwind + Pagefind + Leaflet)
- All 29 sections: verbatim thesis text from thesis_v31.docx + verified research
- All 48 sources populated with thesis literature review discussion
- All 21 terms populated with verbatim definitions + relatedSections
- All 9 timeline events with thesis body text, corrected dates/facts
- 60 drawing entries verified against actual slide images
- 11 topic icons (Gemini-designed, Hawaiian motif-informed)
- GIS data: streams (50 features) + ditches (188 features) from Hawaii State GIS
- Interactive Leaflet map with layer toggles
- High-res cover hero image (3990x2250)
- Static news feed via GitHub Action (6-hour cron)
- Full security audit: XSS fix, keyboard accessibility, ARIA, font preloads, OG images
- Deployed: GitHub Pages + Cloudflare (rebuildinglahaina.org)
- Cloudflare Access for private preview
- WCAG AA accessible, skip-to-content, semantic HTML

## What's Remaining

1. **Topic icon vectors** — replace raster PNGs with proper vector SVGs
2. **Thesis PDF hosting** — 204MB, needs external hosting (Cloudflare R2 or similar)
3. **Mobile testing** — test on actual devices
4. **Content verification** — Ch4+5 sections need re-audit pass

---

## Key File Locations

| What | Where |
|------|-------|
| Website source | `C:\Users\singh\OneDrive\thesis-website\` |
| GitHub | https://github.com/plumice/rebuilding-lahaina |
| Domain | https://rebuildinglahaina.org |
| Thesis text extract | `thesis-website\thesis_source.txt` |
| Parsed content backup | `F:\...\thesis_rebuilding_lahaina\11_website\parsed_content\` |
| Latest PPTX | `C:\Users\singh\OneDrive\PPT\PRES\Lahaina_Thesis_Presentation_Final_COMPLETE.pptx` |
| Latest map images | `C:\Users\singh\OneDrive\PPT\NEWJPSS\` |
| Thesis document | `F:\...\01_writing\current\thesis_v31.docx` |
| Final PDF | `F:\...\09_deliverables\final_pdfs\final_as_thesis.pdf` |
| Icon source image | `C:\Users\singh\OneDrive\WEBSITE_2026\Gemini_Generated_Image_oaq2bcoaq2bcoaq2 (1).png` |

## Commands

```bash
# Set up Node path (required every terminal session)
export PATH="/c/Program Files/nodejs:$PATH"

# Development
npm run dev          # Start dev server (hot reload)
npm run build        # Build for production
npm run preview      # Preview production build

# Git
git push origin main # Push to GitHub (triggers auto-deploy)
```
