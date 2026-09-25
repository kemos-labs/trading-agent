# Parametric Value-at-Risk

## name
Parametric (variance-covariance) Value-at-Risk from fitted return
distributions: fit a Normal (or any scipy.stats family) to a return
series, then compute VaR as the alpha-quantile of the fitted distribution
via the inverse CDF. Includes daily/annualization conventions.

## description
Compute Value-at-Risk without needing a long tail sample: fit the
distribution of daily returns once (`scipy.stats.norm.fit`), then read the
VaR directly from the fitted quantile function (`norm.ppf(alpha, mu, sig)`).
Also covers the PDF/CDF checks that validate the fit and the empirical
(order-statistic) VaR as the model-free alternative. Use this when you need
a smooth, extrapolating risk number for a short history or a quick
risk/return report, complementing the historical VaR in the risk-metrics
skill.

## when to use it
- Quick risk reporting on any return series: daily VaR at 95% from a fitted
  Normal, annualized with `sqrt(252)`.
- Short histories where the empirical 5th percentile is noisy or
  degenerate (few tail observations).
- Comparing risk across assets with a common, reproducible convention.
- Stress/analytics pipelines where VaR must be a smooth function of mu/sig
  (e.g., for sensitivity analysis or optimization).
- When the risk-metrics historical VaR and this parametric VaR agree, your
  tail estimate is robust; disagreement flags non-normality (fat tails).

## the method

### 1. Prepare the return series
```python
import numpy as np
from scipy.stats import norm

cp = np.array(prices)                 # adjusted close, ascending
ret = cp[1:] / cp[:-1] - 1            # simple daily returns
```

### 2. Fit the distribution and validate
```python
mu_fit, sig_fit = norm.fit(ret)       # ML estimates of mean and std
x = np.arange(-5, 5, 0.001)
pdf = norm.pdf(x, mu_fit, sig_fit)
print(np.sum(pdf * 0.001))            # == 1.0: valid density
cdf = norm.cdf(x, mu_fit, sig_fit)    # monotone 0 -> 1
```
- `scipy.stats` families all share `.fit`, `.pdf`, `.cdf`, `.ppf` — swap the
  distribution (e.g., `t` for fat tails) by changing the class.
- Sanity-check the fit: `sum(pdf*dx) == 1`; plot PDF over a histogram of
  returns; compare fitted vs empirical quantiles.

### 3. Parametric VaR
```python
alpha = 0.05                          # 95% confidence
var_daily = max(0.0, -norm.ppf(alpha, mu_fit, sig_fit))  # positive loss number
var_annual = var_daily * np.sqrt(252)
```
- `norm.ppf(alpha, mu, sig)` is the alpha-quantile of the fitted Normal; the
  negative gives the loss magnitude.
- **Clamp at 0**: for a high-mean series the alpha-quantile can be positive
  (no loss at that confidence) — a negative "VaR" would be meaningless. Same
  guard as `skills/risk-metrics`.
- Annualization: multiply the daily std by `sqrt(252)` (and annualize the
  mean as `(1+mu)**252 - 1` if desired) — or re-derive directly from
  annualized parameters. (The book's own example uses 364 trading days;
  252 is the common convention — be explicit about which you use.)

### 4. Empirical VaR (cross-check)
```python
ret_sorted = np.sort(ret)
var_emp = -ret_sorted[int(alpha * len(ret_sorted))]
```
Order the returns and take the value at the alpha-th position — no
distributional assumption. Compare with the parametric number.

## known pitfalls
- **Fat tails**: Normal-fitted VaR understates tail risk — daily equity
  returns are heavy-tailed; check with the empirical VaR and prefer a
  t-distribution for stress levels.
- **sqrt(252) scaling assumes i.i.d. returns**; volatility clustering
  (GARCH behavior) makes annualized VaR optimistic — see
  `skills/arma-garch-modeling` for volatility-aware risk.
- `norm.fit` fits on *all* observations — one crash day pulls mu/sig; winsorize
  or fit on a robust window for stability.
- Simple vs log returns: be consistent; `pct_change`-style simple returns
  are fine for daily VaR at typical magnitudes.
- Always state confidence level and holding period; VaR is a quantile, not a
  worst-case number (pair with cVaR from `skills/risk-metrics`).

## source
Lachowicz, *Python for Quants*, Vol. I, ch3, section 3.5 (Yahoo! Finance
data → `norm.fit` → PDF/CDF → quantile VaR).
Knowledge note: `knowledge/python-for-quants/ch03-fundamentals-of-numpy.md`.
Complementary: `skills/risk-metrics` (historical VaR/cVaR, drawdown, risk
contributions).
