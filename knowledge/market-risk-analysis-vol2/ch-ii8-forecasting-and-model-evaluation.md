# II.8 Forecasting and Model Evaluation

Source: Carol Alexander, *Market Risk Analysis*, Vol. II (Practical Financial
Econometrics), ch II.8.

## Core idea

How to choose between competing econometric models. Two families:
- **Goodness-of-fit (in-sample)**: how well the model captures the estimation
  sample's characteristics.
- **Post-sample (out-of-sample)**: how accurately the model forecasts. This
  is the more important one — an excellent in-sample fit (many parameters)
  often forecasts worse than a parsimonious model, and portfolio risk is
  inherently forward-looking.

There is no definitive best model: accuracy depends on the criterion and the
sample period, and different models win under different criteria.

## Returns models (in-sample)

- **R^2** = ESS/TSS; F test for significance with
  `F = (R^2/(k-1)) / ((1-R^2)/(T-k)) ~ F(k-1, T-k)`. R^2 always rises with
  added regressors — reward **parsimony** via **adjusted R^2** or likelihood-
  based criteria (AIC/BIC: penalize log-likelihood by parameter count).
- **Distributional comparison**: simulate from the fitted model and compare
  the simulated returns distribution or the ACF of squared returns with the
  empirical counterparts (KS-type tests; RMSE/MAE on the ACFs).

## Volatility models (forecasting)

- **Regression R^2 tests are weak**: regressing squared returns on variance
  forecasts gives a very low maximum R^2 even for a correctly specified GARCH
  (Andersen-Bollerslev: max R^2 ≈ 0.36 for realistic parameters) due to the
  noise in squared returns; similarly RMSE-vs-squared-returns criteria are
  poor. Don't reject a volatility model on these grounds.
- **Out-of-sample likelihood**: compare the likelihood of the out-of-sample
  returns under each model's density forecasts — higher likelihood wins.
- **Moving average / EWMA models**: volatility and correlation forecasts are
  flat at the current estimate; evaluate against GARCH-style benchmarks.

## Tail forecasts: coverage tests (Christoffersen 1998)

For interval/tail forecasts (e.g., VaR exceedances):

- **Unconditional coverage (Kupiec)**: likelihood ratio test that the
  observed exceedance rate equals the expected:
  ```
  LR_uc = ((1-pi_exp)^n0 * pi_exp^n1) / ((1-pi_obs)^n0 * pi_obs^n1)
  -2 ln LR_uc ~ chi-sq(1)
  ```
  with n1 = exceedances, n0 = non-exceedances, pi_obs = n1/n.
- **Conditional coverage**: tests that exceedances are *independent* — a
  model is worse if breaches cluster (several VaR violations in a row).
  Combines the coverage LR with an independence LR on the transitions of the
  exceedance indicator; also ~ chi-sq(2) / chi-sq(1) component.

**VaR backtest procedure**: fix alpha and portfolio weights; roll the
estimation window; each step forecast h-period variance (equally weighted or
EWMA), set `VaR = -Phi^-1(alpha) * sigma_hat` (normal linear VaR, or
simulation for GARCH); count exceedances against realized returns; apply both
coverage tests. In the S&P 500 example, EWMA passed both tests for 5% 1-day
VaR while the equally weighted model failed conditional coverage (missed
volatility clustering) — a practical demonstration of why conditional
volatility modeling matters.

## Operational criteria (backtesting)

Subjective, use-case-specific performance criteria for trading models, hedging
models, portfolio optimization, and VaR estimation; the procedure is common
(define loss, forecast, compare out-of-sample, score) but the criteria and
tests differ by use.

## Key takeaways

- Prefer out-of-sample evaluation; penalize complexity (AIC/BIC).
- Squared-return-based volatility diagnostics are inherently low-power — use
  likelihood or coverage tests instead.
- Kupiec unconditional + Christoffersen conditional coverage are the standard
  statistical backtests for VaR/interval forecasts.
- A model that fits best in-sample (Student-t E-GARCH) need not forecast
  best — always check out-of-sample.

Related skills: `skills/risk-metrics`, `skills/parametric-var` (VaR
estimation; this chapter adds the backtest half of the workflow),
`skills/walk-forward-validation`.
