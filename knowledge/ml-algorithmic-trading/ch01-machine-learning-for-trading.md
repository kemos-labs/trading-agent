# Ch01 — Machine Learning for Trading

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 1.

## Purpose
Frames the ML4T thesis: ML extracts signal from ever-larger, more diverse datasets to support investment decisions, and the book's ML4T workflow ties every step — data, features, models, strategy, backtesting — into one process.

## Why ML for trading now
- **Data explosion**: prices, fundamentals, and a fast-growing layer of *alternative data* (text, satellite imagery, credit-card, sensors, social) have made systematic extraction of information feasible and necessary.
- **Signal-to-noise**: financial returns have an extremely low signal-to-noise ratio; only systematic processing of large data volumes can uncover weak, often nonlinear patterns.
- **ML value adds at every stage**: feature engineering (alpha factors), prediction (return/direction/volatility), portfolio construction (allocation, risk), and execution.

## The ML4T workflow
1. **Data** — source and clean market, fundamental, and alternative data; avoid lookahead bias by respecting publication timestamps.
2. **Features** — engineer alpha factors and predictive features (momentum, quality, sentiment…), standardize and validate them.
3. **Models** — train supervised (classification/regression) or unsupervised models; avoid overfitting via honest cross-validation.
4. **Strategy** — convert predictions into positions (signal → sizing → portfolio).
5. **Backtest/evaluation** — simulate out-of-sample performance with realistic costs; guard against multiple-testing bias.
6. **Live deployment** — monitor performance; expect signal decay as markets adapt.

## Key discipline points
- **Domain expertise matters**: data quality and correct labeling are the biggest failure sources — not model choice.
- **Overfitting is the central enemy**: high-capacity models on noisy data overfit easily; use walk-forward and purged validation (see skills `walk-forward-validation`, `purged-cross-validation`).
- **Lookahead bias**: any feature computed with information unavailable at time *t* leaks the future; timestamps must reflect real publication time.
- **Signal decay**: competitive markets arbitrage signals away; monitor and refresh models continuously.
- **Bias–variance trade-off** sharpens as noise rises: match model complexity to data quality.

## Book roadmap (Parts 1–5)
- **Part 1**: data — market/fundamental (ch2), alternative (ch3), features (ch4), portfolio evaluation (ch5).
- **Part 2**: modeling — ML process (ch6), linear (ch7), ML4T workflow (ch8), time series (ch9), Bayesian (ch10), trees (ch11–12), unsupervised (ch13).
- **Part 3**: NLP — text data (ch14), topic modeling (ch15), embeddings (ch16).
- **Part 4**: deep learning — DNNs (ch17), CNNs (ch18), RNNs (ch19), autoencoders (ch20), GANs (ch21), RL (ch22).
- **Part 5**: conclusions (ch23).

## Key takeaways
- ML is an *addition* to the investment process, not a substitute for domain judgment; humans define objectives, curate data, and interpret results.
- The same workflow applies across asset classes and data types; the framework matters more than any single algorithm.
- Honest evaluation (no leakage, realistic costs, statistical significance) is what separates real edge from backtest fiction.
