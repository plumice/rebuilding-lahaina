# Odyssey Ticketing Project — Fixing High-Demand Ticketing

> Version-controlled snapshot of a research + strategy project. The live, primary copy lives in
> Notion (workspace: plumice.backend@gmail.com). This file is a durable backup of structure,
> links, and key substance. **Last saved: 2026-06-08.**

Master index in Notion: https://app.notion.com/p/37982ef1230e8150a87ae2c854e69b5a

---

## What this is

Analysis of why high-demand movie ticket on-sales fail — anchored on Christopher Nolan's
*The Odyssey* IMAX 70mm on-sale (June 4, 2026, which crashed AMC/Fandango/Regal) — and the
design of a B2B "fair-drop" layer to fix it, plus the business case to pitch it.

## Status

- **Phase 1 (Analysis):** complete — 32 flaws / 10 categories, backend teardown, mechanics, fairness principle.
- **Phase 2 (Solution):** designed — architecture, full spec, 20 mapped solutions.
- **Phase 3 (Business):** drafted — stack/integration, competition, investor narrative, deck outline, vision, build + monitoring plans.
- **Founder-owned (open):** company name, raise/valuation, team/traction, own solution ideas.

---

## Executive summary

**Problem.** When scarce tickets drop at a set time and demand >> supply, first-come allocation
fails: sites crash, bots win, and the average person can't get in. The Odyssey on-sale is the
textbook case — $25 IMAX 70mm tickets resold for $500–$1,500; AMC's CEO publicly apologized;
measurable failure within ~6 minutes (Downdetector: 872 AMC reports by 12:13pm).

**Root cause (first principles).** It's an *allocation problem for a deliberately underpriced good*.
Face price is far below the market-clearing price; that gap is the scalper's profit. With the studio
brand requiring a low price, the only fair answer is **rationing**. Technically, the failure is a
shared, unscalable **seat-lock** plus **no fairness layer** — you cannot fix scarcity with more servers.

**The fairness principle.** A fair drop = **Access × Identity × Selection**:
everyone can get in (Access), one real person = one entry (Identity), winner chosen by chance not
speed (Selection). Every fairness flaw breaks one of these. Identity is the linchpin — if it's weak,
the lottery just randomizes among bots.

**The solution.** A B2B fairness-and-resilience layer that sits *in front of* the exhibitor's
existing stack (Vista Connect / AMC Orders API) and optimizes within it — no re-platforming.
Core engine: a **Live Randomized Waiting Room** (open at T, admit everyone to a room, verify
one-human-one-entry, randomize, then meter purchases ≤ backend safe capacity so it can't crash).
Two modes (fair stable queue / register-and-draw). Identity-bound tickets + official face-value
resale kill scalping. Buy the commodity (waiting room, anti-bot); build the cinema-native
orchestration (backend metering, provably-fair draw, anti-scalp).

**Positioning.** Sell to the companies with the problem (B2B). Beachhead: IMAX 70mm / premium
tentpole on-sales. Likely best-aligned buyer: IMAX/studios (brand) as much as exhibitors.

**Vision.** Domain-agnostic — fair-access infrastructure for *any* high-demand drop
(~$64–90B event ticketing market). Think big, start narrow: win uncontested cinema first
(no fairness incumbent), then expand outward, staying out of Ticketmaster's gravity until strong.

---

## The 32 flaws (10 categories)

**Capacity & Infrastructure:** C1 provisioned for average not spike · C2 checkout weakest link ·
C3 seat-lock contention · C4 aggregator coupling · C5 phantom scarcity (cart holds) ·
C6 thundering herd · C7 autoscale lag · C8 DB/connection-pool & cache-stampede ceiling ·
C9 retry-storm metastable failure.

**Queue Fairness:** Q1 crash-prevention ≠ fairness · Q2 FIFO not randomized · Q3 opaque queue state.

**Identity & Bots:** B1 no verified-fan layer · B2 defeatable bot defenses · B3 loyalty ≠ identity ·
B4 account takeover / credential stuffing · B5 anti-bot false positives block real fans.

**Anti-Scalping / Resale:** S1 no transfer lock · S2 no price cap · S3 no identity-bound tickets ·
S4 no official face-value resale/returns/waitlist.

**Allocation Policy:** P1 open rush for scarce inventory · P2 no fair-access reserve ·
P3 fragmented drop timing · P4 no group-aware allocation.

**Accessibility & Inclusion:** AC1 ADA seats swept in fast sellouts · AC2 app/account-only excludes digital-divide.

**Pricing & Fees:** PF1 drip pricing / opaque fees (FTC junk-fee rule).

**Regulatory & Legal:** R1 BOTS Act under-enforced + movies likely out of scope · R2 identity = privacy/PII liability.

**Consumer Protection:** CP1 ultra-early non-refundable sale + change risk.

**Trust & Communication:** T1 no incident comms / status transparency.

Severity: 13 High · 9 Medium-High · 10 Medium.
Fairness mapping: 6 Access · 5 Identity · 3 Selection · 8 Outcome · 10 Not-drop-fairness.

---

## Confirmed backend stack (for the "optimize within their stack" approach)

- **Vista** (Regal + most chains): Vista Cloud on Azure; OCAPI/Connect API
  (`CreateOrder → SetTickets → complete`, `expiryDateUtc` holds); single transaction engine.
- **AMC:** own RESTful Orders API (ecommerce gated by vendor key + contract); New Relic;
  Oracle Cloud ERP; Radiant/NCR in-theatre POS; own virtual waiting room.
- **Fandango:** AWS (CloudFront/S3/Route53), Java/Scala; in-house waiting room; powers IMAX.com.
- **IMAX:** no transaction backend — routes via Fandango/exhibitors; a mandate/policy buyer.

## Competitive reality

- Waiting room (commodity, partner): Queue-it, Cloudflare, Akamai, Queue-Fair.
  Queue-it+Akamai "Hype Event Protection" already does randomized-waiting-room+bot-block
  (proven 50× fairer, 98% bots blocked).
- Anti-bot (commodity, partner): DataDome (has ticketing product), HUMAN, Kasada, Arkose.
- Fair resale / anti-scalp (proven in concerts, absent in cinema): DICE (locked dynamic-QR +
  face-value waitlist resale — the model), Twickets/Tixel, Ticketmaster Verified Fan.
- **Gap = cinema-native, full-stack, B2B layer integrating into exhibitor backends. That's the company.**

---

## Notion page map

| Section | Page | URL |
|---|---|---|
| Hub | Odyssey Ticketing Project | https://app.notion.com/p/37782ef1230e81fea195ffe10569baff |
| Index | START HERE — Master Index | https://app.notion.com/p/37982ef1230e8150a87ae2c854e69b5a |
| Problem | Case Study: Odyssey On-Sale | https://app.notion.com/p/37782ef1230e81bea4c4f37a7e1958a8 |
| Problem | Platform Analysis: Fandango | https://app.notion.com/p/37782ef1230e81a08beeff792a226ac5 |
| Problem | Platform Analysis: AMC | https://app.notion.com/p/37782ef1230e81468d28c5b08c4075db |
| Problem | Platform Analysis: IMAX / Regal | https://app.notion.com/p/37782ef1230e810592a7eaa35d874a8a |
| Problem | Sources | https://app.notion.com/p/37782ef1230e8170b8dcfbe481d53132 |
| Technical | Backend & Architecture Teardown | https://app.notion.com/p/37982ef1230e81898cdceaea6174eeeb |
| Technical | How Ticketing Actually Works | https://app.notion.com/p/37982ef1230e812f8604c07672a78c68 |
| Technical | Stack & Integration Map | https://app.notion.com/p/37982ef1230e8161a262efd7a19fa326 |
| Flaws | Flaws Catalog (comprehensive) | https://app.notion.com/p/37782ef1230e81228b7fdba57b9595c2 |
| Flaws | The Fairness Principle | https://app.notion.com/p/37982ef1230e814680a6e58e91bc21c0 |
| Flaws | First-Principles Breakdown | https://app.notion.com/p/37982ef1230e812e92c7d6c1eba9350a |
| Solution | Solution Architecture & System Design | https://app.notion.com/p/37982ef1230e81c8b215fb9e2192b89b |
| Solution | Solution Spec v1 | https://app.notion.com/p/37982ef1230e812b8665fd187cb43a12 |
| Strategy | Investor Narrative | https://app.notion.com/p/37982ef1230e813c95f8e640f84405eb |
| Strategy | Vision & Expansion Strategy | https://app.notion.com/p/37982ef1230e817ea0acd7f2fbf38b6d |
| Strategy | Competitive Landscape | https://app.notion.com/p/37982ef1230e812f8b4dfa6e1614ce6d |
| Strategy | Pitch Deck Outline | https://app.notion.com/p/37982ef1230e8135af5bdd5991330940 |
| Build | MVP & Pilot Build Plan | https://app.notion.com/p/37982ef1230e81fa9d40e1156024c2c8 |
| Build | On-Sale Monitoring Plan | https://app.notion.com/p/37982ef1230e8122bcdfe24f4a60f435 |
| Databases | Ticketing Flaws Tracker | https://app.notion.com/p/37982ef1230e81378ec3cd319fb871fa |
| Databases | Flaws Database (32) | https://app.notion.com/p/a27459c621ce43289a47fc8eed3fbb27 |
| Databases | Solutions Database (20) | https://app.notion.com/p/9f62942b71d141008da298735af55d14 |

## Open next actions

1. Founder's own solution ideas → pressure-test vs. the Flaws Catalog.
2. Decide primary buyer: exhibitor vs. IMAX/studio.
3. Pure lottery vs. hybrid priced+lottery.
4. Fill founder-owned slides (raise, team, traction) + pick a company name.
