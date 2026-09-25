# Ch18 — Binary Options: American Style

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 18.

## Purpose
American binary ("if touched") options: stopping-time structure, gamma/vega monotonicity, hedging case studies, and the at-settlement variant.

## American binaries
- **American binary (digital)**: pays when the price is *touched* at any time before expiration — path-dependent, with an unknown, unstable "duration" (stopping time). Costs about twice the European equivalent (it can terminate anytime).
- The American binary is a *bet on time* — the distribution of the expected time to extinction is what matters (the contamination principle localizes gamma and vega around the trigger).

## Gamma/vega monotonicity
- **Rule (no drift, flat forward)**: the American binary never changes sign of gamma/vega — it is a pocket of localized long vega (for the owner).
- **Rule (carry)**: the American binary is positive gamma everywhere (for the owner) when the delta hedge against it incurs *negative carry* (forward rising); with positive carry exceeding the time decay, the profile becomes a risk reversal (nonzero third moment).
- Unlike the European binary (a risk reversal), the American binary is generally monotonic in gamma.

## Hedging case studies (the book's method)
- Hedging the 105 "if touched" bet (long $10M): decompose P/L into option leg vs. delta-hedge leg across spot levels; vega is managed with vanilla structures, but near the trigger the "pin" dominates.
- The delta hedge is unwound *at the barrier* — execution risk (gaps, slippage) is the real cost; "gap deltas" matter.
- Non-Greek view: for stopping-time products, state-based analysis (what happens at each strike) beats Greek reports — traders "divorce" a barrier book from vanillas to see the strikes clearly.

## At-settlement binaries ("if settled")
- An at-settlement binary pays only if the underlying *officially settles* through the trigger — acts European *during* the day and American *between* days: creates a **negative gamma hole** around the trigger (mixed gamma).
- The trader doesn't know whether the market will stay in the terminating zone — unwinding the gap delta is the core difficulty.

## Key takeaways
- American binaries are the training wheels for barrier options: they isolate the stopping-time problem.
- Their gamma/vega sign depends on carry vs. time decay — the *sign stability rules* are the hedger's navigation tools.
- Execution risk at the trigger (gap deltas, slippage) dominates model risk for these products.
