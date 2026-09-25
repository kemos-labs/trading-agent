# Ch1 — Introduction to Advanced Algorithmic Trading

**Source:** Halls-Moore, *Advanced Algorithmic Trading* (QuantStart), Chapter 1.

## Purpose
Sets up the book's thesis: the goal of a quant researcher is to find **alpha** — new streams
of *uncorrelated, risk-adjusted returns* — and exploit them via a systematic trading model and
execution infrastructure. Alpha is hard to capture because once widely known it decays: it
ceases to be an uncorrelated source of return and (re)becomes a common **risk factor** with
losing its risk-adjusted edge. The book argues that robust statistical modelling is a more
effective route to alpha than "technical analysis" alone.

## Three pillars of the book (the toolchain)

1. **Bayesian Statistics** — treats probability as a *measure of belief* rather than a long-run
   frequency. Beliefs are represented as probability distributions and updated rationally with
   new evidence via **Bayes' Rule**. Used for inference and prediction about prices.
2. **Time Series Analysis** — "workhorse" methods for financial series, centred on the idea of
   **serial correlation**: how much today's price relates to prior days' prices. Momentum
   strategies derive from *positive* serial correlation of returns. Brings full statistical
   inference (hypothesis tests, goodness-of-fit, model selection) to trends, seasonality,
   long-memory and **volatility clustering**. Done in R.
3. **Machine Learning** — modern statistical learning over large (possibly non-temporal) data.
   Three categories:
   - **Supervised learning**: train an algorithm on labelled training data to detect patterns.
   - **Unsupervised learning**: no labels/rewards; must find structure directly (harder).
   - **Reinforcement learning**: reward-driven (e.g. AlphaGo); noted but out of scope.
   Uses SVM and Random Forests mainly. Done in Python (scikit-learn, pandas).

## Book structure (4 sections)

- **Sections 1–3 (theoretical):** Bayesian statistics (binomial model, conjugate priors,
  stochastic volatility), time series (serial correlation → white noise / random walk →
  ARMA → ARIMA + GARCH → **cointegration** → state space & Hidden Markov Models), and
  ML (regression, decision trees, SVMs, random forests, unsupervised/clustering, NLP).
- **Section 4 (practical):** applies all theory to backtesting via the **QSTrader**
  open-source backtesting engine.

## Key engineering takeaways

- **Tooling:** Python via *Anaconda/Spyder* (v2.7/3.4/3.5) for Bayesian + ML chapters; R via
  *RStudio/CRAN* for time-series chapters. QSTrader is QuantStart's own modular open-source
  backtester (github.com/mhallsmoore/qstrader).
- **QSTrader design philosophy**: highly modular with first-class **risk management,
  position-sizing, portfolio construction, execution**; brokerage fees and bid/ask spread
  (if data available) are turned *on* by default so backtests resemble real trading. Still
  in "alpha" (not for live trading).
- **Alternatives mentioned**: Quantopian, Zipline, PySystemTrade (Carver's futures
  backtester).
- **Prerequisites**: linear algebra, calculus, probability; Python/R programming basics.
  Supporting courses cited (MIT OCW Strang linear algebra, etc.).
- Relationship to prior book *Successful Algorithmic Trading*: the earlier book emphasised
  hypothesis testing, data storage, performance measurement, risk, optimisation, and a
  template event-driven backtester; the present book is more mathematical-modelling-centric.
- Help via QuantStart articles (~200 available) / support email.

## Notes / caveats
- This chapter is purely motivational/contextual (no formulas). Key reusable idea: the
  *alpha-decay → becomes risk factor* principle and the supervised/unsupervised split are
  foundational concepts.
- Emphasises "maths-first, then practical" reading trajectory; defer quality-of-life,
  infrastructure topics to other sources.