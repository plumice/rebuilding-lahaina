# Plan / handoff

Working notes for continuing this audit in another session (e.g. Codex).
This file captures what was done in the 2026-05-02/03 session and what
remains, so the next agent can pick up without re-deriving context.

## What just landed (this commit)

1. **Cross-reference + media audit on `src/content/`** — wrote a small
   Python script to walk all `.md` files, parse YAML frontmatter, and
   verify every `relatedSections` / `relatedSources` / `relatedDrawings`
   / `relatedTerms` / `chapter` ID resolves, and every `image:` /
   `layers[].file` path exists on disk.
   - Result: **0 broken cross-refs, 0 missing media.**
   - Found **43 orphan items** (sources/drawings/terms with no inbound
     reference). Maps & timeline orphans are intentional (standalone
     routes); sources/drawings/terms aren't.

2. **Wired 40 of those orphans into their natural home sections** by
   appending IDs to the appropriate `relatedSources` / `relatedDrawings`
   / `relatedTerms` arrays. Top-scored matches by topic-tag overlap +
   keyword overlap + slug/title mention. Two manual overrides applied:
   - `lsb-classifications` → `zoning-analysis` (instead of the
     auto-suggested `buffer-framework`)
   - `module-baseline-section` → `module-assembly-rules` (instead of
     `literature-methodology`)

3. **Rewrote three "research-note" sources** that I (Singh, Akhil)
   authored but read like author asides on the site:
   - `sources/research-buffers.md` body: `See thesis, §3C Design Principles, pp. 48–58.`
   - `sources/research-streams.md` body: `See thesis, §3B Regional Scale, pp. 44–45.`
   - `sources/research-zoning-breakdown.md` body: `See thesis, §3D Systems, pp. 76–79.`
   - Frontmatter unchanged (schema requires `author:`).
   - Page numbers were resolved by parsing
     `09_deliverables/final_pdfs/thesis_v30.pdf` (147 pages, "Singh |
     Rebuilding Post Disasters" page-header markers) on the T7 Shield
     external drive.
   - These three are **intentionally not wired into any section** — they
     don't add citation value; the sections they'd link from already
     contain the same content. They show as the only remaining orphan
     sources after this commit (3/48).

## Audit residuals (state after this commit)

| Collection | Total | Orphans | Note |
|---|---|---|---|
| sections | 29 | n/a | |
| drawings | 72 | **0** | |
| sources | 48 | **3** | the three thesis pointers — intentional |
| terms | 21 | **0** | |
| maps | 1 | 1 | intentional, surfaced via `/map` route |
| timeline | 9 | 9 | intentional, surfaced via `/timeline` route |

## Open follow-ups (not done in this session)

In rough priority order:

1. **Singhakhil-site companion changes** — same session also added a
   `website` field on the `arch_rebuilding_lahaina` and
   `research_thesis_lahaina` project entries pointing to
   <https://rebuildinglahaina.org>, plus rendering in the detail panel
   and a small badge on the architecture grid card. Those edits are in
   the *other* repo (`plumice/singhakhil-site`) — push status TBD; check
   that repo separately.

2. **Editorial first-person sweep.** Section bodies still have residual
   author voice — examples spotted but not rewritten:
   - `sections/literature-methodology.md` line ~85: "When I went to
     Hawaiʻi, I met with people…"
   - same file: "the methodology I drew from", "I assembled this
     glossary as a discipline"
   These read first-person in a site otherwise framed third-person /
   voiceless. Estimated 30 min to grep + rewrite.

3. **Operational hardening.** During this session, the
   `Deploy to GitHub Pages` workflow was found jammed since 2026-04-07
   — two stuck runs (24089878221, 24248810641) blocked the
   `concurrency: group: pages` lane. Cancelled them; manual deploy via
   `workflow_dispatch` (run 25268781308) succeeded in 1m20s. The
   underlying risk (silent multi-week deploy halt because news-update
   commits use `[skip ci]` and didn't trigger fresh deploys) suggests
   adding a CI alert / staleness check on the deploys workflow.

4. **`/live` events archive.** Currently `scripts/fetch-news.mjs`
   overwrites `public/data/news.json` each run, capped at 8 items —
   so old events roll off Google News' RSS window forever. Proposed
   architecture (not implemented):
   - Modify the script to *merge* new items with existing ones,
     dedupe by link/title, sort newest-first.
   - Split output into two files:
     - `public/data/news-feed.json` (top 8, what `<NewsBulletin>` loads)
     - `public/data/news-archive.json` (full history, ~2 MB after a
       year, only loaded on a new `/live` page)
   - Add a `/live` route that paginates the archive.

5. **Smaller follow-ups.**
   - `npm audit` flagged 12 vulns (9 mod, 3 high) on `npm i` — likely
     transitive dep noise; worth a 5-min scan.
   - Dead external URL sweep on source citation links (slow,
     network-bound).
   - The local working copy at
     `/Users/akhil/Library/CloudStorage/OneDrive-Personal/thesis-website/`
     has CRLF line-ending churn from OneDrive sync (every file shows
     "modified" in `git status` but content is identical to HEAD after
     `tr -d '\r'`). Adding `.gitattributes` with `* text=auto eol=lf`
     would normalize this. Caused this commit to be made from a clean
     clone in `/tmp/lahaina-push` because git operations against the
     OneDrive `.git/` directory were hanging indefinitely on macOS.

## Useful one-liners for the next session

Re-run the cross-reference + media audit:

```bash
# Walks src/content, parses YAML frontmatter, validates every relation
# and image path. Reports broken refs, missing media, orphans by type.
python3 scripts/audit_xrefs.py    # (script not yet committed; see
                                  # /tmp/audit_thesis.py from prior session)
```

Find page numbers in the thesis source for any topic:

```bash
# 1. Extract: pdftotext -layout 09_deliverables/final_pdfs/thesis_v30.pdf /tmp/thesis.txt
# 2. Each "Singh | Rebuilding Post Disasters" line is a page header.
#    Walk them in order; the printed page-number text appears just before
#    each header (e.g. /^[[:space:]]+[0-9]{1,3}[[:space:]]*$/).
```

— end —
