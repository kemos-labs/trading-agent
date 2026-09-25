# Walk-Forward Validation & Leakage-Free Evaluation

## Name
walk-forward-validation

## Description
Evaluate time-series ML/trading models honestly: sequential
train/test splits, rolling walk-forward loops, leakage prevention, and
multiple-testing (data-snooping) awareness. Use whenever a model is
trained on financial data and any performance number will be quoted.

## When to use it
- Before trusting any backtest or ML accuracy figure on time-series data.
- When comparing many model/configurations (snooping risk rises with
  trial count).
- When reporting a strategy's expected performance to yourself or others.
- Whenever preprocessing (scaling, feature selection) touches the full
  dataset.

## The method

### 1. Never shuffle time series; keep time order
Shuffling lets the model peek at the future. Always split
chronologically: train on the past, test on the future.

### 2. Prevent leakage at every preprocessing step
Any statistic computed on the test set leaks future information.
- Fit scalers/normalizers **on training data only**, then transform
  test data.
- Compute features (lags, rolling means) so each row uses only its own
  past — `shift()` before rolling, never centered windows.
- Do feature selection inside the training fold, not on the full
  dataset.

### 3. Walk-forward (rolling) validation
Simulate how the strategy would be retrained through time:

```
train blocks:      [t0, t1) test [t1, t2)
                   [t1, t2) test [t2, t3)
                   [t2, t3) test [t3, t4)  ...
```

- For each step, retrain (or refit) the model on the growing/rolling
  train window and evaluate only on the next out-of-sample block.
- Reported performance = the concatenated out-of-sample equity curve,
  never the best in-sample fold.

### 4. Account for multiple testing (data snooping)
Every trial is a hypothesis test; run enough and some win by chance.
- Fix the number of trials before searching; cap it.
- Prefer random search or Bayesian optimization over exhaustive grid.
- Demand out-of-sample performance comfortably above the cost hurdle;
  if many configurations were tried, treat the best as inflated (White's
  Reality Check / SPA or deflated Sharpe are formal corrections).
- Hold out one final untouched test block for the configuration you
  actually deploy.

### 5. Make the test realistic
- Include transaction costs, slippage, and market impact in the
  evaluation (a model profitable before costs is not a strategy).
- Evaluate across regimes (bull/bear/choppy), not just one period.

## Code pattern (sklearn-style)

```python
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
from sklearn.preprocessing import StandardScaler

X, y = ..., ...            # features lagged so each row only uses past data
tscv = TimeSeriesSplit(n_splits=5)
oos_metrics = []

for train_idx, test_idx in tscv.split(X):
    Xtr, Xte = X[train_idx], X[test_idx]
    ytr, yte = y[train_idx], y[test_idx]

    sc = StandardScaler().fit(Xtr)   # fit on train ONLY
    Xtr, Xte = sc.transform(Xtr), sc.transform(Xte)

    model = MyModel().fit(Xtr, ytr)  # retrain each fold
    oos_metrics.append(evaluate(model.predict(Xte), yte))

final_score = np.mean(oos_metrics)   # the only number worth quoting
```

## Known pitfalls
- Shuffled CV on time series silently fabricates skill — the most
  common fatal error.
- Normalizing with full-sample mean/std; centering with the mean of
  the whole series including the test period.
- Using the best-of-N configuration's in-sample score as expected
  performance (snooping bias).
- Test sets that overlap the training window (e.g., rolling features
  computed across the split boundary with look-ahead).
- Forgetting costs; a "winning" pre-cost model often loses post-cost.

## Source
Kaabar, *Deep Learning for Finance* (O'Reilly, 2024), ch7, ch11.
