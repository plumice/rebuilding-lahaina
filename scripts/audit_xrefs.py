#!/usr/bin/env python3
"""
Cross-reference + media audit for src/content/.

Walks every .md file in each content collection, parses YAML frontmatter,
and verifies:
  - Every relatedSections / relatedSources / relatedDrawings / relatedTerms
    ID resolves to a real file in that collection.
  - Every chapter value is one of the allowed enum values.
  - Every `image:` path, `supportImages[].src`, and `layers[].file` exists
    on disk (under public/ for images, public/data/geojson/ for layers).
  - Each item is reachable: reports orphans (items with no inbound refs).

Exit code 0 = clean, 1 = broken refs or missing media (orphans alone are
informational, not failure).

Usage:
  python3 scripts/audit_xrefs.py [--verbose]
"""

import os
import sys
import yaml
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "src" / "content"
PUBLIC = ROOT / "public"

COLLECTIONS = [
    "sections", "drawings", "sources", "terms",
    "maps", "timeline", "topics", "scales",
]

CHAPTERS = {
    "ch1-introduction", "ch2-overview", "ch3-analysis",
    "ch4-principles", "ch5-design",
}

# (field name on item -> collection it points to)
REF_FIELDS = {
    "relatedSections": "sections",
    "relatedSources": "sources",
    "relatedDrawings": "drawings",
    "relatedTerms": "terms",
}


def load_collection(name):
    """Return {id: (path, frontmatter_dict)} for one collection."""
    items = {}
    base = CONTENT / name
    if not base.exists():
        return items
    for f in sorted(base.glob("*.md")):
        if f.name.startswith("._"):
            continue
        item_id = f.stem
        text = f.read_text(encoding="utf-8", errors="replace")
        if not text.startswith("---"):
            items[item_id] = (f, {})
            continue
        try:
            end = text.index("\n---", 3) + 4
        except ValueError:
            items[item_id] = (f, {})
            continue
        try:
            fm = yaml.safe_load(text[3:end - 4]) or {}
        except yaml.YAMLError as exc:
            print(f"  !! YAML parse error in {f.relative_to(ROOT)}: {exc}",
                  file=sys.stderr)
            fm = {}
        items[item_id] = (f, fm)
    return items


def check_media_path(p, base_hint=None):
    """Resolve an image/layer path against public/ and check existence."""
    if not p:
        return False
    p = str(p).lstrip("/")
    # Drawings tend to use /images/... or images/... rooted at public/
    candidates = [PUBLIC / p]
    if base_hint:
        candidates.append(PUBLIC / base_hint / p)
    return any(c.exists() for c in candidates)


def main():
    verbose = "--verbose" in sys.argv or "-v" in sys.argv

    all_items = {name: load_collection(name) for name in COLLECTIONS}
    sizes = {name: len(items) for name, items in all_items.items()}

    broken_refs = []
    bad_chapters = []
    missing_media = []
    inbound = defaultdict(lambda: defaultdict(int))
    # inbound[collection][id] = number of inbound references

    # Walk every item and validate
    for src_name, items in all_items.items():
        for src_id, (src_path, fm) in items.items():
            rel = src_path.relative_to(ROOT)

            # Chapter validation (sections only)
            if src_name == "sections":
                ch = fm.get("chapter")
                if ch and ch not in CHAPTERS:
                    bad_chapters.append((rel, ch))

            # Relation validation
            for field, target_collection in REF_FIELDS.items():
                refs = fm.get(field, []) or []
                if not isinstance(refs, list):
                    refs = [refs]
                target_ids = all_items.get(target_collection, {})
                for ref_id in refs:
                    if ref_id not in target_ids:
                        broken_refs.append((rel, field, ref_id, target_collection))
                    else:
                        inbound[target_collection][ref_id] += 1

            # Media validation
            img = fm.get("image")
            if img and not check_media_path(img):
                missing_media.append((rel, "image", img))
            for support in fm.get("supportImages", []) or []:
                src = support.get("src") if isinstance(support, dict) else None
                if src and not check_media_path(src):
                    missing_media.append((rel, "supportImages[].src", src))

            # Maps layers
            for layer in fm.get("layers", []) or []:
                if isinstance(layer, dict) and layer.get("file"):
                    lf = layer["file"]
                    if not check_media_path(lf, base_hint="data/geojson"):
                        missing_media.append((rel, "layers[].file", lf))

    # Orphans (items with 0 inbound refs); we tabulate which collections we care about
    orphan_collections = ["sources", "drawings", "terms"]
    orphans = {}
    for col in orphan_collections:
        col_orphans = []
        for item_id in all_items[col]:
            if inbound[col].get(item_id, 0) == 0:
                col_orphans.append(item_id)
        orphans[col] = col_orphans

    # --- Report ---
    print("=" * 60)
    print("CROSS-REFERENCE + MEDIA AUDIT")
    print("=" * 60)
    print()
    print("Collection sizes:")
    for name, n in sizes.items():
        print(f"  {name:10s} {n:4d}")
    print()

    print(f"Broken cross-references: {len(broken_refs)}")
    for rel, field, ref_id, target in broken_refs:
        print(f"  {rel}  [{field}] -> {target}/{ref_id}  (not found)")
    if broken_refs:
        print()

    print(f"Invalid chapter values: {len(bad_chapters)}")
    for rel, ch in bad_chapters:
        print(f"  {rel}  chapter={ch!r}")
    if bad_chapters:
        print()

    print(f"Missing media files: {len(missing_media)}")
    for rel, field, path in missing_media:
        print(f"  {rel}  [{field}] -> {path}  (not on disk)")
    if missing_media:
        print()

    total_orphans = sum(len(v) for v in orphans.values())
    print(f"Orphans (item with 0 inbound refs): {total_orphans}")
    for col, ids in orphans.items():
        if not ids:
            print(f"  {col}: 0")
            continue
        print(f"  {col}: {len(ids)}")
        if verbose or len(ids) <= 8:
            for i in ids:
                print(f"    - {i}")
        else:
            for i in ids[:5]:
                print(f"    - {i}")
            print(f"    ... and {len(ids)-5} more (use --verbose to list)")

    fail = bool(broken_refs or bad_chapters or missing_media)
    print()
    print("RESULT:", "FAIL" if fail else "PASS")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
