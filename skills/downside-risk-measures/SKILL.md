# Downside Risk Measures

## name
Downside risk and performance measures based on lower partial moments:
downside deviation, Sortino ratio, omega statistic, and the kappa index
family (with the lower partial moment definition and threshold choice).

## description
Measure risk and risk-adjusted performance using only the downside (below-
threshold) part of the return distribution: Lower Partial Moments
`LPM_n(τ) = E[max(0, τ - X)^n]`, downside deviation (n=2), the Sortino
ratio (excess return over downside deviation), the omega statistic (ratio
of gains to losses relative to a threshold), and the kappa indices that
generalize them. Use these when returns are skewed/fat-tailed and symmetric
measures (variance, Sharpe) mislead, or when an investor cares only about
shortfall below a threshold.

## when to use it
- Evaluating strategies/portfolios whose returns are skewed or leptokurtic —
  variance-based Sharpe overstates performance because it rewards upside
  volatility equally with downside.
- Ranking investments for a risk-averse investor: downside measures match
  the intuition that only losses below a target (e.g., 0%, the risk-free
  rate, or a benchmark) matter.
- Hedge funds / alternative strategies with option-like payoffs where
  upside kurtosis dominates.
- Setting the threshold τ: risk-free rate (standard for Sortino), zero
  (absolute shortfall), or the benchmark return (active returns).
- Pairing with `skills/risk-metrics` (VaR/cVaR/drawdown) for a complete
  risk report.

## the method

### 1. Lower partial moments (LPM)
```python
import numpy as np

def lpm(r, threshold, n=2):
    """n-th lower partial moment of returns r below threshold."""
    r = np.asarray(r, dtype=float)
    shortfall = np.maximum(threshold - r, 0.0)
    return np.mean(shortfall ** n)

# downside deviation = sqrt of 2nd LPM
downside_dev = np.sqrt(lpm(r, threshold=0.0, n=2))
```
- n=1: expected shortfall below threshold (basis of omega).
- n=2: downside deviation (basis of Sortino).
- n=3,4: more sensitive to negative skewness and extreme losses — for very
  risk-averse investors.

### 2. Sortino ratio
```python
excess = np.mean(r) - rf
# guard: constant returns => zero downside deviation => div-by-zero
downside_dev = max(np.sqrt(lpm(r, threshold=rf, n=2)), 1e-12)
sortino = excess / downside_dev * np.sqrt(252)
```
Sharpe's downside-only analogue: same numerator (excess return over the
risk-free rate), denominator = downside deviation instead of total
volatility.

### 3. Omega statistic (Keating-Shadwick)
```python
gains = np.mean(np.maximum(r - threshold, 0.0))
losses = np.mean(np.maximum(threshold - r, 0.0))
omega = gains / max(losses, 1e-12)   # guard vs zero-loss (all gains) series
```
- Threshold τ = the investor's reference point (rf, 0, benchmark).
- Omega > 1 means the expected gain exceeds the expected loss at τ.

### 4. Kappa indices
```python
# K_n(τ) = (E[R] - τ) / (LPM_n(τ))^(1/n)
kappa_n = (np.mean(r) - threshold) / (lpm(r, threshold, n) ** (1.0/n))
```
- K1 = omega − 1 (when computed consistently).
- K2 = Sortino ratio (threshold = rf).
- Higher-order kappas weight tail losses more; they increase as the
  threshold decreases, and are negative when τ > E[R].

## known pitfalls
- **Degenerate series**: constant returns give zero downside deviation /
  zero losses — Sortino and omega blow up; clamp denominators with a tiny
  epsilon (see snippets) and flag the series as riskless instead.
- **Threshold choice matters and is arbitrary**: risk-free, zero, and
  benchmark thresholds give different rankings; state it explicitly.
- **Sample sensitivity**: with few observations, LPMs of order ≥3 are noisy —
  need enough data for tail estimates.
- **Not a preference ordering**: downside measures *order* investments but,
  without a utility function, cannot say which is best for a particular
  investor (Alexander's caveat).
- **Annualization**: scale the mean and the LPM consistently (e.g.,
  √252 on the downside deviation); don't mix frequencies.
- Sortino ignores upside entirely — two funds with identical downside but
  different upside rank the same; inspect both sides (pair with total
  return/Sharpe).

## source
Alexander, *Market Risk Analysis*, Vol. I (Quantitative Methods in
Finance), ch I.6 (introduction to portfolio theory: kappa indices, omega,
Sortino, LPMs). Knowledge note:
`knowledge/market-risk-analysis-vol1/ch-i6-introduction-to-portfolio-theory.md`.
Complementary: `skills/risk-metrics` (VaR/cVaR/drawdown),
`skills/portfolio-optimization` (allocation), `skills/parametric-var`.
