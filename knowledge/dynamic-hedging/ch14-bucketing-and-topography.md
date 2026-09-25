# Ch14 — Bucketing and Topography

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 14.

## Purpose
Institutional risk-management practice: bucketing the book's Greeks by time interval, and mapping the book's topography across parameters — the static methods behind daily risk reports.

## Straight bucketing
- **Bucketing** = breaking the position's risk into time intervals: delta buckets, gamma buckets, vega buckets, rho buckets, etc.
- **Straight bucketing**: exposure between cash and expiration t for products with known, certain expiration and immediate start.
- Static: markets assumed constant; no convexity shown; higher moments hidden — the method's key weakness.

## Worked example (6-month GBP-USD call)
- Forward from covered interest parity; spot delta = forward delta discounted by the foreign rate (82656 / (1 + (183/360)·0.06915) ≈ 79850).
- Gamma: ±$8,355k per 1% market move (approximation — the third derivative distorts at the maximum-gamma point).
- Vega: $438k per 1 vol point. Rho2 (foreign): delta × rate × 183/360 × 100bp, present-valued (≈$408k). Rho1 (domestic): same minus the premium financing cost (4.578M × 183/360 × 100bp ≈ $23k → net ≈ $385k).
- Convexity of rates lowers the negative P/L from foreign-rate rises.

## American and path-dependent options
- Straight bucketing fails for American (early-exercise) and path-dependent (barrier, compound) options: their exposure is not anchored to a single known expiration; the "duration" is a stopping time.
- For such products the bucketing must be horizon-aware (expected stopping time) — the Greeks are unstable, so nonparametric/state-based views (what happens at each strike) beat Greek reports.

## Topography
- Extend the bucketing concept across the parameter space (spot, vol, rates): a *map* of the book's P/L over moves — the precursor of full scenario grids.
- Correlation matrices and covariance matrices describe portfolio-level topography (see ch22's multiasset matrix and Module D's correlation triangles).

## Key takeaways
- Bucketing is the daily-driver of institutional risk reporting: delta/vega/gamma by time bucket gives a digestible exposure snapshot.
- It is a static approximation — higher moments, convexity, and stopping-time products escape it; supplement with scenario analysis.
- The distinction straight vs. path-aware bucketing decides whether exotic books are measured correctly.
