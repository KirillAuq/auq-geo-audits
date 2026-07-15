#!/usr/bin/env python3
"""Move the id="auq-case-studies" section higher on the page:
  - before the "Queries we tested" section (id="tested-queries") when present
  - otherwise right after the "AI OVERVIEW PERFORMANCE" section (older format)
Idempotent: files already in the right order are rewritten identically.
"""
import glob, os, re, sys

DIR = os.path.dirname(os.path.abspath(__file__))
MARK = '<section class="section" id="auq-case-studies">'

def move(path):
    src = open(path, encoding="utf-8").read()
    start = src.find(MARK)
    if start == -1:
        return "ERROR: no case-studies section"
    end = src.find("</section>", start)
    if end == -1:
        return "ERROR: unterminated case-studies section"
    end += len("</section>")
    block = src[start:end]
    rest = src[:start] + src[end:]

    anchor = rest.find('<section class="section" id="tested-queries">')
    how = "before tested-queries"
    if anchor == -1:
        lbl = rest.find("AI OVERVIEW PERFORMANCE")
        if lbl == -1:
            return "ERROR: no insertion anchor"
        anchor = rest.find("</section>", lbl)
        if anchor == -1:
            return "ERROR: no </section> after AI OVERVIEW PERFORMANCE"
        anchor += len("</section>")
        how = "after AI Overview Performance"

    out = rest[:anchor] + "\n" + block + "\n" + rest[anchor:]
    if out != src:
        open(path, "w", encoding="utf-8").write(out)
        return f"moved ({how})"
    return "unchanged"

def main():
    files = sorted(glob.glob(os.path.join(DIR, "*.html")))
    files = [f for f in files if os.path.basename(f) != "index.html"]
    counts, errs = {}, {}
    for f in files:
        r = move(f)
        counts[r.split(" (")[0]] = counts.get(r.split(" (")[0], 0) + 1
        if r.startswith("ERROR"):
            errs[os.path.basename(f)] = r
    print(counts)
    for k, v in errs.items():
        print(f"  {k}: {v}")
    return 1 if errs else 0

if __name__ == "__main__":
    sys.exit(main())
