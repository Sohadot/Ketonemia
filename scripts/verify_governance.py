#!/usr/bin/env python3
"""Governance verification for Ketonemia.com.

Encodes the reconciliation and machine-parity invariants that keep the asset
coherent, so they are enforced automatically on every change instead of by
hand. Exits non-zero (and prints every failure) if any invariant is violated.

Invariants checked:
  1. Route-count reconciliation: sitemap.xml, data/page-index.json,
     data/reference-pack.json (canonical_pages), and the /architecture/
     JSON-LD hasPart ItemList list exactly the same set of canonical routes
     (every route except the home page "/").
  2. Source-of-truth count: that shared count equals the number declared in
     SYSTEM_ARCHITECTURE.md ("The site has N canonical routes").
  3. Every canonical route is discoverable in llms.txt.
  4. Every data/*.json file is valid JSON.
  5. Every inline JSON-LD block on every page is valid JSON.
  6. The Classification Engine's inline rules are equal (parsed) to
     data/classification-rules.json.
  7. No broken internal links: every internal route link resolves to an
     index.html, and every internal file link points to a file that exists.
  8. FAQ machine-human parity: each FAQPage acceptedAnswer text is identical
     to the corresponding visible answer text (minus its trailing link).

Run from the repository root: python3 scripts/verify_governance.py
"""

import glob
import html as htmlmod
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

failures = []


def fail(msg):
    failures.append(msg)


def ok(msg):
    print(f"  ok  {msg}")


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def iter_jsonld(html):
    for block in re.findall(
        r'<script type="application/ld\+json">(.*?)</script>', html, re.S
    ):
        yield block


def itemlist_routes(html):
    routes = set()
    for block in iter_jsonld(html):
        try:
            data = json.loads(block)
        except json.JSONDecodeError:
            continue  # validity is checked separately

        def walk(node):
            if isinstance(node, dict):
                if node.get("@type") == "ItemList":
                    for it in node.get("itemListElement", []):
                        url = it.get("url") if isinstance(it, dict) else None
                        if url:
                            m = re.search(r"ketonemia\.com(/[^\"]*)", url)
                            routes.add(m.group(1) if m else url)
                for value in node.values():
                    walk(value)
            elif isinstance(node, list):
                for value in node:
                    walk(value)

        walk(data)
    return routes


# ---- 1. Route-count reconciliation ----------------------------------------
sitemap = set(
    re.findall(r"<loc>https://ketonemia\.com(/[^<]*)</loc>", read("sitemap.xml"))
)
sitemap.discard("/")

page_index_data = json.loads(read("data/page-index.json"))
page_index = {p["url"] for p in page_index_data["pages"]}
page_index.discard("/")

reference_pack_data = json.loads(read("data/reference-pack.json"))
reference_pack = set(reference_pack_data["canonical_pages"])
reference_pack.discard("/")

architecture = itemlist_routes(read("architecture/index.html"))

lists = {
    "sitemap.xml": sitemap,
    "data/page-index.json": page_index,
    "data/reference-pack.json": reference_pack,
    "architecture ItemList": architecture,
}
base = sitemap
reconciled = True
for name, routes in lists.items():
    if routes != base:
        reconciled = False
        fail(
            f"route list '{name}' differs: "
            f"only-here={sorted(routes - base)} missing={sorted(base - routes)}"
        )
if reconciled:
    ok(f"four route lists identical at {len(base)} canonical routes")

# ---- 2. Source-of-truth count ---------------------------------------------
arch_md = read("SYSTEM_ARCHITECTURE.md")
m = re.search(r"The site has \*\*(\d+) canonical routes\*\*", arch_md)
if not m:
    fail("SYSTEM_ARCHITECTURE.md: could not find the source-of-truth route count")
else:
    declared = int(m.group(1))
    if declared != len(base):
        fail(
            f"SYSTEM_ARCHITECTURE.md declares {declared} canonical routes "
            f"but the route lists contain {len(base)}"
        )
    else:
        ok(f"SYSTEM_ARCHITECTURE.md source-of-truth count matches ({declared})")

# ---- 3. Routes discoverable in llms.txt -----------------------------------
llms = read("llms.txt")
missing_llms = sorted(r for r in base if r not in llms)
if missing_llms:
    fail(f"routes absent from llms.txt: {missing_llms}")
else:
    ok("every canonical route is present in llms.txt")

# ---- 4. data/*.json valid --------------------------------------------------
json_bad = False
for path in sorted(glob.glob("data/*.json")):
    try:
        json.loads(read(path))
    except json.JSONDecodeError as exc:
        json_bad = True
        fail(f"invalid JSON: {path}: {exc}")
if not json_bad:
    ok("all data/*.json files are valid JSON")

# ---- 5. Inline JSON-LD valid ----------------------------------------------
ld_total = 0
ld_bad = False
for path in sorted(glob.glob("**/*.html", recursive=True)):
    for block in iter_jsonld(read(path)):
        ld_total += 1
        try:
            json.loads(block)
        except json.JSONDecodeError as exc:
            ld_bad = True
            fail(f"invalid JSON-LD in {path}: {exc}")
if not ld_bad:
    ok(f"all {ld_total} inline JSON-LD blocks are valid")

# ---- 6. Classification Engine inline rules == data copy --------------------
engine = read("classification-engine/index.html")
m = re.search(
    r'<script type="application/json" id="classification-rules">(.*?)</script>',
    engine,
    re.S,
)
if not m:
    fail("classification-engine/index.html: inline classification-rules block not found")
else:
    try:
        inline_rules = json.loads(m.group(1))
        data_rules = json.loads(read("data/classification-rules.json"))
        if inline_rules != data_rules:
            fail(
                "classification-engine inline rules differ from "
                "data/classification-rules.json"
            )
        else:
            ok("classification-engine inline rules equal data/classification-rules.json")
    except json.JSONDecodeError as exc:
        fail(f"classification rules JSON error: {exc}")

# ---- 7. No broken internal links ------------------------------------------
valid_routes = {"/"}
for path in glob.glob("**/index.html", recursive=True):
    directory = os.path.dirname(path)
    route = "/" if directory == "" else "/" + directory + "/"
    valid_routes.add(route)

broken = set()
for path in glob.glob("**/*.html", recursive=True):
    for href in re.findall(r'href="(/[^"#?]*)"', read(path)):
        if re.search(r"\.\w+$", href):  # file link (has an extension)
            if not os.path.exists(href.lstrip("/")):
                broken.add((path, href))
            continue
        route = href if href.endswith("/") else href + "/"
        if route not in valid_routes:
            broken.add((path, href))
if broken:
    for src, href in sorted(broken):
        fail(f"broken internal link in {src}: {href}")
else:
    ok(f"no broken internal links ({len(valid_routes)} resolvable routes)")

# ---- 8. FAQ machine-human parity ------------------------------------------
faq_path = "faq/index.html"
if os.path.exists(faq_path):
    faq = read(faq_path)

    def clean(text):
        text = re.sub(r"<a\b[^>]*>.*?</a>", "", text, flags=re.S)  # drop trailing link
        text = re.sub(r"<[^>]+>", "", text)  # drop remaining tags
        text = htmlmod.unescape(text)
        return re.sub(r"\s+", " ", text).strip()

    visible = [
        (clean(q), clean(a))
        for q, a in re.findall(
            r'<div class="faq-item">\s*<h3 class="faq-q">(.*?)</h3>'
            r'\s*<p class="faq-a">(.*?)</p>',
            faq,
            re.S,
        )
    ]
    faq_ld = None
    for block in iter_jsonld(faq):
        data = json.loads(block)
        if data.get("@type") == "FAQPage":
            faq_ld = data
            break
    if faq_ld is None:
        fail("faq/index.html: no FAQPage JSON-LD block found")
    else:
        entities = faq_ld.get("mainEntity", [])
        if len(entities) != len(visible):
            fail(
                f"FAQ: {len(visible)} visible Q&A but "
                f"{len(entities)} in FAQPage JSON-LD"
            )
        else:
            parity = True
            for i, ((vq, va), q) in enumerate(zip(visible, entities)):
                jq = q.get("name", "").strip()
                ja = clean(q.get("acceptedAnswer", {}).get("text", ""))
                if vq != jq:
                    parity = False
                    fail(f"FAQ Q{i}: question name differs from visible heading")
                if va != ja:
                    parity = False
                    fail(f"FAQ Q{i}: acceptedAnswer text differs from visible answer")
            if parity:
                ok(f"FAQ machine-human parity holds across {len(visible)} answers")

# ---- Result ---------------------------------------------------------------
print()
if failures:
    print(f"GOVERNANCE CHECK FAILED — {len(failures)} problem(s):")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)
print("GOVERNANCE CHECK PASSED — all invariants hold.")
sys.exit(0)
