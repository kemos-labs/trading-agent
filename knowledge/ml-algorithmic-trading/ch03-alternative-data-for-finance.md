# Ch03 — Alternative Data for Finance

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 3.

## Purpose
Lays out the alternative-data (alt-data) landscape — text, images, geolocation, sensors, credit-card, web traffic, and more — with a framework for evaluating whether a dataset can actually add alpha.

## Categories of alternative data
- **Social media & text**: news (Reuters, Bloomberg), earnings-call transcripts, analyst reports, tweets, forums (Reddit), regulatory filings (SEC EDGAR).
- **Images**: satellite (crop yields, oil-tanker traffic, retail parking lots), drone, street-level.
- **Geolocation**: foot traffic at stores, mobile-device movement.
- **Sensors/industrial**: shipping (AIS vessel tracking), energy-grid activity, weather.
- **Transactions**: credit/debit-card spending (often aggregated), web-scraped prices, job postings, app rankings.
- **Surveys/crowdsourcing**: consumer-confidence and analyst-expectation aggregates.

## How alt data creates alpha
- **Leading information**: satellite crop estimates precede official yields; card spending precedes same-store sales.
- **Weak signal at scale**: aggregated micro-signals (foot traffic, sentiment) are only exploitable with ML over large volumes.
- **Less crowded**: alts are proprietary/expensive, so the edge decays more slowly than with public data — but costs and competition still erode it.

## Evaluation framework (the book's checklist)
1. **Value potential** — does it contain information about a decision-relevant variable, and can it be linked to securities (ticker mapping)?
2. **Signal-to-noise** — ratio of informative content to noise; correlated features across sources can double-count.
3. **Uniqueness** — how crowded is it; how fast does the edge decay?
4. **Novelty/timeliness** — lead time over public confirmation (lookahead avoidance: use as-of publication).
5. **Coverage & history** — breadth across the universe and enough history for validation.
6. **Provenance & compliance** — legal/regulatory constraints, licensing, privacy (GDPR), data-collection methodology.
7. **Cost/benefit** — subscription vs. capture cost vs. incremental alpha.

## Operational considerations
- **Point-in-time integrity**: alt-data timestamps often reflect *when the vendor processed* the data, not when the event happened — adjust so a live strategy would have seen it.
- **Storage/ETL**: alt data is big, messy, unstructured; build a data pipeline (see skill `data-pipelines`) with versioning and audit.
- **Integration**: combine with prices/fundamentals on a common calendar; model interaction effects (ML thrives on complementary sources).

## Key takeaways
- Evaluate alt data on value, uniqueness, and timeliness before spending on it — most datasets fail the edge test.
- Alt data's real power is *cross-sectional coverage at scale*, not single-source prediction.
- Always model the data as it would have been available at decision time; leakage is the main way alt-data backtests lie.
