# II.4 Introduction to GARCH Models

Source: Carol Alexander, *Market Risk Analysis*, Vol. II (Practical Financial
Econometrics), ch II.4.

## Core idea

Financial returns exhibit **volatility clustering** (Mandelbrot 1963): calm
periods follow calm periods, turbulent periods follow turbulent. Moving
average models assume i.i.d. returns and constant volatility, so their
forecasts equal the current estimate. GARCH (Engle 1982 ARCH; Bollerslev 1986
generalization) models conditional variance as an autoregressive process and
captures clustering: forecasts are higher or lower than the long-run average
over short horizons and converge to the long-term volatility as the horizon
grows.

## The symmetric normal GARCH(1,1)

With conditional distribution `r_t | I_{t-1} ~ N(0, sigma_t^2)`:

```
sigma_t^2 = omega + alpha * r_{t-1}^2 + beta * sigma_{t-1}^2
```

- `omega`: the constant, related to long-run variance `V = omega / (1 - alpha - beta)`.
- `alpha`: sensitivity to the most recent shock (error/ARCH term).
- `beta`: persistence (GARCH term).
- Stationarity requires `alpha + beta < 1`; volatility is positive as long as
  all parameters are positive.

**Unconditional vs conditional variance**: unconditional variance is the
constant long-run average; conditional variance changes every period as new
information arrives.

**Forecasting**: the h-step-ahead variance forecast is a weighted average of
the current conditional variance and the long-run variance, mean-reverting at
rate `(alpha + beta)^h`. Fixing the long-term volatility to a pre-assigned
value (e.g., 20%) is easy: fix omega from the target and estimate only alpha,
beta.

## Asymmetric GARCH

Symmetric GARCH responds identically to positive and negative shocks, but
equity markets show a **leverage effect**: volatility rises more after a
price fall than after a rise of the same magnitude (commodities often show the
reverse asymmetry). Asymmetric models:
- **A-GARCH / GJR-GARCH**: adds a dummy/indicator on negative shocks, e.g.
  `sigma_t^2 = omega + alpha*r_{t-1}^2 + gamma*I(r_{t-1}<0)*r_{t-1}^2 + beta*sigma_{t-1}^2`.
- **E-GARCH**: models `ln(sigma_t^2)`, so no positivity constraints are
  needed and asymmetric response is built in via sign terms; usually the best
  in-sample fit and attractive for option pricing (volatility rather than
  variance as the primitive).

**GARCH-in-mean** adds the conditional variance to the mean equation,
capturing two-way causality between returns and volatility.

## Non-normal errors

Student-t conditional errors (additional degrees-of-freedom parameter) better
capture the heavy tails of daily/high-frequency returns. The likelihood
function changes but the variance equations and forecasting formulas do not.
In the FTSE 100 case study, Student-t E-GARCH gave the best fit of the six
models compared (normal/t for GARCH, GJR, E-GARCH).

## Multivariate: O-GARCH

Estimating a full covariance matrix with multivariate GARCH is
high-dimensional. **O-GARCH** applies PCA (ch II.2) first: take k principal
components of returns, run k *univariate* GARCH models on the component
variances, and reconstruct

```
V_t = W* * Phi_t * W*'
```

where Phi_t is the diagonal matrix of component conditional variances. The
result is always positive semi-definite. With a highly correlated system
(term structure, k = 3), hundreds or thousands of time-varying covariances
follow from just a few univariate GARCH fits. O-GARCH also gives analytic,
mean-reverting h-day forecasts. It is recommended only for highly correlated
systems; the number of components controls noise in the correlation estimates
(e.g., hedging energy futures: few components filter out noise that
RiskMetrics' EWMA would react to).

## Key takeaways

- GARCH = autoregressive conditional variance; `alpha + beta` measures
  persistence, forecasts mean-revert to long-run variance.
- Use GJR/A-GARCH or E-GARCH when shocks are asymmetric (equities); E-GARCH
  avoids positivity constraints.
- Student-t errors for fat tails; verify with likelihood comparisons.
- O-GARCH = PCA + univariate GARCH for tractable positive semi-definite
  covariance matrices on term structures.

Related skills: `skills/arma-garch-modeling`, `skills/risk-metrics`; PCA
mechanics in the ch II.2 note.
