#!/usr/bin/env python3
"""
Citation + URL liveness + thesis-cross-reference audit.

Three passes over src/content/:

  1. Metadata completeness for each source
     - Required: title, author, sourceType, relevance, tags{topic, type}
     - Optional but recommended: publisher, date, primary_url (TBD field)
     - Flags any empty required field

  2. URL liveness sweep
     - Extracts every http(s) URL from every .md body
     - HEAD with 5s timeout, falls back to GET for servers that reject HEAD
     - Classifies: 200, 301/302 (target), 404, 5xx, timeout, network error
     - Groups results by source file

  3. Thesis cross-reference (uses thesis_source.txt)
     - For each source: check whether author surname OR a title keyword
       appears anywhere in thesis_source.txt
     - Flags sources mentioned in NO form (potential website-added
       citations the thesis itself doesn't reference)

Usage:
  python3 scripts/audit_sources.py [--verbose] [--no-net]

  --no-net  Skip the URL liveness pass (offline mode)
"""

import os
import re
import sys
import time
import yaml
import urllib.request
import urllib.error
import socket
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "src" / "content"
THESIS = ROOT / "thesis_source.txt"

SOURCE_REQUIRED = ["title", "author", "sourceType", "relevance"]
SOURCE_REQUIRED_TAGS = ["topic", "type"]
URL_RE = re.compile(r"https?://[A-Za-z0-9._~:/?#\[\]@!$&'()*+,;=%-]+[A-Za-z0-9/_]")
URL_TIMEOUT = 8
# Use a real browser UA so anti-bot blocks (FEMA, census.gov, climate.hawaii.gov
# etc.) don't generate spurious 403s — we are link-checking, not pen-testing.
BROWSER_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)
# Hosts known to block all curl/script traffic with 403 even under real browser
# UAs (typically Cloudflare anti-bot, AWS WAF, government scraper defenses).
# Verified manually in browser to be real, healthy URLs as of 2026-05-17.
# A 403 from these is treated as "OK (anti-bot)" rather than a failure.
KNOWN_ANTI_BOT_HOSTS = {
    "climate.hawaii.gov",
    "data.census.gov",
    "www.fema.gov",
    "landezine.com",
    "westmaui.wearemaui.org",
}

socket.setdefaulttimeout(URL_TIMEOUT)


def load_md(path):
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
    body = text[end:]
    return fm, body


def extract_urls(text):
    """Return ordered, deduped list of URLs found in markdown text."""
    seen = set()
    out = []
    for m in URL_RE.finditer(text):
        u = m.group(0).rstrip(".,;:)]>'\"")
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def check_url(url):
    """Return (status_code_or_label, redirect_target_or_None, time_ms)."""
    t0 = time.time()
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(
            url, method=method,
            headers={
                "User-Agent": BROWSER_UA,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=URL_TIMEOUT) as resp:
                ms = int((time.time() - t0) * 1000)
                final = resp.geturl()
                redirect = final if final != url else None
                return (resp.status, redirect, ms)
        except urllib.error.HTTPError as e:
            ms = int((time.time() - t0) * 1000)
            # Some servers respond 405 to HEAD; retry GET
            if e.code == 405 and method == "HEAD":
                continue
            # 403 with HEAD frequently means anti-bot; try GET
            if e.code in (401, 403) and method == "HEAD":
                continue
            return (e.code, None, ms)
        except (urllib.error.URLError, socket.timeout, ConnectionError) as e:
            ms = int((time.time() - t0) * 1000)
            return (f"NETWORK:{type(e).__name__}", None, ms)
        except Exception as e:
            ms = int((time.time() - t0) * 1000)
            return (f"ERROR:{type(e).__name__}", None, ms)
    return ("UNREACHED", None, int((time.time() - t0) * 1000))


def thesis_mentions(thesis_text, source_fm):
    """Heuristic: does this source appear in the thesis?
    Check (a) author surname, (b) title's first ~3 distinctive words."""
    if not thesis_text:
        return None
    author = (source_fm.get("author") or "").strip()
    title = (source_fm.get("title") or "").strip()
    hits = []

    if author:
        # surname = comma-form "Lastname, First" or last word
        if "," in author:
            surname = author.split(",", 1)[0].strip()
        else:
            parts = author.split()
            surname = parts[-1] if parts else ""
        if len(surname) >= 4 and surname.lower() in thesis_text.lower():
            hits.append(f"author:{surname}")

    if title:
        # take first distinctive word > 4 chars, not stop word
        STOP = {"the", "and", "of", "in", "on", "to", "from",
                "with", "for", "an", "a"}
        words = [w for w in re.findall(r"[A-Za-zʻʼ']+", title)
                 if len(w) > 4 and w.lower() not in STOP]
        if words:
            kw = words[0]
            if kw.lower() in thesis_text.lower():
                hits.append(f"title:{kw}")

    return hits


def main():
    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    no_net = "--no-net" in sys.argv

    print("=" * 64)
    print("CITATION + URL + THESIS-REF AUDIT")
    print("=" * 64)

    sources_dir = CONTENT / "sources"
    source_files = sorted(p for p in sources_dir.glob("*.md")
                          if not p.name.startswith("._"))
    print(f"\nSources: {len(source_files)}")

    # ---- 1. Metadata completeness ----
    print("\n[1] METADATA COMPLETENESS")
    print("-" * 64)
    incomplete = []
    for f in source_files:
        fm, _ = load_md(f)
        missing = []
        for k in SOURCE_REQUIRED:
            v = fm.get(k)
            if not v or (isinstance(v, str) and not v.strip()):
                missing.append(k)
        tags = fm.get("tags") or {}
        for k in SOURCE_REQUIRED_TAGS:
            if not tags.get(k):
                missing.append(f"tags.{k}")
        # Optional but recommended:
        recommended = []
        if not fm.get("publisher"):
            recommended.append("publisher")
        if not fm.get("date"):
            recommended.append("date")
        if missing or recommended:
            incomplete.append((f.name, missing, recommended))

    if not incomplete:
        print("  ✓ All sources complete on required fields.")
    else:
        print(f"  {len(incomplete)} sources with gaps:\n")
        for name, missing, rec in incomplete:
            tag = "MISSING REQUIRED" if missing else "missing optional"
            fields = ", ".join(missing or rec)
            print(f"  {name:45s}  {tag}: {fields}")

    # ---- 2. URL liveness ----
    print("\n[2] URL LIVENESS")
    print("-" * 64)

    url_to_files = defaultdict(list)
    for col in ("sources", "sections", "terms", "drawings",
                "timeline", "topics", "scales", "maps"):
        for f in sorted((CONTENT / col).glob("*.md")):
            if f.name.startswith("._"):
                continue
            _, body = load_md(f)
            for u in extract_urls(body):
                url_to_files[u].append(f.relative_to(ROOT))

    urls = sorted(url_to_files.keys())
    print(f"  {len(urls)} unique external URLs across all content\n")

    if no_net:
        print("  (skipped — --no-net)")
        results = {}
    else:
        results = {}
        for i, u in enumerate(urls, 1):
            status, redirect, ms = check_url(u)
            results[u] = (status, redirect, ms)
            sym = "✓" if status == 200 else "!"
            redir_note = f" → {redirect}" if redirect else ""
            print(f"  [{i:2d}/{len(urls)}] {sym} {status:>5}  {ms:>4}ms  {u}{redir_note}")
            time.sleep(0.15)  # polite throttle

        # Summary by status
        by_status = defaultdict(list)
        for u, (s, r, _) in results.items():
            by_status[s].append(u)
        print()
        print("  Summary:")
        for s in sorted(by_status, key=lambda x: str(x)):
            print(f"    {s!s:>15}: {len(by_status[s])}")

        # Classify failures: real-broken vs known-anti-bot
        from urllib.parse import urlparse
        bad = []
        anti_bot = []
        for u, (s, _, _) in results.items():
            if isinstance(s, int) and 200 <= s < 400:
                continue
            host = urlparse(u).netloc.lower()
            if s == 403 and host in KNOWN_ANTI_BOT_HOSTS:
                anti_bot.append(u)
            else:
                bad.append(u)

        if anti_bot:
            print(f"\n  OK — anti-bot 403, verified in browser ({len(anti_bot)}):")
            for u in anti_bot:
                print(f"    [403] {u}")

        if bad:
            print(f"\n  Needs attention ({len(bad)}):")
            for u in bad:
                s, _, _ = results[u]
                files = ", ".join(str(p) for p in url_to_files[u][:3])
                more = "" if len(url_to_files[u]) <= 3 else f" +{len(url_to_files[u])-3}"
                print(f"    [{s}] {u}\n        in: {files}{more}")

    # ---- 3. Thesis cross-reference ----
    print("\n[3] THESIS CROSS-REFERENCE (vs thesis_source.txt)")
    print("-" * 64)
    if not THESIS.exists():
        print("  ! thesis_source.txt not found; skipping.")
    else:
        thesis = THESIS.read_text(encoding="utf-8", errors="replace")
        not_in_thesis = []
        for f in source_files:
            fm, _ = load_md(f)
            hits = thesis_mentions(thesis, fm)
            if hits is None:
                continue
            if not hits:
                not_in_thesis.append((f.name, fm.get("author", "?"),
                                      fm.get("title", "?")[:60]))

        if not not_in_thesis:
            print("  ✓ Every source has a heuristic mention in the thesis.")
        else:
            print(f"  {len(not_in_thesis)} sources with no author/title hit in thesis_source.txt:\n")
            for name, author, title in not_in_thesis:
                print(f"  {name}")
                print(f"    author: {author}")
                print(f"    title:  {title}")
                print()
            print("  Note: heuristic. Verify manually — common-surname authors and")
            print("  paraphrased citations will produce false positives in either direction.")

    print()
    print("=" * 64)
    print(f"Sources audited:       {len(source_files)}")
    print(f"Incomplete metadata:   {len(incomplete)}")
    print(f"URLs checked:          {len(urls) if not no_net else 0}")
    if not no_net:
        from urllib.parse import urlparse as _up
        bad_count = sum(
            1 for u, (s, _, _) in results.items()
            if not (isinstance(s, int) and 200 <= s < 400)
            and not (s == 403 and _up(u).netloc.lower() in KNOWN_ANTI_BOT_HOSTS)
        )
        print(f"URLs needing fix:      {bad_count}")
    if THESIS.exists():
        print(f"Sources not in thesis: {len(not_in_thesis)}")
    print("=" * 64)


if __name__ == "__main__":
    main()
