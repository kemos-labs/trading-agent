# Risk Metrics

## name
Risk metrics for trading strategies: drawdown, Value at Risk (VaR),
Conditional VaR / Expected Shortfall (cVaR), the VaR/cVaR ratio diagnostic,
and portfolio risk contributions — vectorized in pandas.

## description
Compute and interpret the standard "how bad can it get" report card for any
strategy or portfolio return series: maximum drawdown, historical VaR and
cVaR at a chosen confidence level, the tail-shape diagnostic VaR/cVaR, and
per-asset risk contributions to total portfolio variance. Use this whenever
a backtest needs risk statistics alongside returns — every strategy report
should pair a return metric (Sharpe/Sortino) with these.

## when to use it
- Evaluating any strategy or portfolio: report drawdown, VaR, cVaR beside
  Sharpe/Sortino so tail risk is visible (a strategy can show Sharpe > 1 and
  a 44% drawdown at the same time — the two never contradict).
- Comparing two strategies with similar Sharpe but very different tail
  behavior — cVaR and the VaR/cVaR ratio separate them.
- Portfolio construction: compute risk contributions to know which asset is
  actually driving portfolio variance before rebalancing.
- Setting risk budgets / kill-switches (stop the day after X losses, the week
  after Y% drawdown).

## the method

All inputs are a 1-D return series `r` (strategy or portfolio returns) and an
optional equity curve `equity = (1+r).cumprod()`.

```python
import numpy as np
import pandas as pd

def risk_report(r, equity=None, alpha=0.05):
    """Vectorized risk report card for a return series."""
    r = pd.Series(r).dropna()
    if equity is None:
        equity = (1 + r).cumprod()

    # 1. Max drawdown
    dd = 1 - equity / equity.cummax()
    max_dd = dd.max()

    # 2. Historical VaR at confidence 1-alpha (loss exceeded alpha of the time)
    #    Clamp at 0: if even the alpha-quantile is positive (high-mean
    #    strategy), there is no loss at that confidence — a negative VaR
    #    would make the tail selection below meaningless.
    var = max(0.0, -float(np.quantile(r, alpha)))

    # 3. cVaR / Expected Shortfall: average loss BEYOND the VaR threshold
    tail = r[r <= -var]
    cvar = -tail.mean() if len(tail) else var

    # 4. Tail diagnostic: ~1 means losses cluster at the threshold (thin tail);
    #    large ratio means losses far beyond VaR (heavy tail)
    ratio = cvar / var if not np.isclose(var, 0) else np.nan

    return {"max_drawdown": max_dd, "VaR": var, "cVaR": cvar,
            "VaR/cVaR": ratio}
```

### Portfolio risk contributions
For weights `w` and covariance `Sigma` (annualized or daily, be consistent):

```python
port_var = w @ Sigma @ w                      # scalar portfolio variance
rc = w * (Sigma @ w) / port_var               # per-asset contribution, sums to 1
```

`rc` tells you each asset's share of portfolio risk; an asset with a tiny
weight but a large contribution is a hidden concentration.

### Reporting conventions
- Annualize where relevant: daily VaR/cVaR scale with `sqrt(252)` for
  roughly Gaussian tails; drawdown is scale-free (report as-is).
- Express as percentages of capital; always state the confidence level
  (95% → alpha=0.05) and the return frequency used.

## known pitfalls
- **VaR is not sub-additive** for fat-tailed (non-elliptical) returns; cVaR
  is coherent. Report both, never VaR alone.
- **Historical VaR is sample-dependent**: one extreme day moves it sharply;
  a longer window or parametric (variance-covariance) VaR may be stabler.
- **Do not annualize drawdown** — it is a scale-free percentage.
- The VaR/cVaR ratio needs enough tail observations; with tiny samples the
  tail mean is unreliable.
- Scaling VaR by `sqrt(252)` assumes i.i.d. returns; clustering volatility
  (GARCH behavior) makes daily-to-annual scaling optimistic — prefer
  `skills/arma-garch-modeling` for volatility-aware risk.
- Risk contributions assume a fixed covariance; in regimes they drift —
  re-estimate on a rolling window.

## source
Inglese (Quantreo), *Python for Finance and Algorithmic Trading*, 2nd ed.,
ch5 (risk analysis); ch14 example reporting Sharpe 1.04 alongside drawdown
44% / cVaR 67% (knowledge/python-finance-algo-trading-2ed/ch05-risk-analysis.md).
Complementary: `skills/kelly-position-sizing` (sizing from risk budget),
`skills/vectorized-backtesting` (produce the return series first).
