# Ch05 — Trading Costs

**Source:** Irene Aldridge, *High-Frequency Trading* (2nd ed., 2013), Chapter 5.

## Purpose
The cost structure that "can make or break" an HFT strategy:
transparent (known in advance) vs. implicit (estimated) costs.

## Transparent costs
- **Broker commissions**: fixed or variable; negotiated in advance.
- **Exchange fees**: makers (liquidity suppliers) paid rebates, takers
  charged — "normal" exchanges; "inverted" exchanges reverse this.
  Complex orders (icebergs, VWAP) carry fee premiums.
- **Taxes**: HFT short-term profits are taxed at full rates; a 0.05%
  transaction tax would wipe out ~1/3 of trading volume (Aldridge
  2012 estimate).

## Implicit costs
1. **Bid-ask spread**: the premium for immediacy; compensation to
   patient limit-order traders; **rises with volatility** (limit
   traders demand more compensation when being picked off is likely).
2. **Slippage (latency cost)**: the adverse price move between
   decision and execution. Cost of latency: `COL = E[S_{t+l} − S_t]`
   — the expected dollar difference between slow and fast
   infrastructure. Slippage is worst at open/close and after macro
   announcements (order flow erodes finite liquidity).
3. **Market impact**: the price change caused by the trade itself.

## Market impact estimation
- Standard linear model (post-trade τ-tick impact):
  `ΔP_{t,τ} = α_τ + β_τ·V_t + ε_{t,τ}` where `ΔP_{t,τ} = ln(P_{t+τ}) − ln(P_{t−τ})`.
- Extensions add short-term volatility, spread, and intertrade
  duration as regressors (eq. 9).
- **Empirical results (Eurobund futures, 2009–2010)**: the size-
  independent intercept α (~10⁻⁵) dominates the size coefficient β
  (~10⁻⁷) — a 1-contract trade and a 100-contract trade incur
  *comparable* market impact; size effects only register above ~100
  contracts. Adjusted R² is only 1–2% (comparable to GARCH's ~5%).
  Buy/sell impact asymmetry is not statistically significant — good
  news for capacity.

## Key takeaways
- At tick frequencies, **implicit costs dominate transparent ones** —
  spread, slippage, and impact, not commissions, are the budget.
- Impact is mostly a **size-independent fixed cost** per trade in
  liquid futures; this is why per-trade gains must clear a high bar.
- Slippage is a function of market liquidity and competing order flow,
  not just your own speed.
