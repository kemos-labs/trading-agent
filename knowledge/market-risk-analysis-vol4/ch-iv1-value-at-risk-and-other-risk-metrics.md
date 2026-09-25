# IV.1 Value at Risk and Other Risk Metrics

Source: Carol Alexander, *Market Risk Analysis*, Vol. IV (Value at Risk
Models), ch IV.1.

## Core idea

A market risk metric summarizes the uncertainty in a portfolio's future value
(P&L). Volatility and correlation are only sufficient when returns are
multivariate normal (or Student-t). VaR is the near-universal metric:
the amount that could be lost with chosen probability α. Its attractions:
measures risk factors AND sensitivities, comparable across markets, universal
across activities, scalable from trade to enterprise level, and aggregation/
disaggregation accounts for dependencies.

## VaR definition

100α% VaR is minus the α-quantile of the portfolio return/P&L distribution:
`P(X < x_α) = α`, VaR = −x_α. In a risk model we distinguish the **risk
model** (statistical model for the return distribution: risk-factor mapping +
multivariate distribution + resolution method) from the metric itself.

**Normal linear VaR** (i.i.d. normal returns, percentage terms):

```
VaR_α = Phi^-1(1 - α) * sigma - mu
```

e.g., Φ⁻¹(0.99) = 2.3264 for 1% VaR. In value terms multiply by the current
portfolio value P_t. The expected-return term matters over long horizons but
is negligible over a few days (banks ignore it). Over h days with i.i.d.
returns, use σ_h = σ·√h (square-root-of-time) and μ_h = h·μ.

## Risk factor level and aggregation

- **Systematic (total risk factor) VaR**: measured via the risk-factor
  mapping (equities mapped to indices/betas, cash flows to zero-coupon rates/
  PV01, FX sensitivity = 1). **Specific (residual) VaR**: risk not captured
  by the mapping.
- **Stand-alone VaR**: component risk ignoring diversification; the sum of
  stand-alone VaRs is usually greater than total VaR (normal linear VaR is
  sub-additive in this sense).
- **Marginal VaR**: diversification-adjusted component VaR; the marginal VaRs
  sum to total risk-factor VaR — hence used for real-capital allocation.
- **Incremental VaR**: the VaR associated with a single new trade.

## Risk metrics beyond VaR

- **ETL (expected tail loss)** = conditional VaR = average of losses beyond
  VaR — "how much we lose given VaR is breached". Simple to estimate once a
  VaR model exists.
- **Expected shortfall (ES)**: conditional metric associated with benchmark
  VaR.
- **Coherent risk metrics** (Artzner): sub-additivity, monotonicity,
  positive homogeneity, translation invariance. ETL and ES are coherent; VaR
  and benchmark VaR estimated by simulation are NOT sub-additive — the main
  objection to VaR (it can penalize diversification).
- Downside/benchmark metrics (omega, kappa indices) from portfolio
  management tradition; tracking error is only valid for passive index
  trackers.

## Three resolution methods

1. **Normal linear (parametric) VaR** — analytic formula under i.i.d. normal.
2. **Historical VaR** — empirical quantile of historical (adjusted) returns.
3. **Normal Monte Carlo VaR** — simulate normal returns, compute the quantile.

A case study on $1000/point equity index position shows the same portfolio can
give materially different VaR under the three models — the model choice is
itself a source of risk (model risk, ch IV.6).

## Key takeaways

- VaR = −(α-quantile); normal linear VaR = Φ⁻¹(1−α)σ − μ, scaled by √h
  under i.i.d.
- Systematic VaR via risk-factor mapping; specific VaR is residual.
- Stand-alone VaRs sum ≥ total VaR; marginal VaRs sum = total (capital
  allocation); incremental VaR for new trades.
- VaR is not sub-additive in general; ETL/ES are coherent — prefer ETL.

Related skills: `skills/risk-metrics`, `skills/parametric-var`,
`skills/var-backtesting`, `skills/downside-risk-measures`.
