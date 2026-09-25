# Ch12 — Backtesting through Cross-Validation

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 12.

## Purpose
Presents three backtesting paradigms — walk-forward (historical),
cross-validation (scenario), and the new **Combinatorial Purged
Cross-Validation (CPCV)** — and explains why CPCV fixes the multiple
paths problem.

## The three paradigms
- **Walk-forward (WF)**: simulate the historical path; each decision
  uses only trailing data. Pros: clear historical interpretation,
  reconcilable with paper trading, no leakage if purged (training
  always predates testing, so no embargo needed). Cons: (1) tests only
  *one* path (easily overfit); (2) sequence-dependent — a walk-backward
  backtest often gives different results, exposing overfitting to the
  specific datapoint order; (3) early decisions use little data (warm-up
  problem) — much of the sample is used by only a fraction of
  decisions.
- **CV backtesting**: split so the test period is a specific stress
  scenario (e.g., train 2009–2017, test 2008) — simulates how the
  strategy would fare *ignorant* of that period. Pros: k alternative
  scenarios, equal-size training per decision, every observation tested
  once (no warm-up). Cons: single path still; no historical
  interpretation; training doesn't trail testing → leakage risk
  (purging/embargo required).

## Combinatorial Purged CV (CPCV)
- Split T observations into N groups (chronological). For k test
  groups per split, evaluate **every combination** of N−k train / k
  test groups, purging and embargoing overlaps (ch7).
- Combine forecasts into φ[N,k] **backtest paths**, each producing a
  Sharpe ratio → an *empirical distribution* of Sharpe, not a single
  number.
- φ[N,k] = (N choose k)·(N−k)... specifics: k=1 gives N splits (reduces
  to plain CV); k=2 gives N−1 paths. Training fraction θ = 1 − k/N
  (keep k ≤ N/2); more groups/paths → more scenarios but less training
  data.
- **Why it addresses overfitting**: you get many OOS paths, so you can
  measure the distribution and stability of performance (e.g., what
  fraction of paths lose money), rather than trusting one lucky
  historical path. Also lets you quantify how often the strategy's
  OOS Sharpe is negative.

## Key takeaways
- WF is the most common backtest but the easiest to overfit: a single
  historical path is one draw from the stochastic process.
- CPCV generalizes CV to many train/test combinations with purging +
  embargoing, producing a distribution of out-of-sample performance.
- Use CPCV's Sharpe distribution (mean, min, % negative) as the honest
  estimate of what live trading may look like.
