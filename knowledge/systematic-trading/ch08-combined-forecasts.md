# Ch08 — Combined Forecasts

**Source:** Carver, *Systematic Trading*, Chapter 8. (Staunch systems traders
only.)

## Combining forecasts with weights
Multiple rules disagree (e.g. EWMAC bullish +15 on crude, Carry bearish −10)
→ need one **combined forecast** per instrument: a weighted average with
**forecast weights** (positive, sum to 100%). 50/50 on +15 and −10 → combined
+2.5.

## Choosing forecast weights = portfolio allocation (ch4 tools)
Use handcrafting (or bootstrapping): need rule *correlations* + grouping.
Typical correlations (appendix C): variations of the same rule ~0.7–0.9;
different rules within the same style ~0.5; different styles within one
instrument ~0.25. Group within rules first, then across rules.
Example: EWMAC variations (lookbacks 16/64 correlated 0.7 → weights 42% each,
middle variation 16%; row 11 of table 8), then 50/50 EWMAC vs Carry →
final weights 21/8/21/50. Note: this basic version ignores performance
differences, costs, and per-instrument weights — ch12 and the part-four
example fix that.

## Getting to 10: the forecast diversification multiplier
Individual forecasts have expected |forecast| = 10, but combining
less-than-perfectly-correlated forecasts shrinks variability (same effect as
portfolio diversification: two 10%-vol stocks, 50/50, ρ=0.5 → portfolio vol
8.66%). The framework needs combined forecasts with expected |value| = 10
again, so multiply by a **diversification multiplier** = target vol ÷ natural
portfolio vol (ρ=0.5 → 10/8.66 = 1.15; ρ=0 → 10/7.07 = 1.44). Negative
correlations → dangerously large multipliers: **floor estimated correlations
at zero**. Rule-of-thumb table 18 (n assets × avg ρ): 4 assets at avg ρ 0.5
→ 1.27 (precise formula: 1.31). **Cap the multiplier at 2.5** — bigger means
capped forecasts most of the time, i.e. a de-facto binary rule.

## Cap combined forecasts at ±20
Even with forecasts ≤ ±20, a multiplier >1 can push combined above 20 (two
+16 forecasts, 50/50, multiplier 1.5 → 24). All the individual-forecast
capping reasons apply: cap combined forecasts to |20|.

## Pipeline summary
Per instrument: (1) one forecast per rule variation (expected |·| = 10,
capped ±20); (2) forecast weights (positive, sum 100%); (3) raw combined =
weighted average; (4) diversification multiplier (≥1, ≤2.5, from correlations
or appendix C tables) → rescaled combined; (5) cap rescaled combined at ±20.

## Notes
- This is the first place diversification explicitly *costs* scale: more
  diversifying rules need a bigger multiplier to keep the system's risk
  calibrated — the "volatility standardisation" invariant is maintained all
  the way through the pipeline.
- Next: the combined forecast feeds position sizing; first you must decide
  the **volatility target** (how much to risk).
