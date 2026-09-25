# III.3 Options

Source: Carol Alexander, *Market Risk Analysis*, Vol. III (Pricing, Hedging
and Trading Financial Instruments), ch III.3.

## Core idea

An option gives the right (not obligation) to buy (call) or sell (put) an
underlying at a strike. Its price depends on the underlying price and its
volatility, so option traders are simultaneously trading both. Hedging +
no-arbitrage → **risk-neutral valuation**: price = discounted expected payoff
under the risk-neutral measure. Market prices come from supply/demand; model
prices come from calibrated models (BSM, binomial, LIBOR).

## Foundations

- Underlying modeled as geometric Brownian motion (GBM): log price/returns
  normal → lognormal prices. Black-Scholes-Merton (1973) prices European
  options under GBM; the same year the CBOE launched exchange-traded options.
- **Risk-neutral measure / numeraire**: under the risk-neutral measure all
  asset prices grow at the risk-free rate; option value = discounted
  expectation of payoff. Hedging argument: a self-financing replication
  portfolio makes the option redundant.
- **Binomial model**: discrete-tree approximation of GBM; the building block
  for American options and the basis of many numerical schemes.

## Vanilla options

- European (exercise at expiry only) vs American (any time).
- **Put-call parity**: `C - P = S - X*exp(-rT)` (European, no dividends) —
  links calls and puts of the same strike/maturity; violated prices imply
  arbitrage. Used to derive lower bounds and to price the missing side.
- **Moneyness**: S/X (price), S/X·exp(rT) (forward); ATM/ITM/OTM.
- **American options**: early exercise may be optimal (dividends, deep-ITM
  puts); exercise boundary separates exercise from hold regions; pricing via
  binomial/lattice, finite differences, or (LSM) Monte Carlo.

## Greeks and hedging

Sensitivities to risk factors (the main two: underlying price, volatility):
- **Delta**: ∂V/∂S — directional risk; delta-hedge by trading the underlying.
- **Gamma**: ∂²V/∂S² — convexity; measures delta instability; gamma-hedge
  with other options.
- **Vega**: ∂V/∂σ — volatility risk; vega-hedge with options (the underlying
  has zero vega).
- **Volga**, **rho** (interest rate), **theta** (time decay).
- **Position Greeks** (per unit) vs **value Greeks** (per portfolio, dollar-
  weighted): value Greeks are additive across instruments; position Greeks
  are not. Example solves a linear system to make a portfolio
  gamma-vega-volga neutral, then delta-hedges with spot FX contracts.

## Trading strategies

Directional: bull/bear spreads (call spreads, put spreads, collars); volatility
plays: straddles, strangles, butterflies, condors (isolate volatility from
direction); calendar spreads. Replication of P&L profiles via options
combinations.

## Black-Scholes-Merton model

Under GBM + constant volatility/rates/dividends, any claim satisfies the BSM
PDE; the European call/put have closed forms (the BSM formula with N(d1),
N(d2)). The price equals the cost of a replication portfolio. BSM serves as:
- a pricing formula (under its assumptions), and
- a **transform**: invert market prices → **implied volatility** (ch III.4).

Stochastic-volatility adjustment to BSM prices (e.g., Heston) corrects for
the flat-smile assumption.

## Interest rate options

- **Caps/floors**: portfolios of options on forward rates (caplets/floorlets).
- **Swaptions**: options on swaps.
- **LIBOR market model**: multifactor model with correlated Brownian motions
  driving market forward rates; calibrated via PCA; used to price exotic
  interest-rate options (Bermudan swaptions).

## Key takeaways

- Risk-neutral valuation: price = discounted risk-neutral expected payoff;
  BSM closed form under GBM, binomial for American.
- Put-call parity ties calls/puts; use it to check prices and derive bounds.
- Hedge with value Greeks (additive): delta with the underlying, gamma/vega/
  volga with options — solve the linear hedge system.
- Implied volatility is the market's view of future vol; the BSM formula is
  the standard transform.

Related skills: `skills/binomial-tree-pricing`, `skills/monte-carlo-option-
pricing`, `skills/parametric-var`; see also ch III.4 (volatility) and
`knowledge/market-risk-analysis-vol1/ch-i5` (numerical methods).
