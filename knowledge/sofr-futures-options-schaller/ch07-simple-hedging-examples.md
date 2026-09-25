# Chapter 7: Simple Examples of Hedging with SOFR Futures

## Hedge Ratio Methodology
Hedge ratios are **relative sensitivities**: identify a state variable (e.g., parallel curve shift), compute the change in hedge-target value per unit change in the state variable, and match it with the change in futures portfolio value per unit change.

**Number of contracts** = (desired sensitivity) / (futures BPV)

For a 3M SOFR future: BPV = $25/bp. For a 1M SOFR future: BPV = $41.67/bp.

The desired sensitivity for hedging a cash deposit is: 0.01 × (d/360) × notional, where d = calendar days in the reference period.

## Example 1: Perfect Date Match
Corporate treasurer hedges $50M of 3M overnight repo (Dec 18, 2019 → Mar 18, 2020) with 50 Dec-19 SR3 futures at 98.41 (implied rate 1.587%).

**Result:** The actual compounded SOFR averaged below the implied rate, so the deposit earned less than expected. The futures gained 0.1075 points, producing a $13,438 gain that nearly exactly offset the $13,851 shortfall on the deposit. **Hedge error: $413** — very small.

**Key point:** When dates match perfectly, the hedge is straightforward and effective.

## Example 2: Mismatched Dates
Same treasurer, but hedging a deposit from Dec 2, 2019 to Feb 28, 2020 — a 12-day mismatch at both ends versus the Dec-19 SR3 contract (reference quarter Dec 18–Mar 18).

**Method:** Fit a stepwise overnight forward curve using 1M SOFR futures prices (Dec/Jan/Feb), with jumps at FOMC meeting dates (Dec 11, Jan 29, Mar 18). Three unknowns (step heights), three futures → exact fit.

**Result:** The deposit fell $6,743 short of the forward-implied value. The futures gained $15,575 — **more than twice the shortfall**. The hedge overcompensated because actual SOFR continued falling after Feb 28 while the futures contract's reference quarter extended to Mar 18.

**Lesson:** Date mismatch introduces significant noise. Selling the futures at the end of the lending period (Feb 28) rather than holding to expiry would have reduced the mismatch (gain of $9,375 vs shortfall of $6,743).

## Example 3: 1M Futures for Better Date Alignment
Same deposit, hedged with a strip of three 1M SR1 futures (Dec/Jan/Feb) to better match the reference period.

**Result:** Futures gain of $6,380 vs deposit shortfall of $6,665 → **hedging error of only $285 (4.3%)** — much better than the 3M contract's mismatch.

## Key Lessons

1. **Hedge ratios are relative sensitivities.** Identify the state variable that drives both the hedge target and the hedging instrument, then match sensitivities.

2. **Dates matter enormously.** The closer the hedge instrument's reference period matches the hedge target's, the better the hedge. Mismatches introduce directional risk from curve shape and from events (FOMC meetings, rate jumps) occurring in the mismatched periods.

3. **Assumptions matter.** The parallel-curve-shift assumption is simple and often adequate, but can be improved with jump-diffusion process calibration (Chapter 8) when precision matters. The cost of a more sophisticated model must be weighed against the expected improvement.

4. **1M futures are more precise** for short-dated hedges (better date alignment), but their simple-average convention introduces a small mismatch with compounding-based instruments. 3M futures are better for quarterly-aligned exposures.
