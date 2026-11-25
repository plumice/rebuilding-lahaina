# Thesis v33/v34 vs rebuildinglahaina.org: drift report

**Date:** 2026-10-25 · **Mode:** read-only audit. Nothing on the site or in the thesis was changed.
**Direction of truth:** thesis to website. Every replacement below is quoted from the thesis itself. Where the thesis has no corrected wording yet, the item says so and waits for the author; no replacement prose is proposed anywhere in this report.

## How to read this

- **Thesis quotes** come from the **v34 accepted view** (`01_writing/current/thesis_v34.docx`, all tracked changes treated as accepted, paragraph number `v34¶N`), with the matching line in `01_writing/xml_cache/v33/body_text.md` (`BT:N`). v34 is v33 plus the em dash pass and caption relabel, so the two usually differ only in punctuation (v33 has em dashes, v34 has commas/parentheses/colons). Where v34 also differs in wording, that is noted. v34 is still pending the author's accept.
- **Website locations** are `src/content/...:line` in `/Volumes/T7 Shield/04_CODE/rebuilding-lahaina/`. The working tree matches HEAD (`f381a2e`) for all content files, and a live spot-check on 2026-10-25 confirmed the deployed pages still carry the old text (e.g. `/read/fire-analysis/` still says "1,500 families have left Hawaiʻi entirely").
- **Justification** cites `THESIS_FACTS/audit/v32_fix_worklog.md` entry IDs (FIX n, AL-n, CI-x).
- **Drafted-sentence caveat.** `staging/v34/v34_author_items.md` section B lists thesis sentences that were drafted for the author in July and are flagged for him to rewrite (comments c27, c28, c31 to c34). Where a replacement depends on one of those, it is marked **[drafted, pending author rewrite]**.

## Summary

| # | Category | Findings | Website locations |
|---|---|---:|---:|
| 1 | Factual corrections (thesis corrected, site still old) | 22 | 78 |
| 2 | Content the thesis removed or retracted, still on the site | 5 | 9 |
| 3 | Bibliography / source-page entries the audit fixed | 9 | about 20 files |
| 4 | Formatting: em dashes | 144 `—` in 60 files + 72 ` -- ` in 29 files | 88 files |
| 4 | Formatting: figure caption label / numbering mismatches | 0 (site carries no figure numbers) | 0 |
| 5 | Stale or broken assets and page refs | 5 | 9 |
| 6 | On the site, not in the thesis (flag only) | 9 groups | many |
| T | Thesis-side open items found while auditing (site mirrors the thesis; nothing to change on the site until the thesis is settled) | 12 | 22 |

### Recommended review order (one small batch at a time)

1. **Renter share** (1.1): 8 locations, one sentence each.
2. **Out-of-state migration + "$3 billion" label** (1.2, 1.3, 2.2).
3. **Sea level rise framing and impact figures** (1.4, 1.5, 1.6).
4. **Fire chronology wording** (1.7 winds, 1.8 "damaged or destroyed").
5. **Recovery status updates** (1.11, 1.12; then 1.9 only after T8 is settled in the thesis).
6. **Water** (1.10 Stage 2 lifted, 1.13 Kahana Well, 2.3, 2.4, chart in 5.4).
7. **Precedent figures** (1.16 Broadmoor, 1.17 Lower Ninth Ward, 1.18 Kobe, 1.19 Yamuna, 1.20 soto de ribera).
8. **Regulatory labels** (1.15 County of Maui Rules §15-110, 1.14 capital date, 1.21 "ten or more units").
9. **Source pages** (category 3, one source file per item).
10. **Closer and nodes** (2.1 "Thank you."; 1.22 waits for the c33 rewrite).
11. **Assets** (5.1 PDF download decision, 5.3 broken SVGs, 5.2 page refs).
12. **Em dash sweep** last, per file, after content batches settle (category 4).

Hold every item listed under **T** until the author resolves it in the thesis.

### Top 10 factual findings

1. Renter share: site says "83% renter-occupied" / "More than 80 percent"; thesis now says 48% / "Nearly half" (1.1).
2. ">1,500 families have left Hawaiʻi entirely" rested on a citation the audit found does not exist; thesis now cites UHERO: 430 to 510 moved out of state (1.2).
3. SLR: site says the State report "projects 3.2 feet of rise by mid-century"; thesis now calls 3.2 ft the SLR-XA design standard reached in the latter half of the century, and adds the State's November 2025 move to 4 ft (1.4).
4. SLR impacts: site labels island-wide figures as West Maui / Lahaina and uses 780 / 1,600 / 2.2 miles; thesis body now says Maui island, 760 structures, 1,590 residents, more than 11 miles of Honoapiʻilani Highway (1.5).
5. SLR economic loss: site table says ">$1 billion"; thesis table says "$3.2 billion (Maui island)" (1.6).
6. Kahana Well: site presents it as "coming online early 2026"; thesis says the permit request was withdrawn (1.13, 2.3).
7. Stage 2 water shortage: site presents it as current; thesis notes it was lifted in March 2026 while the structural deficit persists (1.10).
8. Lower Ninth Ward / Broadmoor: site keeps "5,000 structures", "30–50 percent", "60 percent", "90 percent return by 2015"; thesis now reads ~4,800 households, ~30 percent, "the majority", ~74 percent by 2010 (1.16, 1.17).
9. Rebuild progress: site says "fewer than 200 are under construction" (early 2025); thesis now cites the June 2026 Recovery Dashboard: 572 permits, 310 under construction, 234 completed (1.11).
10. Fire damage and winds: site says "destroyed" / "burned" and "sustained winds"; thesis now says "damaged or destroyed" and "wind gusts ... (locally approaching 80)" (1.7, 1.8).

---

## 1. Factual corrections

### 1.1 Renter share (FIX 1, AL-11)
| Website | Current | Thesis replacement |
|---|---|---|
| `sections/buffer-framework.md:43`, `sections/design-interventions.md:35`, `sections/disaster-gentrification.md:37` | "Lahaina was 83% renter-occupied before the fire." | v34¶670 / BT:1285: "Lahaina was 48% renter-occupied before the fire, well above Maui County’s 35%." |
| `sections/fire-analysis.md:45`, `sections/history-of-lahaina.md:81` | "More than 80 percent of Lahaina's pre-fire residents were renters." | v34¶238 / BT:457: "Nearly half of Lahaina’s pre-fire residents were renters, a markedly higher share than Maui County overall. After the fire, renters made up roughly 89 percent of FEMA-assisted displaced residents. They lost possessions, housing, and without property ownership, any automatic claim to return." |
| `sections/literature-methodology.md:21` | "Lahaina's 80-percent renter population faces identical structural disadvantage." | v34¶299 / BT:578: "Lahaina’s renter population, nearly half of pre-fire households, faces identical structural disadvantage." |
| `topics/zoning.md:6` | "with 83% renters and fragmented housing interspersed among tourist accommodations" | v34¶922 / BT:1732: "With renters at roughly 48 percent of households and fragmented multi-family pockets interspersed among single-family parcels and tourist accommodations, the town was structurally vulnerable: too dense to evacuate rapidly, too dispersed to defend collectively." |
| `sources/census-lahaina.md:18` | "over 83% of Lahaina residents were renters before the fire" | Figure per v34¶670 (48%); vintage per fn50/fn159: "U.S. Census Bureau, American Community Survey 5-Year Estimates, 2018–2022, Lahaina CDP." See also 3.6. |

Note: v34¶238 drops the second em dash of "and—without property ownership—any" without adding a comma; quote it as it stands or let the author fix it in the thesis first.

### 1.2 ">1,500 families left Hawaiʻi" (FIX 4, CI-A, AL-3)
- `sections/fire-analysis.md:49`, `terms/fema-acronym.md:12`: "More than 1,500 families have left Hawaiʻi entirely."
- Thesis v34¶244 / BT:466 (fn294 UHERO + DoTax): "State tax-filing analysis indicates the fire reduced Maui’s population by at least 1,000 residents, with roughly 430–510 moving out of state entirely."
- Worklog: the DBEDT "Post-Disaster Migration Analysis" cite was found not to exist.

### 1.3 "$3 billion in federal aid" (FIX 7)
- `sections/fire-analysis.md:49`, `sections/disaster-gentrification.md:29`, `terms/fema-acronym.md:12`: "approximately $3 billion in federal aid allocated" → v34¶244 / BT:466: "approximately $3 billion in total federal support (FEMA and partner agencies) allocated."
- `sections/fire-analysis.md:63`, `terms/fema-acronym.md:14`: "Approximately $3 billion in federal aid committed." → v34¶251 / BT:480: "Approximately $3 billion in total federal support (FEMA and partner agencies) committed."
- `sources/fema-recovery.md:7` (relevance) and `:19` repeat "approximately $3 billion in federal aid".
- Thesis-side: the abstract (v34¶38) still says "approximately $3 billion in aid" (see T11).

### 1.4 SLR "3.2 feet by mid-century" (FIX 2 + Nov 2025 addendum)
- `sections/environmental-analysis.md:50`, `terms/slr-acronym.md:12`, `sources/sea-level-rise-report.md:17`: "projects 3.2 feet of rise by mid-century under current emissions trajectories."
- Thesis v34¶475 / BT:906: "The Hawaiʻi Sea Level Rise Vulnerability and Adaptation Report establishes 3.2 feet as the State’s Sea Level Rise Exposure Area (SLR-XA) design standard, the adopted regulatory benchmark for coastal planning, corresponding to a projection reached in the latter half of this century. In November 2025, the State updated its minimum planning scenario to 4 feet (DLNR Climate Commission, NR25-134)."

### 1.5 SLR impact figures mislabeled as Lahaina / West Maui (FIX 3)
- `sections/environmental-analysis.md:50`, `terms/slr-acronym.md:14`, `topics/coastal.md:6`, `sources/sea-level-rise-report.md:17`: "approximately 3,130 acres of West Maui coastal land face chronic flooding. Within Lahaina, 780 structures ... An estimated 1,600 residents ..."
- `sections/environmental-analysis.md:50` (end), `terms/slr-acronym.md:14`, `sources/post-fire-transport.md:16`: "Approximately 2.2 miles of major roadway, including segments of Front Street"
- Thesis v34¶475 / BT:906: "At 3.2 feet of rise, approximately 3,130 acres of Maui’s coastal land fall within the Sea Level Rise Exposure Area, with the greatest concentration of loss in West Maui. Across the island, roughly 760 structures (many in West Maui’s visitor and residential core, including structures that survived the fire) sit within the exposure area. An estimated 1,590 residents face displacement from flooding independent of fire-related damage. More than 11 miles of major coastal roadway, including segments of Honoapiʻilani Highway, would experience regular inundation."

### 1.6 SLR table, economic loss row (FIX 3, AL-5)
- `sections/environmental-analysis.md:56`: "| Economic Loss | >$1 billion |"
- Thesis table, v34¶485–486 / BT:929–931: "Economic Loss" / "$3.2 billion (Maui island)".
- Rows `:55` (780 structures) and `:57` (1,600 residents) match the thesis table, which itself still disagrees with its own body text (T4).

### 1.7 Winds (FIX 7)
- `sections/fire-analysis.md:21`, `sections/history-of-lahaina.md:57`, `timeline/wildfire-devastation.md:12`: "generating sustained winds exceeding 60 miles per hour"
- Thesis v34¶226 / BT:433: "generating wind gusts exceeding 60 miles per hour (locally approaching 80) across West Maui’s leeward slopes."

### 1.8 "Destroyed / burned" → "damaged or destroyed" (FIX 7)
- `src/pages/index.astro:83`: "destroyed more than 2,200 structures" → v34¶36 / BT:69: "damaged or destroyed more than 2,200 structures, the deadliest American wildfire in over a century."
- `sections/fire-analysis.md:43`, `sections/history-of-lahaina.md:79`, `timeline/wildfire-devastation.md:18`: "More than 2,200 structures burned." → v34¶237 / BT:455: "More than 2,200 structures were damaged or destroyed." (v34 also rewords the next sentence: "The historic core of Lahaina, which is Front Street, the commercial district, residential neighborhoods extending inland was destroyed in hours." This wording is new in v34, not in v33.)
- `timeline/wildfire-devastation.md:5` (description): "destroyed more than 2,200 structures" → same v34¶36 wording.
- `sections/multi-scalar-diagnostic.md:31`: "destroyed approximately 2,200 structures" → v34¶372 / BT:709: "damaged or destroyed approximately 2,200 structures".
- Not changed in the thesis, so leave: "The 2,200 destroyed structures" (v34¶274) and "matches structures destroyed" (v34¶375).

### 1.9 STR pledge date and Bill 9 (AL-2, FIX 6). Hold until T8 is settled
- `sections/fire-analysis.md:53`, `sections/disaster-gentrification.md:33`: "In August 2024, Maui County pledged to convert 7,000 units, a response to sustained pressure." → v34¶246 / BT:470: "In May 2024, Maui County pledged to convert 7,000 units a response to sustained pressure." (v34 lost the punctuation where the em dash was; v33 reads "units—a response".)
- `sections/fire-analysis.md:79`: "In August 2024, Maui County pledged to convert 7,000 short-term vacation rentals to long-term housing. The pledge followed sustained confrontation, not negotiation." → v34¶259: "In May 2024, Maui County pledged to convert 7,000 short-term vacation rentals to long-term housing. The pledge followed sustained confrontation, not negotiation. In December 2025 the pledge became law: Bill 9 (Ordinance 5909) phases out roughly 6,200 apartment-zoned short-term rentals in West Maui by January 2029, and then the remainder of the county by 2031." (v33 BT:496 wording differs slightly: "rentals—West Maui units by January 2029, the remainder of the county by 2031.")
- Why hold: in the thesis, changing the pledge to May makes the next sentence's "That same month ... $4 billion settlement" say May 2024, while v34¶262 says the settlement was "reached in August 2024". The site is currently internally consistent; copying v34¶246 would import the conflict.

### 1.10 Stage 2 water shortage now lifted (FIX 6)
- `sections/disaster-gentrification.md:31`, `sections/fire-analysis.md:51`: thesis adds, after "...rebuild destroyed homes.", v34¶245 / BT:468: "(The Stage 2 declaration was lifted in March 2026 after heavy rainfall temporarily improved reservoir levels; the structural supply deficit persists.)"
- `timeline/water-shortage.md:12` (same text as thesis 3D-a): thesis adds v34¶493 / BT:946: "(The Stage 2 declaration was lifted in March 2026 after heavy rainfall; the structural deficit documented here persists.)"
- `sections/module-system.md:44`, `drawings/module-water-performance.md:31`: "given West Maui's Stage 2 water shortage, which prevents processing of new water meters and restricts irrigation to one day per week." → v34¶1280 / BT:2421: "given West Maui’s structural water shortage; under the Stage 2 declaration (lifted March 2026), new water meters could not be processed and irrigation was restricted to one day per week." **[drafted, pending author rewrite: c34]**
- Also present-tense on the site with no thesis sentence to copy: `sections/water-crisis.md:19`, `drawings/water-system-data.md:37`, `drawings/existing-water-systems.md:22`, `topics/water.md:6` ("ongoing Stage 2"), `topics/policy.md:6`, `sources/stage2-water-shortage.md`. Author to word, or reuse the parenthetical above.

### 1.11 Homes under construction (FIX 6 addendum)
- `sections/fire-analysis.md:71`: "As of early 2025, fewer than 200 are under construction."
- Thesis v34¶255 / BT:488: "As of June 2026, the County’s Recovery Dashboard reported 572 rebuilding permits issued, 310 homes under construction, and 234 completed."

### 1.12 Insurance claims (FIX 6)
- `sections/fire-analysis.md:87`: "Insurance companies have paid over $2 billion in claims."
- Thesis v34¶262 / BT:504: "Insurance companies have paid over $2.6 billion in claims as of early 2025."

### 1.13 Kahana Well (FIX 6, candidate-sweep addendum)
- `terms/cwrm-acronym.md:14`, `timeline/kahana-well.md:12`: "The Kahana Well, coming online early 2026 with 0.96 MGD capacity, will reduce but not eliminate the deficit."
- Thesis v34¶509 / BT:978: "A proposed Kahana Well (0.96 MGD) was expected to reduce but not eliminate the deficit; the water-use permit request was subsequently withdrawn."
- See 2.3 (timeline entry titled "Kahana Well Online") and 2.4 (the 15.7% projection).

### 1.14 Royal capital date (FIX 11)
- `timeline/royal-capital.md:12`: "King Kamehameha III relocated the kingdom's capital to Lahaina in 1820"
- Thesis v34¶203 / BT:389: "The kingdom’s capital was relocated and established at Lahaina around 1820, and the town remained the seat of government until 1845." (v33 reads "was established"; "relocated and" is new in v34.)

### 1.15 "HAR §15-110" → "County of Maui Rules §15-110" (FIX 16)
- `drawings/hale-foundation-detail.md:14`, `drawings/hale-halawai-framing.md:14`, `drawings/hale-halawai-hip-alternate.md:14`, `drawings/hale-kaa-framing.md:14`, `drawings/module-core.md:14`, `drawings/module-isometric.md:28`, `sections/module-system.md:77`, `sources/indigenous-architecture-rules.md:18`, `terms/hale.md:10`, `terms/hale.md:18`
- Thesis v34¶1107 / BT:2084: "as defined in Maui County’s Indigenous Hawaiian Architecture regulations (County of Maui Rules §15-110)". Captions: "Figure 3.49: Hale Halawai Framing Schematic and Specification Table (County of Maui Rules §15-110, p. 110-19)".
- Worklog: HAR denotes State rules; this is a County DPW rule.

### 1.16 Broadmoor return rate (FIX 17)
- `sections/resilience-drivers.md:17`, `sections/literature-methodology.md:23`, `sources/coming-home-new-orleans.md:18`: "achieved 90 percent return by 2015"
- Thesis v34¶283 / BT:546 and v34¶300 / BT:580: "achieved approximately 74 percent return by 2010"

### 1.17 Lower Ninth Ward / Road Home (FIX 23, FA-2, FA-3)
- `sections/resilience-drivers.md:17`, `sections/disaster-gentrification.md:17`, `sources/disaster-inc.md:21`: "lost 5,000 structures" → "lost roughly 4,800 households" (v34¶283 / BT:546; v34¶317 / BT:614)
- Same files plus `sections/literature-methodology.md:21`: "by 30–50 percent" → "by approximately 30 percent" (v34¶283, ¶299, ¶317)
- `sections/resilience-drivers.md:17`: "Renters, 60 percent of the city's displaced population, received no equivalent program." → v34¶283: "Renters, the majority of the city’s displaced population, received no equivalent program."
- `sections/disaster-gentrification.md:17`: "Renters, 60 percent of the city's displaced, received nothing equivalent." → v34¶317: "Renters, the majority of the city’s displaced, received nothing equivalent."

### 1.18 Kobe (FIX 18)
- `sections/resilience-drivers.md:19`: "rebuilt 125,000 housing units within five years, an output rate..."
- Thesis v34¶284 / BT:548: "rebuilt 125,000 housing units within roughly three years under the Hyogo Phoenix Plan, an output rate that Lahaina’s current permitting structure cannot approach." (Thesis also ends the paragraph "proposed in Section 3D." where the site says "proposed in this thesis.")

### 1.19 Yamuna length (FIX 24)
- `sections/literature-methodology.md:31`, `sources/yamuna-river-project.md:20`: "the 22-kilometer stretch"
- Thesis v34¶305 / BT:590: "the roughly 24-kilometer stretch of river bisecting New Delhi"

### 1.20 "Soto de Ribera" (FIX 22)
- `sources/el-parque-del-agua.md:19`: "The Soto de Ribera, a white poplar riparian corridor wrapping the site, functions as a "Silver Forest of origin""
- Thesis v34¶303 / BT:586: "The soto de ribera, a white poplar riparian corridor wrapping the site, as the “Silver Forest of origin”" (lowercase, italic in the docx). The thesis sentence has lost its verb; the site's "functions as" is grammatical. Change only the capitalisation, or let the author fix the thesis sentence first (T10).

### 1.21 Inclusionary threshold (FIX 9)
- `sections/buffer-framework.md:43`, `sections/design-interventions.md:35`, `sections/disaster-gentrification.md:37`: "in any project exceeding ten units"
- Thesis v34¶670 / BT:1285: "in any project of ten or more units"

### 1.22 Three hubs vs eight nodes (FIX 12a/12b/12c). Hold for the author's rewrite
- `sections/hub-operations.md:5,15,37–41`, `sections/redensification-hubs.md:5,21`, `sections/community-anchors.md:19`, `drawings/hub-typology-matrix.md:14`: three hubs; `hub-operations.md:39` "If one hub is damaged or overwhelmed, the other two maintain coverage."
- Thesis v34¶989 / BT:1858: "Deployed across the town, these three typologies yield eight nodes..." **[drafted, pending author rewrite: c33; still carries an em dash on hold in v34]**. Compass fix v34¶988 / BT:1856: "if the northern hub is compromised, the eastern hub sustains coverage."

---

## 2. Content the thesis removed or retracted

| # | Website | What | Thesis status |
|---|---|---|---|
| 2.1 | `sections/contribution.md:29` | Closing line "Thank you." | Removed (worklog Stage 3, "4B closer"). Replacement closing paragraph v34¶1394 / BT:2615: "By holistically targeting these systemic weaknesses through scalable, site-specific interventions, the model challenges conventional, fragmented disaster-recovery paradigms and sets a new footprint for urban resilience, adaptation, and post-disaster recovery. Lahaina’s recovery is still unfolding; this framework is offered not as a finished blueprint but as a replicable methodology, one whose next steps run through publication, community engagement, continued module development, and testing against the next place that has to rebuild." The site's 4B has no equivalent paragraph. |
| 2.2 | `sections/fire-analysis.md:49`, `terms/fema-acronym.md:12` | "More than 1,500 families have left Hawaiʻi entirely." | Retracted (fabricated DBEDT citation). Replacement in 1.2. |
| 2.3 | `timeline/kahana-well.md:2–5,12` | Timeline event "Kahana Well Online", era "2026 (Projected)" | Premise withdrawn (v34¶509). The event did not happen; whether the entry stays is an author call. |
| 2.4 | `sections/water-crisis.md:21`, `drawings/water-system-data.md:35`, `public/images/drawings/derived/water-deficit-chart.svg` (live) | "deficit would only reduce to approximately 15.7%" with Kahana Well "projected 2026" | 15.7% is not in v33/v34, and the well premise is withdrawn. No thesis replacement. |
| 2.5 | `sources/post-fire-transport.md`, `sources/kenneth-frampton-correa.md` | Source pages for citations the audit removed from the bibliography | See 3.2 and 3.3. |

---

## 3. Bibliography and source pages

| # | Website | Current | Thesis (v33 5B bibliography, unchanged in v34) | Worklog |
|---|---|---|---|---|
| 3.1 | `sources/after-great-disasters.md:2` | "...How Six Communities Managed Recovery" | "Johnson, Laurie A., and Robert B. Olshansky. After Great Disasters: An In-Depth Analysis of How Six Countries Managed Community Recovery. Cambridge, MA: Lincoln Institute of Land Policy, 2017." (Year 2017 on the site is already right.) | FIX 18 |
| 3.2 | `sources/kenneth-frampton-correa.md:2–5` | Frampton, Perennial Press, 2000 | Row deleted as a duplicate of "Correa, Charles. Charles Correa. London: Thames & Hudson, 1996." (already `sources/charles-correa.md`) | CI-C, Stage 4 |
| 3.3 | `sources/post-fire-transport.md:2–5` | "Preliminary Post-Fire Transportation Assessment, West Maui", HDOT 2024 | No such document found. v33 row: "State of Hawaiʻi Department of Transportation. West Maui Wildfire Response and Highway Projects Documentation. 2023–2024." Body text also carries the old "2.2 miles ... Front Street" figure (1.5). | CI-A, Stage 4 |
| 3.4 | `sources/managing-catastrophes.md:2` | "Managing Natural Catastrophes" | "Reissberg, Anja Christina. Managing Natural Catastrophies: Viable Systems to Prevent Human Tragedy—The Hawaiʻian Example. Frankfurt: Campus Verlag, 2013." (The dash is part of the published title; v34 author item D row 221.) | CI-B |
| 3.5 | `sources/indigenous-architecture-rules.md:3,18`; `terms/hale.md:18` | Author "County of Maui Department of Public Works"; "HAR Chapter 15-110"; hale.md links "HAR Chapter 15-110" to `https://www.capitol.hawaii.gov/` (State legislature) | "County of Maui Department of Public Works and Environmental Management. “Rules Pertaining to Indigenous Hawaiian Architecture Structures.” Chapter 15-110. Adopted April 2, 2004." Worklog BL lists the County DocumentCenter copy (DID 4434); exact URL [UNVERIFIED — needs source]. | FIX 16, BL |
| 3.6 | `sources/census-lahaina.md:5,18`; `sections/abstract.md:24` | ACS "2019-2023" | Footnotes standardized to 2018–2022 (fn2: "U.S. Census Bureau, American Community Survey 5-Year Estimates, 2018–2022, Lahaina CDP"). Bibliography row reads "2018–2022, 2019–2023". | FIX 1, ACS standardization |
| 3.7 | `sources/sea-level-rise-report.md:5,7` | date "2017, updated 2023"; relevance "provides the 3.5-foot and 6-foot planning thresholds" | "Hawaiʻi Climate Change Mitigation and Adaptation Commission. Hawaiʻi Sea Level Rise Vulnerability and Adaptation Report. Honolulu: State of Hawaiʻi, 2017. Updated 2022, 2023." The thesis uses 3.2 ft (SLR-XA) and 4 ft (Nov 2025); "3.5-foot and 6-foot thresholds" appears nowhere in the thesis. | FIX 2 |
| 3.8 | `sources/steps-to-water.md`, `back-to-future-caves.md`, `under-maui-roof.md`, `resilience-thinking.md`, `managing-catastrophes.md`; Machado & Silvetti in `src/components/diagrams/ResilienceDriversDiagram.astro:27` | Presented as thesis sources | These six are the thesis's uncited bibliography rows; keep-or-cut decision pending (comment c36). Site follows whatever the author decides. | Stage 4 c36 |
| 3.9 | several | Metadata precision only: `disaster-inc.md`, `resilience-stability.md`, `mat-building.md`, `van-eyck-configurative.md` typed "book" but the thesis cites journal articles (e.g. "Perspectives on Politics 10, no. 3 (2012): 633–646"); `back-to-future-caves.md` and `under-maui-roof.md` lack the subtitles in the thesis rows | Low priority | n/a |

---

## 4. Formatting sync

**Figure captions and numbering.** The site carries no figure numbers or "Figure N.N:" labels anywhere in `src/` (searched content, pages, components). There is nothing to relabel to the v34 `Figure N.N: Title` format and no numbering to mismatch. Drawing pages use their own titles (e.g. "Coastal Buffer Map"). Mapping drawing pages to v34 figure numbers would be a new task and should wait for the thesis renumbering pass.

**Em dashes.** Total: **144 `—` in 60 files**, plus **72 spaced double hyphens ` -- ` used as dashes in 29 files** (sources and terms). By area: content prose 113 `—` in 47 files; page/layout/component chrome 26 in 11 files (several are title or label separators, e.g. the footer byline); derived SVG charts 5 in 2 files.

| File | — | ` -- ` |
|---|---:|---:|
| `public/images/drawings/derived/lahaina_principles_prefire.svg` | 4 | 0 |
| `public/images/drawings/derived/water-zones-diagram.svg` | 1 | 0 |
| `src/components/Footer.astro` | 1 | 0 |
| `src/components/MapViewer.astro` | 1 | 0 |
| `src/content/drawings/buffer-coastal.md` | 1 | 0 |
| `src/content/drawings/buffer-framework-diagram.md` | 4 | 0 |
| `src/content/drawings/buffer-periurban.md` | 2 | 0 |
| `src/content/drawings/buffer-riparian.md` | 2 | 0 |
| `src/content/drawings/diagnostic-overlay.md` | 3 | 0 |
| `src/content/drawings/existing-water-systems.md` | 3 | 0 |
| `src/content/drawings/historical-timeline.md` | 8 | 0 |
| `src/content/drawings/housing-typologies.md` | 2 | 0 |
| `src/content/drawings/hub-typology-matrix.md` | 3 | 0 |
| `src/content/drawings/lahaina-base-map.md` | 2 | 0 |
| `src/content/drawings/module-assembly.md` | 2 | 0 |
| `src/content/drawings/module-connections.md` | 1 | 0 |
| `src/content/drawings/module-core.md` | 1 | 0 |
| `src/content/drawings/module-solar-performance.md` | 1 | 0 |
| `src/content/drawings/proposed-green-infrastructure.md` | 2 | 0 |
| `src/content/drawings/regional-rainfall.md` | 1 | 0 |
| `src/content/drawings/regional-topography.md` | 1 | 0 |
| `src/content/drawings/school-aerial-render.md` | 2 | 0 |
| `src/content/drawings/school-floor-plan.md` | 4 | 0 |
| `src/content/drawings/water-capture-network.md` | 1 | 0 |
| `src/content/drawings/water-collection-principles.md` | 2 | 0 |
| `src/content/drawings/water-system-data.md` | 4 | 0 |
| `src/content/drawings/water-zones-mauka-makai.md` | 1 | 0 |
| `src/content/scales/node.md` | 2 | 0 |
| `src/content/scales/regional.md` | 1 | 0 |
| `src/content/scales/site.md` | 3 | 0 |
| `src/content/scales/town.md` | 3 | 0 |
| `src/content/sections/cultural-heritage-strategy.md` | 1 | 0 |
| `src/content/sections/environmental-analysis.md` | 13 | 0 |
| `src/content/sources/after-great-disasters.md` | 0 | 1 |
| `src/content/sources/aldo-van-eyck.md` | 0 | 2 |
| `src/content/sources/architectural-style-book.md` | 0 | 1 |
| `src/content/sources/charles-correa.md` | 0 | 2 |
| `src/content/sources/coming-home-new-orleans.md` | 0 | 1 |
| `src/content/sources/cwrm-aquifer.md` | 0 | 2 |
| `src/content/sources/disaster-inc.md` | 0 | 4 |
| `src/content/sources/el-parque-del-agua.md` | 2 | 4 |
| `src/content/sources/indigenous-architecture-rules.md` | 0 | 2 |
| `src/content/sources/maui-last-hawaiian.md` | 0 | 1 |
| `src/content/sources/no-makou-ka-mana.md` | 0 | 5 |
| `src/content/sources/rainfall-atlas.md` | 0 | 1 |
| `src/content/sources/sea-level-rise-report.md` | 0 | 2 |
| `src/content/sources/shock-doctrine.md` | 0 | 3 |
| `src/content/sources/space-and-learning.md` | 0 | 1 |
| `src/content/sources/stage2-water-shortage.md` | 0 | 2 |
| `src/content/sources/steps-to-water.md` | 0 | 1 |
| `src/content/sources/urban-water-plan.md` | 0 | 2 |
| `src/content/sources/west-maui-community-plan.md` | 0 | 2 |
| `src/content/sources/wsp-highway-survey.md` | 0 | 2 |
| `src/content/sources/yamuna-river-project.md` | 0 | 4 |
| `src/content/terms/ahupuaa.md` | 0 | 5 |
| `src/content/terms/cwrm-acronym.md` | 0 | 5 |
| `src/content/terms/dlnr-acronym.md` | 0 | 1 |
| `src/content/terms/hale.md` | 0 | 4 |
| `src/content/terms/ltrp-acronym.md` | 0 | 1 |
| `src/content/terms/mauka.md` | 0 | 1 |
| `src/content/terms/slr-acronym.md` | 0 | 7 |
| `src/content/terms/wui-acronym.md` | 0 | 3 |
| `src/content/timeline/ahupuaa-system.md` | 3 | 0 |
| `src/content/timeline/aquifer-designation.md` | 4 | 0 |
| `src/content/timeline/kahana-well.md` | 1 | 0 |
| `src/content/timeline/mill-closure.md` | 2 | 0 |
| `src/content/timeline/pioneer-mill.md` | 2 | 0 |
| `src/content/timeline/royal-capital.md` | 2 | 0 |
| `src/content/timeline/statehood.md` | 2 | 0 |
| `src/content/timeline/water-shortage.md` | 3 | 0 |
| `src/content/timeline/wildfire-devastation.md` | 5 | 0 |
| `src/content/topics/coastal.md` | 1 | 0 |
| `src/content/topics/cultural-heritage.md` | 2 | 0 |
| `src/content/topics/ecology.md` | 1 | 0 |
| `src/content/topics/housing.md` | 1 | 0 |
| `src/content/topics/infrastructure.md` | 1 | 0 |
| `src/content/topics/mobility.md` | 3 | 0 |
| `src/content/topics/water.md` | 1 | 0 |
| `src/content/topics/zoning.md` | 1 | 0 |
| `src/layouts/BaseLayout.astro` | 1 | 0 |
| `src/layouts/SectionLayout.astro` | 5 | 0 |
| `src/pages/drawing/index.astro` | 1 | 0 |
| `src/pages/index.astro` | 7 | 0 |
| `src/pages/read/index.astro` | 5 | 0 |
| `src/pages/scale/index.astro` | 1 | 0 |
| `src/pages/source/index.astro` | 2 | 0 |
| `src/pages/timeline.astro` | 1 | 0 |
| `src/pages/topic/[tag].astro` | 1 | 0 |

Note: most `sections/*.md` already had their em dashes stripped in an earlier site pass (only 2 section files still carry them). Where the category 1 replacements land, using the v34 wording quoted above brings the matching v34 punctuation with it.

---

## 5. Stale assets and page references

| # | Item | Finding |
|---|---|---|
| 5.1 | "Download Full Thesis (PDF)" link, `src/components/Footer.astro:12` → `/downloads/final_as_thesis.pdf` | **Returns HTTP 404 on rebuildinglahaina.org** (checked 2026-10-25). The local `public/downloads/final_as_thesis.pdf` is gitignored, so it never deploys. It is byte-identical (SHA-256 `ea6abe12…6ffb7`) to `09_deliverables/final_pdfs/final_as_thesis.pdf`, which THESIS_MAP labels an out-of-date snapshot: a 36-page, 17×11 in InDesign export dated 2024-12-09, i.e. pre-audit. No PDF of v33 or v34 exists yet. Decision for the author: hide the link, or wait for a v34 PDF. |
| 5.2 | `sources/research-buffers.md:17` "§3C Design Principles, pp. 48–58"; `sources/research-streams.md:17` "§3B Regional Scale, pp. 44–45"; `sources/research-zoning-breakdown.md:17` "§3D Systems, pp. 76–79" | Section names still match v33/v34 headings (3B Regional Scale, 3C Design Principles, 3D Systems). The page numbers point at an older pagination; v34 page numbers are [UNVERIFIED — needs a rendered v34 PDF]. Book page ranges on `sources/hawaiian-kingdom.md` and `sources/feathered-gods-fishhooks.md` match thesis fn36–38. |
| 5.3 | Committed drawing pages point at SVGs that are untracked locally and 404 live: `drawings/displacement-analysis.md:8` → `derived/displacement-numbers.svg`; `:11` → `final_ppt_cropped/Slide45.JPG`; `drawings/buffer-coastal.md:8` → `derived/sea-level-rise-chart.svg`; `drawings/redensification-plan.md:8` → `derived/redensification-chart.svg`; `drawings/module-water-performance.md:8` → `derived/module-water-yield.svg` | Broken images on the live site. Content note: `displacement-numbers.svg` prints "83% renters" and "1,500+ families relocated off-island permanently"; `module-water-yield.svg` prints "Stage 2 Water Shortage prevents new water meters". If these are ever committed they need the category 1 corrections first. |
| 5.4 | `public/images/drawings/derived/water-deficit-chart.svg` (tracked, live) | Prints "Stage 2 Water Shortage (Sept 2025)" and "With Kahana Well (projected 2026) ~5.09 MGD still ~15.7% short". Stale per 1.10, 1.13, 2.4. |
| 5.5 | `public/images/drawings/derived/figure_3_1_multi_scalar_framework_fixed.svg`, `figure_3_26_water_system_performance_drought_flood.svg` | Not linked from any page but publicly reachable (HTTP 200). Same filename family as files the 2026-08-31 provenance triage (`02_figures/register_2026-08-31/provenance/`) marked machine-generated; hashes differ from the thesis working files, so not confirmed identical. Flag for the author. |

---

## 6. On the site but not in the thesis (flag only, no judgement)

1. **Abstract.** `sections/abstract.md:15–19` ("revealed critical vulnerabilities...", "Currently there is no clear route map...") is not the thesis abstract (v34¶36–40, "1C / Abstract"). Neither v31 nor v33 contains "no clear route map".
2. **Whole sub-sections with no thesis counterpart** (paragraph-similarity check, below 0.6 against v33; heuristic, some are rewordings): `mobility-street-design.md` (18 paragraphs), `hub-operations.md` (12: Hub 1/2/3 programs, "200-300 students", "200+ people"), `water-system-zones.md` (8), `school-design-detail.md` (7), `literature-methodology.md` (6), `water-crisis.md` (6), `district-typologies.md` (5: "Boulevard District", "Riparian Edge District"; the thesis keeps only "Coastal Edge District" at v34¶988), `redensification-hubs.md` (4), `community-anchors.md:17` (Medellín Library Parks, Singapore Park Connector Network). Across all content: 339 of 610 long paragraphs scored below 0.6; 169 match the thesis near-verbatim.
3. **Hub names** `drawings/hub-typology-matrix.md:18–20`: "Lahaina Luna Park", "Kahoma Health Campus", "Coastal Neighborhood Center". Not in the thesis.
4. **Numbers not found in v33**: "15.7%" (2.4); "2,200 homes" destroyed (`drawings/displacement-analysis.md:9,21,25`, `topics/fire.md:6`, `topics/housing.md:6`; thesis says structures); "3,200 total unit shortfall" and "+60% property value" (`displacement-analysis.md`); "6,941 approved Individual Assistance applications" (`terms/fema-acronym.md:18`); years 1802, 1823, 1834, 1901 (`drawings/historical-timeline.md`); "5,000 feet" (`drawings/regional-topography.md`); "468 feet" (`drawings/school-sections.md`); "2028" (`sources/water-usage-forecast.md`).
5. **Source pages with no matching v33 bibliography row**: `sources/post-event-mobility.md` (Maui County Office of Recovery, "Post-Event Mobility and Evacuation Analysis", 2024), `sources/maui-transportation.md`, `sources/lsb-classifications.md`, `sources/fema-recovery.md` (a FEMA/EPA composite; the thesis has separate FEMA and EPA rows), `sources/research-buffers.md`, `research-streams.md`, `research-zoning-breakdown.md` (the thesis self-cites use different titles, e.g. "Singh, Akhil. Buffer Framework Analysis. 2024."). Existence of the first one is [UNVERIFIED — needs source].
6. **Mokuʻula note** `sections/cultural-heritage-strategy.md:41`: "Friends of Mokuʻula was dissolved circa 2017; the work continues under the Lahaina Restoration Foundation". The thesis now cites the County "Lahaina Royal Complex Master Plan (planning process). 2025–." for this.
7. **Site-generated charts** (`public/images/drawings/derived/*.svg`): text is site-authored, not thesis figures.
8. **Site-only Stage 2 paragraph** `sections/water-crisis.md:19` ("explicitly stated that new or additional water service in West Maui cannot currently be processed").
9. **West Maui Community Plan source page** `sources/west-maui-community-plan.md:19` repeats "Goal 2.1.5" (see T5).

---

## T. Thesis-side items (site mirrors the thesis; resolve in the thesis first)

| # | Thesis (v34 accepted) | Site locations that mirror it | Note |
|---|---|---|---|
| T1 | "more than 80 percent" / "over 80 percent" renters at v34¶37, 220, 268, 274, 319 | `sections/zoning-analysis.md:15,19`, `sections/history-of-lahaina.md:45`, `timeline/statehood.md:14`, `sections/disaster-gentrification.md:21`, `sections/literature-methodology.md:47`, `sections/fire-analysis.md:99` | v34 author item A1; no corrected wording yet. |
| T2 | v34¶670 "Over 1,500 families have already relocated off-island permanently." (fn160 DBEDT) | `buffer-framework.md:43`, `design-interventions.md:35`, `disaster-gentrification.md:37` | Author item A2. |
| T3 | v34¶672 "3.2 feet of sea level rise under NOAA intermediate projections to 2100" | `drawings/buffer-coastal.md:22` | Author item A3 (AL-7). |
| T4 | SLR table rows 780 structures / 1,600 residents (v34¶483, 489) vs body 760 / 1,590 (v34¶475) | `sections/environmental-analysis.md:55,57` | Internal inconsistency after FIX 3. |
| T5 | Body still cites "Goal 2.1.5" and "Goals 2.1.1 through 2.1.3" (v34¶257, 270, 491); footnotes now say Goal 2.1 "Ready and Resilient Systems" | `sections/zoning-analysis.md:21`, `sections/fire-analysis.md:75,103`, `sections/environmental-analysis.md:59`, `terms/slr-acronym.md:16`, `sources/west-maui-community-plan.md:19` | FIX 8 applied to footnotes only. |
| T6 | Body "Ka Koʻo Maui" (v34¶259); bibliography and fn59 "Kākoʻo Maui" | `sections/fire-analysis.md:81` | CI-B applied to citations only. |
| T7 | Body "The Maui Long-Term Recovery Plan" (v34¶256); bibliography consolidated to "Lahaina Long-Term Recovery Plan" | `sections/fire-analysis.md:73`, `terms/ltrp-acronym.md:12` | CI-C applied to citations only. |
| T8 | v34¶246 May 2024 pledge + "That same month ... $4 billion settlement" vs v34¶262 settlement "reached in August 2024" | 1.9 | Date conflict introduced by AL-2. |
| T9 | v34¶246 "7,000 units a response to sustained pressure" | 1.9 | Em dash removed with no punctuation in its place. |
| T10 | v34¶303 "The soto de ribera, ..., as the “Silver Forest of origin”" (no verb) | 1.20 | Grammar. |
| T11 | Abstract v34¶38 still "approximately $3 billion in aid" | none (site abstract differs) | FIX 7 relabel not applied here. |
| T12 | Bibliography still lists Alday & Gupta, "Urban Hydrology," ANU Press 2014 (v34 bibliography) | none | AL-10 found this chapter does not exist. |

---

## Method and tooling

- Sources read: THESIS_MAP.md; v33 `body_text.md` and `word/footnotes.xml` (accepted view); `v32_fix_worklog.md`; `staging/v34/` (author items, em dash review, caption review, drawing mapping); v34 `word/document.xml` read in place (accepted view) to quote current thesis wording.
- `scripts/verify_claims.py` was copied to the session scratchpad and pointed at v33 `body_text.md` for every content folder (repo copy untouched). `scripts/drift_audit.py` was not run: it is built around `thesis_source.txt` section headers and a v32 docx; a scratch paragraph matcher against v33 was used instead for category 6.
- Live checks were HTTP HEAD/GET only (download link, derived SVGs, one page).
- Nothing in the repo, the thesis folder, or any .docx was modified. This file is the only write.
