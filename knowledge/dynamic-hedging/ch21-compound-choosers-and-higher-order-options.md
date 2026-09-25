# Ch21 — Compound, Choosers, and Higher Order Options

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 21.

## Purpose
Options on options: compound options, choosers, and their sensitivity to the fourth moment (volatility of volatility) — a warning about mispricing under constant-volatility models.

## Compound options
- **Compound option (second-order)**: an option on a European option — the right to buy/sell an underlying option (given strike K, maturity t_final) for a price K₁ at an intermediate date t₁. Third-order = option on a compound option; nth-order generalizes with t₁ < t₂ < … < t_final.
- Every strike needs a put/call specification (the indicator function) — four basic combinations (call-on-call, call-on-put, put-on-call, put-on-put).
- **Critical sensitivity**: compound options are extremely sensitive to higher derivatives — the *fourth moment* (volatility of volatility) and the second moment with respect to volatility. They depend on the thickness of the tails far more than vanillas.
- **Pricing warning**: no known closed form with stochastic volatility at the time of writing; constant-volatility models are dangerous; the author prices with the available formula and adds a markup for vvol.

## Chooser options
- **Chooser**: owner decides at an intermediate date whether the structure is a put or a call (possibly at different strikes — "gutspin" chooser; the owner picks the furthest in-the-money).
- **Bounds**: if the choosing date = expiration, the chooser is a straddle; if the decision is immediate, it's the max(call, put). Value increases with the choosing period up to the straddle price.
- The chooser resembles a rainbow option (picking one of two "assets" — the put or the call); its value peaks when the correlation between the put and call reaches its maximum.

## Higher-order structures and cap/floortion context
- Compound elements appear in captions/floortions (options on baskets of caplets/floorlets): the basket element allows covariance-matrix analysis; the compound element demands an analysis of the volatility of volatility; front vs. back contracts have different vol sensitivity.

## Key takeaways
- Compound/chooser options are the tail-risk products: their value and hedge live in vvol and higher moments, not just spot and vol level.
- Constant-volatility pricing systematically misprices them — always apply a vvol markup/assessment.
- Decompose by decision points (intermediate dates/strikes) to understand the structure's state-dependence.
