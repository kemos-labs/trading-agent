# II.1 Factor Models

Source: Carol Alexander, *Market Risk Analysis*, Vol. II (Practical Financial
Econometrics), ch II.1.

## Core idea

A portfolio's return is approximated as a weighted sum of returns to a set of
**market risk factors**; the weights are **factor betas** estimated by
regression. Factor models let a portfolio manager forecast expected returns,
decompose risk, run stress scenarios on factors, and construct optimal
allocations. They apply to any risky-asset portfolio (equities, bonds, hedge
funds, commodities, real estate), though bond portfolios are better served by
principal-component curve models (ch II.2).

Two distinct risks:
- **Systematic risk** — undiversifiable; the risk carried by the factor
  returns times the portfolio's net sensitivity to each factor.
- **Specific (idiosyncratic/residual) risk** — the variance of the regression
  residuals; high for a single asset but diversifies toward zero in a large
  portfolio.

## Single index model

CAPM in return form, with a broad market index (or any benchmark) as the
factor:

```
R_it = alpha_i + beta_i * X_t + eps_it,   eps_it ~ i.i.d.(0, sigma_i^2)
```

- `alpha_i`: expected return relative to the benchmark (positive =
  outperformance).
- `beta_i`: factor sensitivity; `beta_i * sigma_X` = systematic volatility.
- `sigma_i`: specific volatility.

For a portfolio, alpha, beta, and specific return are **weighted sums** of the
individual assets' characteristics — no new estimation needed.

## Risk decomposition

Portfolio variance in the single-factor model splits as:

```
Var(R_p) = beta_p^2 * sigma_X^2 + sum(w_i^2 * sigma_i^2)
```

- `beta_p^2 * sigma_X^2`: systematic risk.
- `sum(w_i^2 * sigma_i^2)`: specific risk, which shrinks as the portfolio
  diversifies (the cross terms vanish under the i.i.d. assumption).

Beta, correlation, and relative volatility are related:
`beta_i = rho_iX * sigma_i / sigma_X`, so the systematic-risk share depends on
how correlated the asset is with the factor.

## Multi-factor models

General formulation: expected return = alpha + sum over factors of
`beta_k * F_k`; betas estimated by multiple linear regression of asset returns
on factor returns. Factor types: market indices, industry, style (value,
growth, momentum, size), economic (interest rates, inflation), statistical
(principal components). For international portfolios, exchange rates enter
with a beta of one. Style attribution decomposes a portfolio's return into
contributions from each factor class.

**Multicollinearity** plagues fundamental factor models: correlated
explanatory variables make OLS betas unstable. Remedy: **orthogonal
regression** — transform the factor set so the regressors are uncorrelated
(e.g., via PCA on the factor returns) before estimating.

## Barra model

The canonical commercial multi-factor model: assets get exposures to **risk
indices** (industry + style descriptors such as value, momentum, size,
liquidity), and **fundamental betas** are estimated per descriptor. Risk is
decomposed into contributions from each risk index plus specific risk.

## Active risk and tracking error

**Tracking error** (volatility of active returns) is only a valid active-risk
metric when the fund tracks a benchmark. For actively managed funds it can
mislead — an increase in tracking error does not imply reduced active risk.
The book shows how to adjust tracking error into a correct basic active-risk
metric by decomposing active returns into factor and specific components.

## Key takeaways

- Factor betas = regression weights; the portfolio's factor characteristics
  are weighted averages of its assets'.
- Decompose total risk into systematic + specific; only specific risk
  diversifies.
- Beware multicollinearity in fundamental factor models — orthogonalize the
  factors.
- Tracking error is a metric for benchmark-tracking, not general active risk.

Related skill: `knowledge/market-risk-analysis-vol1/ch-i4` (regression),
`ch-i2` (linear algebra) and `skills/portfolio-optimization`.
