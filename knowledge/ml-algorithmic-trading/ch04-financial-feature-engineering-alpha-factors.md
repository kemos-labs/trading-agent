# Ch04 — Financial Feature Engineering: How to Research Alpha Factors

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 4.

## Purpose
Presents the research process for **alpha factors** — cross-sectional features that predict the cross-section of returns — and how to evaluate them rigorously before they enter a model.

## The factor research loop
1. **Idea** — a hypothesis about a return driver (momentum, reversal, value, quality, liquidity, volatility, sentiment…).
2. **Data** — panel of features × returns across a broad universe; avoid survivorship bias.
3. **Compute** — factor values per stock per period.
4. **Evaluate** — does the factor separate future winners from losers, cross-sectionally and over time?

## Alpha factor definitions
- **Momentum**: cumulative return over past horizon (1–12 months), excluding the most recent month (short-term reversal confound).
- **Mean reversion**: negative of short-horizon return.
- **Value**: book-to-market, earnings yield (E/P).
- **Quality/profitability**: ROE, gross profitability, accruals.
- **Low volatility/beta**: trailing volatility, downside beta.
- **Size & liquidity**: market cap, Amihud illiquidity, turnover.

## Evaluation methodology (the reusable core)
- **Ranking**: cross-sectionally rank stocks by factor value each period (z-score or percentile).
- **Forward returns**: align factor at *t* with returns over *t+1…t+h* (h = 1 day, 5 days, 1 month).
- **Information coefficient (IC)**: Spearman rank correlation between factor values and forward returns, computed each period, then averaged; IC ≈ 0.05 is meaningful at scale; report its t-stat and stability (hit rate of sign).
- **Quantile spreads**: bucket stocks into quantiles (e.g., deciles) by factor; long top / short bottom; a monotonic spread across quantiles indicates a real, exploitable relationship.
- **Trading simulation**: build a long-short portfolio from the factor, backtest with costs (see `walk-forward-validation`).

## Practical details
- **Winsorize** extreme factor values (clip at ~1st/99th percentile) to tame outliers; standardize (z-score) per cross-section for comparability.
- **Neutralize** unwanted exposures (industry, size, beta) by residualizing the factor via cross-sectional regression — raw factor correlations can be spurious.
- **Multiple testing**: scanning many factors inflates false discoveries; demand higher IC thresholds / use deflated-Sharpe-style corrections (see `purged-cross-validation`, `statistical-significance-testing`).
- **Decay check**: recompute the factor with a lag to confirm the signal is tradeable, not a data artifact.

## Key takeaways
- IC + quantile-spread analysis is the standard pre-ML screen: factors that fail it won't be rescued by a fancy model.
- Cross-sectional, period-by-period evaluation beats pooling everything into one correlation.
- Treat factor research as a hypothesis-testing pipeline with leakage controls — the same discipline ML models need.
