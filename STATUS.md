# Rebuilding Lahaina — Thesis Website Status

**Last updated:** 2026-03-20
**Repo:** https://github.com/plumice/rebuilding-lahaina
**Stack:** Astro 5.x, Tailwind CSS 3.x, Pagefind, Leaflet, Netlify (not yet deployed)

---

## What's Built

### Site Architecture
- Astro 5.x static site with 8 content collections (Zod schemas)
- Three navigation modes: Narrative (read chapter-by-chapter), Topic (browse by theme), Scale (zoom in/out)
- Pagefind full-text search with dark theme styling
- Leaflet interactive map viewer (awaiting GIS data)
- Live news bulletin via Netlify serverless function (works after deploy)
- Mobile hamburger menu with focus trap and escape key
- WCAG AA accessible (focus indicators, contrast, touch targets, skip nav, ARIA)
- Print styles, OG/Twitter meta tags, sitemap, 404 page

### Content Totals

| Collection | Count | Status |
|-----------|-------|--------|
| Sections (thesis text) | 17 | Complete — all with endnotes/citations |
| Drawings | 53 | Complete — using COMPLETE PPTX + latest working files |
| Sources (bibliography) | 48 | Complete — full thesis bibliography |
| Terms (glossary) | 18 | Complete — concepts, Hawaiian terms, acronyms |
| Timeline events | 9 | Complete — pre-contact through 2026 |
| Topics | 11 | Complete — all with intro text |
| Scales | 5 | Complete — regional through node |
| Maps (interactive) | 1 | Placeholder — awaiting GIS data |

### Images
- 69 slides from Final COMPLETE presentation (`complete_ppt/`)
- 28 updated map images from latest working files (`updated_*`)
- 6 site photographs from Lahaina burn documentation
- Old/orphaned images cleaned up (removed ~250 files)

### Design
- Light theme: white background, warm surfaces (#f7f7f5), muted brown accent (#6d5344)
- Typography: EB Garamond (serif, headings/prose) + Inter (sans, UI) — self-hosted
- User-friendly language throughout — designed for general Hawaiian audience, not academics

---

## What's Remaining

### Priority 1: Deploy
- [ ] Connect GitHub repo to Netlify (2-click process from netlify.app dashboard)
- [ ] News bulletin will start working after deploy
- [ ] Site gets a public URL (rebuilding-lahaina.netlify.app or custom domain)

### Priority 2: Thesis PDF
- [ ] The 204MB PDF is too large for GitHub (100MB limit)
- [ ] Options: Netlify Large Media, Google Drive link, or Dropbox link
- [ ] File exists locally at `public/downloads/final_as_thesis.pdf` (gitignored)
- [ ] Footer "Download Full Thesis" link needs a working URL after hosting decision

### Priority 3: GIS Interactive Maps
- [ ] Export GeoJSON layers from ArcGIS Pro OR publish to ArcGIS Online and embed
- [ ] **ArcGIS Online (recommended):** Share → Share as Web Map → paste URL → I embed it
- [ ] **Alternative:** Export layout as 300 DPI PNG → add as zoomable drawing
- [ ] **Manual route:** Export individual GeoJSON layers to `public/data/geojson/`
- [ ] Current map entry (`water-systems-overlay`) has the Leaflet viewer ready but no data

### Priority 4: Polish
- [ ] Test all pages on actual mobile device
- [ ] Custom domain setup (if desired)
- [ ] Add more site photography from the 123 Lahaina burn photos on SSD
- [ ] Consider adding the thesis boards (from `09_deliverables/`) as downloadable content

---

## File Locations

### Website Project
- **Source code:** `C:\Users\singh\OneDrive\thesis-website\`
- **GitHub:** https://github.com/plumice/rebuilding-lahaina

### Thesis Archive (SSD)
- **Main archive:** `F:\ACADEMIC\masters_of_architecture\thesis_rebuilding_lahaina\`
- **Parsed content backup:** `F:\...\11_website\parsed_content\` (mirrors all website content)
- **Latest PPTX:** `C:\Users\singh\OneDrive\PPT\PRES\Lahaina_Thesis_Presentation_Final_COMPLETE.pptx` (364MB)
- **Latest map images:** `C:\Users\singh\OneDrive\PPT\NEWJPSS\` (individual exports)
- **Thesis document:** `F:\...\01_writing\current\thesis_v31.docx`
- **Final PDF:** `F:\...\09_deliverables\final_pdfs\final_as_thesis.pdf` (204MB)
- **GIS data:** `F:\...\06_gis\` (raster + shapefiles, needs ArcGIS Pro to export)

### Tools & Skills
- **UX Audit skill:** `C:\Users\singh\.claude\skills\ux-audit\SKILL.md` (installed, tested, 100% pass rate)
- **Node.js:** v22.14.0 at `C:\Program Files\nodejs\`
- **GitHub CLI:** v2.88.1, authenticated as `plumice`
- **Git config:** name="Akhil Singh", email="akhil@placeholder.com" (repo-level, needs real email)

---

## Key Decisions Made

1. **Astro 5.x** over Next.js — content-heavy static site, interactive islands only where needed
2. **Light theme** — user requested white/black, easy on eyes for Hawaiian audience
3. **Plain language** — all navigation and descriptions written for non-academic general public
4. **PPT as source of truth** — drawings use the Final COMPLETE presentation as the most current version
5. **Pagefind** over Algolia — build-time indexing, no external service, zero cost
6. **Netlify** — user already has account for portfolio site
7. **Google News RSS** for live news bulletin — no API key needed

---

## Session History

This site was designed, planned, and built in a single Claude Code session on 2026-03-20:

1. Brainstormed design with user → wrote spec document
2. Wrote 15-task implementation plan → reviewed and approved
3. Built all 15 tasks via subagent-driven development
4. Switched from dark to light theme per user request
5. Made site user-friendly for Hawaiian audience (plain language, mobile menu, etc.)
6. Added live news bulletin
7. Populated all content from thesis archive on SSD
8. Ran full UX audit (25 issues found, all critical/important fixed)
9. Created reusable UX audit skill (tested, 100% pass rate vs 82% baseline)
10. Completed bibliography (48 sources) with endnotes on every section
11. Updated all drawings to latest versions (COMPLETE PPTX + working files)
12. Cleaned up ~250 old orphaned images
13. Pushed to GitHub (plumice/rebuilding-lahaina)
