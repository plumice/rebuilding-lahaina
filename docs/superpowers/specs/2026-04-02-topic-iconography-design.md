# Topic Iconography System — Design Spec

**Date:** 2026-04-02
**Status:** Approved
**Scope:** 11 topic icons + style guide + Astro component + placement integration

---

## Design Philosophy

A custom SVG icon set rooted in Hawaiian visual traditions and the thesis's own concepts. Each icon derives its form from a specific element of the research — not generic symbols decorated with Hawaiian aesthetics, but visual arguments drawn from the thesis translated into a consistent symbol system.

The icons occupy the space between petroglyph abstraction and kapa pattern geometry: abstract enough to work at 16px, but with enough formal specificity (curve language, weight variation, asymmetry) to feel distinctly Hawaiian rather than generic.

---

## Style Guide

### Grid & Sizing

- Base canvas: 24x24px with 2px padding (20x20 active area)
- Three render sizes via CSS: 16px (tag pills), 24px (cards/inline), 48px (section headers)
- Each icon is a single SVG with `viewBox="0 0 24 24"`

### Stroke Language

- Stroke width: 1.5px (consistent across all icons)
- Stroke linecap: `round`
- Stroke linejoin: `round`
- No fills by default — stroke-only
- Corner radius on all angles: minimum 2px (organic warmth, no sharp technical corners)

### Color

- Default: `currentColor` (inherits from parent text color)
- Typical rendering: text-muted (#555555) in neutral state, accent (#6d5344) on hover/active
- Icons never introduce colors outside the existing palette

### Hawaiian Curve Language

What makes these icons *not* Feather/Lucide/generic:

- No perfectly straight horizontal/vertical lines — subtle organic variation in all strokes
- Curves reference natural forms: water flow, mountain ridgelines, wave patterns
- Asymmetry is permitted — not every icon requires bilateral symmetry (petroglyph influence)
- Weight distribution can vary subtly within an icon (thicker at base, thinner at tips) — hand-carved mark quality
- Rounded terminations on all strokes — no flat cut ends

---

## The 11 Icons

### 1. Water — `water.svg`
**Form:** Three parallel curved lines flowing top-left to bottom-right (mauka-to-makai direction), diverging as they descend.
**Source:** Ahupuaʻa water flow logic; stream patterns from GIS map; how mountain water fans across the coastal plain.

### 2. Fire — `fire.svg`
**Form:** Two asymmetric curves rising from a base point, leaning in the kauaʻula wind direction (mountain to coast).
**Source:** Wind-driven brushfire shape specific to the Lahaina event, not a campfire. References the kauaʻula wind from the West Maui mountains.

### 3. Coastal — `coastal.svg`
**Form:** Curved horizon line with wave crest below and subtle land contour above. Shoreline meeting water.
**Source:** Reef patterns from the aerial render; the SLR-XA boundary defining the coastal buffer zone.

### 4. Cultural Heritage — `cultural-heritage.svg`
**Form:** Abstracted hale roof profile — 45-degree pitch with ridge beam visible, sitting on two posts.
**Source:** The module system's hale translation; traditional Hawaiian structure form; the 45-degree roof pitch specified in the thesis.

### 5. Ecology — `ecology.svg`
**Form:** Native ʻulu (breadfruit) leaf — lobed form with 3-5 rounded divisions.
**Source:** Indigenous species present in the ahupuaʻa agricultural system. Species-specific, not generic.

### 6. Housing — `housing.svg`
**Form:** The 26x26 module footprint in plan view — a square with four corner columns marked as small circles.
**Source:** Directly from thesis drawings. The fundamental building unit of the recovery framework.

### 7. Infrastructure — `infrastructure.svg`
**Form:** Cross-section of the plantation ditch system — trapezoidal channel with a water line.
**Source:** Pioneer Mill irrigation network; central to the water crisis analysis.

### 8. Mobility — `mobility.svg`
**Form:** Y-shaped branching path — single line splitting into two routes, both connecting forward. No dead ends.
**Source:** Thesis argument about eliminating trap streets; the network diagram, not a vehicle.

### 9. Policy — `policy.svg`
**Form:** Overlapping rectangular forms suggesting land parcels with a dividing line.
**Source:** The Māhele land division; governance and regulation through the lens of Hawaiian land tenure history.

### 10. Recovery — `recovery.svg`
**Form:** Hapu'u fern fiddlehead unfurling — a spiral growth form.
**Source:** The hapu'u fern is one of the first plants to return after disturbance in Hawaiian forests. Regeneration without literalism.

### 11. Zoning — `zoning.svg`
**Form:** Horizontal bands stepping from narrow at top to wide at bottom — the four mauka-to-makai elevation zones.
**Source:** Topographic analysis elevation zones; the four-buffer framework (hinterland, peri-urban, urban, coastal).

---

## File Structure

```
public/icons/topics/
  water.svg
  fire.svg
  coastal.svg
  cultural-heritage.svg
  ecology.svg
  housing.svg
  infrastructure.svg
  mobility.svg
  policy.svg
  recovery.svg
  zoning.svg

src/components/
  TopicIcon.astro       # Component: renders inline SVG by topic name + size
```

---

## Astro Component

`TopicIcon.astro` accepts:
- `topic: string` — one of the 11 topic slugs
- `size: 'sm' | 'md' | 'lg'` — maps to 16px, 24px, 48px
- `class?: string` — optional additional CSS classes

Renders the SVG inline (not as `<img>`) so `currentColor` inheritance works. Icons are imported as raw SVG strings at build time — no runtime fetch.

---

## Placement

### Topic Index Page (`/topic/`)
- 48px icon positioned to the left of or above the topic title in each card
- Icon renders in accent color (#6d5344)

### Topic Detail Pages (`/topic/[tag]`)
- 48px icon next to the page h1 title

### Tag Pills (throughout the site)
- 16px icon before the topic text label inside tag pill components
- Icon inherits the pill's text color

### Content Cards (section listings, drawing listings)
- 24px icon in the card metadata area, identifying which topic the content belongs to

### Section Pages (`/read/[slug]`)
- 24px icons next to each topic tag in the tag area below the title

---

## Accessibility

- Each SVG includes `role="img"` and `aria-label="[Topic name] icon"`
- Icons are decorative when adjacent to text labels — use `aria-hidden="true"` in those contexts
- Sufficient contrast: icons inherit text color which already meets WCAG AA

---

## Not in Scope

- Scale icons (regional, town, district, node, site) — future phase
- Drawing type icons — future phase
- Animated icons — not appropriate for this site's tone
- Icon font — SVGs are superior for accessibility and color inheritance
