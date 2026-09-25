# Alpha Factor Evaluation (IC & Quantile Spreads)

## name
Cross-sectional alpha-factor evaluation: information coefficient (IC),
quantile spreads, and the pre-ML screening discipline for factor research.

## description
A repeatable pipeline for deciding whether a predictive feature (momentum,
value, sentiment, an ML prediction, any score) actually separates future
winners from losers across a universe of assets. Computes the factor
cross-sectionally per period, aligns it with forward returns, and scores it
three ways: (1) the information coefficient (rank correlation with forward
returns), (2) quantile long-short spreads, and (3) stability/significance
over time. This is the standard screen before any factor enters a model
or strategy — a factor that fails it won't be rescued by a fancier model.

## when to use it
- You have a panel of per-asset, per-period feature values (any signal:
  alpha factor, model prediction, sentiment score, topic weight).
- You want to know if the feature predicts the cross-section of future
  returns, before building a strategy or model.
- You are comparing many candidate factors/features and need a fair,
  comparable metric (IC rank, not raw correlation).
- You need the numeric output (IC, t-stat, quantile spreads) to report
  as evidence alongside a strategy.

## the method
Input: panel indexed by (period t, asset i) with `factor` and `fwd_return`
(the return over t+1…t+h), aligned point-in-time.

1. **Clean the factor per cross-section** (each period t separately):
   - **Winsorize** extreme values: clip at ~1st/99th percentile.
   - **Standardize**: z-score within each cross-section (factor − mean) / std.
   - Optionally **neutralize** unwanted exposures (industry, size, beta)
     by cross-sectional regression and taking the residual.
2. **Compute the IC per period**: Spearman rank correlation between
   `factor` and `fwd_return` across assets at each t.
   ```python
   ic = df.groupby('period').apply(
       lambda g: g['factor'].corr(g['fwd_return'], method='spearman'))
   ```
3. **Summarize**:
   - mean IC (|IC| ≈ 0.02–0.05 is meaningful at scale),
   - t-stat = mean(IC) / (std(IC) / √n_periods),
   - hit rate = share of periods with IC of the expected sign,
   - IC autocorrelation (lower is better for independence).
4. **Quantile spreads**: bucket assets into quantiles (e.g., deciles) by
   factor each period; average forward return per bucket across time;
   check *monotonic* progression and the long-top/short-bottom spread
   (top − bottom bucket mean return).
5. **Costed sanity check**: only if IC/spreads survive, run a long-short
   simulation with transaction costs (see `walk-forward-validation`).

## known pitfalls
- **Pooling everything** into one big correlation hides time-varying
  behavior and inflates n — always compute IC period-by-period first.
- **Lookahead**: `fwd_return` must start *after* the factor's timestamp;
  features built with full-sample statistics leak the future.
- **Survivorship bias**: a factor evaluated on today's index membership
  overstates its edge — include delisted names.
- **Multiple testing**: screening many factors guarantees false positives —
  demand higher t-stat thresholds or correct (deflated Sharpe,
  see `purged-cross-validation` / `statistical-significance-testing`).
- **Skewed/outlier factors**: raw (unwinsorized) factors corrupt rank
  correlations less than Pearson, but still winsorize before ranking.
- **Sign instability**: a factor that flips sign across periods is noise;
  check the hit rate, not just the mean IC.

## source
Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed.,
Packt 2020), Chapter 4 — the alpha-factor research loop; consistent with
the factor-evaluation practice throughout the book (ch8, ch14–16).
