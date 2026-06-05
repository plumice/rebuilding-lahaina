---
name: thesis-content-audit
description: Use when modifying, reviewing, or auditing content in the Rebuilding Lahaina thesis website (src/content/) — including sections, sources, drawings, terms, timeline, maps, topics, scales. Encodes content-integrity rules from CODEX.md and the validated audit scripts. Apply whenever editing thesis prose, citation metadata, related-* arrays, image alt-text, tags, or external URLs.
---

# Thesis Content Audit

A consolidated reference for working on the `src/content/` of the
Rebuilding Lahaina thesis website (`/Volumes/T7 Shield/Projects/rebuilding-lahaina`).
Wraps the rules in `CODEX.md` with the validated audit tooling so any agent
working on this site can verify changes before committing.

## When to Use

Trigger this on:
- Any edit to a file under `src/content/`
- Any change to `relatedSections`, `relatedSources`, `relatedDrawings`,
  `relatedTerms`, `image:`, `alt:`, `tags:`, `chapter:`, `order:`
- Any addition of an external URL anywhere on the site
- Before committing content changes (run both audits)
- Receiving a request to "rewrite", "polish", "improve", or "sweep" thesis prose

**Do NOT use for:** layout / component / styling / build-pipeline changes.

## Iron Rules (from CODEX.md)

These are NON-negotiable. Violations of the letter are violations of the spirit.

1. **Canonical thesis lives in the T7 thesis project, not this repo.**
   Working canonical: `/Volumes/T7 Shield/ACADEMIC/masters_of_architecture/thesis_rebuilding_lahaina/01_writing/current/thesis_v32.docx`
   (byte-identical clone of v31 established 2026-05-18). v31 preserved
   as immutable baseline. Edits to v32 follow the structured Tier 0–G
   plan in `THESIS_FACTS/sources/v32_upgrade_targets.md`. Operational
   map: `THESIS_MAP.md` in the project root — READ FIRST before any v32
   work. Website section bodies should match v32 verbatim. Do NOT
   paraphrase, "improve", or directly insert paragraphs into v32 from
   website work — additions go through the Tier A–F upgrade pipeline.
   Drift between v32 and website is diagnosed with
   `python3 scripts/drift_audit.py`; resolution is handled deliberately
   in the thesis project, never by editing website prose to mask drift.
2. **No fabrication.** Do not invent facts, citations, statistics,
   precedents, or claims. Anything added must come from the thesis,
   from `thesis_source.txt`, or from the author's research files at
   `F:\ACADEMIC\masters_of_architecture\thesis_rebuilding_lahaina\`.
3. **No em-dashes (—) in content.** The author does not use them. Use
   commas, periods, or semicolons.
4. **"structures" not "homes"** — the thesis says "2,200 structures."
5. **Hawaiian diacriticals matter.** Preserve ʻokina (ʻ) and kahakō
   (ā, ē, ī, ō, ū) in all Hawaiian words: Mokuʻula, Nāhiʻenaʻena,
   ahupuaʻa, Kāʻanapali, Hawaiʻi, mālama ʻāina, loʻi kalo, kuleana.
6. **First-person voice is intentional, not editorial drift.** The thesis
   is partly first-person — methodology, scale-by-scale diagnostic,
   key-terms intro, buffer framework, and the dedication/acknowledgements.
   All 20 occurrences across 8 section files were verified verbatim against
   `thesis_source.txt` on 2026-05-16. Do not "sweep" or rewrite these.
   The site's third-person framing wraps thesis voice intentionally.

## Required Pre-Commit Validation

Run BOTH scripts before committing any content change. Both must pass.

```bash
python3 scripts/audit_xrefs.py     # xref + media integrity
python3 scripts/audit_sources.py   # citation metadata + URL liveness
```

**`audit_xrefs.py` checks:**
- Every `relatedSections/Sources/Drawings/Terms` ID resolves to a real file
- Every `image:`, `supportImages[].src`, `layers[].file` exists on disk
- Every `chapter:` is one of the 5 valid enum values
- Reports orphans (items with 0 inbound references)

**`audit_sources.py` checks:**
- All 48 sources have required fields: title, author, sourceType, relevance, tags{topic, type}
- Flags missing optional fields: publisher, date
- Sweeps every external URL (HEAD then GET, browser UA) for HTTP status
- Cross-references each source author/title against `thesis_source.txt`
- Allowlists known anti-bot 403s (FEMA, census.gov, landezine.com, etc.)

**Required pass state:**
- 0 broken cross-references
- 0 missing media
- 0 incomplete source metadata (required fields)
- 0 URLs needing fix (after anti-bot allowlist)
- 0 sources missing from thesis cross-reference

## Intentional Exceptions

Items audits will surface that are correct-as-is:

| Item | Why it's intentional |
|---|---|
| `sources/research-buffers`, `research-streams`, `research-zoning-breakdown` orphans | Three thesis pointers ("See thesis, §X, pp. Y–Z"). Don't wire them into sections. |
| `maps/water-systems-overlay` 1 orphan | Standalone route via `/map` |
| `timeline/*` 9 orphans | Standalone route via `/timeline` |
| 403 from `climate.hawaii.gov`, `data.census.gov`, `www.fema.gov`, `landezine.com`, `westmaui.wearemaui.org` | Anti-bot blocks; sites work in real browsers (verified 2026-05-17) |

## Schema Quick Reference

Drawn from `src/content.config.ts`. All collections require `tags.topic` (min 1).
Sections, drawings, maps also require `tags.scale` and `tags.type`.

| Collection | Required | Recommended |
|---|---|---|
| sections | title, chapter, order, summary, tags{topic,scale,type} | relatedDrawings, relatedSources, relatedTerms |
| drawings | title, image, alt, scaleLevel, drawingType, tags{topic,scale,type} | relatedSections, display.variant, supportImages |
| sources | title, author, sourceType, relevance, tags{topic,type} | publisher, date |
| terms | term, definition, category, tags{topic} | relatedSections |
| maps | title, description, layers, defaultCenter, defaultZoom, tags{topic,scale,type} | relatedSections, relatedDrawings |
| timeline | date, era, title, description, sortOrder, tags{topic} | relatedSections |
| topics | title, summary | — |
| scales | title, summary | — |

**Enum values:**
- topic: water, mobility, housing, coastal, cultural-heritage, zoning, fire, recovery, ecology, infrastructure, policy
- scale: regional, district, town, site, node
- type: analysis, proposal, precedent, data, documentation
- chapter: ch1-introduction, ch2-overview, ch3-analysis, ch4-principles, ch5-design
- sourceType: book, report, government-doc, research-note
- term category: concept, hawaiian, acronym

## Standard Citation Format

When adding a new source, format the frontmatter exactly:

```yaml
---
title: "Book or Article Title"
author: "Lastname, Firstname"           # Always "Last, First" for surname extraction
publisher: "Publisher Name"             # Don't mash date into this field
date: "YYYY" or "YYYY-YYYY"             # Separate field
sourceType: "book" | "report" | "government-doc" | "research-note"
relevance: "One sentence on why this source matters to the thesis."
tags:
  topic: [<one or more topic enum values>]
  type: [<one or more type enum values, usually 'precedent' or 'data'>]
relatedSections:
  - section-slug-1
  - section-slug-2
---

Body text — verbatim from the thesis if the source is discussed in the thesis;
otherwise a faithful summary of the source's relevance to the thesis argument.

## External Links

- [Canonical URL Title](https://example.com/path)
```

**Rules for external links:**
- Always include the link in a `## External Links` (sources) or `## Primary Sources` (sections) markdown section, not the frontmatter
- For dead links, find a Wayback snapshot or an authoritative alternative (architect's site, museum collection, government page) before removing
- Don't link to paywalled JSTOR/ScienceDirect/SpringerLink — use the publisher's free landing page or a Wikipedia article
- Don't link to PDFs unless they're permanently hosted (.gov, university .edu, archive.org)

## Common Mistakes

| Mistake | Why it's wrong | Correct approach |
|---|---|---|
| "Sweeping" first-person voice in literature-methodology or multi-scalar-diagnostic | All 20 first-person instances are verbatim thesis text | See Iron Rule #6; do nothing |
| Removing "I assembled this glossary" or "When I went to Hawaiʻi" | Verbatim thesis voice | Leave alone |
| Adding em-dashes for readability | Forbidden by CODEX.md | Use comma/period/semicolon |
| Writing "homes" for "structures" | Inaccurate; thesis says structures | Use "structures" |
| Adding `relatedSections` to one side without the other | Creates asymmetric refs | Update both files |
| Stripping a 403 URL from a source as "dead" | May be anti-bot, not dead | Verify in browser before removing; add host to KNOWN_ANTI_BOT_HOSTS if it works |
| Adding a new drawing without wiring it into a section | Creates an orphan | Append the drawing ID to at least one section's `relatedDrawings` |
| Spelling "Hawaii" without okina | Cultural respect failure | Use "Hawaiʻi" |

## Red Flags

If you find yourself doing any of these, STOP:

- "This first-person passage reads awkward, let me rewrite it" → verify in `thesis_source.txt` first; if verbatim, leave it
- "I'll polish this section's prose" → don't; section body is verbatim
- "This em-dash looks better here" → no
- "This URL returns 403, let me remove the citation" → verify with browser UA; check anti-bot allowlist
- "I'll just add this drawing without wiring it" → wire it, or delete it
- "I'll skip the audit, the change is small" → run both audits anyway; they're fast (~30s)

## Recovery Patterns

**Local working tree drifted from origin?** See PLAN.md for the 2026-05-16
reconciliation pattern: stash → cleanup macOS `._*` pollution → merge (NOT
rebase — rebase fails on this exFAT mount) → resolve content conflicts in
favor of origin (newer "the thesis" cleanup + orphan wiring), keep stash
as safety net until commit.

**Pages site returning 404?** Check `gh api repos/plumice/rebuilding-lahaina/pages`.
If 404, Pages was disabled. Re-enable with:
```bash
gh api repos/plumice/rebuilding-lahaina/pages -X POST -f build_type=workflow
gh api repos/plumice/rebuilding-lahaina/pages -X PUT -f cname=rebuildinglahaina.org
```
Then Cloudflare cache purge + set SSL/TLS mode to "Flexible" while GitHub
provisions the cert.

**macOS `._*` files polluting `.git/` or `src/content/`?**
```bash
find . -name '._*' -not -path './node_modules/*' -not -path './.astro/*' \
  -not -path './dist/*' -not -path './output/*' -not -path './.playwright-cli/*' \
  -delete 2>/dev/null
find .git -name '._*' -delete 2>/dev/null
```

## Bibliography of Validated State

As of 2026-05-17 (commit `d957079` + subsequent fixes):

- 29 sections (5 chapters: 3 + 4 + 8 + 5 + 9)
- 73 drawings
- 48 sources (3 intentional orphans documented above)
- 21 terms
- 1 map
- 9 timeline events
- 11 topics
- 5 scales
- 23 unique external URLs (19 OK, 4 anti-bot 403, 0 dead)
- 191 pages, 3665 words in Pagefind index

## Cross-References

- `CODEX.md` — full critical rules + stack details
- `PLAN.md` — open follow-ups, recovery patterns, historical context
- `STATUS.md` — last project status snapshot
- `thesis_source.txt` — extracted full thesis text for verbatim verification
- `scripts/audit_xrefs.py` — cross-reference + media audit (this file)
- `scripts/audit_sources.py` — citation + URL + thesis-ref audit
