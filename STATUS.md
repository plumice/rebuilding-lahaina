# Rebuilding Lahaina — Thesis Website Status

**Last updated:** 2026-04-02
**Repo:** https://github.com/plumice/rebuilding-lahaina
**Stack:** Astro 5.x, Tailwind CSS 3.x, Pagefind, Leaflet, Netlify
**Node:** v22.14.0 | `export PATH="/c/Program Files/nodejs:$PATH"` before npm commands

---

## Project Stats

| Metric | Count |
|--------|-------|
| Total pages | 185+ |
| Content files | 184 |
| Sections (thesis text) | 29 |
| Drawings | 60 |
| Sources (bibliography) | 48 |
| Terms (glossary) | 21 |
| Timeline events | 9 |
| Topics | 11 |
| Scales | 5 |
| Maps (interactive) | 1 |
| Image files | 31 (updated + complete_ppt/) |
| Searchable words | 2,554 |
| Git commits | 52 |

---

## Project Structure

```
thesis-website/
├── astro.config.mjs          # Astro config (static, Tailwind, sitemap)
├── tailwind.config.mjs        # Design tokens (light theme)
├── package.json               # Dependencies + postbuild (Pagefind)
├── netlify.toml               # Deploy config + serverless functions
├── tsconfig.json              # TypeScript strict
├── STATUS.md                  # This file
│
├── netlify/functions/
│   └── news.mts               # Live news feed serverless function
│
├── public/
│   ├── favicon.svg
│   ├── downloads/
│   │   └── final_as_thesis.pdf  # (gitignored, 204MB)
│   ├── data/geojson/            # GIS data (awaiting export)
│   └── images/drawings/
│       ├── complete_ppt/        # 69 slides from COMPLETE PPTX
│       ├── updated_*.jpg        # Latest map images from working files
│       ├── prefire_aerial_satellite.jpg
│       └── postfire_aerial_satellite.jpg
│
├── src/
│   ├── content.config.ts       # Zod schemas for all 8 collections
│   ├── content/
│   │   ├── sections/    (29)   # Thesis text with endnotes
│   │   ├── drawings/    (60)   # Drawing metadata + image refs
│   │   ├── sources/     (48)   # Complete bibliography
│   │   ├── terms/       (21)   # Glossary
│   │   ├── timeline/     (9)   # Historical events
│   │   ├── maps/         (1)   # Interactive map configs
│   │   ├── topics/      (11)   # Topic page intros
│   │   └── scales/       (5)   # Scale page intros
│   │
│   ├── layouts/
│   │   ├── BaseLayout.astro    # Global shell (nav, footer, meta)
│   │   ├── SectionLayout.astro # Thesis section pages
│   │   └── DrawingLayout.astro # Drawing detail pages
│   │
│   ├── pages/
│   │   ├── index.astro         # Homepage (hero + news + entry points)
│   │   ├── read/               # Narrative path (chapter-by-chapter)
│   │   ├── topic/              # Topic explorer
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
│   │   ├── Nav.astro           # Mobile hamburger + desktop nav
│   │   ├── Footer.astro        # Attribution + source/glossary links
│   │   ├── NewsBulletin.astro  # Live Maui news feed (card format)
│   │   ├── SearchBar.astro     # Search link
│   │   ├── TagPills.astro      # Tag display with Pagefind filters
│   │   ├── ContentCard.astro   # Reusable content card
│   │   ├── Breadcrumbs.astro   # Navigation breadcrumbs
│   │   ├── DrawingViewer.astro # Zoomable image (medium-zoom)
│   │   ├── MapViewer.astro     # Leaflet interactive map
│   │   ├── Sidebar.astro       # Related content sidebar
│   │   ├── PrevNext.astro      # Section navigation
│   │   ├── ScaleNav.astro      # Scale level selector
│   │   └── Timeline.astro      # Timeline visualization
│   │
│   └── styles/
│       ├── global.css          # Design tokens + base styles
│       └── fonts.css           # Self-hosted Inter + EB Garamond
│
└── docs/superpowers/
    ├── specs/                  # Design spec
    └── plans/                  # Implementation plan
```

---

## Content by Chapter

### Ch1: Introduction (3 sections)
- Dedication, Abstract, Research Questions & Hypotheses

### Ch2: Overview (4 sections)
- Key Terms, Resilience Drivers, Community Anchors, Literature & Methodology

### Ch3: Analysis (8 sections)
- History of Lahaina, Environmental Analysis, Zoning & Land Use, The Water Crisis, Pioneer Mill Water Infrastructure, Fire Analysis, Disaster Gentrification, Cultural Heritage Strategy

### Ch4: Principles (5 sections)
- Multi-Scalar Diagnostic, Buffer Framework, Water/Green/Mobility Systems, Street-by-Street Mobility, Water System Zones

### Ch5: Design (9 sections)
- Redensification & Hubs, Design Interventions, Module System, School Design Detail, Module Assembly Rules, District Typologies, Hub Operations, Results & Discussion, Contribution

---

## What's Done

- Full site scaffold (Astro 5.x + Tailwind + Pagefind + Leaflet)
- 29 thesis sections with endnotes/citations on every page
- 60 drawing entries — all verified against actual slide images
- 48 sources — complete thesis bibliography
- 21 terms, 9 timeline events, 11 topics, 5 scales
- Light theme, WCAG AA accessible, mobile-friendly
- Cover rendering as hero image
- News bulletin floating on homepage
- GitHub repo: plumice/rebuilding-lahaina
- UX audit skill created and installed
- All content archived to SSD at F:\...\11_website\parsed_content\

## What's Remaining

1. **Deploy to Netlify** — connect repo from netlify.app dashboard
2. **Thesis PDF hosting** — 204MB, needs Netlify Large Media or external link
3. ~~**GIS data**~~ — DONE: streams (70 features) + ditches (213 features) from Hawaii State GIS
4. **Mobile testing** — test on actual devices
5. **Custom domain** — optional

---

## Key File Locations

| What | Where |
|------|-------|
| Website source | `C:\Users\singh\OneDrive\thesis-website\` |
| GitHub | https://github.com/plumice/rebuilding-lahaina |
| Parsed content backup | `F:\...\thesis_rebuilding_lahaina\11_website\parsed_content\` |
| Latest PPTX | `C:\Users\singh\OneDrive\PPT\PRES\Lahaina_Thesis_Presentation_Final_COMPLETE.pptx` |
| Latest map images | `C:\Users\singh\OneDrive\PPT\NEWJPSS\` |
| Thesis document | `F:\...\01_writing\current\thesis_v31.docx` |
| Final PDF | `F:\...\09_deliverables\final_pdfs\final_as_thesis.pdf` |
| UX audit skill | `C:\Users\singh\.claude\skills\ux-audit\SKILL.md` |

## Commands

```bash
# Set up Node path (required every terminal session)
export PATH="/c/Program Files/nodejs:$PATH"

# Development
npm run dev          # Start dev server (hot reload)
npm run build        # Build for production
npm run preview      # Preview production build

# Git
git push origin main # Push to GitHub
```
