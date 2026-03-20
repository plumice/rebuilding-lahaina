# Rebuilding Lahaina — Thesis Website Design Spec

**Date:** 2026-03-20
**Author:** Akhil Singh
**Status:** Draft

---

## 1. Purpose & Audience

A public-facing resource site for the "Rebuilding Lahaina" thesis (M.Arch, Tulane School of Architecture, 2025). The site makes the full thesis content searchable, tagged, and navigable for four primary audiences:

- **Urban planners / policy makers** — seeking data, zoning analysis, buffer strategies, recovery frameworks
- **Researchers / academics** — seeking sources, methodology, GIS data, case study comparisons
- **Lahaina community members** — understanding what's proposed, the recovery vision
- **Architecture / design professionals** — examining design interventions, drawings, module system, precedents

The site is a structured knowledge base that also reads as a coherent narrative. Every piece of content is tagged and searchable.

---

## 2. Information Architecture

Three navigation modes pointing to the same underlying content:

### 2.1 Narrative Path (by thesis structure)
- Linear reading through five chapters, broken into digestible subsections
- Each subsection is its own page with previous/next navigation
- Full front-to-back reading experience

### 2.2 Topic Explorer (by system/theme)
- Entry points: Water, Mobility, Housing, Coastal, Cultural Heritage, Zoning, Fire, Recovery, Ecology, Infrastructure, Policy
- Each topic page aggregates all related content (text, drawings, maps, sources, terms) via tags
- Cross-links between related topics

### 2.3 Scale Navigator (by spatial scale)
- Regional > District > Town > Site > Node
- Each scale level shows relevant drawings, analysis, and proposals at that zoom level

### 2.4 Connecting Layer: Tags + Search
- Every content entry tagged with: topic(s), scale(s), content type, chapter
- Full-text search with tag filtering
- Tag pages show everything with that tag across all content types

---

## 3. Content Model

Six collections, each a set of markdown files with typed frontmatter. **Astro 5.x** content collections with Zod schemas.

**Slug convention:** All slugs are derived from the markdown filename (without extension). Use lowercase, hyphens only. Example: `pioneer-mill-water-infrastructure.md` → slug `pioneer-mill-water-infrastructure`. Cross-references between collections use these filename-derived slugs.

**Narrative ordering:** Sections are ordered by `chapter` (alphabetical sort on the enum value) then `order` (ascending integer, unique within each chapter). Previous/next navigation follows this sort.

### 3.1 Sections (~40-60 entries)
Thesis text broken into subsections. The markdown body contains the full web-adapted text with inline image references.

```yaml
---
title: "Pioneer Mill Water Infrastructure"
chapter: "ch3-analysis"       # enum, required
order: 5                       # integer, unique within chapter, required
summary: "One-line summary"    # required, used in cards and meta description
relatedDrawings: ["water-infrastructure-existing"]  # slugs from drawings collection
relatedSources: ["wsp-highway-survey"]              # slugs from sources collection
tags:
  topic: [water, infrastructure]   # enum array, at least one required
  scale: [district, town]          # enum array, at least one required
  type: [analysis]                 # enum array, at least one required
---

Body text here — web-adapted thesis content for this subsection.
```

### 3.2 Drawings (~30 entries)
Every plate/drawing from the drawing index. The markdown body contains extended description/analysis notes.

```yaml
---
title: "Composite Regional Analysis"          # required
image: "/images/drawings/composite-regional.jpg"  # required, path in public/
alt: "Combined systems map identifying developable edges and constraint zones across West Maui"  # required, meaningful alt text
scaleLevel: "regional"                        # enum: regional|district|town|site|node, required
drawingType: "composite-map"                  # free text (analytical-map, section, plan, diagram, rendering, etc.)
relatedSections: ["regional-analysis"]        # slugs from sections collection
tags:
  topic: [water, coastal, ecology]
  scale: [regional]
  type: [analysis]
---

Extended description or analysis notes for this drawing.
```

### 3.3 Sources (~50+ entries)
Books, reports, technical documents, research notes. Body text is optional (for extended annotations).

```yaml
---
title: "After Great Disasters"                # required
author: "Johnson, Laurie A. & Olshansky, Robert B."  # required
publisher: "Lincoln Institute of Land Policy"  # optional
date: "2017"                                   # optional (string, not date type — handles "1960s", "2023–2025")
sourceType: "book"                             # enum: book|report|government-doc|research-note, required
relevance: "Post-disaster urban planning; governance; building back better framework"  # required
tags:
  topic: [recovery, policy]                    # enum array, at least one required
  type: [precedent]                            # enum array, at least one required
---
```

### 3.4 Terms (~15+ entries)
Key terms, definitions, Hawaiian glossary, acronyms. Category distinguishes display grouping.

```yaml
---
term: "Ahupua'a"                              # required
definition: "Traditional Hawaiian land divisions extending from mountains to sea..."  # required
category: "hawaiian"                           # enum: concept|hawaiian|acronym, required
relatedSections: ["ahupuaa-system"]            # slugs from sections collection, optional
tags:
  topic: [cultural-heritage, water]            # enum array, at least one required
---
```

### 3.5 Maps (~5-8 entries)
Interactive GIS map configurations. Body text provides extended context shown in the description panel.

```yaml
---
title: "Water Systems Overlay"                 # required
description: "Pre-fire and proposed water infrastructure"  # required
layers:                                        # array, at least one required
  - name: "Existing Streams"
    file: "/data/geojson/streams.geojson"
    color: "#4488cc"
  - name: "Historic Ditches"
    file: "/data/geojson/ditches.geojson"
    color: "#c4a265"
defaultCenter: [20.8783, -156.6825]            # [lat, lng], required
defaultZoom: 14                                # integer, required
relatedSections: ["water-infrastructure"]      # slugs from sections collection, optional
relatedDrawings: ["proposed-water-system"]     # slugs from drawings collection, optional
tags:
  topic: [water, infrastructure]               # enum array, at least one required
  scale: [district, town]                      # enum array, at least one required
  type: [analysis]                             # enum array, at least one required
---

Extended context for the map description panel.
```

### 3.6 Timeline Events (~10 entries)
Historical events from pre-contact through projected future. Body text optional for extended detail.

```yaml
---
date: "2023-08"                                # string (handles "Pre-Contact", "~1860s", etc.), required
era: "August 2023"                             # display label, required
title: "Wildfire Devastation"                  # required
description: "Fire destroys ~2,200 homes, displaces 6,000-7,000 residents..."  # required
sortOrder: 7                                   # integer for chronological sort, required
relatedSections: ["wildfire-context"]          # slugs from sections collection, optional
tags:
  topic: [fire, recovery]                      # enum array, at least one required
---
```

### 3.7 Topic & Scale Page Content

Topic pages (e.g., "Water") and Scale pages (e.g., "Regional") need intro text. These live as markdown files in two additional content directories:

- `src/content/topics/water.md` — frontmatter has `title`, `summary`; body has the intro text
- `src/content/scales/regional.md` — same pattern

These are not full collections with complex schemas — just simple content files for page introductions.

### 3.8 Tag Taxonomy

Applied across all collections. Defined as Zod enums in `config.ts`:

- **Topic:** water, mobility, housing, coastal, cultural-heritage, zoning, fire, recovery, ecology, infrastructure, policy
- **Scale:** regional, district, town, site, node
- **Type:** analysis, proposal, precedent, data, documentation
- **Chapter:** ch1-introduction, ch2-overview, ch3-analysis, ch4-principles, ch5-design

The chapter taxonomy maps to the thesis structure as follows:
- **ch1-introduction** → Part One (Dedication, Abstract, Research Questions)
- **ch2-overview** → Part Two (Key Terms, Resilience Drivers, Community Anchors case studies)
- **ch3-analysis** → Part Three (History of Lahaina, Environmental Analysis, Zoning, Infrastructure & Water)
- **ch4-principles** → Part Four A–C (Multi-Scalar Diagnostic, Design Principles & Buffers, Systems)
- **ch5-design** → Part Four D–F (Redensification & Hubs, Design Interventions, Module System)

---

## 4. Page Structure

### 4.1 Global Elements (every page)
- Fixed nav bar: logo, search trigger, three navigation links (Read / Topics / Scales) — these are links to landing pages, not a mode toggle
- Tag breadcrumbs showing current location
- Footer: thesis info, full PDF download link (`/downloads/final_as_thesis.pdf` — stable URL), author contact
- Skip-to-content link and ARIA landmarks for accessibility
- Open Graph and Twitter Card meta tags per page (title, description, og:image)
- 404 page with search bar and navigation links

### 4.2 Homepage
- Hero with thesis title, abstract summary, and a striking drawing/render
- Three entry points: "Read the Thesis" / "Explore by Topic" / "Explore by Scale"
- Featured content cards (key drawings, interactive map preview)
- Prominent search bar

### 4.3 Section Page (individual thesis subsection)
- Body text with inline figures and drawing references
- Sidebar: related terms, sources, drawings
- Previous/next navigation within narrative
- Tag pills linking to topic and scale pages

### 4.4 Drawing Page (individual plate/drawing)
- Large zoomable image viewer (medium-zoom)
- Description, scale, drawing type
- Related sections and sources below
- Tags

### 4.5 Topic Page (e.g., "Water")
- Introduction/summary for that topic
- Aggregated grid: relevant sections, drawings, maps, sources, terms
- Filterable by scale or content type within the topic

### 4.6 Scale Page (e.g., "Regional")
- Overview of analysis at this scale
- All drawings, sections, and maps at this zoom level

### 4.7 Map Page (interactive GIS)
- Full-width Leaflet map with toggleable layers
- Layer legend and description panel
- Links to related sections and drawings

### 4.8 Search Results Page
- Full-text results grouped by collection type
- Tag filters in sidebar to narrow results

---

## 5. Visual Design

Carries forward the existing dark theme from the current `index.html`:

- **Background:** `#0a0a0a` (--bg), `#141414` (--surface)
- **Accent:** `#c4a265` (gold)
- **Text:** `#e8e8e8` (primary), `#999` (muted — raised from `#888` for WCAG AA compliance at small sizes)
- **Borders:** `#222`
- **Typography:** EB Garamond (serif, headings/body prose) + Inter (sans, UI/labels/nav). Self-hosted with `font-display: swap` to avoid FOIT.
- **Minimum text size:** 0.8rem (no text smaller than this for accessibility)
- **Content pages:** generous whitespace, clear typographic hierarchy for long-form reading
- **Drawings/images:** dark card frames, plate-like presentation
- **Responsive:** mobile-first, adapts from single column (mobile) to sidebar layout (desktop)

---

## 6. Tech Stack

| Layer | Choice | Version | Rationale |
|-------|--------|---------|-----------|
| Framework | Astro | 5.x | Content collections with typed Zod schemas, static output, interactive islands |
| Content | Markdown/MDX | — | One file per entry, frontmatter holds all metadata and tags |
| Styling | Tailwind CSS | 4.x | Utility-first, maps to design tokens, fast iteration |
| Search | Pagefind | latest | Build-time indexing, zero external dependencies, fast client-side search |
| GIS Maps | Leaflet | 1.9.x | Open source, lightweight, works with GeoJSON converted from shapefiles |
| Image Zoom | medium-zoom | latest | Hover/click zoom on drawings and figures |
| Image Optimization | Astro `<Image />` | built-in | Automatic WebP conversion, responsive srcsets, lazy loading |
| Sitemap | @astrojs/sitemap | latest | Auto-generated sitemap.xml for SEO |
| Deploy | Netlify | — | Existing account, static hosting, auto-deploy from git |
| Repo | Git (GitHub) | — | Version control, triggers Netlify builds on push |

### 6.1 Search Implementation Notes
Pagefind requires `data-pagefind-filter` attributes on rendered HTML for tag filtering. Every page template must emit filter attributes for topic, scale, type, and chapter tags. This enables the "full-text search with tag filtering" described in Section 2.4.

### 6.2 Image Optimization Strategy
- Thesis drawings and figures are processed through Astro's built-in `<Image />` component
- Source images stored in `src/assets/images/` (not `public/`) so Astro can optimize them
- Output format: WebP with JPEG fallback
- Maximum width: 2400px for drawings, 1200px for inline figures
- Lazy loading on all images below the fold
- GIS map static fallback images kept small (< 200KB each)

### 6.3 GIS Data Pipeline
- Convert shapefiles to GeoJSON using mapshaper with simplification
- Target: each GeoJSON file under 1MB (simplify vertex density as needed)
- GeoJSON files served from `public/data/geojson/`
- Leaflet loads layers on demand (not all at once)

---

## 7. Project Structure

```
thesis-website/
├── astro.config.mjs
├── tailwind.config.mjs
├── package.json
├── netlify.toml
├── public/
│   ├── images/
│   │   └── maps/              # static map fallback images
│   ├── data/
│   │   └── geojson/           # converted shapefiles for Leaflet
│   └── downloads/
│       └── final_as_thesis.pdf
├── src/
│   ├── assets/
│   │   └── images/
│   │       ├── drawings/      # thesis figures (processed by Astro <Image />)
│   │       ├── renders/       # key renders
│   │       └── photography/   # site photos
│   ├── content/
│   │   ├── config.ts          # collection schemas + tag taxonomy (Zod)
│   │   ├── sections/          # ~40-60 markdown files
│   │   ├── drawings/          # ~30 markdown files
│   │   ├── sources/           # ~50+ markdown files
│   │   ├── terms/             # ~15+ markdown files
│   │   ├── maps/              # ~5-8 markdown files
│   │   ├── timeline/          # ~10 markdown files
│   │   ├── topics/            # ~11 markdown files (topic page intros)
│   │   └── scales/            # ~5 markdown files (scale page intros)
│   ├── layouts/
│   │   ├── BaseLayout.astro   # global nav, footer, meta tags
│   │   ├── SectionLayout.astro
│   │   └── DrawingLayout.astro
│   ├── pages/
│   │   ├── index.astro        # homepage
│   │   ├── read/[...slug].astro    # narrative path
│   │   ├── topic/[tag].astro       # topic explorer
│   │   ├── scale/[level].astro     # scale navigator
│   │   ├── drawing/[...slug].astro
│   │   ├── source/[...slug].astro
│   │   ├── term/[...slug].astro
│   │   ├── map/[...slug].astro
│   │   ├── timeline.astro
│   │   ├── search.astro
│   │   └── 404.astro          # custom 404 with search + nav
│   ├── components/
│   │   ├── Nav.astro
│   │   ├── SearchBar.astro
│   │   ├── TagPills.astro
│   │   ├── ContentCard.astro
│   │   ├── DrawingViewer.astro
│   │   ├── MapViewer.astro    # Leaflet island (client:load)
│   │   ├── ScaleNav.astro
│   │   ├── Sidebar.astro
│   │   └── Timeline.astro
│   └── styles/
│       └── global.css         # design tokens from current theme
```

---

## 8. Content Pipeline

### 8.1 Source Material Locations
- **Thesis text:** `/f/ACADEMIC/masters_of_architecture/thesis_rebuilding_lahaina/01_writing/current/thesis_v31.docx`
- **Figures:** `/f/.../02_figures/thesis_figures/jpgs/`
- **SVGs:** `/f/.../02_figures/svgs/`
- **Renders:** `/f/.../03_renders/`
- **Site photography:** `/f/.../05_photography/site_photography/lahaina_burn/`
- **GIS data:** `/f/.../06_gis/` (shapefiles to convert to GeoJSON)
- **Final PDF:** `/f/.../09_deliverables/final_pdfs/final_as_thesis.pdf`
- **Research data:** `/f/.../10_data_research/`

### 8.2 Content Creation Workflow
1. Extract thesis text from v31.docx, split into markdown subsections
2. Export/copy figures to `public/images/drawings/`
3. Write frontmatter for each drawing, source, term, timeline entry
4. Convert relevant shapefiles to GeoJSON for map pages
5. Tag everything according to the taxonomy
6. Build and verify search index picks up all content

---

## 9. Future Growth

The content model is extensible:
- New collections can be added (e.g., interviews, community feedback, updates)
- New tags can be added to the taxonomy without restructuring
- Additional GIS layers can be added as new GeoJSON files
- The site can grow as the project evolves beyond the thesis
