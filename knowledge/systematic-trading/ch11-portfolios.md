# Ch11 — Portfolios

**Source:** Carver, *Systematic Trading*, Chapter 11. (Combining trading
subsystems into a full system.)

## Portfolios & instrument weights
Diversification is the only free lunch (doubles SR across asset classes), yet
amateurs hold <5 shares and traders stick to 1–2 markets. Each instrument gets
a **trading subsystem**; capital is shared across subsystems with
**instrument weights** (positive, sum to 100%). Portfolio instrument position
= subsystem position × weight (× diversification multiplier — see below).

## Instrument weights: asset allocators & systems traders
All subsystems are vol-standardised, so the ch4 handcrafting (or bootstrap)
method applies directly.
- **Correlations needed**: between *subsystem returns*, not instrument
  returns. Rule of thumb: dynamic systems — multiply instrument-return
  correlations (appendix C tables 50–55) by **0.7**; static asset allocators
  — use them unadjusted (×1.0).
- Don't adjust instrument weights for Sharpe ratios — rarely enough evidence
  of different subsystem performance (costs are the exception, ch12).
- Example (S&P 500, NASDAQ, 20-yr bond): group bonds (100%) + equities
  (50/50) → 50/25/25 weights.

## Instrument weights: semi-automatic traders
Opportunistic, changing instruments → allocate **equally** across a
**maximum** number of concurrent bets: weight = 100% ÷ max bets (10 bets →
10% each). Keep max ≤ 2.5 × expected average bets (risk control, below).

## Instrument diversification multiplier
Diversified subsystems have lower portfolio risk than the average member →
need a multiplier to restore the target. Same mechanics as the forecast
diversification multiplier (ch8): use subsystem correlations + appendix-D
formula or table 18 approximation (n subsystems × avg correlation). Example:
bond/equity corr 0.1→0.07, S&P/NASDAQ 0.75→0.53 after ×0.7; avg ~0.25 → 3
assets → multiplier 1.41. Semi-automatic: multiplier = max bets ÷ average
bets (5/4 = 1.25). **Cap at 2.5** — correlations jump in crises (2008) and
the multiplier would otherwise be dangerously high.

## Portfolio of positions and trades (worked example, €100k target)
Per subsystem (ch10 chain): e.g. US 20-yr bond — price vol 0.52%, block value
$1,500 → instrument currency vol $780 → ×0.88 USD/EUR = €686; daily target
€6,250 → scalar 9.11; forecast +10 → subsystem position 9.11. S&P: 7.43 ×
(−10)/10 = −7.43; NASDAQ: 9.28 × (−15)/10 = −13.9.
Portfolio position = subsystem × weight × multiplier: bond 9.11×0.5×1.41 =
6.42 → round to 6; S&P −7.43×0.25×1.41 = −2.62 → −3; NASDAQ −13.9×0.25×1.41
= −4.91 → −5.
Trades = rounded target − current position (bond: buy 2; S&P: sell 1; NASDAQ:
none). **Position inertia**: don't trade if current position is within 10% of
the rounded target — avoids tiny costly round trips (133.48 vs 133.52:
0.75% apart → no trade). Research: inertia barely affects pre-cost
performance, so it's pure cost savings.

## Summary pipeline
subsystem position (ch10) × instrument weight × instrument diversification
multiplier → portfolio instrument position → round → compare to current with
10% inertia → trade size.

## Notes
- This completes the framework: forecast → combined forecast → position →
  portfolio — every step deterministic arithmetic on vol-standardised
  quantities; only rounding enters at the very end.
- The framework is now complete for all three trader archetypes; ch12 handles
  the cross-cutting realities of speed (costs) and size (account).
