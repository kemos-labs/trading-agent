# Ch11 — The Dangers of Backtesting

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 11.

## Purpose
A catalog of backtesting errors — from the seven sins to the deeper
problem that even flawless backtests are probably wrong because of
multiple testing — plus the Probability of Backtest Overfitting (PBO).

## The seven sins (Luo et al., 2014)
1. **Survivorship bias** — using today's universe, ignoring delisted
   firms.
2. **Look-ahead bias** — using info not public at decision time
   (release dates, delays, backfills).
3. **Storytelling** — ex-post rationalization of random patterns.
4. **Data mining / snooping** — training on the test set.
5. **Transaction costs** — unrealistic (true cost is only knowable by
   trading).
6. **Outliers** — strategies that rely on a few extreme outcomes.
7. **Shorting** — borrow cost/availability unknown, relationship-
   dependent.

## Even a flawless backtest is probably wrong
- A "flawless" backtest is produced by an expert — and expertise means
  having run tens of thousands of backtests. Selection bias on multiple
  tests guarantees some are false discoveries. The better you are at
  backtesting, the more false positives you generate.
- A backtest is a *hypothetical*, not an experiment: history is one
  path of a stochastic process; it proves nothing about the future.
- Purpose of a backtest: **discard** bad models, never improve them.
  Adjusting a model because of backtest results is dangerous. Finish
  model specification first; if the backtest fails, start over.

## Probability of Backtest Overfitting (PBO)
- **Backtest overfitting = selection bias on multiple backtests**: a
  strategy developed to monetize random historical patterns.
- **CSCV (Combinatorially Symmetric Cross-Validation)** procedure:
  1. Split the return matrix M (T×N configurations) into S submatrices.
  2. Form all combinations c of S/2 submatrices; training set J =
     union; test set = complement.
  3. Rank each configuration IS (training) and OOS (test).
  4. Compute the logit λ_c = log(relative-rank-out-of-sample /
     (1 − relative-rank)), 0 at the median — high λ = IS/OOS
     consistency, low overfitting.
  5. **PBO = probability that the IS-optimal strategy underperforms
     OOS** — the relative frequency of λ ≤ 0 across all combinations.
- Empirically, IS Sharpe of the best of many trials decays strongly
  OOS; PBO quantifies exactly how likely the winner is a fluke.

## Key takeaways
- Backtest errors divide into data errors (survivorship, look-ahead),
  process errors (snooping, multiple testing), and economics errors
  (costs, shorting, outliers).
- Report PBO alongside any backtest result; a high PBO means the
  strategy is a lottery ticket, not an edge.
- Never research by backtesting — research by feature importance
  (ch8); backtest only fully-specified models, once.
