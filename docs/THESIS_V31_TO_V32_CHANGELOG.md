# Thesis V31 → V32 Changelog

**Date:** 2026-05-18
**V31 path:** `/Users/akhil/Library/CloudStorage/OneDrive-Personal/THESIS/CURRENT WRITING/Thesis_V31.docx`
**V32 path:** `/Users/akhil/Library/CloudStorage/OneDrive-Personal/THESIS/CURRENT WRITING/Thesis_V32.docx`

V31 is the as-submitted Tulane M.Arch thesis (defended 2025). V32 is V31
with documented post-V31 author additions backfilled to keep the canonical
academic source in sync with the public website (`rebuildinglahaina.org`).

V31 is preserved unedited as the archival snapshot. V32 is the live
working copy and the new source of truth for content. Audit tooling
(`scripts/drift_audit.py`) compares the website's `thesis_source.txt`
against V32.

---

## What changed V31 → V32

### 4 substantive paragraphs inserted (verified author-written)

Each was identified by the 2026-05-17 drift audit as present on the
website (`thesis_source.txt`) but absent from V31. The author confirmed
each was written by him post-V31. They are inserted after the V31
anchor paragraph noted; V31 surrounding text is unchanged.

#### #1 — Water contamination (Sec 3D, after V31 ¶503)

> Negative pressure pulled combustion byproducts—volatile organic compounds
> including benzene—into water mains. The contamination extended beyond
> the burn zone through the interconnected distribution network, rendering
> potable water unsafe across broader service areas.

**Anchor:** Figure callout "F3. / Water System Failure Diagram — Lahaina
Water Distribution System (August 8, 2023)"

**Notes:** Adds the causal mechanism for the failure diagram. Verifiable
via Hawaii DOH unsafe-water advisories issued post-Lahaina-fire.

#### #2 — Pre-fire density analysis (Sec 3D, after V31 ¶660)

> Pre-fire Lahaina exhibited a dispersed residential pattern that achieved
> neither the efficiency of compact urbanism nor the fire-safety benefits
> of low-density separation. With 83% renters and fragmented multi-family
> pockets interspersed among single-family parcels and tourist
> accommodations, the town was structurally vulnerable—too dense to
> evacuate rapidly, too dispersed to defend collectively.

**Anchor:** "This whole situation put a lot of people at displacement
risk. It is usually way harder for renters..."

**Notes:** Improves analytical register; introduces the dispersed-density
diagnosis the design framework responds to.

#### #3 — Architectural lineage synthesis (Sec 3D, after V31 ¶787)

> This lineage—Amsterdam Orphanage, Gandhi Ashram, Hertzberger's schools,
> St. Xavier's—creates a coherent architectural foundation for the Lahaina
> Primary School. Each precedent demonstrates how educational and civic
> programs can be organized as a layered, resilient, and socially anchored
> field.

**Anchor:** "Purpose: Synthesizes the four precedents into a coherent
architectural lineage..."

**Notes:** Closes a hole in V31 where a synthesis paragraph was promised
("Purpose:" stub) but not delivered.

#### #4 — Hale Halawai framing specifications (Sec 3D, after V31 ¶823)

> F3. 49 / Hale Halawai Framing Schematic and Specification Table
> (HAR §15-110, p. 110-19). The table provides minimum structural member
> dimensions for assembly halls ranging from 12' × 20' to 30' × 60'. For
> the maximum 30' × 60' configuration: pou kihi (corner post) requires 6"
> minimum diameter, lohelau (wall plate) 4" diameter, kauhuhu (main ridge
> pole) 3" diameter, o'a (rafters) 4" diameter, with maximum post spacing
> of 5' and rafter spacing of 3' × 7'.

**Anchor:** "Across these precedents, several rules emerge: aggregation
rather than monumentality..."

**Notes:** Primary regulatory source citation (Hawaiʻi Administrative
Rules §15-110). Supports the peer-review-identified "most original
contribution" of the thesis (the hale/mat-building structural synthesis).

---

## What did NOT change V31 → V32

- All V31 prose is intact and unmodified.
- No figures were added, removed, or repositioned.
- No tables were modified.
- Bibliography and endnotes are unchanged.
- Page numbering and styles are inherited from V31.

The 77 smaller divergences listed in `docs/drift-audit/2026-05-18-v32-vs-website-drift.md`
(short glossary expansions, brief notes, table cells) remain as drift
between V32 and the website. They are queued for a future backfill or
website rollback decision.

---

## Reproducibility

```bash
# Re-extract V32 text
python3 -c "from docx import Document; d=Document('/Users/akhil/Library/CloudStorage/OneDrive-Personal/THESIS/CURRENT WRITING/Thesis_V32.docx'); print('\n'.join(p.text.strip() for p in d.paragraphs if p.text.strip()))" > /tmp/thesis_v32_extracted.txt

# Run drift audit (auto-extracts if needed)
python3 scripts/drift_audit.py
```

Both V31 and V32 are stored on OneDrive Personal and synced across the
author's machines. The original V31.docx hash (228.6 MB, 229,571,328
bytes; first paragraph "REBUILDING POST DISASTERS: LAHAINA") is the
unmodified archive copy.
