# Ch07 — Adapting Black-Scholes-Merton: The Delta

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 7.

## Purpose
The first Greek demystified: what delta is, why the continuous-time delta is not a hedge ratio in practice, the modified delta, and forward vs. cash deltas.

## Delta definitions
- **Delta** = ∂F/∂U — sensitivity of derivative price to the underlying; the hedge ratio for an *infinitely small* move.
- Continuous-time delta is "useless" practically: no infinitely small moves exist, and a portfolio of options makes delta depart from any single hedge ratio. **Risk Management Rule**: use continuous-time models for pricing/benchmark fair value, NOT for hedging.

## Modified delta
- Finite-increment version: ΔF/ΔU over a meaningful move, ideally symmetric:
  Δ = (ΔF⁺/ΔU⁺ + ΔF⁻/ΔU⁻)/2 (average of up- and down-moves).
- Depends on the magnitude of the increment — hence on the operator's time frame, volatility expectation, and utility. **Rule**: delta depends on the operator's perception of future volatility and frequency of adjustments.

## Delta as a risk measure fails
- Two positions with identical delta can have opposite risk profiles: long 1,000 calls vs. short 1,000 puts of the same delta — same delta (~$200k), wildly different P/L shapes (one gains in rallies, other loses). Delta alone cannot distinguish long-volatility from short-volatility risk.

## Cash delta vs. forward delta
- BSM delta is a *cash* delta (amount of cash to hedge); for European options the true exposure is the *forward*. Cash delta = discounted forward delta; in FX the forward delta is discounted by the foreign rate (covered interest parity: F = e^(r−rf)t·S; delta of forward = e^(−rf·t)).

## The half-billion-dollar delta (barrier warning)
- Barrier-option deltas explode at the barrier (the "10,000% delta" story): a risk manager vetoed a trade because delta implied a $500M equivalent position, though max loss was $400k. The delta is meaningless near a barrier — leaving the trade alone as a bet with positive expected value is often the conservative approach.

## Delta and volatility
- Rising volatility raises the delta of out-of-the-money calls and lowers that of in-the-money calls (lognormal drift).
- Delta ≠ probability of exercise — delta accounts for payoff size; the binary option accounts only for frequency (see ch17).

## Key takeaways
- Use the modified (finite-increment) delta for hedging, not the theoretical tangent.
- Delta is a poor standalone risk measure; gamma, vega, and third derivatives complete the picture.
- Near barriers and exotics, delta limits are dangerous management tools — scenario analysis beats Greek limits.
