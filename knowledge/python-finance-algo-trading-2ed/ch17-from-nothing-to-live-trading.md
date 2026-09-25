# Chapter 17 — From Nothing to Live Trading

## Core idea
The operationalization chapter: how to take a strategy from backtest to
production — a written trading plan, a trading journal, disciplined bet
sizing, and a *portfolio* of strategies rather than one bet.

## The trading plan
- Written *before* research, with a fresh mind; decide in advance: which
  market (FX/stocks/crypto), which timeframe, low-spread and/or volatile
  assets, overnight exposure, min/max trades per day, and performance/risk
  targets.
- It is the **accept/reject filter** for every strategy idea. Do not rewrite
  the plan when results disappoint — keep searching (expect ~100 tries per
  good strategy).
- For algorithmic trading the plan codifies entry/exit and money management
  rules the code will implement.

## The strategy-building process
1. Trading plan (accept/reject criteria).
2. Import quality data ("garbage in, garbage out") — as much as possible.
3. Preprocess: features/targets, standardization, PCA.
4. Model the target (ML/DL or rules).
5. **Backtest at most twice** to avoid overfitting the results.
6. Apply the plan's entry/exit/TPSL during incubation.
7. Compare incubation results to backtest — check the return distributions
   match; if production returns decay, upgrade or stop.
8. Repeat per strategy.

## Trading journal (for algos)
- Not per-trade entries (the algo is deterministic) but: manual analysis of
  trade quality (e.g., "stop-loss above support too many times" → new SL
  rule; "false signals after news" → pause before news), tracking
  **backtest-vs-production return distribution drift**, and a log of coding
  issues/solutions.

## Bet sizing & compounding
- **Never risk all capital on one strategy**; never risk more than ~1% of
  capital on one trade; kill-switches: stop the day after 3 losses, stop the
  week after a 5% loss.
- **Compounding is double-edged**: 1% per trade over a year → ~52% chance of
  being a losing trader; 30% per trade → ~100% (three straight losses leave
  10% of capital, needing +900% to recover). Recovery asymmetry:
  `required_gain = loss/(1-loss)`.

## Strategy portfolio
- One strategy is not the end: build multiple, combine **uncorrelated (ideally
  negatively correlated)** strategies to cut portfolio volatility — echoing
  ch3 (allocation) and ch16 (screening).

## Bottom line
The process discipline — plan first, backtest twice, incubate, journal
production-vs-backtest drift, size small, diversify — is the risk-management
backbone of the whole book. It aligns with the knowledge base's process
notes (`ch06-money-and-risk-management`) and `kelly-position-sizing`
sizing cautions.
