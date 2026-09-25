# Chapter 7 — Statistical Arbitrage Trading

## Core idea
Statistical arbitrage exploits persistent *disequilibria* between related
instruments rather than pure riskless mispricing. The canonical example in
this chapter is **pairs trading** built on cointegration.

## Stationarity first
- A series is (weakly) stationary if it fluctuates around a constant mean
  with constant variance and no trend.
- Stationary series *mean-revert*, which is exactly the property a stat-arb
  strategy needs: deviations from the mean eventually correct.

## Cointegration
- Two non-stationary series are **cointegrated** if a linear combination of
  them is stationary: `spread_t = y_t - beta·x_t ~ I(0)`.
- Unlike correlation (a contemporaneous statistic), cointegration is a
  *long-run equilibrium* property: the pair can drift apart temporarily but
  the spread reverts.
- **Engle-Granger approach**: regress `y` on `x` to get `beta`, then test the
  residual spread for stationarity (ADF test). The regression beta is the
  hedge ratio.
- Riskless tri-currency arbitrage example (NZD/AUD → AUD/CAD → NZD/CAD) shows
  the pure-arbitrage ideal; pairs trading is the statistical, less-than-riskless
  version that survives in practice.

## Pairs trading strategy
1. Estimate the hedge ratio `beta` and the spread on a training window.
2. Standardize the spread (z-score with rolling mean/std).
3. Trade the spread: short the spread when z is high, long when z is low
   (mean reversion), exit when z returns to ~0.
4. Position: long `y`, short `beta·x` (or vice versa) so the portfolio P&L is
   driven by the spread, not the market.

## Pitfalls
- Cointegration can **break** (regime change); re-test periodically.
- High transaction costs on two legs can kill the edge — include spread/fees.
- Overfitting the hedge ratio on a short window; use a long, stable sample.
- Correlation ≠ cointegration: two correlated random walks are not
  cointegrated and will not mean-revert.

## Bottom line
This is the book's link to the knowledge base's existing
`skills/cointegration-testing` and `skills/kalman-filter-pairs` skills:
stationarity → cointegration → hedge ratio → spread z-score → mean-reverting
trade. The chapter confirms the same pipeline at a practitioner level.
