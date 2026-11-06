# Generic reusable protocol: "What do LLMs say [brand] is?"

## Purpose
Replace citation-only identity prose ("answer text was not stored") with an independent, source-backed check of how major LLMs describe the brand versus the brand's own public description.

## Non-goals
- Do not mix these branded identity prompts into the Google AI Overview 38-query set.
- Do not infer answer text from AIO citation domains.
- Do not change the AIO visibility score based on this section.
- Do not invent confidence percentages.

## Inputs
1. Brand display name and primary domain.
2. Exact neutral prompt: `What does {Brand} do?` (no system message, no dossier, no examples).
3. Brand-owned baseline URLs (at minimum homepage; prefer also `/about` and `/llms.txt` if present).

## Transport (supported, documented)
Prefer DataForSEO AI Optimization **LLM Responses Live** with account Basic Auth (`DATAFORSEO_LOGIN` / `DATAFORSEO_PASSWORD` aliased as needed):
- ChatGPT: `POST /v3/ai_optimization/chat_gpt/llm_responses/live`
- Gemini: `POST /v3/ai_optimization/gemini/llm_responses/live`
- Claude: `POST /v3/ai_optimization/claude/llm_responses/live`
- Perplexity: `POST /v3/ai_optimization/perplexity/llm_responses/live`

Resolve `model_name` from each provider's Models endpoint first.
Docs hub: https://docs.dataforseo.com/v3/ai_optimization/llm_responses/overview.md/

## Sampling
- Target ≥3 distinct providers/products when credentials allow.
- Prefer 2 samples per provider; minimum 1 clearly labelled snapshot.
- Record for each call: provider, exact model id returned, UTC timestamp, web_search enabled/observed, full response text, citations/annotations/search_results, API cost, failures verbatim.

## Provider parameter gotchas (observed 2026-11-06)
- Gemini: do **not** send `web_search_country_iso_code` (returns 40501). Use `web_search: true` alone.
- Perplexity sonar-family: web search is typically on by default; still record the result flag.
- `user_prompt` max 500 characters.

## Baseline extraction
Fetch brand-owned pages in the same session. Store direct quotes with URLs and fetch date. Extract category labels, buyers, capabilities, positioning. Note slogan variants (e.g. organizational intelligence vs people ops).

## Comparison rubric (qualitative only)
For each provider sample, judge dimensions: category, buyers, capabilities, positioning, factual accuracy.
Verdict vocabulary:
- `exact_or_near_slogan` — uses the brand's lead slogan/category phrase
- `semantic_alignment` — same meaning without exact slogan
- `omission` — baseline theme absent
- `contradiction` — clear factual conflict with brand-owned claims
- `unknown` — insufficient evidence in the answer
Never output numeric confidence.

## Reporting slot
Section title: **What do LLMs say [brand] is?**
Contents: baseline quotes; per-provider snapshots; qualitative comparison; costs/limits.
Keep AIO citation stats elsewhere if still useful as instrumentation, but do not present them as the brand-identity answer.

## Safety
- Auth only via env to `api.dataforseo.com`.
- Never print/write credentials.
- Secret-scan raw JSON before sharing.
- No persistent Promptwatch monitors required for this one-off path.
