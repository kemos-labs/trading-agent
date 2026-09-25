# Ch09 — Vega and the Volatility Surface

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 9.

## Purpose
Vega (volatility sensitivity) for a book: why raw vega is meaningless for portfolios, the term structure of volatility, forward volatility, and the weighted (modified) vega approach.

## Vega basics
- **Vega** = ∂F/∂σ — sensitivity of the option to implied volatility for its own maturity; any convex structure has a vega. Best computed by repricing at perturbed volatilities.
- Bell-shaped in the money dimension, maximum ATM (by the forward). **Rule**: ATM vega is *stable* to volatility; away-from-the-money options are convex in volatility for the owner (their vega rises as vol rises), concave for the seller.
- Most vegas decrease with time — except lookbacks and reverse knock-outs whose vegas can increase with time.

## Vega vs. gamma
- Vega ≈ σ·t·Γ·S² (integral of expected gamma rebalancing P/L over the option's life at one volatility minus another). A long option's vega P/L from a vol rise equals the expected sum of gamma profits under the new volatility — barring slippage.

## Why raw vega is wrong for a book
- **Rule**: never compare, net, or add vegas of different maturities without weighting — front volatility moves more than back volatility (a crash raises 1-month vol much more than 1-year vol).
- The **modified vega**: bucket maturities, estimate each bucket's volatility-of-volatility and the correlation matrix between buckets, build an exposure vector, and compute a single weighted number via matrix algebra (vega for 10% vol moves × daily vol-of-vol per bucket).
- This captures sensitivity to *nonparallel* shifts of the volatility surface; neighboring buckets cancel more than distant ones.

## Forward volatility and the surface
- Non-time-homogeneous options (forward-start) are sensitive to *forward* (between-date) volatility, not just a single maturity vol — the term structure is the map of future vol expectations.
- Correlations between maturity buckets are low (0.1–0.3); shorter buckets are far more volatile (3% daily vs. 0.85% for the 6-12m bucket).

## Key takeaways
- Vega exposure must be maturity-weighted; raw summed vega misstates book risk badly.
- The volatility surface (smile + term structure) is the real object of study — it moves in nonparallel ways.
- Scenario analysis by repricing dominates derivative-based approximations for book-level vega risk.
