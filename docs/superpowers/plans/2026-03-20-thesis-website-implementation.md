# Rebuilding Lahaina — Thesis Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a public-facing Astro 5.x static site that presents the "Rebuilding Lahaina" thesis as a searchable, tagged knowledge base with three navigation modes (narrative, topic, scale), interactive GIS maps, and zoomable drawing viewers.

**Architecture:** Astro 5.x with content collections (Zod schemas) for six content types. Static HTML output with interactive Leaflet map islands and Pagefind search. Dark theme carried from existing prototype. Deployed to Netlify.

**Tech Stack:** Astro 5.x, Tailwind CSS 3.x (with @astrojs/tailwind integration), Pagefind, Leaflet 1.9.x, medium-zoom, @astrojs/sitemap

**Spec:** `docs/superpowers/specs/2026-03-20-thesis-website-design.md`

**Validation approach:** Astro's Zod schemas validate content at build time. Each task ends with a successful `npm run build` or `npm run dev` check. No separate test framework needed — schema violations and broken references cause build failures.

---

## File Map

### New files created by this plan:

**Config & project root:**
- `package.json` — dependencies and scripts
- `astro.config.mjs` — Astro configuration with Tailwind and sitemap integrations
- `tailwind.config.mjs` — Tailwind theme with design tokens
- `netlify.toml` — Netlify build config
- `tsconfig.json` — TypeScript config for Astro
- `.gitignore` — node_modules, dist, .astro

**Content schemas:**
- `src/content.config.ts` — Zod schemas for all 8 collections

**Styles:**
- `src/styles/global.css` — design tokens, base typography, Tailwind imports
- `src/styles/fonts.css` — self-hosted font declarations

**Layouts:**
- `src/layouts/BaseLayout.astro` — global shell (nav, footer, meta, OG tags, skip-to-content)
- `src/layouts/SectionLayout.astro` — narrative section pages with sidebar
- `src/layouts/DrawingLayout.astro` — drawing detail pages with zoom viewer

**Pages:**
- `src/pages/index.astro` — homepage
- `src/pages/read/index.astro` — narrative reading landing (chapter list)
- `src/pages/read/[...slug].astro` — individual section pages
- `src/pages/topic/index.astro` — topic explorer landing
- `src/pages/topic/[tag].astro` — individual topic pages
- `src/pages/scale/index.astro` — scale navigator landing
- `src/pages/scale/[level].astro` — individual scale pages
- `src/pages/drawing/index.astro` — drawing index landing
- `src/pages/drawing/[...slug].astro` — drawing detail pages
- `src/pages/source/index.astro` — source index landing
- `src/pages/source/[...slug].astro` — source detail pages
- `src/pages/term/index.astro` — term index landing
- `src/pages/term/[...slug].astro` — term detail pages
- `src/pages/map/index.astro` — map index landing
- `src/pages/map/[...slug].astro` — interactive map pages
- `src/pages/timeline.astro` — timeline page
- `src/pages/search.astro` — search results page
- `src/pages/404.astro` — custom 404

**Components:**
- `src/components/Nav.astro` — fixed navigation bar
- `src/components/Footer.astro` — site footer
- `src/components/SearchBar.astro` — Pagefind search trigger
- `src/components/TagPills.astro` — tag display component
- `src/components/ContentCard.astro` — reusable content card
- `src/components/DrawingViewer.astro` — zoomable image component
- `src/components/MapViewer.astro` — Leaflet interactive map island
- `src/components/Sidebar.astro` — related content sidebar
- `src/components/Timeline.astro` — timeline visualization
- `src/components/PrevNext.astro` — previous/next section navigation
- `src/components/Breadcrumbs.astro` — tag-based breadcrumbs

**Sample content (seed data for development — 1-2 entries per collection):**
- `src/content/sections/abstract.md`
- `src/content/sections/pioneer-mill-water-infrastructure.md`
- `src/content/drawings/composite-regional-analysis.md`
- `src/content/drawings/fire-footprint-before-after.md`
- `src/content/sources/after-great-disasters.md`
- `src/content/sources/wsp-highway-survey.md`
- `src/content/terms/ahupuaa.md`
- `src/content/terms/adaptive-recovery.md`
- `src/content/terms/fema-acronym.md`
- `src/content/maps/water-systems-overlay.md`
- `src/content/timeline/wildfire-devastation.md`
- `src/content/timeline/ahupuaa-system.md`
- `src/content/topics/water.md`
- `src/content/topics/fire.md`
- `src/content/scales/regional.md`
- `src/content/scales/town.md`

**Static assets:**
- `public/data/geojson/.gitkeep` — placeholder for GIS data
- `public/downloads/.gitkeep` — placeholder for PDF
- `public/images/maps/.gitkeep` — placeholder for map fallbacks
- `src/assets/images/drawings/.gitkeep` — placeholder for thesis figures
- `src/assets/images/renders/.gitkeep` — placeholder for renders
- `src/assets/images/photography/.gitkeep` — placeholder for photos

**Fonts:**
- `public/fonts/inter-*.woff2` — Inter font files (downloaded)
- `public/fonts/eb-garamond-*.woff2` — EB Garamond font files (downloaded)

### Existing files:
- `index.html` — current prototype (preserved as reference, not modified)
- `docs/superpowers/specs/2026-03-20-thesis-website-design.md` — design spec

---

## Task 1: Project Scaffolding

**Files:**
- Create: `package.json`, `astro.config.mjs`, `tailwind.config.mjs`, `tsconfig.json`, `.gitignore`, `netlify.toml`

- [ ] **Step 1: Initialize Astro project**

```bash
cd /c/Users/singh/OneDrive/thesis-website
npm create astro@latest . -- --template minimal --no-install --no-git --typescript strict
```

If prompted about overwriting, allow it (the existing `index.html` is in the root, Astro uses `src/`).

- [ ] **Step 2: Install dependencies**

```bash
npm install astro@latest @astrojs/tailwind @astrojs/sitemap tailwindcss@3 @tailwindcss/typography
npm install medium-zoom leaflet
npm install -D @types/leaflet autoprefixer
```

- [ ] **Step 3: Configure Astro**

Write `astro.config.mjs`:

```javascript
import { defineConfig } from 'astro/config';
import tailwindcss from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://rebuilding-lahaina.netlify.app',
  integrations: [tailwindcss(), sitemap()],
  output: 'static',
});
```

- [ ] **Step 4: Configure Tailwind with design tokens**

Write `tailwind.config.mjs`:

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        bg: '#0a0a0a',
        surface: '#141414',
        'surface-hover': '#1a1a1a',
        border: '#222222',
        text: '#e8e8e8',
        'text-muted': '#999999',
        accent: '#c4a265',
        'accent-dim': 'rgba(196,162,101,0.12)',
      },
      fontFamily: {
        serif: ['"EB Garamond"', 'Georgia', 'serif'],
        sans: ['Inter', '-apple-system', 'sans-serif'],
      },
      fontSize: {
        'min': '0.8rem',
      },
    },
  },
  plugins: [require('@tailwindcss/typography')],
};
```

- [ ] **Step 5: Write Netlify config**

Write `netlify.toml`:

```toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/404.html"
  status = 404
```

- [ ] **Step 6: Update .gitignore**

Ensure `.gitignore` includes:

```
node_modules/
dist/
.astro/
.env
```

- [ ] **Step 7: Create asset placeholder directories**

```bash
mkdir -p src/assets/images/drawings src/assets/images/renders src/assets/images/photography
mkdir -p public/data/geojson public/downloads public/images/maps public/fonts
touch src/assets/images/drawings/.gitkeep src/assets/images/renders/.gitkeep src/assets/images/photography/.gitkeep
touch public/data/geojson/.gitkeep public/downloads/.gitkeep public/images/maps/.gitkeep
```

- [ ] **Step 8: Verify build**

```bash
npm run build
```

Expected: Build succeeds with empty Astro project.

- [ ] **Step 9: Commit**

```bash
git add -A
git commit -m "feat: scaffold Astro 5.x project with Tailwind and Netlify config"
```

---

## Task 2: Content Collection Schemas

**Files:**
- Create: `src/content.config.ts`

- [ ] **Step 1: Write content collection schemas**

Write `src/content.config.ts`:

```typescript
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const topicEnum = z.enum([
  'water', 'mobility', 'housing', 'coastal', 'cultural-heritage',
  'zoning', 'fire', 'recovery', 'ecology', 'infrastructure', 'policy',
]);

const scaleEnum = z.enum([
  'regional', 'district', 'town', 'site', 'node',
]);

const typeEnum = z.enum([
  'analysis', 'proposal', 'precedent', 'data', 'documentation',
]);

const chapterEnum = z.enum([
  'ch1-introduction', 'ch2-overview', 'ch3-analysis',
  'ch4-principles', 'ch5-design',
]);

const tagsSchema = z.object({
  topic: z.array(topicEnum).min(1),
  scale: z.array(scaleEnum).min(1).optional(),
  type: z.array(typeEnum).min(1).optional(),
});

const sections = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/sections' }),
  schema: z.object({
    title: z.string(),
    chapter: chapterEnum,
    order: z.number().int(),
    summary: z.string(),
    relatedDrawings: z.array(z.string()).default([]),
    relatedSources: z.array(z.string()).default([]),
    relatedTerms: z.array(z.string()).default([]),
    tags: tagsSchema.extend({
      scale: z.array(scaleEnum).min(1),
      type: z.array(typeEnum).min(1),
    }),
  }),
});

const drawings = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/drawings' }),
  schema: z.object({
    title: z.string(),
    image: z.string(),
    alt: z.string(),
    scaleLevel: scaleEnum,
    drawingType: z.string(),
    relatedSections: z.array(z.string()).default([]),
    tags: tagsSchema.extend({
      scale: z.array(scaleEnum).min(1),
      type: z.array(typeEnum).min(1),
    }),
  }),
});

const sources = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/sources' }),
  schema: z.object({
    title: z.string(),
    author: z.string(),
    publisher: z.string().optional(),
    date: z.string().optional(),
    sourceType: z.enum(['book', 'report', 'government-doc', 'research-note']),
    relevance: z.string(),
    tags: tagsSchema.extend({
      type: z.array(typeEnum).min(1),
    }),
  }),
});

const terms = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/terms' }),
  schema: z.object({
    term: z.string(),
    definition: z.string(),
    category: z.enum(['concept', 'hawaiian', 'acronym']),
    relatedSections: z.array(z.string()).default([]),
    tags: tagsSchema,
  }),
});

const maps = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/maps' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    layers: z.array(z.object({
      name: z.string(),
      file: z.string(),
      color: z.string(),
    })).min(1),
    defaultCenter: z.tuple([z.number(), z.number()]),
    defaultZoom: z.number().int(),
    relatedSections: z.array(z.string()).default([]),
    relatedDrawings: z.array(z.string()).default([]),
    tags: tagsSchema.extend({
      scale: z.array(scaleEnum).min(1),
      type: z.array(typeEnum).min(1),
    }),
  }),
});

const timeline = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/timeline' }),
  schema: z.object({
    date: z.string(),
    era: z.string(),
    title: z.string(),
    description: z.string(),
    sortOrder: z.number().int(),
    relatedSections: z.array(z.string()).default([]),
    tags: tagsSchema,
  }),
});

const topics = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/topics' }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
  }),
});

const scales = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/scales' }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
  }),
});

export const collections = {
  sections,
  drawings,
  sources,
  terms,
  maps,
  timeline,
  topics,
  scales,
};
```

- [ ] **Step 2: Create content directories**

```bash
mkdir -p src/content/sections src/content/drawings src/content/sources
mkdir -p src/content/terms src/content/maps src/content/timeline
mkdir -p src/content/topics src/content/scales
```

- [ ] **Step 3: Verify build with empty collections**

```bash
npm run build
```

Expected: Build succeeds. Collections are defined but empty (Astro allows empty collections).

- [ ] **Step 4: Commit**

```bash
git add src/content.config.ts
git commit -m "feat: add Zod content collection schemas for all 8 collections"
```

---

## Task 3: Seed Content

Create 1-2 entries per collection so all subsequent page development has real data to render.

**Files:**
- Create: all files listed under "Sample content" in the file map

- [ ] **Step 1: Create seed sections**

Write `src/content/sections/abstract.md`:

```markdown
---
title: "Abstract"
chapter: "ch1-introduction"
order: 1
summary: "Thesis scope, methods, and broader implications for disaster-resilient urbanism."
relatedDrawings: []
relatedSources: []
relatedTerms: ["ahupuaa", "adaptive-recovery"]
tags:
  topic: [recovery, infrastructure]
  scale: [regional, town]
  type: [documentation]
---

The 2023 wildfire in Lahaina revealed critical vulnerabilities in infrastructure, water management, and disaster preparedness. Lack of water to control the fires, poor accessibility to certain areas of the city and other dysfunctionalities ended in one of the most catastrophic events in Hawaiian history.

Currently there is no clear route map for the rebuilding of the city nor its adaptation to climate events and their increasing frequency and violence. This thesis proposes recovery through a multi-scale plan that includes the major urban systems, the relation of the urban fabric with the coast and the hinterland, and a sequence of strategic nodes to serve the communities. It integrates water systems, slow mobility, and human-centered infrastructure to create a resilient and adaptive framework for Lahaina's long-term redevelopment.

By holistically targeting these systemic weaknesses through scalable site-specific interventions, the model challenges conventional fragmented disaster recovery paradigms and sets a new footprint for urban resilience, adaptation and post-disaster recovery.
```

Write `src/content/sections/pioneer-mill-water-infrastructure.md`:

```markdown
---
title: "Pioneer Mill Water Infrastructure"
chapter: "ch3-analysis"
order: 5
summary: "Historic ditch systems, aquifer designation, and the water crisis blocking Lahaina's recovery."
relatedDrawings: ["composite-regional-analysis"]
relatedSources: ["wsp-highway-survey"]
relatedTerms: []
tags:
  topic: [water, infrastructure]
  scale: [district, town]
  type: [analysis]
---

The Pioneer Mill Company developed an expansive network of ditches, reservoirs, and pipes across West Maui beginning around 1901. By 1935, electric pumps were irrigating over 10,000 acres of sugarcane. This water infrastructure — originally built for plantation agriculture — became the backbone of Lahaina's municipal water supply after the mill closed.

In June 2022, the Commission on Water Resource Management (CWRM) designated the entire Lahaina Aquifer Sector as a Surface and Ground Water Management Area, imposing state-level regulatory control over all water withdrawals. This designation reflected the severity of the water deficit: demand exceeds reliable capacity by 41.8%.

The Stage 2 Water Shortage Declaration of September 2025 means new water meters cannot be processed, directly blocking reconstruction of the 2,200 homes destroyed in the fire. Even with the projected Kahana Well coming online in 2026, the deficit would only reduce to approximately 15.7% — still insufficient for full recovery demand.
```

- [ ] **Step 2: Create seed drawings**

Write `src/content/drawings/composite-regional-analysis.md`:

```markdown
---
title: "Composite Regional Analysis"
image: "/images/drawings/placeholder.jpg"
alt: "Combined systems map identifying developable edges and constraint zones across West Maui"
scaleLevel: "regional"
drawingType: "composite-map"
relatedSections: ["pioneer-mill-water-infrastructure"]
tags:
  topic: [water, coastal, ecology]
  scale: [regional]
  type: [analysis]
---

Combined systems identifying developable edges and constraint zones. Overlays rainfall, streams, sea level rise projections, and topographic data to define where development is feasible and where natural systems must be preserved.
```

Write `src/content/drawings/fire-footprint-before-after.md`:

```markdown
---
title: "Fire Footprint: Before & After"
image: "/images/drawings/placeholder.jpg"
alt: "Pre-fire urban fabric compared to post-fire footprint with 1-foot contour intervals"
scaleLevel: "town"
drawingType: "figure-ground"
relatedSections: ["abstract"]
tags:
  topic: [fire, recovery]
  scale: [town]
  type: [analysis]
---

Pre-fire urban fabric vs. post-fire footprint with 1-foot contour intervals. This figure-ground study reveals the extent of destruction and the topographic conditions that influenced fire spread.
```

- [ ] **Step 3: Create seed sources**

Write `src/content/sources/after-great-disasters.md`:

```markdown
---
title: "After Great Disasters: An In-Depth Analysis of How Six Communities Managed Recovery"
author: "Johnson, Laurie A. & Olshansky, Robert B."
publisher: "Lincoln Institute of Land Policy"
date: "2017"
sourceType: "book"
relevance: "Post-disaster urban planning; governance; building back better framework"
tags:
  topic: [recovery, policy]
  type: [precedent]
---
```

Write `src/content/sources/wsp-highway-survey.md`:

```markdown
---
title: "Reconnaissance Level Architectural Historic Resource Survey, Honoapi'ilani Highway"
author: "WSP USA Inc."
publisher: "State of Hawai'i DOT"
date: "Oct 2024"
sourceType: "report"
relevance: "40 architectural resources; 11 water structures; Olowalu Sugar Plantation Historic District"
tags:
  topic: [infrastructure, cultural-heritage]
  type: [data]
---
```

- [ ] **Step 4: Create seed terms**

Write `src/content/terms/ahupuaa.md`:

```markdown
---
term: "Ahupua'a"
definition: "Traditional Hawaiian land divisions extending from mountains to sea, integrating natural water systems for agriculture and community sustenance."
category: "hawaiian"
relatedSections: ["abstract"]
tags:
  topic: [cultural-heritage, water]
---
```

Write `src/content/terms/adaptive-recovery.md`:

```markdown
---
term: "Adaptive Recovery"
definition: "Framework for rebuilding that incorporates flexibility and resilience to adapt to future climate, social, and economic changes."
category: "concept"
relatedSections: ["abstract"]
tags:
  topic: [recovery]
---
```

Write `src/content/terms/fema-acronym.md`:

```markdown
---
term: "FEMA"
definition: "Federal Emergency Management Agency"
category: "acronym"
relatedSections: []
tags:
  topic: [recovery, policy]
---
```

- [ ] **Step 5: Create seed map, timeline, topic, and scale entries**

Write `src/content/maps/water-systems-overlay.md`:

```markdown
---
title: "Water Systems Overlay"
description: "Pre-fire and proposed water infrastructure across Lahaina"
layers:
  - name: "Existing Streams"
    file: "/data/geojson/streams.geojson"
    color: "#4488cc"
  - name: "Historic Ditches"
    file: "/data/geojson/ditches.geojson"
    color: "#c4a265"
defaultCenter: [20.8783, -156.6825]
defaultZoom: 14
relatedSections: ["pioneer-mill-water-infrastructure"]
relatedDrawings: ["composite-regional-analysis"]
tags:
  topic: [water, infrastructure]
  scale: [district, town]
  type: [analysis]
---

This map overlays the existing stream network with the historic plantation ditch system to reveal the degraded water infrastructure that contributed to Lahaina's vulnerability.
```

Write `src/content/timeline/ahupuaa-system.md`:

```markdown
---
date: "Pre-Contact"
era: "Pre-Contact"
title: "Ahupua'a System"
description: "Traditional Hawaiian land management from mountain to sea; integrated water systems for agriculture and community."
sortOrder: 1
relatedSections: ["abstract"]
tags:
  topic: [cultural-heritage, water]
---
```

Write `src/content/timeline/wildfire-devastation.md`:

```markdown
---
date: "2023-08"
era: "August 2023"
title: "Wildfire Devastation"
description: "Fire destroys ~2,200 homes, displaces 6,000-7,000 residents, eliminates historic sites and infrastructure."
sortOrder: 7
relatedSections: ["abstract"]
tags:
  topic: [fire, recovery]
---
```

Write `src/content/topics/water.md`:

```markdown
---
title: "Water"
summary: "Water systems, infrastructure, and management across Lahaina — from historic plantation ditches to proposed capture and distribution networks."
---

Water is the central thread of the Lahaina thesis. The 2023 wildfire was worsened by a lack of water to fight the fire, and the ongoing Stage 2 Water Shortage blocks reconstruction. This topic covers the historic ditch systems, aquifer conditions, proposed water capture strategies, and the regulatory framework governing water use in West Maui.
```

Write `src/content/topics/fire.md`:

```markdown
---
title: "Fire"
summary: "The August 2023 wildfire, its causes, impacts, and the post-disaster recovery framework."
---

The August 2023 Lahaina wildfire was one of the most catastrophic events in Hawaiian history, destroying approximately 2,200 homes and displacing 6,000-7,000 residents. This topic covers the fire event, its root causes in infrastructure and land management failures, and the recovery strategies proposed by the thesis.
```

Write `src/content/scales/regional.md`:

```markdown
---
title: "Regional"
summary: "Coast-to-peak analysis of West Maui — topography, rainfall, streams, sea level rise, and composite constraint mapping."
---

The regional scale examines West Maui from the coast to the peak of the mountain, analyzing the natural systems that flow mauka (mountain) to makai (sea). At this scale, the thesis maps rainfall patterns, stream networks, the historic ditch system, sea level rise projections, and topographic constraints to identify where development is feasible and where natural systems must be preserved.
```

Write `src/content/scales/town.md`:

```markdown
---
title: "Town"
summary: "Lahaina town-level analysis — zoning, land use, fire footprint, density, and the proposed buffer system."
---

At the town scale, the thesis analyzes Lahaina's zoning classifications, land ownership patterns, pre- and post-fire building footprints, and infrastructure networks. This is where the four-buffer system — coastal, riparian, peri-urban, and water collection — takes shape as a spatial framework for recovery.
```

- [ ] **Step 6: Create a placeholder drawing image**

Create a simple SVG placeholder that browsers can render. Use SVG instead of a broken JPEG:

```bash
cat > public/images/drawings/placeholder.svg << 'EOF'
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800" viewBox="0 0 1200 800">
  <rect fill="#141414" width="1200" height="800"/>
  <text fill="#555" font-family="sans-serif" font-size="24" x="600" y="400" text-anchor="middle">Drawing Placeholder</text>
</svg>
EOF
```

Then update the seed drawing entries to reference `placeholder.svg` instead of `placeholder.jpg`.

Note: Real images will be copied from the SSD in the content population phase.

- [ ] **Step 7: Verify build with seed content**

```bash
npm run build
```

Expected: Build succeeds. Zod schemas validate all seed content frontmatter.

- [ ] **Step 8: Commit**

```bash
git add src/content/ public/images/drawings/placeholder.jpg
git commit -m "feat: add seed content for all 8 collections"
```

---

## Task 4: Global Styles & Fonts

**Files:**
- Create: `src/styles/global.css`, `src/styles/fonts.css`

- [ ] **Step 1: Download and set up self-hosted fonts**

Download variable WOFF2 files from Google Fonts. These URLs extract the raw font files:

```bash
cd /c/Users/singh/OneDrive/thesis-website
curl -L -o public/fonts/inter-variable.woff2 "https://fonts.gstatic.com/s/inter/v18/UcCo3FwrK3iLTcviYwY.woff2"
curl -L -o public/fonts/eb-garamond-variable.woff2 "https://fonts.gstatic.com/s/ebgaramond/v27/SlGDmQSNjdsmc35JDF1K5E55.woff2"
curl -L -o public/fonts/eb-garamond-variable-italic.woff2 "https://fonts.gstatic.com/s/ebgaramond/v27/SlGFmQSNjdsmc35JDF1K5GRwUjcdlA.woff2"
```

Note: If these direct URLs don't work (Google periodically changes them), use https://gwfh.mranftl.com/fonts (google-webfonts-helper) to download Inter (variable, latin) and EB Garamond (variable, latin) as WOFF2 and place in `public/fonts/`. As a fallback, the site will use system fonts (`font-display: swap`) until fonts are available.

Write `src/styles/fonts.css`:

```css
@font-face {
  font-family: 'Inter';
  src: url('/fonts/inter-variable.woff2') format('woff2');
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'EB Garamond';
  src: url('/fonts/eb-garamond-variable.woff2') format('woff2');
  font-weight: 400 800;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'EB Garamond';
  src: url('/fonts/eb-garamond-variable-italic.woff2') format('woff2');
  font-weight: 400 800;
  font-style: italic;
  font-display: swap;
}
```

- [ ] **Step 2: Write global styles**

Write `src/styles/global.css`:

```css
@import './fonts.css';

@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --bg: #0a0a0a;
    --surface: #141414;
    --surface-hover: #1a1a1a;
    --border: #222222;
    --text: #e8e8e8;
    --text-muted: #999999;
    --accent: #c4a265;
    --accent-dim: rgba(196, 162, 101, 0.12);
    --serif: 'EB Garamond', Georgia, serif;
    --sans: Inter, -apple-system, sans-serif;
  }

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  html {
    scroll-behavior: smooth;
  }

  body {
    font-family: var(--sans);
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    font-size: 1rem;
  }

  /* Skip to content link */
  .skip-to-content {
    position: absolute;
    left: -9999px;
    top: 0;
    z-index: 999;
    padding: 0.5rem 1rem;
    background: var(--accent);
    color: var(--bg);
    font-weight: 600;
  }

  .skip-to-content:focus {
    left: 0;
  }

  /* Prose styling for thesis content */
  .prose {
    font-family: var(--serif);
    font-size: 1.05rem;
    line-height: 1.8;
    color: #ccc;
    max-width: 65ch;
  }

  .prose p {
    margin-bottom: 1.2em;
  }

  .prose h2 {
    font-size: 1.6rem;
    font-weight: 400;
    margin-top: 2em;
    margin-bottom: 0.8em;
    color: var(--text);
  }

  .prose h3 {
    font-size: 1.2rem;
    font-weight: 500;
    margin-top: 1.5em;
    margin-bottom: 0.6em;
    color: var(--text);
  }

  /* Section label (e.g., "01 — Abstract") */
  .section-label {
    font-family: var(--sans);
    font-size: 0.8rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 0.8rem;
  }

  .section-title {
    font-family: var(--serif);
    font-size: clamp(1.6rem, 3vw, 2.4rem);
    font-weight: 400;
    margin-bottom: 1rem;
    color: var(--text);
  }
}
```

- [ ] **Step 3: Verify build**

```bash
npm run build
```

- [ ] **Step 4: Commit**

```bash
git add src/styles/
git commit -m "feat: add global styles, design tokens, and self-hosted font setup"
```

---

## Task 5: Base Layout

**Files:**
- Create: `src/layouts/BaseLayout.astro`, `src/components/Nav.astro`, `src/components/Footer.astro`

- [ ] **Step 1: Write Nav component**

Write `src/components/Nav.astro`:

```astro
---
const { pathname } = Astro.url;

const navLinks = [
  { href: '/read/', label: 'Read' },
  { href: '/topic/', label: 'Topics' },
  { href: '/scale/', label: 'Scales' },
  { href: '/drawing/', label: 'Drawings' },
  { href: '/timeline', label: 'Timeline' },
  { href: '/search', label: 'Search' },
];
---

<nav class="fixed top-0 left-0 right-0 z-50 bg-[rgba(10,10,10,0.92)] backdrop-blur-lg border-b border-border px-8 flex items-center justify-between h-14" role="navigation" aria-label="Main navigation">
  <a href="/" class="font-serif text-lg tracking-wide text-accent no-underline">
    Rebuilding <em>Lahaina</em>
    <span class="text-text-muted font-light"> — Thesis</span>
  </a>
  <ul class="list-none flex gap-7">
    {navLinks.map(({ href, label }) => (
      <li>
        <a
          href={href}
          class:list={[
            'text-text-muted no-underline text-[0.8rem] font-medium tracking-widest uppercase transition-colors hover:text-text',
            { 'text-text': pathname.startsWith(href) },
          ]}
        >
          {label}
        </a>
      </li>
    ))}
  </ul>
</nav>
```

- [ ] **Step 2: Write Footer component**

Write `src/components/Footer.astro`:

```astro
---
---

<footer class="border-t border-border py-12 text-center text-[0.8rem] text-[#444] tracking-widest uppercase" role="contentinfo">
  <p>Akhil Singh &bull; Tulane School of Architecture &bull; M.Arch 2025 &bull; Rebuilding Lahaina</p>
  <p class="mt-2">
    <a href="/downloads/final_as_thesis.pdf" class="text-accent hover:text-text transition-colors no-underline">
      Download Full Thesis (PDF)
    </a>
  </p>
</footer>
```

- [ ] **Step 3: Write BaseLayout**

Write `src/layouts/BaseLayout.astro`:

```astro
---
import Nav from '../components/Nav.astro';
import Footer from '../components/Footer.astro';
import '../styles/global.css';

interface Props {
  title: string;
  description?: string;
  ogImage?: string;
}

const {
  title,
  description = 'Rebuilding Lahaina — A thesis on post-disaster recovery, resilient urbanism, and water systems for Lahaina, Maui.',
  ogImage = '/images/og-default.jpg',
} = Astro.props;

const canonicalUrl = new URL(Astro.url.pathname, Astro.site);
---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title} | Rebuilding Lahaina</title>
    <meta name="description" content={description} />
    <link rel="canonical" href={canonicalUrl} />

    <!-- Open Graph -->
    <meta property="og:title" content={`${title} | Rebuilding Lahaina`} />
    <meta property="og:description" content={description} />
    <meta property="og:image" content={ogImage} />
    <meta property="og:url" content={canonicalUrl} />
    <meta property="og:type" content="website" />

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content={`${title} | Rebuilding Lahaina`} />
    <meta name="twitter:description" content={description} />
    <meta name="twitter:image" content={ogImage} />
  </head>
  <body>
    <a href="#main-content" class="skip-to-content">Skip to content</a>
    <Nav />
    <main id="main-content" class="pt-14">
      <slot />
    </main>
    <Footer />
  </body>
</html>
```

- [ ] **Step 4: Create a minimal index page to test layout**

Write `src/pages/index.astro`:

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout title="Home">
  <div class="min-h-screen flex items-center justify-center">
    <h1 class="font-serif text-4xl text-accent">Rebuilding Lahaina</h1>
  </div>
</BaseLayout>
```

- [ ] **Step 5: Verify dev server**

```bash
npm run dev
```

Open in browser: `http://localhost:4321`. Expected: dark page with nav bar, "Rebuilding Lahaina" centered, and footer.

- [ ] **Step 6: Commit**

```bash
git add src/layouts/ src/components/Nav.astro src/components/Footer.astro src/pages/index.astro
git commit -m "feat: add BaseLayout with Nav, Footer, OG tags, and accessibility"
```

---

## Task 6: Tag Pills & Content Card Components

**Files:**
- Create: `src/components/TagPills.astro`, `src/components/ContentCard.astro`, `src/components/Breadcrumbs.astro`

- [ ] **Step 1: Write TagPills component**

Write `src/components/TagPills.astro`:

```astro
---
interface Props {
  topics?: string[];
  scales?: string[];
  types?: string[];
}

const { topics = [], scales = [], types = [] } = Astro.props;
---

<div class="flex flex-wrap gap-2">
  {topics.map((tag) => (
    <a href={`/topic/${tag}`} class="inline-block text-[0.8rem] px-2 py-0.5 border border-accent text-accent rounded-sm tracking-wide uppercase no-underline hover:bg-accent-dim transition-colors" data-pagefind-filter={`topic:${tag}`}>
      {tag.replaceAll('-', ' ')}
    </a>
  ))}
  {scales.map((tag) => (
    <a href={`/scale/${tag}`} class="inline-block text-[0.8rem] px-2 py-0.5 border border-border text-text-muted rounded-sm tracking-wide uppercase no-underline hover:bg-surface-hover transition-colors" data-pagefind-filter={`scale:${tag}`}>
      {tag}
    </a>
  ))}
  {types.map((tag) => (
    <span class="inline-block text-[0.8rem] px-2 py-0.5 border border-border text-text-muted rounded-sm tracking-wide uppercase" data-pagefind-filter={`type:${tag}`}>
      {tag}
    </span>
  ))}
</div>
```

- [ ] **Step 2: Write ContentCard component**

Write `src/components/ContentCard.astro`:

```astro
---
interface Props {
  title: string;
  href: string;
  description?: string;
  label?: string;
  tags?: string[];
}

const { title, href, description, label, tags = [] } = Astro.props;
---

<a href={href} class="block bg-surface border border-border p-6 transition-all hover:border-[#333] hover:-translate-y-0.5 no-underline group">
  {label && (
    <div class="text-[0.8rem] text-accent tracking-widest uppercase mb-2">
      {label}
    </div>
  )}
  <h3 class="font-serif text-lg font-normal mb-1 text-text group-hover:text-accent transition-colors">
    {title}
  </h3>
  {description && (
    <p class="text-[0.85rem] text-text-muted leading-relaxed">
      {description}
    </p>
  )}
  {tags.length > 0 && (
    <div class="mt-3 flex flex-wrap gap-1">
      {tags.map((tag) => (
        <span class="text-[0.8rem] text-[#555] tracking-wide uppercase">
          {tag.replaceAll('-', ' ')}
        </span>
      ))}
    </div>
  )}
</a>
```

- [ ] **Step 3: Write Breadcrumbs component**

Write `src/components/Breadcrumbs.astro`:

```astro
---
interface Crumb {
  label: string;
  href?: string;
}

interface Props {
  crumbs: Crumb[];
}

const { crumbs } = Astro.props;
---

<nav aria-label="Breadcrumb" class="text-[0.8rem] text-text-muted tracking-wide uppercase mb-6">
  <ol class="flex gap-2 list-none">
    {crumbs.map((crumb, i) => (
      <li class="flex items-center gap-2">
        {i > 0 && <span class="text-border">/</span>}
        {crumb.href ? (
          <a href={crumb.href} class="text-text-muted hover:text-text no-underline transition-colors">
            {crumb.label}
          </a>
        ) : (
          <span class="text-text">{crumb.label}</span>
        )}
      </li>
    ))}
  </ol>
</nav>
```

- [ ] **Step 4: Commit**

```bash
git add src/components/TagPills.astro src/components/ContentCard.astro src/components/Breadcrumbs.astro
git commit -m "feat: add TagPills, ContentCard, and Breadcrumbs components"
```

---

## Task 7: Section Pages (Narrative Path)

**Files:**
- Create: `src/layouts/SectionLayout.astro`, `src/components/PrevNext.astro`, `src/components/Sidebar.astro`, `src/pages/read/index.astro`, `src/pages/read/[...slug].astro`

- [ ] **Step 1: Write PrevNext component**

Write `src/components/PrevNext.astro`:

```astro
---
interface Link {
  slug: string;
  title: string;
}

interface Props {
  prev?: Link;
  next?: Link;
}

const { prev, next } = Astro.props;
---

<nav class="flex justify-between border-t border-border pt-8 mt-12" aria-label="Section navigation">
  {prev ? (
    <a href={`/read/${prev.slug}`} class="text-text-muted hover:text-text no-underline transition-colors">
      <span class="text-[0.8rem] tracking-widest uppercase block mb-1">Previous</span>
      <span class="font-serif text-lg">{prev.title}</span>
    </a>
  ) : <div />}
  {next ? (
    <a href={`/read/${next.slug}`} class="text-text-muted hover:text-text no-underline transition-colors text-right">
      <span class="text-[0.8rem] tracking-widest uppercase block mb-1">Next</span>
      <span class="font-serif text-lg">{next.title}</span>
    </a>
  ) : <div />}
</nav>
```

- [ ] **Step 2: Write Sidebar component**

Write `src/components/Sidebar.astro`:

```astro
---
import { getCollection } from 'astro:content';

interface Props {
  relatedDrawings?: string[];
  relatedSources?: string[];
  relatedTerms?: string[];
}

const { relatedDrawings = [], relatedSources = [], relatedTerms = [] } = Astro.props;

const allDrawings = await getCollection('drawings');
const allSources = await getCollection('sources');
const allTerms = await getCollection('terms');

const drawings = allDrawings.filter((d) => relatedDrawings.includes(d.id));
const sources = allSources.filter((s) => relatedSources.includes(s.id));
const terms = allTerms.filter((t) => relatedTerms.includes(t.id));
---

<aside class="space-y-8" role="complementary" aria-label="Related content">
  {drawings.length > 0 && (
    <div>
      <h4 class="text-[0.8rem] tracking-widest uppercase text-accent mb-3">Related Drawings</h4>
      <ul class="space-y-2 list-none">
        {drawings.map((d) => (
          <li>
            <a href={`/drawing/${d.id}`} class="text-text-muted hover:text-text no-underline text-sm transition-colors">
              {d.data.title}
            </a>
          </li>
        ))}
      </ul>
    </div>
  )}
  {terms.length > 0 && (
    <div>
      <h4 class="text-[0.8rem] tracking-widest uppercase text-accent mb-3">Key Terms</h4>
      <ul class="space-y-2 list-none">
        {terms.map((t) => (
          <li>
            <a href={`/term/${t.id}`} class="text-text-muted hover:text-text no-underline text-sm transition-colors">
              {t.data.term}
            </a>
          </li>
        ))}
      </ul>
    </div>
  )}
  {sources.length > 0 && (
    <div>
      <h4 class="text-[0.8rem] tracking-widest uppercase text-accent mb-3">Sources</h4>
      <ul class="space-y-2 list-none">
        {sources.map((s) => (
          <li>
            <a href={`/source/${s.id}`} class="text-text-muted hover:text-text no-underline text-sm transition-colors">
              {s.data.title}
            </a>
          </li>
        ))}
      </ul>
    </div>
  )}
</aside>
```

- [ ] **Step 3: Write SectionLayout**

Write `src/layouts/SectionLayout.astro`:

```astro
---
import BaseLayout from './BaseLayout.astro';
import TagPills from '../components/TagPills.astro';
import PrevNext from '../components/PrevNext.astro';
import Sidebar from '../components/Sidebar.astro';
import Breadcrumbs from '../components/Breadcrumbs.astro';

interface Link {
  slug: string;
  title: string;
}

interface Props {
  title: string;
  chapter: string;
  summary: string;
  tags: { topic: string[]; scale: string[]; type: string[] };
  relatedDrawings?: string[];
  relatedSources?: string[];
  relatedTerms?: string[];
  prev?: Link;
  next?: Link;
}

const { title, chapter, summary, tags, relatedDrawings, relatedSources, relatedTerms, prev, next } = Astro.props;

const chapterLabels: Record<string, string> = {
  'ch1-introduction': '01 — Introduction',
  'ch2-overview': '02 — Subject Overview',
  'ch3-analysis': '03 — Research Analysis',
  'ch4-principles': '04 — Design Principles',
  'ch5-design': '05 — Design',
};
---

<BaseLayout title={title} description={summary}>
  <div class="max-w-6xl mx-auto px-6 py-20">
    <Breadcrumbs crumbs={[
      { label: 'Read', href: '/read/' },
      { label: chapterLabels[chapter] || chapter, href: '/read/' },
      { label: title },
    ]} />

    <div class="section-label">{chapterLabels[chapter] || chapter}</div>
    <h1 class="section-title mb-4">{title}</h1>

    <TagPills topics={tags.topic} scales={tags.scale} types={tags.type} />

    <div class="grid grid-cols-1 lg:grid-cols-[1fr_280px] gap-12 mt-10">
      <article class="prose" data-pagefind-body>
        <slot />
      </article>

      <Sidebar relatedDrawings={relatedDrawings} relatedSources={relatedSources} relatedTerms={relatedTerms} />
    </div>

    <PrevNext prev={prev} next={next} />
  </div>
</BaseLayout>
```

- [ ] **Step 4: Write read index page**

Write `src/pages/read/index.astro`:

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import ContentCard from '../../components/ContentCard.astro';
import { getCollection } from 'astro:content';

const sections = await getCollection('sections');
const sorted = sections.sort((a, b) => {
  if (a.data.chapter !== b.data.chapter) return a.data.chapter.localeCompare(b.data.chapter);
  return a.data.order - b.data.order;
});

const chapterLabels: Record<string, string> = {
  'ch1-introduction': '01 — Introduction',
  'ch2-overview': '02 — Subject Overview',
  'ch3-analysis': '03 — Research Analysis',
  'ch4-principles': '04 — Design Principles',
  'ch5-design': '05 — Design',
};

const chapters = Object.entries(chapterLabels).map(([key, label]) => ({
  key,
  label,
  sections: sorted.filter((s) => s.data.chapter === key),
}));
---

<BaseLayout title="Read the Thesis" description="Read the full Rebuilding Lahaina thesis organized by chapter.">
  <section class="max-w-4xl mx-auto px-6 py-20">
    <div class="section-label">Narrative Path</div>
    <h1 class="section-title mb-4">Read the Thesis</h1>
    <p class="text-text-muted text-[0.92rem] leading-relaxed mb-12 max-w-2xl">
      Read the full thesis from start to finish, organized by chapter. Each section is a self-contained page.
    </p>

    {chapters.map(({ label, sections: chapterSections }) => (
      <div class="mb-10">
        <h2 class="font-serif text-xl mb-4 text-text">{label}</h2>
        <div class="grid gap-px bg-border border border-border">
          {chapterSections.map((section) => (
            <ContentCard
              title={section.data.title}
              href={`/read/${section.id}`}
              description={section.data.summary}
              tags={section.data.tags.topic}
            />
          ))}
        </div>
      </div>
    ))}
  </section>
</BaseLayout>
```

- [ ] **Step 5: Write dynamic section page**

Write `src/pages/read/[...slug].astro`:

```astro
---
import SectionLayout from '../../layouts/SectionLayout.astro';
import { getCollection, render } from 'astro:content';

export async function getStaticPaths() {
  const sections = await getCollection('sections');
  const sorted = sections.sort((a, b) => {
    if (a.data.chapter !== b.data.chapter) return a.data.chapter.localeCompare(b.data.chapter);
    return a.data.order - b.data.order;
  });

  return sorted.map((section, i) => ({
    params: { slug: section.id },
    props: {
      section,
      prev: i > 0 ? { slug: sorted[i - 1].id, title: sorted[i - 1].data.title } : undefined,
      next: i < sorted.length - 1 ? { slug: sorted[i + 1].id, title: sorted[i + 1].data.title } : undefined,
    },
  }));
}

const { section, prev, next } = Astro.props;
const { Content } = await render(section);
---

<SectionLayout
  title={section.data.title}
  chapter={section.data.chapter}
  summary={section.data.summary}
  tags={section.data.tags}
  relatedDrawings={section.data.relatedDrawings}
  relatedSources={section.data.relatedSources}
  relatedTerms={section.data.relatedTerms}
  prev={prev}
  next={next}
>
  <Content />
</SectionLayout>
```

- [ ] **Step 6: Verify build and test navigation**

```bash
npm run build
```

Expected: Build succeeds. Pages generated at `/read/`, `/read/abstract`, `/read/pioneer-mill-water-infrastructure`.

- [ ] **Step 7: Commit**

```bash
git add src/layouts/SectionLayout.astro src/components/PrevNext.astro src/components/Sidebar.astro src/pages/read/
git commit -m "feat: add narrative path — section pages with sidebar and prev/next navigation"
```

---

## Task 8: Drawing Pages

**Files:**
- Create: `src/layouts/DrawingLayout.astro`, `src/components/DrawingViewer.astro`, `src/pages/drawing/[...slug].astro`

- [ ] **Step 1: Write DrawingViewer component**

Write `src/components/DrawingViewer.astro`:

```astro
---
interface Props {
  src: string;
  alt: string;
  title: string;
}

const { src, alt, title } = Astro.props;
---

<figure class="bg-surface border border-border p-4">
  <img
    src={src}
    alt={alt}
    class="w-full h-auto cursor-zoom-in zoomable"
    loading="lazy"
  />
  <figcaption class="mt-3 text-[0.8rem] text-text-muted tracking-wide">
    {title}
  </figcaption>
</figure>

<script>
  import mediumZoom from 'medium-zoom';
  mediumZoom('.zoomable', {
    background: 'rgba(10, 10, 10, 0.95)',
    margin: 24,
  });
</script>
```

- [ ] **Step 2: Write DrawingLayout**

Write `src/layouts/DrawingLayout.astro`:

```astro
---
import BaseLayout from './BaseLayout.astro';
import DrawingViewer from '../components/DrawingViewer.astro';
import TagPills from '../components/TagPills.astro';
import Breadcrumbs from '../components/Breadcrumbs.astro';
import { getCollection } from 'astro:content';

interface Props {
  title: string;
  image: string;
  alt: string;
  scaleLevel: string;
  drawingType: string;
  relatedSections?: string[];
  tags: { topic: string[]; scale: string[]; type: string[] };
}

const { title, image, alt, scaleLevel, drawingType, relatedSections = [], tags } = Astro.props;

const allSections = await getCollection('sections');
const sections = allSections.filter((s) => relatedSections.includes(s.id));
---

<BaseLayout title={title} description={alt}>
  <div class="max-w-5xl mx-auto px-6 py-20" data-pagefind-body>
    <Breadcrumbs crumbs={[
      { label: 'Drawings', href: '/drawing/' },
      { label: scaleLevel, href: `/scale/${scaleLevel}` },
      { label: title },
    ]} />

    <div class="section-label">{scaleLevel} Scale — {drawingType}</div>
    <h1 class="section-title mb-4">{title}</h1>

    <TagPills topics={tags.topic} scales={tags.scale} types={tags.type} />

    <div class="mt-8">
      <DrawingViewer src={image} alt={alt} title={title} />
    </div>

    <div class="prose mt-8">
      <slot />
    </div>

    {sections.length > 0 && (
      <div class="mt-12">
        <h3 class="text-[0.8rem] tracking-widest uppercase text-accent mb-4">Related Sections</h3>
        <ul class="space-y-2 list-none">
          {sections.map((s) => (
            <li>
              <a href={`/read/${s.id}`} class="text-text-muted hover:text-text no-underline transition-colors">
                {s.data.title}
              </a>
            </li>
          ))}
        </ul>
      </div>
    )}
  </div>
</BaseLayout>
```

- [ ] **Step 3: Write drawing index and detail pages**

Write `src/pages/drawing/index.astro`:

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import ContentCard from '../../components/ContentCard.astro';
import { getCollection } from 'astro:content';

const drawings = await getCollection('drawings');

const scaleOrder = ['regional', 'district', 'town', 'site', 'node'];
const byScale = scaleOrder
  .map((scale) => ({
    scale,
    drawings: drawings.filter((d) => d.data.scaleLevel === scale),
  }))
  .filter((group) => group.drawings.length > 0);
---

<BaseLayout title="Drawings" description="Complete index of all analytical and design drawings.">
  <section class="max-w-5xl mx-auto px-6 py-20">
    <div class="section-label">Drawing Index</div>
    <h1 class="section-title mb-4">Plates & Drawings</h1>
    <p class="text-text-muted text-[0.92rem] leading-relaxed mb-12 max-w-2xl">
      Complete index of all analytical and design drawings produced for the thesis, organized by scale.
    </p>

    {byScale.map(({ scale, drawings: scaledDrawings }) => (
      <div class="mb-10">
        <h2 class="font-serif text-xl mb-4 text-text capitalize">{scale} Scale</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          {scaledDrawings.map((drawing) => (
            <ContentCard
              title={drawing.data.title}
              href={`/drawing/${drawing.id}`}
              description={drawing.data.alt}
              label={drawing.data.drawingType}
              tags={drawing.data.tags.topic}
            />
          ))}
        </div>
      </div>
    ))}
  </section>
</BaseLayout>
```

Write `src/pages/drawing/[...slug].astro`:

```astro
---
import DrawingLayout from '../../layouts/DrawingLayout.astro';
import { getCollection, render } from 'astro:content';

export async function getStaticPaths() {
  const drawings = await getCollection('drawings');
  return drawings.map((drawing) => ({
    params: { slug: drawing.id },
    props: { drawing },
  }));
}

const { drawing } = Astro.props;
const { Content } = await render(drawing);
---

<DrawingLayout
  title={drawing.data.title}
  image={drawing.data.image}
  alt={drawing.data.alt}
  scaleLevel={drawing.data.scaleLevel}
  drawingType={drawing.data.drawingType}
  relatedSections={drawing.data.relatedSections}
  tags={drawing.data.tags}
>
  <Content />
</DrawingLayout>
```

- [ ] **Step 4: Verify build**

```bash
npm run build
```

Expected: Drawing pages generated with zoom viewer.

- [ ] **Step 5: Commit**

```bash
git add src/layouts/DrawingLayout.astro src/components/DrawingViewer.astro src/pages/drawing/
git commit -m "feat: add drawing pages with zoomable image viewer"
```

---

## Task 9: Source, Term, and Timeline Pages

**Files:**
- Create: `src/pages/source/[...slug].astro`, `src/pages/source/index.astro`, `src/pages/term/[...slug].astro`, `src/pages/term/index.astro`, `src/pages/timeline.astro`, `src/components/Timeline.astro`

- [ ] **Step 1: Write source pages**

Write `src/pages/source/index.astro`:

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import { getCollection } from 'astro:content';

const sources = await getCollection('sources');
const byType = ['book', 'report', 'government-doc', 'research-note'].map((type) => ({
  type,
  label: type === 'government-doc' ? 'Government Documents' : type === 'research-note' ? 'Research Notes' : type.charAt(0).toUpperCase() + type.slice(1) + 's',
  sources: sources.filter((s) => s.data.sourceType === type),
})).filter((g) => g.sources.length > 0);
---

<BaseLayout title="Sources" description="Complete directory of research sources.">
  <section class="max-w-5xl mx-auto px-6 py-20">
    <div class="section-label">Source Directory</div>
    <h1 class="section-title mb-12">Research Sources & References</h1>

    {byType.map(({ label, sources: typed }) => (
      <div class="mb-10">
        <h2 class="font-serif text-xl mb-4">{label}</h2>
        <div class="border border-border">
          {typed.map((source) => (
            <a href={`/source/${source.id}`} class="block p-4 border-b border-border hover:bg-surface-hover no-underline transition-colors" data-pagefind-body>
              <div class="font-serif text-base text-text">{source.data.title}</div>
              <div class="text-[0.85rem] text-text-muted mt-1">{source.data.author} {source.data.date && `— ${source.data.date}`}</div>
            </a>
          ))}
        </div>
      </div>
    ))}
  </section>
</BaseLayout>
```

Write `src/pages/source/[...slug].astro`:

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import TagPills from '../../components/TagPills.astro';
import Breadcrumbs from '../../components/Breadcrumbs.astro';
import { getCollection, render } from 'astro:content';

export async function getStaticPaths() {
  const sources = await getCollection('sources');
  return sources.map((source) => ({
    params: { slug: source.id },
    props: { source },
  }));
}

const { source } = Astro.props;
const { Content } = await render(source);
---

<BaseLayout title={source.data.title} description={source.data.relevance}>
  <div class="max-w-3xl mx-auto px-6 py-20" data-pagefind-body>
    <Breadcrumbs crumbs={[
      { label: 'Sources', href: '/source/' },
      { label: source.data.title },
    ]} />

    <div class="section-label">{source.data.sourceType.replace('-', ' ')}</div>
    <h1 class="section-title mb-2">{source.data.title}</h1>
    <p class="text-text-muted text-lg font-serif mb-2">{source.data.author}</p>
    {source.data.publisher && <p class="text-text-muted text-sm">{source.data.publisher}{source.data.date && `, ${source.data.date}`}</p>}

    <div class="mt-6 mb-6">
      <TagPills topics={source.data.tags.topic} types={source.data.tags.type} />
    </div>

    <div class="bg-surface border-l-[3px] border-accent p-6 text-text-muted font-serif text-base leading-relaxed">
      {source.data.relevance}
    </div>

    <div class="prose mt-8">
      <Content />
    </div>
  </div>
</BaseLayout>
```

- [ ] **Step 2: Write term pages**

Write `src/pages/term/index.astro`:

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import { getCollection } from 'astro:content';

const terms = await getCollection('terms');
const concepts = terms.filter((t) => t.data.category === 'concept');
const hawaiian = terms.filter((t) => t.data.category === 'hawaiian');
const acronyms = terms.filter((t) => t.data.category === 'acronym');

const groups = [
  { label: 'Key Terms', terms: concepts },
  { label: 'Hawaiian Terms', terms: hawaiian },
  { label: 'Acronyms', terms: acronyms },
].filter((g) => g.terms.length > 0);
---

<BaseLayout title="Terms & Glossary" description="Core terminology used throughout the thesis.">
  <section class="max-w-4xl mx-auto px-6 py-20">
    <div class="section-label">Glossary</div>
    <h1 class="section-title mb-12">Definitions & Key Terms</h1>

    {groups.map(({ label, terms: grouped }) => (
      <div class="mb-10">
        <h2 class="font-serif text-xl mb-4">{label}</h2>
        <div class="space-y-4">
          {grouped.map((term) => (
            <a href={`/term/${term.id}`} class="block border-b border-border pb-4 no-underline hover:bg-surface-hover transition-colors" data-pagefind-body>
              <h4 class="text-[0.85rem] tracking-wide uppercase text-accent mb-1">{term.data.term}</h4>
              <p class="text-text-muted text-[0.9rem] leading-relaxed">{term.data.definition}</p>
            </a>
          ))}
        </div>
      </div>
    ))}
  </section>
</BaseLayout>
```

Write `src/pages/term/[...slug].astro`:

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import TagPills from '../../components/TagPills.astro';
import Breadcrumbs from '../../components/Breadcrumbs.astro';
import { getCollection, render } from 'astro:content';

export async function getStaticPaths() {
  const terms = await getCollection('terms');
  return terms.map((term) => ({
    params: { slug: term.id },
    props: { term },
  }));
}

const { term } = Astro.props;
const { Content } = await render(term);

const sections = await getCollection('sections');
const related = sections.filter((s) => term.data.relatedSections.includes(s.id));
---

<BaseLayout title={term.data.term} description={term.data.definition}>
  <div class="max-w-3xl mx-auto px-6 py-20" data-pagefind-body>
    <Breadcrumbs crumbs={[
      { label: 'Terms', href: '/term/' },
      { label: term.data.term },
    ]} />

    <div class="section-label">{term.data.category}</div>
    <h1 class="section-title mb-4">{term.data.term}</h1>

    <div class="bg-surface border-l-[3px] border-accent p-6 font-serif text-lg leading-relaxed text-[#ccc] mb-6">
      {term.data.definition}
    </div>

    <TagPills topics={term.data.tags.topic} />

    <div class="prose mt-8">
      <Content />
    </div>

    {related.length > 0 && (
      <div class="mt-12">
        <h3 class="text-[0.8rem] tracking-widest uppercase text-accent mb-4">Used In</h3>
        <ul class="space-y-2 list-none">
          {related.map((s) => (
            <li>
              <a href={`/read/${s.id}`} class="text-text-muted hover:text-text no-underline transition-colors">
                {s.data.title}
              </a>
            </li>
          ))}
        </ul>
      </div>
    )}
  </div>
</BaseLayout>
```

- [ ] **Step 3: Write Timeline component and page**

Write `src/components/Timeline.astro`:

```astro
---
import { getCollection } from 'astro:content';

const events = await getCollection('timeline');
const sorted = events.sort((a, b) => a.data.sortOrder - b.data.sortOrder);
---

<div class="relative pl-8">
  <div class="absolute left-0 top-0 bottom-0 w-px bg-border" />
  {sorted.map((event) => (
    <div class="relative mb-8 pl-6">
      <div class="absolute -left-[2.28rem] top-[0.35rem] w-[7px] h-[7px] rounded-full bg-accent" />
      <div class="text-[0.8rem] text-accent tracking-wide mb-1">{event.data.era}</div>
      <h4 class="font-serif text-base mb-1">{event.data.title}</h4>
      <p class="text-[0.85rem] text-text-muted leading-relaxed">{event.data.description}</p>
    </div>
  ))}
</div>
```

Write `src/pages/timeline.astro`:

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
import Timeline from '../components/Timeline.astro';
---

<BaseLayout title="Timeline" description="Key events in Lahaina's history from pre-contact to the present.">
  <section class="max-w-3xl mx-auto px-6 py-20" data-pagefind-body>
    <div class="section-label">Historical Context</div>
    <h1 class="section-title mb-4">Lahaina — Key Events</h1>
    <p class="text-text-muted text-[0.92rem] leading-relaxed mb-12 max-w-2xl">
      Major spatial and infrastructural events that shaped the town.
    </p>

    <Timeline />
  </section>
</BaseLayout>
```

- [ ] **Step 4: Verify build**

```bash
npm run build
```

Expected: All source, term, and timeline pages generated.

- [ ] **Step 5: Commit**

```bash
git add src/pages/source/ src/pages/term/ src/pages/timeline.astro src/components/Timeline.astro
git commit -m "feat: add source, term, and timeline pages"
```

---

## Task 10: Topic & Scale Pages

**Files:**
- Create: `src/pages/topic/index.astro`, `src/pages/topic/[tag].astro`, `src/pages/scale/index.astro`, `src/pages/scale/[level].astro`, `src/components/ScaleNav.astro`

- [ ] **Step 1: Write topic pages**

Write `src/pages/topic/index.astro`:

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import ContentCard from '../../components/ContentCard.astro';
import { getCollection } from 'astro:content';

const topics = await getCollection('topics');
---

<BaseLayout title="Explore by Topic" description="Browse thesis content by thematic topic.">
  <section class="max-w-4xl mx-auto px-6 py-20">
    <div class="section-label">Topic Explorer</div>
    <h1 class="section-title mb-4">Explore by Topic</h1>
    <p class="text-text-muted text-[0.92rem] leading-relaxed mb-12 max-w-2xl">
      Browse all thesis content organized by thematic topic. Each topic aggregates related sections, drawings, maps, and sources.
    </p>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      {topics.map((topic) => (
        <ContentCard
          title={topic.data.title}
          href={`/topic/${topic.id}`}
          description={topic.data.summary}
        />
      ))}
    </div>
  </section>
</BaseLayout>
```

Write `src/pages/topic/[tag].astro`:

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import ContentCard from '../../components/ContentCard.astro';
import Breadcrumbs from '../../components/Breadcrumbs.astro';
import { getCollection, render } from 'astro:content';

export async function getStaticPaths() {
  const topics = await getCollection('topics');
  return topics.map((topic) => ({
    params: { tag: topic.id },
    props: { topic },
  }));
}

const { topic } = Astro.props;
const { Content } = await render(topic);
const tag = topic.id;

const sections = (await getCollection('sections')).filter((s) => s.data.tags.topic.includes(tag));
const drawings = (await getCollection('drawings')).filter((d) => d.data.tags.topic.includes(tag));
const sources = (await getCollection('sources')).filter((s) => s.data.tags.topic.includes(tag));
const terms = (await getCollection('terms')).filter((t) => t.data.tags.topic.includes(tag));
const maps = (await getCollection('maps')).filter((m) => m.data.tags.topic.includes(tag));
---

<BaseLayout title={topic.data.title} description={topic.data.summary}>
  <section class="max-w-5xl mx-auto px-6 py-20" data-pagefind-body>
    <Breadcrumbs crumbs={[
      { label: 'Topics', href: '/topic/' },
      { label: topic.data.title },
    ]} />

    <div class="section-label">Topic</div>
    <h1 class="section-title mb-4">{topic.data.title}</h1>

    <div class="prose mb-12">
      <Content />
    </div>

    {sections.length > 0 && (
      <div class="mb-10">
        <h2 class="font-serif text-xl mb-4">Sections</h2>
        <div class="grid gap-4">
          {sections.map((s) => (
            <ContentCard title={s.data.title} href={`/read/${s.id}`} description={s.data.summary} label={s.data.chapter} />
          ))}
        </div>
      </div>
    )}

    {drawings.length > 0 && (
      <div class="mb-10">
        <h2 class="font-serif text-xl mb-4">Drawings</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          {drawings.map((d) => (
            <ContentCard title={d.data.title} href={`/drawing/${d.id}`} description={d.data.alt} label={d.data.drawingType} />
          ))}
        </div>
      </div>
    )}

    {maps.length > 0 && (
      <div class="mb-10">
        <h2 class="font-serif text-xl mb-4">Interactive Maps</h2>
        <div class="grid gap-4">
          {maps.map((m) => (
            <ContentCard title={m.data.title} href={`/map/${m.id}`} description={m.data.description} label="Interactive Map" />
          ))}
        </div>
      </div>
    )}

    {sources.length > 0 && (
      <div class="mb-10">
        <h2 class="font-serif text-xl mb-4">Sources</h2>
        <div class="grid gap-4">
          {sources.map((s) => (
            <ContentCard title={s.data.title} href={`/source/${s.id}`} description={`${s.data.author} — ${s.data.relevance}`} label={s.data.sourceType} />
          ))}
        </div>
      </div>
    )}

    {terms.length > 0 && (
      <div class="mb-10">
        <h2 class="font-serif text-xl mb-4">Terms</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          {terms.map((t) => (
            <ContentCard title={t.data.term} href={`/term/${t.id}`} description={t.data.definition} label={t.data.category} />
          ))}
        </div>
      </div>
    )}
  </section>
</BaseLayout>
```

- [ ] **Step 2: Write scale pages**

Write `src/components/ScaleNav.astro`:

```astro
---
const scales = [
  { id: 'regional', label: 'Regional' },
  { id: 'district', label: 'District' },
  { id: 'town', label: 'Town' },
  { id: 'site', label: 'Site' },
  { id: 'node', label: 'Node' },
];

interface Props {
  active?: string;
}

const { active } = Astro.props;
---

<nav class="flex gap-1 mb-8" aria-label="Scale navigation">
  {scales.map((scale) => (
    <a
      href={`/scale/${scale.id}`}
      class:list={[
        'px-4 py-2 text-[0.8rem] tracking-widest uppercase no-underline transition-colors border',
        active === scale.id
          ? 'bg-accent text-bg border-accent'
          : 'bg-surface text-text-muted border-border hover:text-text hover:border-[#333]',
      ]}
    >
      {scale.label}
    </a>
  ))}
</nav>
```

Write `src/pages/scale/index.astro`:

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import ScaleNav from '../../components/ScaleNav.astro';
import ContentCard from '../../components/ContentCard.astro';
import { getCollection } from 'astro:content';

const scales = await getCollection('scales');
---

<BaseLayout title="Explore by Scale" description="Browse thesis content by spatial scale.">
  <section class="max-w-4xl mx-auto px-6 py-20">
    <div class="section-label">Scale Navigator</div>
    <h1 class="section-title mb-4">Explore by Scale</h1>
    <p class="text-text-muted text-[0.92rem] leading-relaxed mb-12 max-w-2xl">
      The thesis operates across five spatial scales. Select a scale to see all analysis, drawings, and proposals at that level.
    </p>

    <ScaleNav />

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-8">
      {scales.map((scale) => (
        <ContentCard
          title={scale.data.title}
          href={`/scale/${scale.id}`}
          description={scale.data.summary}
        />
      ))}
    </div>
  </section>
</BaseLayout>
```

Write `src/pages/scale/[level].astro`:

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import ScaleNav from '../../components/ScaleNav.astro';
import ContentCard from '../../components/ContentCard.astro';
import Breadcrumbs from '../../components/Breadcrumbs.astro';
import { getCollection, render } from 'astro:content';

export async function getStaticPaths() {
  const scales = await getCollection('scales');
  return scales.map((scale) => ({
    params: { level: scale.id },
    props: { scale },
  }));
}

const { scale } = Astro.props;
const { Content } = await render(scale);
const level = scale.id;

const sections = (await getCollection('sections')).filter((s) => s.data.tags.scale?.includes(level));
const drawings = (await getCollection('drawings')).filter((d) => d.data.tags.scale?.includes(level));
const maps = (await getCollection('maps')).filter((m) => m.data.tags.scale?.includes(level));
---

<BaseLayout title={`${scale.data.title} Scale`} description={scale.data.summary}>
  <section class="max-w-5xl mx-auto px-6 py-20" data-pagefind-body>
    <Breadcrumbs crumbs={[
      { label: 'Scales', href: '/scale/' },
      { label: scale.data.title },
    ]} />

    <div class="section-label">Scale</div>
    <h1 class="section-title mb-4">{scale.data.title}</h1>

    <ScaleNav active={level} />

    <div class="prose mb-12">
      <Content />
    </div>

    {drawings.length > 0 && (
      <div class="mb-10">
        <h2 class="font-serif text-xl mb-4">Drawings at this Scale</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          {drawings.map((d) => (
            <ContentCard title={d.data.title} href={`/drawing/${d.id}`} description={d.data.alt} label={d.data.drawingType} />
          ))}
        </div>
      </div>
    )}

    {sections.length > 0 && (
      <div class="mb-10">
        <h2 class="font-serif text-xl mb-4">Sections</h2>
        <div class="grid gap-4">
          {sections.map((s) => (
            <ContentCard title={s.data.title} href={`/read/${s.id}`} description={s.data.summary} />
          ))}
        </div>
      </div>
    )}

    {maps.length > 0 && (
      <div class="mb-10">
        <h2 class="font-serif text-xl mb-4">Interactive Maps</h2>
        <div class="grid gap-4">
          {maps.map((m) => (
            <ContentCard title={m.data.title} href={`/map/${m.id}`} description={m.data.description} label="Interactive Map" />
          ))}
        </div>
      </div>
    )}
  </section>
</BaseLayout>
```

- [ ] **Step 3: Verify build**

```bash
npm run build
```

Expected: Topic and scale pages generated with aggregated content.

- [ ] **Step 4: Commit**

```bash
git add src/pages/topic/ src/pages/scale/ src/components/ScaleNav.astro
git commit -m "feat: add topic explorer and scale navigator pages"
```

---

## Task 11: Homepage

**Files:**
- Modify: `src/pages/index.astro` (rewrite)

- [ ] **Step 1: Write the full homepage**

Rewrite `src/pages/index.astro`:

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
import ContentCard from '../components/ContentCard.astro';
import Timeline from '../components/Timeline.astro';
import { getCollection } from 'astro:content';

const sections = await getCollection('sections');
const drawings = await getCollection('drawings');
const maps = await getCollection('maps');
const featured = drawings.slice(0, 3);
---

<BaseLayout title="Home">
  <!-- HERO -->
  <div class="min-h-screen flex flex-col justify-end p-12 md:p-16 relative overflow-hidden"
    style="background: linear-gradient(180deg, rgba(10,10,10,0) 0%, rgba(10,10,10,0.85) 70%, #0a0a0a 100%), linear-gradient(135deg, #1a1510 0%, #0a0a0a 100%);">
    <div class="absolute inset-0 pointer-events-none" style="background: repeating-linear-gradient(0deg, transparent, transparent 120px, rgba(196,162,101,0.03) 120px, rgba(196,162,101,0.03) 121px);" />

    <div class="relative z-10">
      <div class="text-[0.85rem] text-text-muted tracking-widest uppercase mb-3">
        Graduate Thesis — Tulane School of Architecture
      </div>
      <h1 class="font-serif text-[clamp(2.8rem,6vw,5rem)] font-normal leading-[1.1] mb-5 max-w-[700px]">
        Rebuilding <em class="text-accent italic">Lahaina</em>
      </h1>
      <div class="font-serif text-lg text-text-muted mb-8">
        Akhil Singh &nbsp;|&nbsp; Director: Inaki Alday &nbsp;|&nbsp; Co-Director: Sean Fowler
      </div>
      <div class="flex gap-8 flex-wrap text-[0.8rem] text-text-muted tracking-wide uppercase opacity-60">
        <span>M.Arch 2025</span>
        <span>Post-Disaster Recovery</span>
        <span>Resilient Urbanism</span>
        <span>Water Systems</span>
      </div>
    </div>
  </div>

  <!-- SEARCH BAR -->
  <section class="max-w-3xl mx-auto px-6 pt-16 pb-8">
    <a href="/search" class="block bg-surface border border-border p-4 flex items-center gap-3 hover:border-[#333] transition-colors no-underline group">
      <svg class="w-5 h-5 text-text-muted group-hover:text-accent transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
      <span class="text-text-muted text-sm group-hover:text-text transition-colors">Search all thesis content...</span>
    </a>
  </section>

  <!-- ENTRY POINTS -->
  <section class="max-w-5xl mx-auto px-6 py-12">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <a href="/read/" class="block bg-surface border border-border p-8 text-center no-underline hover:border-accent transition-colors group">
        <div class="text-[0.8rem] text-accent tracking-widest uppercase mb-3">Narrative</div>
        <h2 class="font-serif text-2xl mb-2 text-text group-hover:text-accent transition-colors">Read the Thesis</h2>
        <p class="text-text-muted text-sm">Follow the full argument from context through design</p>
      </a>
      <a href="/topic/" class="block bg-surface border border-border p-8 text-center no-underline hover:border-accent transition-colors group">
        <div class="text-[0.8rem] text-accent tracking-widest uppercase mb-3">Thematic</div>
        <h2 class="font-serif text-2xl mb-2 text-text group-hover:text-accent transition-colors">Explore by Topic</h2>
        <p class="text-text-muted text-sm">Water, housing, mobility, coastal resilience, and more</p>
      </a>
      <a href="/scale/" class="block bg-surface border border-border p-8 text-center no-underline hover:border-accent transition-colors group">
        <div class="text-[0.8rem] text-accent tracking-widest uppercase mb-3">Spatial</div>
        <h2 class="font-serif text-2xl mb-2 text-text group-hover:text-accent transition-colors">Explore by Scale</h2>
        <p class="text-text-muted text-sm">Regional, district, town, site, and node</p>
      </a>
    </div>
  </section>

  <!-- ABSTRACT -->
  <section class="max-w-4xl mx-auto px-6 pb-20">
    <div class="section-label">Abstract</div>
    <div class="bg-surface border border-border border-l-[3px] border-l-accent p-8 font-serif text-lg leading-[1.8] text-[#ccc]">
      The 2023 wildfire in Lahaina revealed critical vulnerabilities in infrastructure, water management, and disaster preparedness. This thesis proposes recovery through a multi-scale plan that includes the major urban systems, the relation of the urban fabric with the coast and the hinterland, and a sequence of strategic nodes to serve the communities.
    </div>
  </section>

  <!-- FEATURED DRAWINGS -->
  {featured.length > 0 && (
    <section class="max-w-5xl mx-auto px-6 pb-20">
      <div class="section-label">Featured Drawings</div>
      <h2 class="section-title mb-8">Selected Plates</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        {featured.map((d) => (
          <ContentCard
            title={d.data.title}
            href={`/drawing/${d.id}`}
            description={d.data.alt}
            label={d.data.scaleLevel}
            tags={d.data.tags.topic}
          />
        ))}
      </div>
    </section>
  )}

  <!-- MAP PREVIEW -->
  {maps.length > 0 && (
    <section class="max-w-5xl mx-auto px-6 pb-20">
      <div class="section-label">Spatial Data</div>
      <h2 class="section-title mb-8">Interactive Maps</h2>
      <div class="grid gap-4">
        {maps.map((m) => (
          <ContentCard
            title={m.data.title}
            href={`/map/${m.id}`}
            description={m.data.description}
            label="Interactive Map"
            tags={m.data.tags.topic}
          />
        ))}
      </div>
    </section>
  )}
</BaseLayout>
```

- [ ] **Step 2: Verify build and check homepage**

```bash
npm run build && npm run preview
```

- [ ] **Step 3: Commit**

```bash
git add src/pages/index.astro
git commit -m "feat: build homepage with hero, entry points, abstract, and featured drawings"
```

---

## Task 12: Interactive Map Pages

**Files:**
- Create: `src/components/MapViewer.astro`, `src/pages/map/[...slug].astro`, `src/pages/map/index.astro`

- [ ] **Step 1: Write MapViewer component (Leaflet island)**

Write `src/components/MapViewer.astro`:

```astro
---
interface Layer {
  name: string;
  file: string;
  color: string;
}

interface Props {
  id: string;
  center: [number, number];
  zoom: number;
  layers: Layer[];
}

const { id, center, zoom, layers } = Astro.props;
---

<div id={`map-${id}`} class="w-full h-[600px] bg-surface border border-border relative" data-center={JSON.stringify(center)} data-zoom={zoom} data-layers={JSON.stringify(layers)}>
  <noscript>
    <p class="p-8 text-text-muted">Interactive map requires JavaScript.</p>
  </noscript>
</div>

<!-- Layer toggle panel -->
<div id={`legend-${id}`} class="bg-surface border border-border p-4 mt-2">
  <h4 class="text-[0.8rem] tracking-widest uppercase text-accent mb-3">Layers</h4>
  <div class="space-y-2">
    {layers.map((layer) => (
      <label class="flex items-center gap-2 cursor-pointer text-sm text-text-muted hover:text-text transition-colors">
        <input type="checkbox" checked class="accent-accent" data-layer-name={layer.name} />
        <span class="w-3 h-3 rounded-full inline-block" style={`background: ${layer.color}`} />
        {layer.name}
      </label>
    ))}
  </div>
</div>

<script>
  import L from 'leaflet';
  import 'leaflet/dist/leaflet.css';

  document.querySelectorAll('[id^="map-"]').forEach(async (el) => {
    const mapEl = el as HTMLElement;
    const id = mapEl.id.replace('map-', '');
    const center = JSON.parse(mapEl.dataset.center!) as [number, number];
    const zoom = Number(mapEl.dataset.zoom);
    const layers = JSON.parse(mapEl.dataset.layers!) as Array<{ name: string; file: string; color: string }>;

    const map = L.map(mapEl.id).setView(center, zoom);

    L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
      attribution: '&copy; OSM &amp; CARTO',
      maxZoom: 19,
    }).addTo(map);

    const layerMap = new Map<string, L.GeoJSON>();

    for (const layerDef of layers) {
      try {
        const resp = await fetch(layerDef.file);
        if (!resp.ok) continue;
        const geojson = await resp.json();
        const geoLayer = L.geoJSON(geojson, {
          style: { color: layerDef.color, weight: 2, opacity: 0.8, fillOpacity: 0.15 },
        }).addTo(map);
        layerMap.set(layerDef.name, geoLayer);
      } catch {
        // GeoJSON file not available yet — skip silently during development
      }
    }

    // Layer toggle
    const legendEl = document.getElementById(`legend-${id}`);
    legendEl?.querySelectorAll('input[data-layer-name]').forEach((checkbox) => {
      const input = checkbox as HTMLInputElement;
      const name = input.dataset.layerName!;
      input.addEventListener('change', () => {
        const layer = layerMap.get(name);
        if (!layer) return;
        if (input.checked) {
          map.addLayer(layer);
        } else {
          map.removeLayer(layer);
        }
      });
    });
  });
</script>
```

- [ ] **Step 2: Write map pages**

Write `src/pages/map/index.astro`:

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import ContentCard from '../../components/ContentCard.astro';
import { getCollection } from 'astro:content';

const maps = await getCollection('maps');
---

<BaseLayout title="Interactive Maps" description="Explore Lahaina's spatial data through interactive GIS maps.">
  <section class="max-w-4xl mx-auto px-6 py-20">
    <div class="section-label">GIS Maps</div>
    <h1 class="section-title mb-4">Interactive Maps</h1>
    <p class="text-text-muted text-[0.92rem] leading-relaxed mb-12 max-w-2xl">
      Explore Lahaina's spatial data through interactive maps with toggleable layers.
    </p>

    <div class="grid gap-4">
      {maps.map((m) => (
        <ContentCard
          title={m.data.title}
          href={`/map/${m.id}`}
          description={m.data.description}
          label="Interactive Map"
          tags={m.data.tags.topic}
        />
      ))}
    </div>
  </section>
</BaseLayout>
```

Write `src/pages/map/[...slug].astro`:

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import MapViewer from '../../components/MapViewer.astro';
import TagPills from '../../components/TagPills.astro';
import Breadcrumbs from '../../components/Breadcrumbs.astro';
import { getCollection, render } from 'astro:content';

export async function getStaticPaths() {
  const maps = await getCollection('maps');
  return maps.map((m) => ({
    params: { slug: m.id },
    props: { map: m },
  }));
}

const { map } = Astro.props;
const { Content } = await render(map);

const sections = (await getCollection('sections')).filter((s) => map.data.relatedSections.includes(s.id));
const drawings = (await getCollection('drawings')).filter((d) => map.data.relatedDrawings.includes(d.id));
---

<BaseLayout title={map.data.title} description={map.data.description}>
  <section class="max-w-6xl mx-auto px-6 py-20" data-pagefind-body>
    <Breadcrumbs crumbs={[
      { label: 'Maps', href: '/map/' },
      { label: map.data.title },
    ]} />

    <div class="section-label">Interactive Map</div>
    <h1 class="section-title mb-4">{map.data.title}</h1>

    <TagPills topics={map.data.tags.topic} scales={map.data.tags.scale} />

    <div class="mt-8">
      <MapViewer
        id={map.id}
        center={map.data.defaultCenter}
        zoom={map.data.defaultZoom}
        layers={map.data.layers}
      />
    </div>

    <div class="prose mt-8">
      <Content />
    </div>

    {(sections.length > 0 || drawings.length > 0) && (
      <div class="mt-12 grid grid-cols-1 md:grid-cols-2 gap-8">
        {sections.length > 0 && (
          <div>
            <h3 class="text-[0.8rem] tracking-widest uppercase text-accent mb-4">Related Sections</h3>
            <ul class="space-y-2 list-none">
              {sections.map((s) => (
                <li><a href={`/read/${s.id}`} class="text-text-muted hover:text-text no-underline transition-colors">{s.data.title}</a></li>
              ))}
            </ul>
          </div>
        )}
        {drawings.length > 0 && (
          <div>
            <h3 class="text-[0.8rem] tracking-widest uppercase text-accent mb-4">Related Drawings</h3>
            <ul class="space-y-2 list-none">
              {drawings.map((d) => (
                <li><a href={`/drawing/${d.id}`} class="text-text-muted hover:text-text no-underline transition-colors">{d.data.title}</a></li>
              ))}
            </ul>
          </div>
        )}
      </div>
    )}
  </section>
</BaseLayout>
```

- [ ] **Step 3: Verify build**

```bash
npm run build
```

Expected: Map pages generated. Maps will show empty (no GeoJSON yet) but the Leaflet base map should load with the dark tile layer.

- [ ] **Step 4: Commit**

```bash
git add src/components/MapViewer.astro src/pages/map/
git commit -m "feat: add interactive GIS map pages with Leaflet and layer toggles"
```

---

## Task 13: Search with Pagefind

**Files:**
- Create: `src/pages/search.astro`, `src/components/SearchBar.astro`
- Modify: `astro.config.mjs` (add pagefind post-build)
- Modify: `package.json` (add postbuild script)

- [ ] **Step 1: Install Pagefind**

```bash
npm install -D pagefind
```

- [ ] **Step 2: Add postbuild script to package.json**

Add to `scripts` in `package.json`:

```json
"postbuild": "npx pagefind --site dist"
```

- [ ] **Step 3: Write search page**

Write `src/pages/search.astro`:

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout title="Search" description="Search all thesis content.">
  <section class="max-w-4xl mx-auto px-6 py-20">
    <div class="section-label">Search</div>
    <h1 class="section-title mb-8">Search the Thesis</h1>

    <div id="search-container" class="min-h-[400px]">
      <link href="/pagefind/pagefind-ui.css" rel="stylesheet" />
      <div id="search" />
    </div>
  </section>
</BaseLayout>

<script>
  async function initSearch() {
    const { PagefindUI } = await import('/pagefind/pagefind-ui.js');
    new PagefindUI({
      element: '#search',
      showSubResults: true,
      showImages: false,
    });
  }
  initSearch();
</script>

<style is:global>
  /* Override Pagefind UI to match dark theme */
  .pagefind-ui {
    --pagefind-ui-scale: 1;
    --pagefind-ui-primary: #c4a265;
    --pagefind-ui-text: #e8e8e8;
    --pagefind-ui-background: #141414;
    --pagefind-ui-border: #222222;
    --pagefind-ui-tag: #1a1a1a;
    --pagefind-ui-border-width: 1px;
    --pagefind-ui-border-radius: 2px;
    --pagefind-ui-font: Inter, -apple-system, sans-serif;
  }

  .pagefind-ui__search-input {
    background: #0a0a0a !important;
    color: #e8e8e8 !important;
  }

  .pagefind-ui__result-link {
    color: #c4a265 !important;
  }

  .pagefind-ui__result-excerpt {
    color: #999 !important;
  }
</style>
```

- [ ] **Step 4: Write SearchBar component for nav**

Write `src/components/SearchBar.astro`:

```astro
---
---

<a href="/search" class="text-text-muted hover:text-text transition-colors text-[0.8rem] font-medium tracking-widest uppercase no-underline" aria-label="Search">
  Search
</a>
```

- [ ] **Step 5: Verify build with Pagefind indexing**

```bash
npm run build
```

Expected: Build succeeds, then Pagefind runs and outputs index statistics (number of pages indexed).

- [ ] **Step 6: Commit**

```bash
git add src/pages/search.astro src/components/SearchBar.astro package.json
git commit -m "feat: add Pagefind search with dark theme styling"
```

---

## Task 14: 404 Page & Final Polish

**Files:**
- Create: `src/pages/404.astro`

- [ ] **Step 1: Write 404 page**

Write `src/pages/404.astro`:

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout title="Page Not Found">
  <section class="max-w-2xl mx-auto px-6 py-32 text-center">
    <div class="text-accent text-6xl font-serif mb-4">404</div>
    <h1 class="section-title mb-4">Page Not Found</h1>
    <p class="text-text-muted mb-8">The page you're looking for doesn't exist or has been moved.</p>

    <div class="flex justify-center gap-4 flex-wrap">
      <a href="/" class="px-6 py-3 bg-accent text-bg text-sm tracking-widest uppercase no-underline hover:opacity-90 transition-opacity">
        Go Home
      </a>
      <a href="/search" class="px-6 py-3 border border-border text-text-muted text-sm tracking-widest uppercase no-underline hover:text-text hover:border-[#333] transition-colors">
        Search
      </a>
    </div>
  </section>
</BaseLayout>
```

- [ ] **Step 2: Verify full build**

```bash
npm run build
```

Expected: Clean build, all pages generated, Pagefind index created.

- [ ] **Step 3: Commit**

```bash
git add src/pages/404.astro
git commit -m "feat: add 404 page with search and navigation links"
```

---

## Task 15: Full Build Verification & Dev Server Test

- [ ] **Step 1: Run full build**

```bash
npm run build
```

Expected: Clean build with no errors. Check output for number of pages generated.

- [ ] **Step 2: Run preview server**

```bash
npm run preview
```

Open `http://localhost:4321` and verify:
- Homepage renders with hero, entry points, abstract
- Navigation links work (Read, Topics, Scales, Drawings, Timeline, Search)
- `/read/` shows chapter list with section cards
- `/read/abstract` shows section with sidebar
- Previous/next navigation works between sections
- `/drawing/` shows drawings by scale
- `/topic/water` shows aggregated water content
- `/scale/regional` shows regional content with scale nav
- `/timeline` shows timeline events
- `/search` loads Pagefind and returns results
- `/map/water-systems-overlay` shows Leaflet map (base tiles load, layers may be empty)
- 404 page works for invalid URLs

- [ ] **Step 3: Final commit**

```bash
git add -A
git commit -m "chore: verify full build — all pages, search, and maps functional"
```

---

## Next Steps (Post-Plan)

After the site scaffold is built and working with seed content, the major remaining work is **content population** — extracting and converting the full thesis into markdown entries:

1. **Extract thesis text** from `thesis_v31.docx` → split into ~40-60 section markdown files
2. **Export figures** from SSD → copy to `src/assets/images/drawings/`
3. **Convert GIS shapefiles** → GeoJSON with mapshaper simplification
4. **Write all source entries** from the bibliography
5. **Write all term entries** from the glossary
6. **Write all timeline entries**
7. **Write all drawing entries** with proper image paths
8. **Write all topic and scale intro content**
9. **Tag everything** according to the taxonomy
10. **Download and self-host fonts** (Inter + EB Garamond WOFF2 files)
11. **Copy final thesis PDF** to `public/downloads/`

This content work is best done incrementally — add a few entries, build, verify, repeat.
