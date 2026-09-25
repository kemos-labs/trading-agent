# III.5 Portfolio Mapping

Source: Carol Alexander, *Market Risk Analysis*, Vol. III (Pricing, Hedging
and Trading Financial Instruments), ch III.5.

## Core idea

Map large portfolios to a finite set of **risk factors** with portfolio
**sensitivities** to each factor, then portfolio value change becomes a
function of factor changes. For linear portfolios (bonds, swaps, FRAs, cash,
futures, forwards) the mapping is exactly linear with constant sensitivities;
for options portfolios it is non-linear and needs (at least) second-order
Taylor approximations. Risk-factor sensitivities are only aggregable in
**value terms** and only comparable within an asset class.

## Cash flow mapping (interest-rate portfolios)

- Risk factors: zero-coupon rates at standard vertices (1m, 2m, ..., 30y) —
  a **zero curve** (LIBOR at the long end for interbank). All cash-flow
  portfolios in a currency share one curve; PV01 vector is the sensitivity
  vector.
- **PV01 invariance**: mapping cash flows to vertices must preserve present
  value, duration, and PV01. A cash flow at time T between vertices T1 < T < T2
  splits into weights x (to T2) and 1-x (to T1) chosen so the weighted average
  maturity matches: `x = (T - T1)/(T2 - T1)` (present-value preservation);
  PV01-invariant conditions: continuous compounding `sum x_i*T_i = T`;
  discrete compounding `sum x_i*T_i/(1+R_i) = T/(1+R_T)`. Interpolate the
  non-vertex zero rate (Svensson/cubic splines).
- The mapped portfolio P&L is a linear function: `dV = sum PV01_i * dr_i` —
  all non-linearity lives in the (constant) sensitivities; risk analysis is
  then matrix-based.

## Futures/forward portfolios

Risk factors = spot price + discount curve + basis. Basis risk may be hard to
model (large and uncertain in commodities); prefer a set of **constant
maturity futures** as risk factors in that case. Cash-flow mapping principles
extend directly.

## Options portfolios: delta-gamma mapping

- Risk factors: underlying prices (or rates) and implied volatility surfaces;
  minor: discount rate and time.
- Portfolio value is non-linear in the underlying, so use the second-order
  Taylor (delta-gamma) approximation:
  `dV ~= delta*dS + 0.5*gamma*dS^2 + vega*dsigma + theta*dt + rho*dr`.
- **Position Greeks are not additive across underlyings; value Greeks are.**
  Use value delta / value gamma (dollar Greeks) to net over the portfolio.
- **Price beta mapping**: reduce the number of underlying price factors by
  mapping many assets to one index/reference via beta — value delta/gamma
  w.r.t. the index depend on each asset's beta.
- **Multivariate delta-gamma**: with many underlyings the approximation
  involves the full covariance matrix of factor changes — matrix algebra and
  PCA are used to reduce the factor dimension.
- Interest-rate (rho) and time (theta) sensitivities are also expressed in
  value terms; the option portfolio has a curve of zero-coupon rate factors
  by maturity.
- **Volatility beta mapping**: each option has its own implied-vol factor —
  huge dimension. Map to reference **volatility indices** by maturity via a
  volatility beta, similar to price beta mapping (Vftse term-structure case
  study).

## Risk measurement practice

- Banks decompose undiversifiable risk into factor volatility × portfolio
  sensitivity; sensitivities can't be compared across asset classes (PV01 vs
  beta vs Greeks).
- Traders operate under limits on net value delta, gamma, vega (sometimes
  theta, rho); mapping lets them check positions against limits and identify
  hedge needs. Banks increasingly replace sensitivity limits with VaR limits.

## Key takeaways

- Cash-flow mapping to a zero curve with PV01 sensitivities is exact and
  linear; preserve PV, duration, and PV01 when splitting flows between
  vertices.
- Options need delta-gamma (second-order) mapping; use value Greeks to net
  across underlyings.
- Reduce factor dimension with beta mappings (price and volatility) and PCA.
- Sensitivity limits (delta/gamma/vega) are the traditional risk control;
  VaR is replacing them.

Related skills: `skills/risk-metrics`, `skills/portfolio-optimization`,
`knowledge/market-risk-analysis-vol2/ch-ii2` (PCA for factor reduction).
