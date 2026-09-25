# Ch11 — The Greeks and Their Behavior

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 11.

## Purpose
The dynamics of the Greeks: how delta and gamma *bleed* with time, the "speed" (third derivatives) with spot, and the moments of an option position.

## Time and space effects
- Time and volatility exert the same effect on first/second derivatives (variance is a proportion of time); time acts independently only on the carry/discount terms.
- **Bleed** = change in delta/gamma with the passage of time (repricing one day shorter): delta bleed and gamma bleed.
- Time pushes OTM options further OTM (deltas shrink) and ITM options further ITM (deltas grow); gamma effects are mixed for OTM options.
- **Rule**: an option position that is long up-gamma and short down-gamma (long OTM calls, short OTM puts) bleeds into shorter delta over time, and vice versa — provable via put-call parity.

## Speed and third derivatives
- The "D"s: DdeltaDspot, DgammaDspot, DvegaDspot — how the Greeks themselves move with spot. Books with mixed strikes concentrate away from the money and have guaranteed meaningful daily bleeds.
- Weekend/friday effects: time systems advance in 24-hour jumps (some 365-day, some 7-day); "which delta sheet" disagreements affect hedges.

## Moments of an option position
- The normal distribution is characterized by mean and variance; option books live in the higher moments:
  - **First moment**: delta — exposure to the mean (direction).
  - **Second moment**: gamma — exposure to variance.
  - **Third moment**: delta of the gamma ("skew") — asymmetry; positive if gamma becomes more positive in rallies.
  - **Fourth moment**: gamma of the gamma ("tails") — convexity of the book; positive → the position is convex (gamma increases when the market moves away from center).
- Odd moments indicate symmetry, even moments convexity. Books spread across time and space become sensitive to "moments of moments" without bound.

## Vega as a function of spot and vol
- Vega depends on where spot is relative to strikes and on the volatility level; "option clusters" (low vol/flat vega, high vol/negative vega) map the Greek landscape — books can be convex or concave to vol depending on the cluster.

## Key takeaways
- Single-option intuition fails for books: the mixture of strikes produces bleed and higher-moment exposures that simple Greeks miss.
- Risk limits based on delta alone are dangerous; the third/fourth derivatives and scenario analysis are the real control.
- Time decay (bleed) is topical — it reverses at the strike that caused it — so Greek dynamics must be analyzed in (spot, time) space.
