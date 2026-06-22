# Session Log / Chat Backup — Odyssey Ticketing Project

> Durable backup of the working session(s) for this project. Captures the conversation
> arc, decisions, and any content that exists only in chat (not yet synced to Notion).
> Companion to `README.md` (the project snapshot). **Backed up: 2026-06-13.**

Notion master index: https://app.notion.com/p/37982ef1230e8150a87ae2c854e69b5a

---

## Session arc (what was done, in order)

1. **Kickoff** — analyze Fandango/AMC/IMAX ticketing for the Odyssey fiasco; find flaws; propose
   solutions; sync to Notion (workspace plumice.backend@gmail.com).
2. **Phase 1 research + Notion build** — created the hub + Case Study, per-platform analyses,
   Flaws Catalog, Solutions placeholder, Sources.
3. **Ticketing Flaws Tracker** (separate project) — Flaws Database (started 16, grew to 32) +
   Solutions Database (20), two-way related; views added.
4. **Backend & Architecture Teardown** — Vista/AMC/Fandango/IMAX stacks; confidence-tagged;
   added Confidence field to the DB.
5. **How Ticketing Actually Works** — end-to-end mechanics from Vista/AMC dev docs; the
   unscalable seat-lock; access-failure cascade.
6. **Flaw expansion** — added accessibility, pricing, regulatory, consumer-protection, trust,
   plus the access-cascade flaws (C6–C9). Total 32 across 10 categories.
7. **Fairness Principle** — Access × Identity × Selection; tagged every flaw by which condition
   it breaks; "By Fairness Condition" board view.
8. **Solution Architecture + Solution Spec v1** — Live Randomized Waiting Room; two modes;
   B2B "optimize within their stack" constraint (§0.5).
9. **Stack & Integration Map** — per-company integration points; found Queue-it+Akamai "Hype
   Event Protection" (validates mechanism; reframes moat → buy commodity, build cinema-native).
10. **Competitive Landscape** — waiting-room + anti-bot (commodity); DICE/Twickets/Verified Fan
    (concerts, not cinema); the gap = cinema-native B2B layer.
11. **Investor Narrative + Pitch Deck Outline (14 slides) + MVP/Pilot Build Plan + Monitoring Plan.**
12. **First-Principles Breakdown** — allocation of an underpriced good; stakeholder incentive map;
    identity is the linchpin; supply lever; demand segmentation; red-team.
13. **Vision & Expansion** — domain-agnostic; ~$64–90B event ticketing TAM; think big / start narrow;
    concentric expansion rings; stay out of Ticketmaster's gravity.
14. **Saved progress** — Master Index in Notion; `README.md` snapshot committed + pushed to
    branch `claude/odyssey-ticketing-analysis-RC83K`.
15. **Strategic Decisions (v1)** — resolved the four open questions (BELOW). *Notion write was
    pending approval at backup time, so the content is preserved here.*

---

## Strategic Decisions & Recommendations (v1) — PRESERVED FROM CHAT

(Recommendations for founder ratification.)

**Decision 1 — Primary buyer? REC: IMAX/studio is the champion; the exhibitor is the integration point.**
Exhibitors partly benefit from the frenzy (revenue + PR), so their pain is blunted. IMAX/studio
bears the brand damage and wants "real fans in seats," and IMAX can mandate a standard across
partner on-sales. Sell top-down to IMAX/studio; land the pilot at a cooperating exhibitor. Lead
with resilience + brand protection, not "fairness" as an abstraction. Beachhead-within-beachhead:
Filmed-for-IMAX / 70mm tentpole events.

**Decision 2 — Pure lottery vs hybrid pricing? REC: fair lottery is the default + brand; a fixed-premium tier is optional/off-by-default; never dynamic pricing.**
Dynamic/surge pricing on the prestige tier is the Ticketmaster wound. A small fixed-premium
"skip-the-line"/charity tier can capture surplus only if an exhibitor wants it. Don't lead with
pricing — it muddies the fairness differentiator.

**Decision 3 — Supply optimization vs allocation? REC: allocation is the moat; supply optimization is the easy-yes "land" feature.**
Scarcity is partly manufactured. The system should recommend supply actions first (add showtimes/
waves/runs/waitlist) — immediately ROI-positive and politically easy — then ration the truly-fixed
remainder. "Help you sell more and fairer" beats "ration your hottest product."

**Decision 4 — Build identity, or is identity the company? REC: buy detection primitives; BUILD a thin dedup layer that becomes a portable verified-human credential. Identity is the compounding moat.**
One-human-one-entry is the whole game; a verified human is verified across every vertical, so the
identity graph compounds horizontally (cinema → concerts → sports). Buy DataDome/HUMAN for
detection; build dedup + portable credential + privacy-by-design (flaw R2).

**The flywheel:** fans who get a fair, trusted process follow it to the next event → we accumulate
verified, opted-in demand → we arrive at the next exhibitor with fans in hand, not just software.
The verified-human credential is both the fairness mechanism and a distribution asset — a two-sided
network effect Ticketmaster can't easily replicate vertical-by-vertical.

**Net posture:** Sell resilience + brand protection to IMAX/studios; integrate at a cooperating
exhibitor; default to a clean fair lottery with optional fixed-premium tiers (never dynamic pricing);
lead commercially with supply-optimization + crash-proofing as the easy yes; quietly build the
portable verified-human identity graph as the cross-vertical moat.

---

## Open threads (next time)

1. **Founder's own solution ideas** — the original Phase-2 input, still the missing piece to
   pressure-test against the Flaws Catalog.
2. Ratify/override the four Strategic Decisions above (sync to Notion once approved).
3. Founder-owned: company name; raise/valuation; team & traction.
4. Optional deepenings offered: identity-layer-as-platform war-game; two-sided flywheel GTM;
   narrowing the wedge to "Filmed-for-IMAX / 70mm" specifically.

## Sync status at backup

- **Notion:** all pages live EXCEPT "Strategic Decisions & Recommendations (v1)" (write pending
  approval — content preserved above).
- **Git:** `README.md` + this `SESSION-LOG.md` on branch `claude/odyssey-ticketing-analysis-RC83K`.
