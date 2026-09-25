# Ch08 — Feature Importance

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 8.

## Purpose
Makes the case that feature importance — not backtesting — is the
proper research tool, and presents the main importance measures
(MDI, MDA, SFI) plus how to deal with substitution effects via
orthogonalization.

## "Backtesting is not a research tool. Feature importance is."
- Repeatedly backtesting the same data until a nice result appears is
  multiple testing → false discovery (ASA calls it fraud). ~20 trials
  at 5% significance suffice to find a false strategy.
- Feature importance is computed *ex-ante*, before simulating
  performance, and tells you *why* a pattern exists — it opens the
  black box. Hunters don't blindly eat what their dogs retrieve.

## Substitution effects and the three measures
- **Substitution effects** = ML multicollinearity: a feature's
  importance is diluted by correlated features.
- **MDI (mean decrease impurity)**: in-sample, fast, tree-only. Average
  impurity decrease per feature across trees. Sums to 1, bounded [0,1].
  Set `max_features=1` to avoid masking (every feature gets a chance);
  replace zero importances with NaN before averaging (a 0 means "never
  randomly chosen," not "irrelevant"). Dilutes substitutes.
- **MDA (mean decrease accuracy)**: out-of-sample, slow. Fit once,
  score OOS, then permute each column one at a time and measure the
  performance loss. Measures predictive importance; more robust to
  substitution than MDI.
- **SFI (single feature importance)**: fit one model per single
  feature (purged CV); the most computationally expensive, but cleanest
  estimate of a feature's standalone importance.

## Orthogonalization (PCA) as confirmation
- PCA on features (unsupervised, label-free) ranks principal
  components; compare that ranking to the label-based importance
  ranking. If the same features are important to both, the pattern is
  unlikely to be overfit (PCA couldn't have seen the labels).
- Report the correlation between eigenvalues and importances
  (e.g., weighted Kendall's tau ≈ 0.8 in the book's example).
- Orthogonal features also speed convergence and allow dimensionality
  reduction by dropping small-eigenvalue components.

## Parallelized vs. stacked importance
- **Parallelized**: fit per-instrument, aggregate across the universe —
  fast, but substitution effects add variance to rankings.
- **Stacked**: pool all instruments into one dataset — handles
  instrument-specific substitution, but assumes stationarity across
  instruments.

## Key takeaways
- Research via feature importance, not backtesting; a backtest only
  discards bad models, it never improves them.
- Use MDI for fast screening, MDA/SFI for robust confirmation, and PCA
  rank-correlation to guard against overfitting.
- Features important across many instruments/criteria are more likely
  to reflect a real economic mechanism worth understanding.
