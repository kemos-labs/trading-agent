# Chapter 8: Hedging the CME Term SOFR Rate

## The CME Term SOFR Methodology
CME publishes 1M, 3M, 6M, and 12M term rates using the first 13 1M and first 5 3M SOFR futures contracts as inputs. The core algorithm:

1. **Data aggregation:** Divide the trading day (7 a.m.–2 p.m. CT) into 14 × 30-minute intervals. In each interval, compute VWAP for each futures contract plus a random-time bid-ask snapshot. If VWAP is within the bid-ask, use it; otherwise use the nearest quote. The daily reference price is the volume-weighted average across all 14 intervals.

2. **Curve fitting:** Assume the overnight forward rate is a **step function with jumps only at FOMC meeting dates** (the "pure jump process"). This reduces the yield curve from ~250 unknown daily rates to ~10 step values.

3. **Objective function (Eq. 8.1–8.2):**
   Minimize: Σ w_m × (P_m − P̂_m)² + Σ w_q × (P_q − P̂_q)² + λ × Σ (θ_{i+1} − θ_i)²

   where the first two sums are squared pricing errors for 1M and 3M futures, and the last term is a **regularity penalty** (penalizing large step-to-step differences). λ = 1/(#FOMC meetings/year) ≈ 0.33.

4. **Term rates:** Compound the fitted step function using the ISDA formula.

## Key Properties of the Fit
- The fit is **global and non-local**: changes in any futures price can affect the entire curve. Futures whose reference periods are well outside the term rate's horizon can still influence the published term rate.
- The regularity penalty λ ≈ 0.33 can shift the 6M term rate by ~0.5bp — small in isolation, but material on billions of notional.
- The methodology is **opaque by design**: input prices, intermediate calculations, and the value of λ are not publicly disclosed.

## The Precise Hedging Approach
To hedge a forward-starting 3M CME Term SOFR payment:

1. **Build the stepwise curve** exactly as CME does (same FOMC-date step function, same objective function with same λ).
2. **Compute sensitivities:** Bump each of the 18 futures input prices by ±5bp independently, refit the curve each time, and compute the resulting change in the forward term rate and the associated interest payment.
3. **Construct the hedge:** For each futures contract j, sell N_j contracts where:
   N_j = (Δ payment / Δ futures price for contract j) in dollar terms

**Worked example:** Hedge a $100M 2-year loan's second quarterly payment (3M CME Term SOFR starting Apr 27, 2022) as of Jan 27, 2022. The hedge uses 13 1M and 5 3M contracts:
- Net short: 45 1M contracts + 25 3M contracts
- Equivalent to ~100 3M contracts in hedging power (consistent with $100M × 90/360)
- Most hedge weight is concentrated on contracts covering the payment's reference period (Apr–Jul 2022), but contracts outside this period still carry non-zero weights due to the global fit.

**Performance test:** A +25bp parallel shift in all forward rates post-Mar 16 produces a $63,263 increase in the interest payment, offset by a $62,830 gain in the futures portfolio — **hedge error of 0.7%**. A −40bp shift: $101,168 payment decrease vs $99,739 futures loss — **error of 1.4%**.

## Practical Considerations
- **Computational cost:** 36 nonlinear optimizations per quarterly payment (central differencing for each of 18 contracts × 2 bumps). A 5-year loan requires hundreds of optimizations.
- **Global nature of the fit:** Futures with no temporal overlap with the term rate can still affect it — a design feature, but one that introduces model risk.
- **Opacity:** The CME Benchmark Administrator does not publish input prices or intermediate calculations. Methodology changes are communicated only to licensed users, not the broader market.

**Key tradeoff:** The precise hedge is complex and computationally intensive but accurate. The approximate hedge (Chapter 2, jump-process calibration) is simpler but less precise. The choice depends on the hedger's accuracy requirements and infrastructure.
