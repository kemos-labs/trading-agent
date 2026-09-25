# Chapter 1 — Read me (Introduction)

## What this chapter is
The opening chapter of *Python for Finance and Algorithmic Trading* (2nd ed.,
Inglese/Quantreo) is purely practical: it points to the companion GitHub
repository and the Anaconda-based setup used throughout the book. There is no
trading theory here — it is the "how to use this book" chapter.

## Key takeaways
- All book code lives in a public GitHub repository; notebooks are organized
  chapter by chapter, and the README lists additional reading.
- The recommended environment is **Jupyter Notebook via Anaconda Navigator**;
  a setup notebook installs the required libraries (NumPy, pandas, Matplotlib,
  scikit-learn, TensorFlow/Keras).
- The book is code-first: every strategy is implemented, backtested, and
  judged with the same metrics pipeline (Sharpe, Sortino, VaR, cVaR,
  drawdown) introduced in later chapters.

## Why it matters for the knowledge base
This chapter establishes the book's working pattern that recurs through all 17
chapters:
1. Fetch data with `yfinance` (Yahoo Finance).
2. Engineer features (lags, technical indicators) and a target (next-period
   return or direction).
3. Split into train/test (and later train/test/validation) sets.
4. Fit a model, produce `prediction`, build `strategy = sign(prediction) * returns`.
5. Evaluate with `backtest_dynamic_portfolio` (Sharpe/Sortino/VaR/cVaR/drawdown).

## Connections
- The strategy-evaluation metrics recur throughout the book and are distilled
  in `knowledge/python-finance-algo-trading-2ed/ch04` and `ch05`.
- The end-to-end workflow is executed at scale in `ch16` (the full project).
- The `skills/vectorized-backtesting` and `skills/alpha-factor-evaluation`
  skills codify the same signal → returns → metrics skeleton in reusable form.

## Chapter structure at a glance
The book is organized in three parts that mirror a complete trading system:

1. **Part 1 — Foundations** (ch1–6): Python setup, portfolio optimization,
   backtesting, and risk analysis. This is the evaluation layer every
   strategy must pass through.
2. **Part 2 — Machine learning** (ch7–12): statistical arbitrage, ARMA,
   linear/logistic regression, feature and target engineering, SVM, and
   ensembles. Each learner plugs into the same feature→fit→sign-trade→
   backtest pipeline.
3. **Part 3 — Deep learning and production** (ch13–17): DNN, RNN, RCNN, the
   full multi-strategy project, and going live with a trading plan and
   journal.

## Bottom line
A short meta-chapter; the value is the discipline it introduces — every
strategy, however simple, is run through the same data → model → signal →
backtest → risk-metrics pipeline, which is exactly the repeatable skeleton
promoted in the `vectorized-backtesting` skill. The rest of the book is
systematic variation on that one loop.
