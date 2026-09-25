# Ch10 — Theta and Minor Greeks

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 10.

## Purpose
Time decay (theta) and the supporting Greeks: modified theta, shadow theta, convexity, plus the barrier trader's "stealth" and "health" measures.

## Theta and the "rent"
- **Theta** = loss in time value from the passage of time (traders call it the "rent" paid for gamma). If an option is priced at the right volatility (rates = 0), expected time decay is zero — time decay is not the expected P/L.
- Convention: theta excludes premium financing costs (self-financing neutrality).

## Modified theta and shadow theta
- **Modified theta**: today's price at current vol minus tomorrow's price at the *one-day-shorter* option's volatility — interpolated with √time, capturing the expected drop along the vol curve.
- **Shadow theta**: regular theta plus the price impact of the expected decline in implied vol in a quiet market (quiet → vol expectations fall). Reverse decay can occur before scheduled events (vol is held high). **Rule**: if the trader believes vol will drop in a frozen market, include that in time decay.
- Theta is path-independent and weak: it cannot capture whipsaw; tighter rebalancing mitigates accelerated time decay.

## Minor Greeks
- **Rho**: sensitivity to interest rates (Rho1 domestic, Rho2 foreign); stable for short-dated options.
- **Speed (DdeltaDspot)**, DgammaDspot, DvegaDspot — third derivatives; matter for books (see ch11).
- **Vega ratio**: deep-ITM vega ≈ 100 − delta of the mirror OTM option; put-call parity equalizes vegas of same-strike European puts/calls.

## Stealth and health (barrier tools)
- **Stealth** = percentage difference between strike and trigger — how much the barrier option resembles a vanilla (high stealth → vanilla-like).
- **Health** = percentage difference between current spot and trigger — execution risk: how close the trader is to the barrier unwind point; warning when it drops below 1 standard deviation.
- The expected stopping time (first exit time) is a more potent measure (ch18/19).

## Convexity
- **Convexity** = second derivative w.r.t. a parameter: gamma for spot, vega-convexity d²V/dσ² for vol, bond convexity d²B/dy².
- OTM options are convex to volatility and rates; convexity must be associated with the volatility of the parameter concerned.

## Key takeaways
- Theta is only meaningful jointly with gamma (and vol expectations) — the "rent" for convexity.
- Shadow theta/gamma handle the market's habit of changing vol when spot is quiet or moves.
- Stealth and health are simple, practical barrier-risk yardsticks; the expected exit time is the deeper measure.
