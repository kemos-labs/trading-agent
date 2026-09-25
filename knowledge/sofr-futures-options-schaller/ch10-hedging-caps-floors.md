# Chapter 10: Hedging Caps and Floors with SOFR Futures Options

## The Fundamental Problem
Hedging SOFR-based caps/floors with SOFR futures options is far harder than hedging swaps with SOFR futures (Chapter 9). The difficulty stems from two compounding issues:

1. **Options on 3M SOFR futures expire before the reference quarter** — so during the period when a caplet/floorlet's value is being determined, no 3M options exist.
2. **Options on 1M SOFR futures undergo the metamorphosis** into American-type arithmetic-average Asian options — for which no pricing model exists, meaning Greeks cannot be calculated.

This is in sharp contrast to the ED world, where options on 3M ED futures cover the same 3M LIBOR period as the cap/floor, enabling a near-perfect hedge.

## Two-Stage Hedging Framework

### Stage 1: Before Reference Period (Standard Options)
When the 3M SOFR future's reference quarter hasn't started, its options are standard American options on a forward rate. Hedging a SOFR-based IMM floor is as straightforward as hedging an IMM swap:
- Buy calls on 3M SOFR futures at strike = 100 − floor rate, matching the floorlet's dates.
- If dates/strikes don't match, use term-structure models (borrowed from ED options methodology) to compute hedge ratios.

### Stage 2: During Reference Quarter (Exotic Options)
Once the 3M options expire, switch to **options on 1M SOFR futures** as the only basis-free hedging instrument available. But these are Asian options — path-dependent, no closed-form pricing, no Greeks.

**Available approaches without a pricing model:**

1. **Static payoff replication:** Buy calls on consecutive 1M SOFR futures at strike = 100 − floor rate. This guarantees the minimum rate but is likely overpriced (pays for optionality that may not be needed).

2. **Dynamic strike adjustment:** As SOFR values become known during the reference period, adjust the strike downward to avoid overpaying. The adjusted strike for day k when n_k days are known:
   
   S_k = S_t − (A_n − S_t) × n_k / (n_t − n_k)
   
   where A_n = average of known SOFR values, S_t = original strike.
   
   This is analogous to delta hedging transferring P&L from expiry to pre-expiry, and the adjusted strike converges toward the floor rate as expiry approaches.

3. **Back-month 1M options for partial Greeks:** Options on the 2nd and 3rd 1M contracts are still standard → Greeks can be computed for a partial hedge against implied volatility changes. This shortens the unhedged period from ~3M to ~1M but doesn't eliminate it.

**Practical hedging sequence:**
1. Use 3M options while they trade.
2. Switch to 1M options with payoff replication + strike adjustment.
3. If early unwind is possible, use back-month 1M options for partial vega hedge.

## Daily Floors: An Additional Mismatch
The ARRC recommends applying floors to **each daily SOFR value** (for loans with prepayment options), not to the compounded rate over the reference period. This creates a **further mismatch** between the floor and the options on SOFR futures (which reference the compounded/averaged rate).

**Simulation results** (Vasicek + jump process):
- **Pure diffusion process:** Premium for daily vs compound floor is small (2–5% depending on parameters). Can be handled by overhedging by ~10%.
- **Pure jump process:** Premium is large and highly parameter-dependent:
  - Single FOMC meeting: 44% premium (equal probability of ±25bp/unchanged).
  - Two FOMC meetings: 72% premium.
  - Extreme scenario (certain −25bp then +25bp): 129% premium.
- **Jump-diffusion:** Premiums lie between the two extremes, closer to diffusion for typical parameters.

**Key insight:** The severity of the daily-floor mismatch depends critically on the assumed stochastic process. For diffusion-dominant dynamics, a simple overhedge may suffice. For jump-dominant dynamics (which dominate at low rates with active Fed policy), the floor must be modeled directly.

## Summary of SOFR Option Hedging Challenges

| Challenge | Cause | Impact |
|---|---|---|
| 3M options expire early | Specifications exclude reference quarter | No hedging instrument during most critical period |
| 1M options are Asian | Arith. avg + American exercise | No pricing model → no Greeks |
| Simple averaging (1M) | Contract specification | Mismatch with compounding-based caps/floors |
| Daily floor (ARRC) | Regulatory recommendation | Underlying differs from options on futures |
| Limited 1M product suite | Only 4 months listed | Cannot hedge long-dated caps/floors with 1M alone |

**Bottom line:** The transition from LIBOR to SOFR was designed to improve benchmark quality, but its unintended consequence is a significantly more complex options market. A functioning SOFR options market may require: (a) CME switching to European exercise + compounding for 1M contracts; (b) academic progress on American arithmetic Asian option pricing under jump-diffusion; or (c) both.
