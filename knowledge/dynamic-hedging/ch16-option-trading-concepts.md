# Ch16 — Option Trading Concepts

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 16.

## Purpose
The core trading concepts: replication (static vs. dynamic), neutral spreading, and the path-dependence that dynamic hedging imposes.

## Replication
- **Option replication** = a self-financing method to reproduce an option's payoff with other instruments; in practice covers all operations done through options.
- **Static replication**: find a match requiring no continuous rebalancing — reduces P/L variance and transaction costs. Easiest form: put-call-asset arbitrage. Warn against statically replicating instruments with a *stopping time* (binaries, barriers) with constant-duration instruments.
- **Recursive replication** (the author's method): enumerate future states (asset-price nodes), then find trades that match the Greeks on every state (delta, modified gamma, modified vega, theta, modified rho, bleed, correlation delta). The best static hedge matches Greeks on all nodes — but spread costs can eat the income, pushing the choice to dynamic hedging.

## Dynamic hedging
- **Dynamic hedging**: keep minimum Greek exposure, rebalancing continuously toward neutrality — starts with delta rebalancing, extends to gamma (via options), rho, etc.
- **Makes every option path dependent** — the central warning of the book. With transaction costs, the *path* of the market (not just the terminal price) determines the hedger's P/L.
- Rule: variance of P/L is usually underestimated; time diversification does not work for a leveraged trader continuously monitored by risk management.

## Neutral spreading
- **Neutral spreading**: buy some options against selling others (different strikes/expirations) — a dynamic-hedging form that accepts some Greek risk for compensation; the market-making craft (many successful firms started as spreaders).
- Spreading captures the central limit (reduces luck, maximizes skill), insulates from model/formula risk (put-call parity forces same-strike puts/calls to the same time value), and gives leverage access.

## Path-dependence in practice
- The "nasty path" table: a delta-hedged short option can bleed losses day after day while spot drifts slowly against the gamma — the P/L path, not the final spot, is what hurts; absorbing P/L barriers (stop-outs) make results worse than the worst-case scenario analysis suggests.
- Skew and implied-volatility evolution widen the gap between idealized and realized hedging P/L.

## Key takeaways
- Replication choice is a cost-vs-robustness trade-off: static (cheap, fragile) vs. dynamic (robust, costly, path-dependent).
- Every dynamically hedged position is path-dependent — evaluate hedging P/L over paths, not just terminal states.
- Spreading is the foundational market-making technique; it insulates against model error.
