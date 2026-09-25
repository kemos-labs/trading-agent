# Chapter 16 — Real-life Full Project

## Core idea
The book's capstone: build an automated multi-strategy trading system from
scratch — screen 150 FX assets with 3 ML algorithms, pick the best, and
allocate a portfolio across the survivors. This is the whole book's pipeline
run at scale, honestly.

## The three-way data split
Beyond train/test, production predictive work needs a **validation set**:
- **Train**: fit predictive models. Train-set strategy returns are not
  meaningful (the model saw that data).
- **Test**: pick the *best models* by strategy Sharpe on unseen data.
- **Validation**: after choosing models *and* the capital allocation, run the
  final portfolio backtest on data none of the decisions touched.
This discipline prevents both model overfitting and allocation overfitting.

## Strategy screening (450 strategies)
1. **Asset filter**: keep symbols with spread below a threshold (~0.07%).
2. For each of 150 assets × 3 models (LinearRegression, SVR `epsilon=1.5`,
   DecisionTree `max_depth=6`) build features (ch10), fit on train, predict,
   and compute a **spread-penalized Sharpe on the test set**:
   ```python
   sharpe = sqrt(252) * (returns.mean() - spread/100) / returns.std()
   ```
   The spread penalty means higher-spread assets must earn more edge.
3. Deep learning is excluded here — some assets only have ~1000 rows; deep
   nets need more data.
4. **Model diversity is deliberate**: linear (linear patterns), SVR
   (nonlinear), tree (other interactions). If all three agree a pair is
   good, confidence rises.

## Portfolio layer
- Take the best assets/strategies (e.g., Bitcoin, JPN225, NAS100, US2000,
  XPTUSD with Sortinos 2.9 → 0.7) and allocate capital using **voting**
  across algorithms and **mean-variance allocation** (ch3) on test-set
  strategy returns.
- The portfolio's volatility is lower than any single strategy — the ch14
  44%-drawdown single-strategy problem, addressed.

## Pitfalls
- Using train data for any selection step = leakage → inflated results.
- Spread units: sometimes percentage, sometimes not — verify before
  penalizing.
- `try/except` per asset hides failures — log which symbols fail and why.
- Only ~a few of hundreds of screened strategies survive: expect most to
  fail, by design.

## Bottom line
The blueprint for a robust ML trading pipeline: screen at scale, penalize
costs inside the metric, split data three ways so no decision touches the
final test, then diversify across models/assets. This is the process-level
lesson that turns the single-strategy chapters into a system.
