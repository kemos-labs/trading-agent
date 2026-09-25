# Ch12 — Speed and Size

**Source:** Carver, *Systematic Trading*, Chapter 12.

## Speed of trading
Trade fast enough to earn, not so fast costs eat the edge. Example: pre-cost
SR 1.5 paying ⅔ of profits in costs → after-cost SR 0.5 (at a 20% target:
30% pre-cost → 20% costs → 10% net); if real SR <1.0 it loses money.
Overtrading = overconfidence.

## Calculating trading costs
- **Execution cost**: back-tests assume mid-price; small traders pay at most
  **half the spread** (Euro Stoxx: 0.5 points ≈ €5, 0.015% of price). Large
  traders (order > inside depth) pay more (a 5,000-lot sell averaged 3,365.2
  vs mid 3,369.5 → 4.3 points; splitting risks drift).
- **Cost types**: execution, per-ticket fees (£5–15), per-unit fees (€3/
  contract), percentage fees (UK stamp duty 0.5%); holding costs ignored
  for speed decisions.
- **Standardised cost** = (2 × cost per block) ÷ (16 × instrument currency
  volatility) — the annualised SR lost per round trip, vol-standardised so
  comparable across instruments (Euro Stoxx 0.002; FTSE spread bet 0.01;
  low-vol bond ETF 0.08 SR). Implication: **low-vol instruments are
  effectively more expensive** (another reason to exclude them).

## Turnover
**Turnover** = round trips per year (1 = 12-month holding; 52 = 1 week).
Cost in SR/yr = standardised cost × turnover (0.01 × 10 = 0.10 SR).
Sources in order: (1) forecast changes; (2) price-vol/ICV changes; (3)
capital changes from P&L; (4) FX changes (small); (5) system parameters
(eliminate by not meddling). Estimate via back-test (blocks traded/yr ÷ 2 ×
avg absolute blocks held) or rule of thumb.

## Using costs to make design decisions
- **Speed limit**: never pay more than ⅓ of a *conservative* pre-cost SR in
  costs. Staunch: max 0.40 SR/instrument → max 0.13 SR/yr. Semi-auto &
  asset allocators: max 0.25 SR → max 0.08 SR/yr. Day trading needs
  standardised cost ≤ 0.00025 — only with negative execution costs ⇒ almost
  nobody.
- **Which instruments**: tables 34–35 map holding period to affordable
  instruments (3-day → cheapest futures; 1 month → nearly all futures; 6.5
  weeks → index spread bets; 6 months → cheapest ETFs; 2.5 yr → individual
  equities). Carver's recommended rule set → turnover 12.5 ⇒ max cost 0.01
  SR (nearly all futures, index spread bets).
- **Stops (semi-automatic)**: holding period ∝ stop tightness; stops must
  fit the instrument's cost (spread bets need ≥ ~6-week holding; the intro's
  "1 week, £1/point" system needed 83% pre-cost returns to break even).
- **Rule selection**: reject variations too expensive for the instrument
  (turnover > 130 on cheapest futures, >65 on Euro Stoxx, >13 on spread
  bets); drop fast rules to the most expensive instrument.
- **Forecast weights**: assume equal pre-cost SR across rules (no faster-
  rule advantage) and adjust for cost differences via ch4 table 12 column A
  (costs are predictable); within the speed limit adjustments are tiny.
- **Risk percentage**: use after-cost SR.
- **Slower volatility estimation**: updating the vol estimate is the #2
  turnover source. Table 36: with slow rules a 20-week look-back cuts
  turnover (asset allocator no-rule: 1.6 → 0.4, cost 0.13 → 0.032 SR) —
  but >20 weeks hurts performance. Fast rules: keep 5 weeks. Semi-auto:
  adjust existing vol estimates only if changed >25%.
- **Instrument weights**: expensive instruments perform no worse after
  costs if traded slowly; slower traders need no cost adjustment (assume
  equal post-cost SR; handcrafted weights stand).

## Trading with more or less capital
- **Too much capital**: the half-spread assumption fails when orders
  exceed inside depth — market orders eat the book, limit orders risk
  front-running, splitting is slow & uncertain. Needs serious execution
  research.
- **Too little capital**: minimum block sizes make risk lumpy (€40k at 50%
  target → S&P max position 1.05 → always 1 contract). **Maximum possible
  position** = 2 × volatility scalar × instrument weight × diversification
  multiplier (forecast ±20); asset allocators use 1 × (forecast +10). If
  max < 4 blocks: increase weight, cut portfolio size, or drop the
  instrument.

## Determining overall portfolio size
Hold the most diversified portfolio consistent with max-position feasibility:
at least one instrument per major asset class, none with max position < 4
blocks; add within a class only if no max-position problem appears. Semi-
auto: shrink the max number of bets or skip instruments.

## Summary
- **Standardised cost** = 2C/(16×ICV) SR per round trip; subsystem cost =
  turnover × standardised cost.
- **Speed limit**: ≤0.13 SR/yr (staunch) or ≤0.08 SR/yr (others).
- Levers: instrument selection, stop width, rule pruning, forecast weights,
  vol look-back, instrument weights, after-cost SR; portfolio diversified
  subject to max-position ≥ 4 blocks.

## Notes
- Cost in SR units lets costs, turnover, and performance speak the same
  risk-adjusted language as the rest of the framework; speed limits + max
  positions constrain instrument count and rule speed.
