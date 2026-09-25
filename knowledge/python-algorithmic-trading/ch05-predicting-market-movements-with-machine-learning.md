# Ch5 — Predicting Market Movements with Machine Learning

**Source:** *Python for Algorithmic Trading: From Idea to Cloud Deployment* —
Yves Hilpisch (O'Reilly, 2021)

## The problem setup

Assume the efficient market hypothesis doesn't hold universally: patterns
repeat, so past returns can predict future direction. For trading, it's
enough to predict the **direction** (up/down) rather than magnitude —
a classification problem. Inputs are **lagged** prices/returns.

## Linear regression for price prediction

- OLS review with NumPy: `np.polyfit(x, y, deg=1)` / `np.polyval` for
  monomial regression; extrapolation = prediction beyond the data domain.
- Time-series twist: the ordering matters. With `lags` lagged prices as
  features (e.g. 3 lags: today, yesterday, day-before → predict tomorrow),
  the model is a matrix equation A·x = b solved by least squares.
- **GDX/Gold regression strategy**: regress the GDX ETF's return on
  lags of its price (and gold's), sign the fitted prediction to get
  position, backtest vectorized (position.shift(1) × returns). The book
  reports ~53% hit ratio in-sample and shows a regression-based strategy
  beating the buy-and-hold GDX (out-of-sample, after costs, with 7 lags).

## Logistic regression (scikit-learn)

- The scikit-learn API: instantiate model → `fit(X, y)` → `predict(X)`.
- Target: `np.sign(data['return'])` (direction classes −1/+1); features:
  `cols = ['lag_%d' % lag]` from `data['price'].shift(lag)`.
- `LogisticRegression(C=1e7, solver='lbfgs', max_iter=1000)` — high C
  downweights regularization. Hit ratio ≈ 53–54.5% (3 lags) on GLD;
  more lags (5) → lower hit ratio but higher gross performance.
- Strategy P&L: `data['strategy'] = data['prediction'] * data['return']`;
  cumulative via `cumsum().apply(np.exp)`.
- Warning: the in-sample numbers are optimistic — overfitting trap. The
  honest version fits on a training (in-sample) period and evaluates on a
  test (out-of-sample) period; the book generalizes the backtester to a
  class (ScikitVectorBacktester) doing exactly this split.

## Deep learning (Keras)

- Neural-network classifiers predict direction from lagged inputs; the
  book introduces the Keras API (Sequential model, Dense layers) as the
  deep-learning option — same classification framing, nonlinear decision
  boundary.
- Same evaluation pipeline: fit on train, predict sign, shift, backtest,
  compare with benchmark.

## Key takeaways

- Prediction problem = direction classification from lagged features;
  ~50% is chance, so 53–55% hit ratios are small but tradeable edges that
  costs can erase.
- scikit-learn workflow (fit/predict) + pandas lag features + vectorized
  P&L is the standard ML-for-trading skeleton.
- In-sample results are traps: always split train/test; the honest
  performance is the out-of-sample one, net of costs.
- Hit ratio is only half the story — market timing (when predictions are
  right) and trade frequency also drive P&L.
