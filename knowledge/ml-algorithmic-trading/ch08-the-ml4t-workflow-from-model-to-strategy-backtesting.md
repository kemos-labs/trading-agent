# Ch08 — The ML4T Workflow: From Model to Strategy Backtesting

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 8.

## Purpose
Ties the ML pipeline to a tradeable strategy: take model predictions, convert them into a long-short portfolio, and backtest honestly with Zipline — the book's reference backtesting stack.

## From predictions to positions
1. **Predict** return/direction per asset per period (any model from Part 2).
2. **Rank** assets cross-sectionally by predicted signal.
3. **Size positions**: long top quantile, short bottom quantile (e.g., top/bottom decile), equal weight within buckets; optionally weight by signal magnitude or volatility target (see `volatility-targeted-position-sizing`).
4. **Rebalance** on a schedule (daily/weekly) with costs.

## Backtesting with Zipline
- **Zipline** is an event-driven backtester: ingest price/volume data, define an `initialize()` + `handle_data()` strategy, run over a historical window, and produce a performance DataFrame.
- **Pipeline API**: compute factor scores cross-sectionally per trading day (e.g., `CustomFactor` returning z-scored momentum); `set_benchmark()` for relative performance.
- **Bundles**: pre-processed daily/minute datasets; avoid survivorship-biased universes.
- **pyfolio**: tearsheets — cumulative returns, drawdowns, Sharpe/Sortino, rolling betas, and per-period return analysis; the standard evaluation output.

## Backtest integrity rules
- **Out-of-sample discipline**: fit/tune models on an in-sample window, then run the *same* strategy on held-out data; walk-forward retraining matches live conditions (skills `walk-forward-validation`, `purged-cross-validation`).
- **Costs**: Zipline models commission and slippage; test with realistic spreads and impact, especially for high turnover.
- **No lookahead**: signals at day *t* must use data ≤ *t*; use adjusted prices and point-in-time fundamentals.
- **Multiple testing**: hundreds of backtested variants guarantee false positives; demand significance (deflated Sharpe, see `purged-cross-validation`).

## Benchmarking and attribution
- Compare against a benchmark (e.g., SPY); compute active returns.
- Decompose via factor regression (ch7): how much of the strategy is beta/factor exposure vs. genuine alpha?
- Evaluate turnover and capacity: a strategy whose edge dies under realistic costs isn't viable.

## Key takeaways
- A model is only a strategy once predictions become cost-aware positions; the backtest is where most edges die.
- Zipline + pyfolio give a reproducible, event-driven pipeline for factor-to-strategy research.
- The evaluation framework — out-of-sample, costed, benchmarked, significance-tested — is the real deliverable, not the equity curve.
