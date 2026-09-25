# Ch10 — Capital Asset Pricing

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes) — Steven
Shreve

## The optimization problem

An agent with initial wealth X₀ invests in stock and money market to
maximize E[log X_n] (log utility = maximize expected growth rate; Kelly
criterion territory). Key observations:

- Whatever portfolio is used, the discounted wealth X_k/(1+r)^k is a
  **martingale under the risk-neutral measure Q**: the agent can't create
  value out of nothing. Hence E_Q[X_n/(1+r)^n] = X₀ — the **budget
  constraint (BC)**.
- Conversely, any random variable ξ satisfying the BC can be produced by
  some portfolio: treat ξ as a European derivative paying ξ at time n, and
  hedge it (the market is complete).

So the problem reduces to a constrained optimization: find the terminal
wealth ξ maximizing E_P[log ξ] subject to E_Q[ξ/(1+r)^n] = X₀.

## Solution

Solve with Lagrange multipliers (maximize Σ log x_k·P(ω_k) subject to
Σ ζ_n(ω_k)·x_k·P(ω_k) = X₀, where ζ_n = Z_n/(1+r)^n is the state price
density). First-order condition gives

```
ξ ∝ 1/ζ_n = (1+r)^n / Z_n
```

i.e. terminal wealth is **inversely proportional to the state price
density** — optimal portfolios are long the cheapest states, short the
expensive ones. The agent holds a portfolio whose payoff is richest in
states where the density (market price of risk) is low.

## Portfolio construction

The optimal ξ is a European claim; the hedging portfolio (delta replication
from ch3–4) implements it. Two-fund separation emerges: the optimal
investment is a combination of the money market and a "growth-optimal"
portfolio whose weight in the stock depends on the market price of risk.

## Relation to CAPM intuition

- The growth-optimal portfolio plays the role of the market portfolio.
- Expected returns on assets are explained by covariance with the
  state-price-density-driven growth-optimal portfolio (a discrete CAPM):
  assets with high covariance with ζ (bad states) get higher expected
  returns.
- The density process Z encodes the market price of risk: Z_{k+1}/Z_k =
  discount-factor increments; E[Z] = 1.

## Key takeaways

- Any tradable strategy must satisfy the budget constraint
  E_Q[discounted terminal wealth] = initial wealth; completeness makes the
  constraint both necessary and sufficient.
- Log-optimal (growth-optimal) terminal wealth = c/ζ_n — inversely
  proportional to the state price density.
- The optimal portfolio is implemented by delta-hedging the claim; it is
  the discrete CAPM's growth-optimal/market portfolio.
- Pricing of any claim = E_Q[discounted payoff]; utility only selects which
  claim to hold.
