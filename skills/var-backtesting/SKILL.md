# VaR / Forecast Backtesting (Coverage Tests)

## name
Statistical backtesting of VaR (and other interval/tail forecasts) using
Kupiec's unconditional coverage likelihood-ratio test and Christoffersen's
conditional (independence) coverage test, including the rolling-window VaR
backtest procedure.

## description
Given a series of out-of-sample VaR forecasts and realized returns, test
whether the model's exceedance rate matches the promised level
(unconditional coverage) and whether exceedances arrive independently rather
than in clusters (conditional coverage). This is the standard statistical
validation half of a VaR workflow: `skills/parametric-var` and
`skills/risk-metrics` estimate risk; this skill tells you whether the
estimates are trustworthy out of sample. It also applies to any interval or
tail forecast (volatility forecasts feeding a distributional tail).

## when to use it
- Validating any VaR model (normal linear VaR, historical simulation,
  GARCH-based VaR via simulation) against realized returns.
- Comparing competing volatility/risk models: the best in-sample fit need
  not be the best forecaster — coverage tests are the out-of-sample arbiter.
- Regulatory/business reporting where a model that under- or over-predicts
  tail risk is a serious defect (clustered breaches are far worse than
  isolated ones).
- Generalizing to any forecast of an interval of the distribution (e.g., a
  volatility forecast used to predict the lower 1% tail).

## the method

### 1. Rolling-window VaR backtest setup
Fix the significance level `alpha` (e.g., 0.05 for 95% VaR) and keep portfolio
weights constant. Roll the estimation window; at each step t:

```python
import numpy as np
from scipy.stats import norm, chi2

def var_forecast(returns_window, alpha=0.05, method="ewma", lam=0.94):
    if method == "ewma":
        # RiskMetrics EWMA variance, lambda ~ 0.94 daily
        var = np.var(returns_window, ddof=0)  # seed
        for r in returns_window:
            var = lam * var + (1 - lam) * r**2
        sigma = np.sqrt(var)
    else:  # equally weighted
        sigma = np.std(returns_window, ddof=1)
    # normal linear VaR (positive magnitude)
    return -norm.ppf(alpha) * sigma
```

Each step, flag an **exceedance** if the realized h-period return loses more
than the VaR forecast:

```python
def exceedances(var_forecasts, realized):
    return (np.asarray(realized) < -np.asarray(var_forecasts)).astype(int)
```

### 2. Unconditional coverage (Kupiec)
LR test that the observed exceedance rate equals the promised one:

```python
def kupiec_lr(violations, alpha):
    n1 = violations.sum(); n0 = len(violations) - n1
    pi_obs = n1 / len(violations)
    lr = ((1 - alpha) ** n0 * alpha ** n1) / \
         ((1 - pi_obs) ** n0 * pi_obs ** n1)
    stat = -2 * np.log(lr)
    return stat, 1 - chi2.cdf(stat, df=1)  # (statistic, p-value)
```

- `stat ~ chi-squared(1)` under H0 (model is accurate).
- Reject if `stat` exceeds the critical value (3.84 at 5%, 2.71 at 10%) —
  i.e., if the observed exceedance rate differs significantly from `alpha`.

### 3. Conditional coverage (Christoffersen)
Tests *independence* of the exceedance indicator — clustering is a model
failure (a bank's VaR must not fail several days in a row). Build the
transition matrix of the indicator (0->0, 0->1, 1->0, 1->1 counts) and
compare to the independence assumption:

```python
def christoffersen_lr(violations, alpha):
    n00 = ((violations[:-1] == 0) & (violations[1:] == 0)).sum()
    n01 = ((violations[:-1] == 0) & (violations[1:] == 1)).sum()
    n10 = ((violations[:-1] == 1) & (violations[1:] == 0)).sum()
    n11 = ((violations[:-1] == 1) & (violations[1:] == 1)).sum()
    # independence LR: compare unrestricted transition probs to one-param
    pi0 = n01 / max(n00 + n01, 1e-12); pi1 = n11 / max(n10 + n11, 1e-12)
    pi = (n01 + n11) / max(n00 + n01 + n10 + n11, 1e-12)
    L_un = (1 - pi0)**n00 * pi0**n01 * (1 - pi1)**n10 * pi1**n11
    L_0  = (1 - pi)**(n00 + n10) * pi**(n01 + n11)
    stat = -2 * np.log(L_0 / max(L_un, 1e-12))
    return stat, 1 - chi2.cdf(stat, df=1)  # independence component
```

Christoffersen's full **conditional-coverage** test combines the two:
`LR_cc = LR_uc + LR_ind ~ chi-squared(2)`. The code above implements the
independence component (chi-squared(1)) — for the combined test simply add
the Kupiec statistic.

## known pitfalls
- **Low power of squared-return diagnostics**: regressing squared returns on
  variance forecasts gives a tiny maximum R^2 even for a correctly specified
  GARCH (Andersen-Bollerslev: ~0.36 max) — do NOT reject a volatility model
  on that basis; use likelihood or coverage tests instead.
- **Clustered violations are the real failure**: unconditional coverage can
  pass while the model misses volatility clustering (equally weighted
  covariance fails Christoffersen's test where EWMA passes on the same S&P
  500 data).
- **Violations are binary**: short out-of-sample windows have few
  exceedances — the chi-squared approximation is poor; use enough data
  (hundreds of days).
- **Frequency/length consistency**: forecast and realized returns must cover
  the same horizon (1-day vs 10-day VaR are different tests).
- **Weight changes break the test**: hold portfolio weights constant during
  the backtest or the exceedance series mixes different portfolios.
- **Zero-variance guards**: clamp denominators (transitions, pi) with an
  epsilon for degenerate series.

## source
Alexander, *Market Risk Analysis*, Vol. II (Practical Financial
Econometrics), ch II.8 (forecasting and model evaluation; coverage tests and
the VaR backtest). Knowledge note:
`knowledge/market-risk-analysis-vol2/ch-ii8-forecasting-and-model-evaluation.md`.
Complementary: `skills/parametric-var` (forecast to test),
`skills/risk-metrics`, `skills/walk-forward-validation`.
