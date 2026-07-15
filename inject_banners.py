#!/usr/bin/env python3
"""Inject conversion banners into all audit pages:
  A) "Work with AUQ" execution banner after the Executive Summary section
  B) Case-studies section (4 cards + CTA) right before the footer
Idempotent: skips files already containing id="auq-work-banner".
"""
import glob, html as htmllib, os, re, sys

DIR = os.path.dirname(os.path.abspath(__file__))

STYLE = """
<style>
  .auq-banner { background: var(--c-dark); border-radius: var(--r-comfort); padding: 40px 44px; position: relative; overflow: hidden; display: flex; align-items: center; justify-content: space-between; gap: 32px; flex-wrap: wrap; box-shadow: var(--shadow-lg); }
  .auq-banner::before { content: ""; position: absolute; width: 480px; height: 480px; top: -160px; right: -120px; background: radial-gradient(circle at 40% 40%, rgba(239, 44, 193, 0.28) 0%, transparent 60%), radial-gradient(circle at 70% 70%, rgba(189, 187, 255, 0.30) 0%, transparent 65%); border-radius: 50%; filter: blur(70px); pointer-events: none; }
  .auq-banner .txt { position: relative; z-index: 1; max-width: 640px; display: flex; flex-direction: column; gap: 10px; }
  .auq-banner .txt .mono-label { color: var(--c-muted-dark); }
  .auq-banner h3 { color: var(--c-text-dark); font-size: 26px; letter-spacing: -0.4px; line-height: 1.15; margin: 0; }
  .auq-banner p { color: rgba(255,255,255,0.75); font-size: 15px; line-height: 1.5; margin: 0; }
  .auq-banner .act { position: relative; z-index: 1; display: flex; flex-direction: column; align-items: flex-start; gap: 10px; }
  .auq-banner .btn-light { display: inline-flex; align-items: center; gap: 8px; background: var(--c-text-dark); color: var(--c-dark); padding: 12px 22px; border-radius: var(--r-sharp); font-size: 14px; letter-spacing: -0.14px; font-weight: 500; text-decoration: none; transition: transform 0.15s ease; white-space: nowrap; }
  .auq-banner .btn-light:hover { transform: translateY(-1px); }
  .auq-banner .terms { font-family: var(--f-mono); font-size: 11px; text-transform: uppercase; letter-spacing: 0.10em; color: var(--c-muted-dark); }
  .cases-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 16px; }
  a.case-card { display: flex; flex-direction: column; gap: 10px; background: var(--c-bg); border: 1px solid var(--c-border-light); border-radius: var(--r-comfort); padding: 26px; box-shadow: var(--shadow); text-decoration: none; color: var(--c-text); transition: transform 0.15s ease, box-shadow 0.15s ease; }
  a.case-card:hover { transform: translateY(-2px); box-shadow: var(--shadow-lg); }
  a.case-card .metric { font-size: 34px; font-weight: 500; line-height: 1.0; letter-spacing: -1.0px; background: linear-gradient(135deg, var(--c-magenta), var(--c-lavender)); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; }
  a.case-card .client { font-size: 16px; font-weight: 500; letter-spacing: -0.16px; }
  a.case-card .what { font-size: 14px; line-height: 1.45; letter-spacing: -0.14px; color: var(--c-muted-light); flex: 1; }
  a.case-card .link { font-family: var(--f-mono); font-size: 11px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.10em; color: #5a55c9; }
  .cases-cta { margin-top: 32px; display: flex; align-items: center; gap: 20px; flex-wrap: wrap; }
  .cases-cta .all-link { font-size: 14px; letter-spacing: -0.14px; color: var(--c-text); text-decoration: underline; text-underline-offset: 3px; }
  .cases-cta .all-link:hover { opacity: 0.6; }
</style>
"""

BANNER_A = STYLE + """
<section class="section" id="auq-work-banner"><div class="container">
  <div class="auq-banner">
    <div class="txt">
      <span class="mono-label">Work with AUQ</span>
      <h3>We don't hand you a report and walk away. We execute it.</h3>
      <p>AUQ is an execution team, not a consultancy. We ship the fixes, content, and citations this audit calls for &mdash; and we work month-to-month, so we re-earn the engagement every 30 days.</p>
    </div>
    <div class="act">
      <a class="btn-light" href="https://auq.io/contact-us/">Start with a month &rarr;</a>
      <span class="terms">No long-term contracts</span>
    </div>
  </div>
</div></section>
"""

BANNER_B = """
<section class="section" id="auq-case-studies"><div class="container">
  <div class="section-head">
    <span class="mono-label">Case Studies</span>
    <h2>This playbook has already worked. Here's the proof.</h2>
    <p class="lede">Executed by AUQ for B2B SaaS teams with the same gaps this audit found.</p>
  </div>
  <div class="cases-grid">
    <a class="case-card" href="https://auq.io/case-studies/fraud-net-content-automation-for-geo/">
      <span class="metric">1,000+</span>
      <span class="client">Fraud.net</span>
      <span class="what">AI citations earned in 6 months through GEO prompt research and content automation.</span>
      <span class="link">Read the case study &rarr;</span>
    </a>
    <a class="case-card" href="https://auq.io/case-studies/microblink/">
      <span class="metric">+173%</span>
      <span class="client">Microblink</span>
      <span class="what">Organic traffic growth from technical SEO, content automation, and GEO-focused linkbuilding.</span>
      <span class="link">Read the case study &rarr;</span>
    </a>
    <a class="case-card" href="https://auq.io/case-studies/akool-seo-for-ai-video-tools/">
      <span class="metric">+30,000</span>
      <span class="client">AKOOL</span>
      <span class="what">Visits in 6 months via technical optimizations and content strategy we executed end-to-end.</span>
      <span class="link">Read the case study &rarr;</span>
    </a>
    <a class="case-card" href="https://auq.io/case-studies/deepinfra/">
      <span class="metric">+200%</span>
      <span class="client">DeepInfra</span>
      <span class="what">Technical blog traffic growth from a blog redesign, author training, and SaaS linkbuilding.</span>
      <span class="link">Read the case study &rarr;</span>
    </a>
  </div>
  <div class="cases-cta">
    <a class="btn-cta" href="https://auq.io/contact-us/">Get results like these for {BRAND} &rarr;</a>
    <a class="all-link" href="https://auq.io/cases/">See all case studies</a>
  </div>
</div></section>
"""

def inject(path):
    src = open(path, encoding="utf-8").read()
    if 'id="auq-work-banner"' in src:
        return "skip (already injected)"
    m = re.search(r"<title>(.*?) GEO Audit", src)
    brand = htmllib.escape(m.group(1).strip()) if m else "your brand"

    # A: after the Executive Summary section's closing </section>
    lbl = src.find("EXECUTIVE SUMMARY")
    if lbl == -1:
        return "ERROR: no Executive Summary anchor"
    close = src.find("</section>", lbl)
    if close == -1:
        return "ERROR: no </section> after Executive Summary"
    close += len("</section>")
    src = src[:close] + BANNER_A + src[close:]

    # B: before the footer
    foot = src.rfind("<footer")
    if foot == -1:
        return "ERROR: no <footer>"
    src = src[:foot] + BANNER_B.replace("{BRAND}", brand) + src[foot:]

    open(path, "w", encoding="utf-8").write(src)
    return f"ok (brand: {brand})"

def main():
    files = sorted(glob.glob(os.path.join(DIR, "*.html")))
    files = [f for f in files if os.path.basename(f) != "index.html"]
    results = {}
    for f in files:
        results[os.path.basename(f)] = inject(f)
    ok = sum(1 for v in results.values() if v.startswith("ok"))
    skip = sum(1 for v in results.values() if v.startswith("skip"))
    err = {k: v for k, v in results.items() if v.startswith("ERROR")}
    print(f"injected: {ok}, skipped: {skip}, errors: {len(err)}")
    for k, v in err.items():
        print(f"  {k}: {v}")
    return 1 if err else 0

if __name__ == "__main__":
    sys.exit(main())
