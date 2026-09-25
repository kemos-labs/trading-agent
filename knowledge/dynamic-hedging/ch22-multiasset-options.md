# Ch22 — Multiasset Options

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 22.

## Purpose
Options on several assets: rainbow, basket, and product structures — with the correlation dimension as the central, unstable risk.

## Categories of multiasset structures
- **Choice** (best of, worst of, rainbow): payoff = largest in-the-money portion among the strike-asset pairs; one expiration in the simple case.
- **Linear combinations** (baskets, spreads): the sum of exponentials is not an exponential — pricing complications and minor skew exposure; resemble Asian options in difficulty.
- **Products/quotients**: easy to price, harder to hedge (e.g., the Mexican structured note case).

## Rainbow options and correlation
- Dual-asset example (two assets at 100, 15.7% vol each, 50% correlation): the payoff covers more area than either single option but less than the sum of two independent options.
- **Correlation vega**: sensitivity of price to the correlation parameter — for n assets there are n(n−1)/2 correlation vegas (a correlation matrix of vegas). Correlation is often written off as constant — the most dangerous assumption (ch6).
- Extremes: ρ = +1 → structure trades like either single option (or the higher-vol one); ρ = −1 → twice a regular option (one asset is guaranteed ITM).
- A call on A + put on B structure has the opposite correlation behavior: negative correlation depresses its price.

## The covariance matrix
- Portfolio-level risk = covariance matrix Σ (the "volatility" of a multiasset book); it must be positive definite (no negative "volatility"); correlation and vol boundaries keep it arbitrage-free.
- Correlated vs. uncorrelated Greeks: the dual-asset option has more than one delta; the hedger's assumptions about correlation stability change how to trade the structure.

## Indexed notes case study
- A Mexico USD-denominated note paying max(CETES option, LIBOR option) is a multiasset structure that can only be decomposed via correlation analysis — and is priced on a statistical (expected expiration value) basis because the market is incomplete; use term (expiration) volatility and correlation, not instantaneous ones.

## Key takeaways
- Multiasset exotics are all managed by the same dynamic-hedging machinery — learn one (the rainbow), generalize to the rest.
- Correlation is a first-class Greek: estimate it, monitor its instability, and hedge it if the structure demands.
- Covariance-matrix positivity (arbitrage-free) is the constraint that keeps multiasset books sane.
