#!/usr/bin/env python3
"""
Numeric-claim verification for src/content/sections/.

Walks every section body, extracts quantitative claims, and verifies each
against the canonical source-of-truth `thesis_source.txt`. Flags claims
that appear unsourced.

Claim categories detected:
  - Currency:        $X billion, $X million, $XB, $XM
  - Percentages:     X percent, X%
  - Counts w/ units: 2,200 structures; 6,000 residents; 50 miles
  - Years:           2023, 1999, 2019-2023
  - Measurements:    4.26 MGD, 80 inches, 84 acres, 35-foot
  - Date ranges:     decade-long, 18-month, century

For each claim, checks:
  1. Verbatim presence in thesis_source.txt (HIGH confidence)
  2. Number tokens match nearby context in thesis (MEDIUM confidence)
  3. Number tokens appear anywhere in thesis (LOW confidence)
  4. Not found (UNSOURCED — needs author attention)

False-positive avoidance:
  - Skip page numbers ("pp. 48-58", "p. 110-19")
  - Skip section/regulation refs ("§15-110", "HAR 15-110")
  - Skip URLs and acronyms (FEMA-4724, DR-4724)
  - Skip module dimensions when in tables (already structural data)

Usage:
  python3 scripts/verify_claims.py [--verbose] [--section <name>]

Exit code 0 = all claims sourced, 1 = unsourced claims present.
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict

import yaml

ROOT = Path(__file__).resolve().parent.parent
SECTIONS_DIR = ROOT / "src" / "content" / "sections"
THESIS_PATH = ROOT / "thesis_source.txt"

# Exclude page/section/regulation refs from claim extraction
EXCLUDE_PATTERNS = [
    re.compile(r"\bpp?\.\s*\d+(-\d+)?", re.I),         # pp. 48-58
    re.compile(r"§\s*\d+[-.]?\d*"),                     # §15-110
    re.compile(r"HAR\s*§?\s*\d+[-.]?\d*", re.I),        # HAR 15-110
    re.compile(r"DR-?\d+"),                             # DR-4724, DR4724
    re.compile(r"https?://\S+"),                        # URLs
    re.compile(r"\b\d{4,5}\s*(?:sq\s*ft|square\s*feet)", re.I),  # 57,460 sq ft (architectural, not journalistic)
]

# Claim patterns — each yields (matched_text, normalized_numbers)
CLAIM_PATTERNS = [
    # Currency: $3 billion, $4 billion, $5 million, $2B
    (re.compile(r"\$\s*\d+(?:\.\d+)?\s*(?:billion|million|thousand|trillion|B\b|M\b|K\b)", re.I),
     "currency"),
    # Percentages: 80 percent, 80%, 41.8%, 83%
    (re.compile(r"\b\d+(?:\.\d+)?\s*(?:percent|%)", re.I),
     "percentage"),
    # Large counts with units: 2,200 structures, 6,000 residents
    (re.compile(r"\b\d{1,3}(?:,\d{3})+\s+(?:structures?|units?|homes?|families|residents?|people|workers|deaths?|fatalities|acres?|miles?|feet|ft|inches?|gallons?|households?|claims?|sites?|properties)", re.I),
     "count-large"),
    # Years: 2023, 1999, 1860s
    (re.compile(r"\b(?:18|19|20)\d{2}s?\b"),
     "year"),
    # Measurements: 4.26 MGD, 80 inches, 84 acres, 50 miles
    (re.compile(r"\b\d+(?:\.\d+)?\s*(?:MGD|mgd|acres?|miles?|feet|ft\b|inches?|stories|hectares?|kilometers?|km\b|meters?|m\b)", re.I),
     "measurement"),
    # Counts under 1000 with significant units (smaller but real claims)
    (re.compile(r"\b\d{2,3}\s+(?:residents?|families|structures?|units?|deaths?|fatalities|stories)", re.I),
     "count-small"),
    # Date ranges & durations: 18-month, 36 months, decade-long, century
    (re.compile(r"\b\d+(?:\.\d+)?\s*-?\s*(?:day|days|month|months|year|years|week|weeks|decade|decades|century|centuries)\b", re.I),
     "duration"),
]


def load_frontmatter_and_body(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return {}, text
    try:
        end = text.index("\n---", 3) + 4
    except ValueError:
        return {}, text
    try:
        fm = yaml.safe_load(text[3:end - 4]) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, text[end:]


def strip_excluded(text):
    """Remove excluded patterns from text so they don't yield false claims."""
    for pat in EXCLUDE_PATTERNS:
        text = pat.sub(" ", text)
    return text


def extract_numbers(s):
    """Pull all integer/decimal tokens from a string (e.g. '$3.2 billion' -> ['3.2'])."""
    return re.findall(r"\d+(?:\.\d+)?", s.replace(",", ""))


def find_claims(body):
    """Return list of dicts with claim, category, context, line_no."""
    cleaned = strip_excluded(body)
    claims = []
    seen_spans = set()
    for line_no, line in enumerate(cleaned.split("\n"), start=1):
        for pat, cat in CLAIM_PATTERNS:
            for m in pat.finditer(line):
                span = (line_no, m.start(), m.end())
                if span in seen_spans:
                    continue
                seen_spans.add(span)
                ctx_start = max(0, m.start() - 70)
                ctx_end = min(len(line), m.end() + 70)
                claims.append({
                    "text": m.group(0).strip(),
                    "category": cat,
                    "context": line[ctx_start:ctx_end].strip(),
                    "line_no": line_no,
                    "numbers": extract_numbers(m.group(0)),
                })
    return claims


def verify_against_thesis(claim, thesis_text, thesis_lower):
    """
    Classify the claim:
      HIGH    - exact claim text appears in thesis
      MEDIUM  - all numeric tokens appear within a 200-char window in thesis
      LOW     - all numeric tokens appear somewhere in thesis (not co-located)
      UNSOURCED - one or more tokens missing
    """
    text = claim["text"].lower()
    if text in thesis_lower:
        return "HIGH"
    nums = claim["numbers"]
    if not nums:
        return "LOW"
    # Find any window where all numbers co-occur within 200 chars
    first = nums[0]
    for m in re.finditer(re.escape(first), thesis_text):
        window = thesis_text[max(0, m.start() - 200): m.end() + 200]
        if all(n in window for n in nums):
            return "MEDIUM"
    # Are all tokens at least present somewhere?
    if all(n in thesis_text for n in nums):
        return "LOW"
    return "UNSOURCED"


def main():
    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    section_filter = None
    if "--section" in sys.argv:
        i = sys.argv.index("--section")
        if i + 1 < len(sys.argv):
            section_filter = sys.argv[i + 1]

    thesis_text = THESIS_PATH.read_text(encoding="utf-8", errors="replace")
    thesis_lower = thesis_text.lower()

    section_files = sorted(p for p in SECTIONS_DIR.glob("*.md") if not p.name.startswith("._"))
    if section_filter:
        section_files = [p for p in section_files if section_filter in p.name]

    print("=" * 70)
    print("NUMERIC-CLAIM VERIFICATION")
    print("=" * 70)
    print(f"Source-of-truth: {THESIS_PATH.relative_to(ROOT)}")
    print(f"Sections scanned: {len(section_files)}")
    print()

    by_section = []
    totals = defaultdict(int)
    unsourced_items = []

    for sec_file in section_files:
        fm, body = load_frontmatter_and_body(sec_file)
        claims = find_claims(body)
        verdicts = defaultdict(list)
        for c in claims:
            verdict = verify_against_thesis(c, thesis_text, thesis_lower)
            verdicts[verdict].append(c)
            totals[verdict] += 1
            if verdict == "UNSOURCED":
                unsourced_items.append((sec_file.name, c))
        by_section.append((sec_file.name, len(claims), verdicts))

    # Per-section summary
    print(f"{'SECTION':<45} {'TOTAL':>6} {'HI':>4} {'MED':>4} {'LOW':>4} {'UNS':>4}")
    print("-" * 70)
    for name, total, v in by_section:
        if total == 0:
            continue
        flag = " " if not v["UNSOURCED"] else "!"
        print(f"{flag}{name:<44} {total:>6} {len(v['HIGH']):>4} {len(v['MEDIUM']):>4} {len(v['LOW']):>4} {len(v['UNSOURCED']):>4}")

    print()
    print(f"TOTALS: {sum(totals.values())} claims  "
          f"| HIGH {totals['HIGH']}  MEDIUM {totals['MEDIUM']}  LOW {totals['LOW']}  "
          f"UNSOURCED {totals['UNSOURCED']}")
    print()

    # Detail on unsourced claims
    if unsourced_items:
        print("=" * 70)
        print(f"UNSOURCED CLAIMS ({len(unsourced_items)}) — needs verification:")
        print("=" * 70)
        for section, c in unsourced_items:
            print(f"\n[{section}] line {c['line_no']}  ({c['category']})")
            print(f"  CLAIM:   {c['text']!r}")
            print(f"  CONTEXT: …{c['context']}…")

    # Detail on low-confidence claims when verbose
    if verbose and totals["LOW"]:
        print()
        print("=" * 70)
        print(f"LOW-CONFIDENCE CLAIMS ({totals['LOW']}) — numbers present in thesis but not co-located:")
        print("=" * 70)
        for name, total, v in by_section:
            for c in v["LOW"]:
                print(f"\n[{name}] line {c['line_no']}  ({c['category']})")
                print(f"  CLAIM:   {c['text']!r}")
                print(f"  CONTEXT: …{c['context']}…")

    sys.exit(1 if totals["UNSOURCED"] else 0)


if __name__ == "__main__":
    main()
