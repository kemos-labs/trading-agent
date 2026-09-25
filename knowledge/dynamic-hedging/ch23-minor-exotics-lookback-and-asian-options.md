# Ch23 — Minor Exotics: Lookback and Asian Options

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 23.

## Purpose
Lookback, ladder, and Asian options — "minor exotics": no new trading insight, but rich in skew exposure and hedging nuance.

## Lookback options
- **Lookback (floating strike)**: the owner sells the high or buys the low over the period; very costly (≈ twice a vanilla premium) — rarely traded.
- **One-sided gamma**: once a maximum is reached, gamma exists only if a new extreme is set — a "cliff with a flat top" gamma profile, unlike the bell shape of a vanilla. The hedger is not whipsawed both ways.
- **Roll-over replication** (Goldman-Sosin-Gatto): a lookback call = original ATM call + the stochastic-integral cost of rolling down to a lower strike whenever the market drops ("strike bonus"). This reveals the skew exposure: a lookback call is *more valuable* with a downside skew (its gamma sits at the lowest price); a lookback put less so.
- **Rule**: the lookback's third-moment exposure cannot be hedged with vanillas — its gamma stays at the recorded extreme while vanilla gamma drifts.

## Ladder options
- **Ladder (discrete lookback)**: sell the high / buy the low in set increments (e.g., $5). Cheaper than a lookback (payoff capped at the lookback's); decomposable as a strip of knock-in options: long KI(S,S), short KI(S,S+5), long KI(S+5,S+5), … — useful for skew modeling (each KI priced by ch19's methods).

## Asian options
- **Asian**: payoff depends on a weighted combination of prices over a period — average floating strike (like a lookback on the average) or fixed strike settled at the average. Geometric vs. arithmetic averages.
- **The pricing problem**: the geometric average of a lognormal process is lognormal (closed-form, simple BSM-style); the *arithmetic* average is not — it's a sum of exponentials, with little lognormality, hence no closed form (only approximations/moment-matching or Monte Carlo).
- **Hedging intuition**: the variance of the average ≈ 1/3 the variance of the underlying (ratio of second moments ~ 1/√3) → hedge an Asian with a vanilla in ~1.73:1 gamma-neutral ratio; the residual spread is short the skew. A sum of exponentials does not compound like an exponential of a sum.
- Asians are "easy to hedge, hard to price" — commonly given to junior traders for their regularity.

## Key takeaways
- Lookbacks/ladders concentrate gamma at the extreme — a one-sided, un-hedgeable-with-vanillas risk profile.
- The arithmetic-average Asian is the canonical "hard to price, easy to hedge" structure — Monte Carlo and moment-matching are the practical tools.
- Skew is the common thread: exotic payoffs interact with the skew structure in ways vanilla intuition misses.
