#!/usr/bin/env python3
"""
Canonical index generator for the auq.io/audits/ page.

Regenerates index.html (the dark, sortable/filterable AUQ audits table) from
EVERY audit report in this folder, so the full set is always represented in the
correct design. Idempotent: run it as often as you like.

    python3 build-index.py            # uses this script's folder
    python3 build-index.py <folder>   # or an explicit folder

Run this after adding new <slug>.html audit reports to the repo, then commit
index.html. Do NOT commit the audit engine's build-index.js output here — it
uses a different (older) design and only indexes one batch folder, which
collapses this page. See README-INDEX.md.
"""
import re, glob, os, sys, html, statistics
from collections import Counter

BASE = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(BASE, "index.template.html")
OUT = os.path.join(BASE, "index.html")

def band(s):
    return "Absent" if s < 26 else "Low" if s < 51 else "Competitive" if s < 76 else "Dominant"

# 1) parse every audit page (title "<Brand> GEO Audit" + numeric score)
audits = []
for path in sorted(glob.glob(os.path.join(BASE, "*.html"))):
    f = os.path.basename(path)
    if f in ("index.html", "index.template.html", "404.html"):
        continue
    h = open(path, encoding="utf-8", errors="replace").read()
    mt = re.search(r'<title>\s*([^<]*?)\s+GEO Audit', h)
    ms = re.search(r'class="big">\s*(\d+)\b', h)
    if not (mt and ms):
        continue
    slug = f[:-5]
    score = int(ms.group(1))
    brand = mt.group(1).strip()
    md = (re.search(r'>Site</span>\s*<span class="v">\s*([^<\s]+)', h)
          or re.search(r'class="k">Site</span><span class="v">([^<]+)', h))
    domain = md.group(1).strip() if md else slug
    audits.append((slug, brand, domain, score, band(score)))

if not audits:
    sys.exit("No audit pages found in " + BASE)

# initial order: score desc, then brand asc (the page's JS re-sorts on load)
audits.sort(key=lambda a: (-a[3], a[1].lower()))

def row(slug, brand, dom, score, bd):
    bl = bd.lower()
    eb, ed, es = (html.escape(x, quote=True) for x in (brand, dom, slug))
    dbrand = html.escape(brand.lower(), quote=True)
    return (f'<tr data-band="{bd}" data-brand="{dbrand}" data-domain="{ed}" data-score="{score}">'
            f'<td class="c-brand"><a href="{es}.html">{eb}</a></td>'
            f'<td class="c-domain">{ed}</td>'
            f'<td class="c-score"><span class="score s-{bl}">{score}</span></td>'
            f'<td class="c-band"><span class="pill p-{bl}">{bd}</span></td>'
            f'<td class="c-go"><a href="{es}.html" aria-label="Open the {eb} audit">Open</a></td></tr>')

rows_html = "\n" + "\n".join(row(*a) for a in audits) + "\n      "
scores = [a[3] for a in audits]
counts = Counter(a[4] for a in audits)
total = len(audits)
median = int(round(statistics.median(scores)))

repl = {
    "@@ROWS@@": rows_html,
    "@@TOTAL@@": str(total),
    "@@MEDIAN@@": str(median),
    "@@DOMINANT@@": str(counts.get("Dominant", 0)),
    "@@COMPETITIVE@@": str(counts.get("Competitive", 0)),
    "@@LOW@@": str(counts.get("Low", 0)),
    "@@ABSENT@@": str(counts.get("Absent", 0)),
    "@@HIGHEST@@": str(max(scores)),
    "@@LOWEST@@": str(min(scores)),
}

doc = open(TEMPLATE, encoding="utf-8").read()
for tok, val in repl.items():
    doc = doc.replace(tok, val)
leftover = re.findall(r'@@[A-Z]+@@', doc)
if leftover:
    sys.exit("Unfilled tokens: " + ", ".join(sorted(set(leftover))))

open(OUT, "w", encoding="utf-8").write(doc)
print(f"index.html: {total} audits | Dominant {counts.get('Dominant',0)} "
      f"Competitive {counts.get('Competitive',0)} Low {counts.get('Low',0)} "
      f"Absent {counts.get('Absent',0)} | median {median} | "
      f"high {max(scores)} low {min(scores)}")
