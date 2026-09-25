# Ch02 — The Generalized Option

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 2.

## Purpose
A six-step framework for decomposing any option structure into the dimensions that matter for risk management — before pricing or hedging.

## The six dimensions
1. **Homogeneity of the structure** — is the payoff *time-homogeneous* (constant through time) or does it contractually change (deferred strike, window barriers, flexible barriers that widen over time)? Nontime-homogeneous structures are the hardest to manage.
2. **Type of payoff** — continuous (**ramp**, like vanillas) vs. discontinuous (**digital**/bet, all-or-nothing). Discontinuous payoffs are hard to hedge because market hedges are mostly continuous; but a bet is a small, harmless product *if traded as a bet* — dynamic hedging should be avoided with digitals.
3. **Barriers** — a trigger price that, when reached, alters the payoff (knock-in/knock-out).
4. **Payoff type variations** — American (early exercise/"if touched") vs. European (at expiration); path-dependence.
5. **Underlying instrument(s)** — cash, forward, futures; single vs. multiple assets (rainbow, basket, cross-currency).
6. **Assumptions on the pricing process** — constant volatility, no jumps, etc.; the distributional assumptions that the model makes.

## Decomposability
- **Decomposable**: a structure is the *sum* of simpler structures — a strangle = put + call; a cap = sum of caplets; a European double bet = two single bets.
- **Not decomposable**: double barrier ≠ two barriers; option on a basket/spread ≠ options on components; American double bet.
- **Limit-decomposable**: a lookback = infinite series of knock-ins; a binary = infinite narrow call spreads — useful for intuition even though nobody executes the replication.
- Decomposition is a *value-discovery and hedging orientation*; replication is the practical execution — often the two diverge.

## Pricing vs. hedging difficulty
- **Inverse relationship**: options trivial to price (binaries) are hard to hedge; options hard to price (Asians) are easy to hedge.
- Quants struggle with options easy to hedge (American) and find trivial what is arduous to trade (bets).

## Key takeaways
- Always decompose a structure to its smallest fragments before deciding how to hedge.
- The payoff-type (ramp vs. digital) and homogeneity dimensions dominate the hedging strategy.
- Time-dependent structures (barriers, deferred strikes) change their Greeks across periods — the model must accommodate the changing payoff.
