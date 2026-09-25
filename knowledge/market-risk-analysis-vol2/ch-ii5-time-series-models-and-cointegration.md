# II.5 Time Series Models and Cointegration

Source: Carol Alexander, *Market Risk Analysis*, Vol. II (Practical Financial
Econometrics), ch II.5.

## Core idea

Stationary processes are mean-reverting and therefore predictable; integrated
processes (random walks) have infinite variance and are unpredictable — the
best forecast of tomorrow's price is today's. Individual asset prices are
typically integrated, but a **linear combination** of them (a spread) can be
stationary; such prices are **cointegrated**: tied together in the long run by
a common stochastic trend. Correlation measures short-term comovement of
returns and says nothing about long-term price relationships; cointegration
is the long-term measure.

## Stationary processes

A process is stationary if mean and variance are finite constants and the
joint distribution of (X_t, X_s) depends only on t-s (weak/covariance
stationarity relaxes the third condition to covariances). The AR(1):

```
X_t = alpha + phi * X_{t-1} + eps_t,   eps_t ~ i.i.d.(0, sigma^2),  |phi| < 1
```

has unconditional mean `alpha/(1-phi)` and variance `sigma^2/(1-phi^2)` —
finite only when |phi| < 1, the stationarity condition. Mean-reversion speed
after a shock increases as phi decreases; phi = 0 gives the i.i.d. process
(fastest reversion).

**Unit root tests** (augmented Dickey-Fuller) test whether the AR coefficient
equals 1 (a stochastic trend) against the stationary alternative.

## Cointegration

Formal definition: X and Y (both integrated) are cointegrated if there exists
a coefficient such that the **disequilibrium**

```
Z_t = X_t - beta * Y_t
```

is stationary. The cointegrating vector is (1, -beta). Two integrated series
have at most one cointegrating vector; n series can have up to n-1.
Cointegrated prices share a **common stochastic trend** (Stock & Watson):
X_t = W_t + eps^X, Y_t = W_t + eps^Y with W a random walk — the spread
X - Y = eps^X - eps^Y is stationary even though each series wanders.

## Testing for cointegration

- **Engle-Granger**: regress one log price on the other(s), test the
  residuals for stationarity (ADF). Simple; OLS minimizes residual variance
  so it suits benchmark tracking where the dependent variable is clear.
- **Johansen**: maximum-likelihood procedure over the whole system; trace
  tests determine the number of cointegrating vectors. Better when there is
  no natural dependent variable or when n > 2.

**Engle-Granger index tracking**: regress log(index) on log(stock prices);
if residuals are stationary, normalize the betas to sum to 1 — the
cointegration-optimal tracking portfolio has stationary, minimum-variance
tracking error. With too few stocks, cointegration may be undetectable.

## Error correction models (ECM)

The Granger representation theorem: cointegrated variables have a
misspecified VAR in differences — the lagged disequilibrium term must be
included. The ECM (second stage of the analysis):

```
dX_t = ... + theta_1 * Z_{t-1} + eps_1t
dY_t = ... + theta_2 * Z_{t-1} + eps_2t
```

The **error correction** is the self-regulating mechanism: with
Z = X - beta*Y and beta > 0, we need theta_1 < 0 and theta_2 > 0 — a large
positive Z pulls X down and Y up, restoring equilibrium; magnitudes give the
speed of adjustment. The Engle-Yoo test for cointegration is based on the
significance of the theta coefficients.

**Granger causality**: if lagged X helps predict Y beyond Y's own lags, X
Granger-causes Y. Cointegration implies Granger causality between returns;
the converse does not hold (common volatility could cause it).

## Applications

Index tracking, enhanced index tracking, statistical arbitrage, pairs
trading, calendar spread trading. Correlation-based long-short strategies
have no reversion mechanism and require constant rebalancing; cointegrated
strategies are anchored by the long-run equilibrium.

## Key takeaways

- Correlation ≠ cointegration: returns can be highly correlated with no
  price cointegration, and vice versa.
- Two-stage analysis: (1) find/estimate the long-run equilibrium (unit-root
  test the spread), (2) model short-run dynamics with an ECM.
- Use Engle-Granger when the dependent variable is clear (tracking),
  Johansen for general multivariate systems.

Related skills: `skills/cointegration-testing`, `skills/kalman-filter-pairs`,
`knowledge/market-risk-analysis-vol1/ch-i4` (regression).
