# Keeping `index.html` correct (auq.io/audits/)

`index.html` is the public audits page: the dark, sortable/filterable AUQ table
of **every** audit in this repo. It is **generated** — do not hand-edit it.

## After adding audit reports

Drop the new `<slug>.html` report(s) into this folder, then regenerate:

```bash
python3 build-index.py
git add -A && git commit -m "Add audits + rebuild index" && git push
```

`build-index.py` reads every `*.html` audit in the folder and rewrites
`index.html` from `index.template.html`, filling in the rows and all counts
(total, band pills, stat cards, median, high/low). It is idempotent — safe to
run any time.

## Do NOT commit the audit engine's index here

The GEO-audit engine / handover skill produces its own `index.html` via
`scripts/build-index.js`. That file is a **different, older design** (a light
card grid) and it only lists the reports in one batch output folder. If that
file is committed here it **replaces the full table and collapses the page to a
single batch** (this has happened — see commits `6135681`, `b438613`).

So: generate the engine's reports wherever you like, copy the `<slug>.html`
report files into this repo, and build the index **here** with
`python3 build-index.py`. Never copy the engine's `index.html` into this repo.

## Files

| File | Role |
|---|---|
| `index.html` | Generated output — the live page. Do not hand-edit. |
| `index.template.html` | The page shell with `@@TOKENS@@` for the dynamic values. |
| `build-index.py` | The generator. `python3 build-index.py [folder]`. |
