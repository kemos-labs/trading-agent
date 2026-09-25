# Kelly Position Sizing

## name
Kelly criterion and fractional-Kelly / volatility-targeting position sizing
for trading strategies, with estimation-error guardrails.

## description
Size positions to maximize long-run growth (Kelly) or to hit a risk
budget (volatility targeting). Includes the discrete and continuous Kelly
formulas, fractional-Kelly de-risking, the over-betting trap, and the
vol-target approximation used when edge estimates are noisy.

## when to use it
- You need a defensible, formula-driven position size instead of
  "feel" or fixed notional.
- You are building a portfolio/live sizing layer for any strategy
  (options, vol trades, equities) and want growth-optimal or
  risk-budgeted allocation.
- Evaluating whether a strategy's sizing (not just its signal) is
  responsible for its returns or drawdowns.
- Anytime an agent must decide "how big is this trade?" mechanically.

## the method

### 1. Discrete Kelly (Bernoulli bets)
For win probability p, loss probability q = 1 − p, payoff odds b (net
gain per unit staked):

```
f* = (b·p − q) / b  =  p − q/b
```

f* is the fraction of capital to stake maximizing expected log-growth.

### 2. Continuous Kelly (returns ~ normal)
With mean m and variance σ² of the strategy's per-trade (or per-period)
return:

```
f* = m / σ²
```

f* grows with expected return and shrinks with variance — equivalently,
f* scales with Sharpe / σ.

### 3. Fractional Kelly (recommended)
Trade k·f* with k ∈ [0.25, 0.5] typically. Growth is reduced only
mildly while variance and tail risk fall sharply; protects against
estimation error.

### 4. Volatility targeting (robust proxy)
When edge estimates are too noisy for Kelly, target a constant
portfolio/strategy volatility instead:

```
weight_t = target_vol / σ_forecast_t
```

Re-estimate σ (e.g. EWMA, GARCH, or realized vol) and rebalance
periodically. This is a practical Kelly approximation that is robust to
bad mean estimates — you only need the variance.

## known pitfalls
- **Kelly is fragile to input errors**: an overestimated edge or win
  probability leads to over-betting and negative expected growth. Always
  use fractional Kelly.
- **Never bet beyond ~2× Kelly**: expected growth turns negative past
  roughly 2f* — over-betting is worse than under-betting.
- **Fat tails and skew break the Gaussian version**: options/vol
  strategies have skewed, heavy-tailed P&L; short-vol has negative skew
  (rare large losses), so full Kelly is too aggressive — cut size further.
- **Kelly maximizes long-run growth, not safety**: it implies deep
  drawdowns; trade a fraction if drawdown tolerance is limited.
- **Daily-rebalanced leveraged products**: constant-leverage return ≈
  L·μ − ½·L²·σ² — the volatility drag term matters when sizing anything
  with daily reset (leverage must be penalized in σ).

## example (vectorized, pandas)
```python
import numpy as np
import pandas as pd

def kelly_fraction(returns: pd.Series) -> float:
    m = returns.mean()
    v = returns.var()
    if v <= 0:
        return 0.0
    return m / v  # continuous Kelly; multiply by 0.25–0.5 for fractional

def vol_target_weight(returns: pd.Series, target_vol: float,
                      lookback: int = 60) -> pd.Series:
    rv = returns.rolling(lookback).std() * np.sqrt(252)  # annualized
    return (target_vol / rv).clip(upper=3.0).fillna(0.0)
```

## source
Sinclair, *Volatility Trading* 2nd ed., ch8 (Money Management — Kelly,
fractional Kelly, vol targeting, and the two-traders sizing example).
