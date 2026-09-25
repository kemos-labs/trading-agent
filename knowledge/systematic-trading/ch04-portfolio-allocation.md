# Ch04 — Portfolio Allocation

**Source:** Carver, *Systematic Trading*, Chapter 4. (Semi-automatic traders
can skip.)

## The problem
Allocating capital between instruments (instrument weights) and between
trading rules (forecast weights). Portfolio weights can be over-fitted just
like rules — optimised weights look great in back-test, fail live, and are
usually extreme (all-in on a few assets).

## Why classic (Markowitz) optimisation goes bad
- Inputs: expected returns, stdevs, correlations. Optimisers treat estimated
  means/correlations as if precisely known.
- Demo: 3 assets (NASDAQ, S&P 500, 20-yr US bond), 1999–2014, vol-
  standardised returns, single-period optimisation each year on all past data:
  all-in NASDAQ at the tech peak → NASDAQ dumped, then ~100% bonds, ending
  68% bonds / 32% S&P / 0% NASDAQ. Extreme and unstable weights.
- Key insight: **not all statistical estimates are created equal**. 15 years
  of data cannot distinguish the three assets' Sharpe ratios (their SR
  distributions overlap), but *can* distinguish correlations (equities ~0.9
  correlated; bonds near-zero with both). The optimiser only sees the point
  estimates, not their uncertainty — so it reacts to insignificant SR noise.
- When equal weights are justified: same expected vol (always true after
  volatility standardisation), same SR, same correlation. When SRs differ
  significantly → up-weight high SR; when correlations differ → up-weight
  diversifiers.

## Saving optimisation from itself
- **Bootstrapping**: repeat the optimisation on many historical sub-periods,
  average the resulting weights. Justification: past is a guide but we don't
  know which part will repeat, so weight all periods equally. Noisy
  differences → average approaches equal weights; real differences → similar
  portfolios recur and the average reflects them. Result: stable, spread-out
  weights (53% bonds / 27% S&P / 20% NASDAQ vs single-period's 68/32/0).
  Labour-intensive (needs custom code or spreadsheet black belt).

## Handcrafting: making weights by hand
Bottom-up: form groups of similar (highly-correlated) assets; within and
between groups use a fixed table of optimal weights (derived from bootstrap
experiments on artificial data). Assumes equal vol (free after
standardisation) and, initially, equal SR.
- **Group weight table (Table 8)**: 1 asset → 100%; 2 assets → 50/50; n assets
  with identical correlations → equal weights; 3 assets use correlation
  triples (e.g. (0,0.5,0): 30/40/30; (0,0.9,0): 27/46/27; (0.5,0,0.5):
  37/26/37; (0,0.5,0.9): 45/45/10; (0.9,0,0.9): 39/22/39; (0.5,0.9,0.5):
  29/42/29; (0.9,0.5,0.9): 42/16/42). Round correlations; floor negatives at
  zero.
- Portfolio weight of each asset = product of its weights at every grouping
  level. E.g. 16 assets (UK/US banks+retailers, UK/US bonds) grouped
  sector→country→asset class: bonds get 50/50 at the top level, so each UK
  bond ends ~12.5% vs equal-weight 6.25% — diversifiers get more, matching
  the bootstrap answer in seconds with no computing.
- **Are we cheating?** Handcrafting is in-sample (weights use all history),
  so back-tested SR is mildly overstated — but far less than single-period
  optimisation. In-sample handcrafting vs rolling bootstrap on Carver's ch15
  system: SR 0.54 vs 0.52 (insignificant), while in-sample single-period
  gave 0.84 and *out-of-sample* single-period dropped to 0.30.

## Incorporating Sharpe ratios into handcrafted weights
Adjust within a group using relative SR difference vs group average:
- Column A (SR known with certainty, e.g. costs): −0.5 diff → ×0.32,
  0.5 diff → ×1.83 (aggressive).
- Column B (uncertain SR, >10 yrs data or forecast): −0.5 → ×0.65, +0.5 →
  ×1.35.
- Column C (<10 yrs data): **no adjustment at all** (SR estimates are
  statistically meaningless).
Procedure: start weights → estimate SRs → compute each asset's difference
from group average → look up multiplier → multiply → normalise to 100% →
repeat at higher grouping levels using group-level SR estimates. Example:
equities group NASDAQ 50/S&P 50 with SRs 0 and 0.5 (avg 0.25, ±0.25) → ×0.85
/ ×1.15 → 42/58; then bonds vs equities 50/50 with SRs 0.75 vs 0.25 (avg
0.5) → ×1.15/×0.85 → 58/42. Final: 18% NASDAQ, 24% S&P, 58% bonds — same
direction as bootstrap, nowhere near single-period's extremes.

## Realism table (Table 14): % of back-tested SR to trust
- Single-period optimisation, in-sample: 25%. Out-of-sample: 75%.
- Bootstrapping, in-sample: 60%; out-of-sample: 75%.
- Handcrafted, no SR, in-sample: 70%; handcrafted with SR, in-sample: 65%.
(Assumes ~25% of past performance came from unrepeatable secular trends.)

## Notes
- Volatility standardisation is what makes this simple: equal-vol returns mean
  only SRs and correlations are needed, and negative weights are impossible
  (can't short rules) so weights live in [0,1].
- Recurring discipline: prefer stable, diversified, hand-built weights over
  mathematically "optimal" but unstable ones.
