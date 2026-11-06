# ChartHop GEO audit notes

Score 34 of 100, Low band. Domain charthop.com. Run 52feda2902cf8791. Completed 2026-11-06T17:07:09.649Z.

Measurement archive SHA256 8c649bff859bc366c98207a0e4a81ef7b9a8f6bb033da71090b1b0db466763c2. Report HTML SHA256 1fb0884b6fc859e7fbc1c6a7493344400d45ec27240c70a663742f91f6c85acb. Canonical JSON SHA256 7157dbeff5ad492d44a65549c9cb05eef06812fb70befdfff43f6e4643fb7125.

This run did not call DataForSEO again. Geo-audit-handover was not committed, pushed, or opened as a pull request. No index.html was written.

## What was measured

Google AI Overviews, United States, English, desktop. 38 queries, 2 standard reads each, 76 reads. Live reads 0. Trigger rate 100%. Errors 0 of 38. Recorded cost 0.1824 USD.

Buckets: owned 3, mentioned and not cited 14, invisible 21.

Query set: 35 category queries from five roots (people analytics, headcount planning, workforce planning, organizational intelligence, HRIS) plus three comparison queries (alternatives to ChartHop, ChartHop vs BambooHR, ChartHop vs HiBob). No branded queries were run. Seeds BambooHR and HiBob come from public compare pages on charthop.com.

## Score formula

Source is normalize_aio.js. pctRound is Math.round of 100 times the ratio.

- Your pages being quoted, weight 35: round(100 x 3 / 38) = 8.
- Inclusion in category answers, weight 25: round(100 x (3 + 14) / 38) = 45.
- Identity accuracy, weight 20: round(100 x 5 / 6) = 83. A theme is present if any query cites the domain or names the brand.
- Topic coverage breadth, weight 20: round(100 x 1 / 6) = 17. A theme is strong when owned is at least as large as mentioned and invisible, and owned is greater than 0.

Overall is round(0.35 x 8 + 0.25 x 45 + 0.20 x 83 + 0.20 x 17) = round(34.05) = 34. Bands: 0 to 25 Absent, 26 to 50 Low, 51 to 75 Competitive, 76 to 100 Dominant.

Six theme groups enter the score. Five are the category roots. The sixth is the comparison queries, grouped under the brand name. That comparison group is the only strong group (2 owned, 1 mentioned).

Identity 83 and the coverage table use different rules. The coverage table uses plurality. Organizational intelligence is cited on 1 of 7 and still shows Invisible. Workforce planning is named on 1 of 7 and still shows Invisible. Both still count as present for the identity component. Breadth 17 is the comparison group, not a category.

## Citation facts

Owned queries, source-list order:

- organizational intelligence platform: charthop.com is place 6 of 11. The report table prints the first three domains, so that row omits charthop.com. Those three are lumina.express, phdata.io, wizpresso.com.
- ChartHop vs BambooHR: place 2 of 7. Visible top three: google.com, charthop.com, getguru.com.
- ChartHop vs HiBob: place 3 of 6. Visible top three: google.com, marketplace.workology.com, charthop.com. en.wikipedia.org is also in that list.

alternatives to ChartHop is named and not cited. Stored domains on that list include google.com, webcatalog.io, gartner.com, orgplease.com.

Theme counts:

- people analytics: named on 6 of 7, cited on 0.
- headcount planning: named on 6 of 7, cited on 0.
- workforce planning: cited on 0 of 7, named on 1.
- organizational intelligence: cited on 1 of 7. That query is organizational intelligence platform. This is the homepage title category.
- HRIS: cited on 0 of 7, named on 0.

google.com is on all 38 citation lists. The peer table drops queries where charthop.com is already a source, so google.com shows 35 there. It is not treated as the category winner. workday.com is on 8 queries, none of them owned.

The only quotation in the report is the fetched homepage title: ChartHop | Organizational intelligence for people analytics, headcount planning and HCM. Answer text was not stored. No AI wording was inferred from domains.

Case-study figures on the page (Fraud.net, Microblink, AKOOL, DeepInfra) are other AUQ clients. They were not measured for ChartHop. Success targets were left empty. No search volume and no share of voice were measured.

The visible component label for the 20% identity term is Identity accuracy, matching the method name. The engine JSON key still stores that same 83.

## Findings

1. charthop.com is a cited source on 3 of 38 AI answers. It is named and not cited on 14, and absent on 21.
2. Organizational intelligence is the homepage title and is cited on 1 of 7 queries. People analytics is named on 6 of 7 and cited on 0.
3. ChartHop vs BambooHR and ChartHop vs HiBob cite charthop.com. alternatives to ChartHop names the brand and does not cite the domain.

## Checks

verify.js: OK, trigger 100%, errors 0/38.
check-reports.js: clean. Google Tag Manager GTM-NCFX8NJ is in the file.
Visual check: desktop 1280 px full page and mobile 390 px full page. Score 34, Low band, and the three component values render. On a phone the query table keeps the status column readable and the source column can be scrolled sideways.

## Publish, for a later destination agent

Repository: https://github.com/KirillAuq/auq-geo-audits
Branch: master
Add charthop.html at the repository root. Do not replace index.html. Insert one card into the existing catalogue: ChartHop, charthop.com, score 34, Low band, link charthop.html. The HTML already contains GTM-NCFX8NJ. Do not commit anything in Geo-audit-handover. Do not send credentials. Confirm charthop.html is absent before adding. Skip GitHub code search if it returns 429.

## Salebot handoff

At a glance, ChartHop scored 34/100. The domain is a cited source on 3 of 38 AI Overviews, named but not cited on 14, and absent on 21.

The homepage title leads with organizational intelligence, and that theme is cited on 1 of 7 queries. People analytics is named on 6 of 7 and cited on none. ChartHop vs BambooHR and ChartHop vs HiBob already cite charthop.com. No branded queries were in the AI Overview set. AI Overview answer text was not stored, so the score does not quote AI Overview wording.

A later identity check, stored under evidence/charthop/identity-test/, asked the exact prompt “What does ChartHop do?” eight times. Those API answers are quoted in the report section “What do LLMs say ChartHop is?” They are not AI Overview text and they do not change the score of 34.

## Added identity test, 2026-11-06

The identity section that said “Citation record only” and “Answer text was not stored” was replaced after a separate measurement. The AI Overview score, the 38-query counts, and the component scores 8, 45, 83, and 17 were not recalculated.

Prompt, with no system message and no brand baseline: What does ChartHop do?

Transport: DataForSEO AI Optimization LLM Responses Live. Two calls each for ChatGPT, Gemini, Claude, and Perplexity. Web search was on in every returned result. ChatGPT, Claude, and Gemini requests set web_search to true. The Perplexity sonar-pro request did not send that field. These are API model snapshots, not consumer-app screenshots.

Returned model ids: gpt-5.4-mini-2026-03-17, gemini-2.5-flash, claude-sonnet-4-5-20250929, sonar-pro. Timestamps are in the raw JSON. Reported API costs sum to 0.2296 USD.

The run notes say the first Gemini attempts failed on the field web_search_country_iso_code. The two Gemini answers in the report are the later calls that sent web_search true only.

Brand pages fetched the same day, and not given to the models: homepage and About lead with organizational intelligence; llms.txt leads with an AI-powered people operations platform and says to lead with AI-powered people analytics and headcount planning.

No wrong-industry contradiction was detected in the eight answers. That is not a verification of every product claim. No numeric confidence was assigned.

Supplied archive SHA256 e318234df08cd6b2ccdceb1f1487ab63dd3e8450894ddac19762934cc08b946e. The copy of that archive is identity-test-source.tgz. Extracted files rewrite local filesystem paths to relative names. Raw response JSON was scanned before commit; no credentials were found. The public HTML does not contain local filesystem paths.
