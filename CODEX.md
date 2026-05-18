# Codex Guide — Rebuilding Lahaina Thesis Website

This document provides context for any AI agent (Codex, Claude, etc.) working on this codebase.

> **For content-only work** (anything under `src/content/`), also load
> `.claude/skills/thesis-content-audit/SKILL.md`. It encodes the rules below
> plus the validated audit scripts (`scripts/audit_xrefs.py`,
> `scripts/audit_sources.py`) and known-good baselines.

## What This Is

An academic thesis website for "Rebuilding Post Disasters: Lahaina" (M.Arch, Tulane, 2025) by Akhil Singh. It is a public resource for Lahaina residents, planners, researchers, and architects. Every word of content is sourced from the thesis document or the author's verified research files.

## Critical Rules

### Content Integrity
- **Section bodies originate from `Thesis_V31.docx` and include documented post-V31 author additions.** Canonical source: `/Users/akhil/Library/CloudStorage/OneDrive-Personal/THESIS/CURRENT WRITING/Thesis_V31.docx`. The website's `thesis_source.txt` is a working extract that has been extended by the author with ~2,000 words across sections 2A, 3B, 3C, 3D (glossary expansions, table entries, and 4 substantive paragraphs of new analysis). All post-V31 drift was audited on 2026-05-17 and recorded at `docs/drift-audit/2026-05-17-v31-vs-website-drift.md`. Do not paraphrase or "improve" existing prose — but new authorial additions are welcome and must be tracked in the next drift audit. Re-run `python3 scripts/drift_audit.py` after substantive content changes to keep the audit current.
- **No fabrication.** Do not add facts, citations, statistics, precedents, or claims that are not in the thesis or the author's research files at `F:\ACADEMIC\masters_of_architecture\thesis_rebuilding_lahaina\`.
- **No em dashes (—) in content.** The author does not use them. Use commas, periods, or semicolons instead.
- **"structures" not "homes"** — the thesis says "2,200 structures" not "2,200 homes."
- **Hawaiian diacriticals matter.** Preserve ʻokina (ʻ) and kahakō (ā, ē, ī, ō, ū) in all Hawaiian words: Mokuʻula, Nāhiʻenaʻena, ahupuaʻa, Kāʻanapali, Hawaiʻi, etc.
- **First-person voice is intentional, not editorial drift.** The thesis is partly written in first-person — especially the methodology, scale-by-scale diagnostic, key-terms intro, buffer framework, and the dedication/acknowledgements. Do NOT rewrite "I compiled / I conducted / I assembled / I tested / I selected / I went to Hawaiʻi" passages or the "we expect / we can imagine" rhetorical we. All 20 such instances across 8 section files were verified verbatim against `thesis_source.txt` on 2026-05-16. The site's third-person framing wraps thesis voice intentionally; preserve the contrast.

### Source Linking
- Every data source, agency, or referenced work should link to its public URL where available.
- Key sources: FEMA (fema.gov/disaster/4724), CWRM (dlnr.hawaii.gov/cwrm), Hawaii GIS (geoportal.hawaii.gov), Rainfall Atlas (rainfall.geography.hawaii.edu), NPS Lahaina (nps.gov/places/lahaina-historic-district.htm), Friends of Mokuʻula (friendsofmokuula.org), Maui Recovers (mauirecovers.org).

### Code Quality
- Do not introduce new dependencies without justification.
- Match existing naming conventions and file structure.
- Do not add comments, docstrings, or type annotations to code you didn't change.
- Do not bypass linting, type checks, or build verification.

## Stack

- **Framework:** Astro 5.x (static output)
- **Styling:** Tailwind CSS 3.x + @tailwindcss/typography
- **Search:** Pagefind (postbuild indexing)
- **Maps:** Leaflet + GeoJSON (16 layers from Hawaii State GIS)
- **Fonts:** Inter (sans) + EB Garamond (serif), self-hosted woff2, preloaded
- **Hosting:** GitHub Pages + Cloudflare (orange cloud proxy, Access for private preview)
- **Domain:** rebuildinglahaina.org (Cloudflare Registrar)
- **News:** Static JSON via GitHub Action cron (every 6 hours)
- **TypeScript:** Strict mode

## Key File Locations

| What | Where |
|------|-------|
| Content collections | `src/content/` (sections, drawings, sources, terms, timeline, maps, topics, scales) |
| Layouts | `src/layouts/` (BaseLayout, SectionLayout, DrawingLayout) |
| Components | `src/components/` (Nav, Footer, MapViewer, DrawingViewer, TopicIcon, TagPills, etc.) |
| GIS data | `public/data/geojson/` (16 GeoJSON files) |
| Images | `public/images/drawings/` (complete_ppt/, reference/, updated_*) |
| Topic icons | `public/icons/topics/` (11 PNGs, pending SVG replacement) |
| News data | `public/data/news.json` (auto-updated by GitHub Action) |
| Thesis source text | `thesis_source.txt` (extracted from thesis_v31.docx) |
| Design specs | `docs/superpowers/specs/` |
| Session logs | `docs/logs/` |

## Content Collections (Zod schemas in src/content.config.ts)

| Collection | Count | Key Fields |
|---|---|---|
| sections | 29 | title, chapter, order, summary, relatedDrawings, relatedSources, relatedTerms, tags |
| drawings | 65 | title, image, alt, scaleLevel, drawingType, relatedSections, tags |
| sources | 48 | title, author, sourceType, relevance, tags |
| terms | 21 | term, definition, category, relatedSections, tags |
| timeline | 9 | date, era, title, description, sortOrder, relatedSections, tags |
| topics | 11 | title, summary |
| scales | 5 | title, summary |
| maps | 1 | title, description, layers, defaultCenter, defaultZoom, relatedSections, relatedDrawings, tags |

## Tag System

Topics: water, fire, coastal, cultural-heritage, ecology, housing, infrastructure, mobility, policy, recovery, zoning
Scales: regional, town, district, node, site
Types: analysis, proposal, documentation, precedent

## Build & Deploy

```bash
export PATH="/c/Program Files/nodejs:$PATH"  # Required on Windows
npm run build          # astro check + astro build + pagefind
npm run dev            # Local dev server
git push origin main   # Triggers GitHub Pages deploy via .github/workflows/deploy.yml
```

## Known Issues / TODO

- [ ] Section mini-maps need alignment verification (some layers extend beyond Lahaina study area)
- [ ] Topic icons are raster PNGs — need replacement with proper SVGs
- [ ] Hybrid hale architectural spec (from supplementary_docs/) not yet integrated into module-system page
- [ ] Thesis PDF (204MB) needs external hosting solution
- [ ] Cloudflare Rocket Loader must stay OFF (breaks Pagefind search)

## GIS Data

All GeoJSON from Hawaii State GIS REST services (geodata.hawaii.gov), clipped to Lahaina study area bbox: lat 20.84-20.95, lon -156.70 to -156.58. Regional polygon layers (aquifers, watersheds, hydro_units) are only on the full Map Explorer page, not embedded section maps, because they are too coarse for town-scale zoom.

## Author Context

Akhil Singh — M.Arch graduate, Tulane School of Architecture, 2025. Works across architecture, photography, and design. The thesis proposes a multi-scalar recovery framework for Lahaina after the 2023 wildfire, organized around water-sensitive infrastructure, reconfigured mobility, and community hubs. The site is meant to be a lasting public resource, not just a portfolio piece.
