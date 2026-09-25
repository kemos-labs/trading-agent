# Chapter 8 — Dynamic Hedging

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## The idea

Buying an underpriced option isn't enough — you must establish a
**delta-neutral hedge** (opposing underlying position at ratio 100/Δ)
and **rebalance periodically** so the position is direction-neutral.
This turns the option's life into a *series of bets* at favorable odds,
smoothing short-run luck toward the theoretical edge.

## Stock example (underpriced call)

- S = 97.70, 10 weeks to expiry, r = 6%, "true" (crystal-ball) vol
  37.62%. June 100 call theoretical 5.89, market 5.00 → buy 100 calls
  (Δ50) and sell 50 stock. Edge = 100 × 0.89 = 89.00.
- Weekly rebalancing: recompute Δ with current S (vol & rate held
  constant), trade stock to zero total deltas. Rising S → positive
  deltas → sell stock; falling S → buy stock. Long gamma forces **buy
  low / sell high**.
- At expiry (S = 103.85): option leg 100×(3.85−5.00) = −115.00; original
  hedge 50×(97.70−103.85) = −307.50; but **adjustments +467.55**
  (forced trades). Interest: option carry −500×6%×70/365 = −5.75; on
  hedge credit +4,885×6%×70/365 = +56.21; on adjustment cash flows
  −5.28. Total cash flow +90.24 → PV 90.24/(1+0.06×70/365) = **89.21** ≈
  theoretical 89.00.
- Only volatility is unobservable; here the 10 weekly moves really
  annualize to 37.62%.

## Frictionless assumptions & reality

Model assumes: unrestricted trading, one constant rate for borrow/lend,
zero transaction costs, no taxes. Real world: short-sale restrictions
and rebate haircuts, locked-limit futures, borrowing≠lending rates,
transaction costs, taxes. Interest is the least consequential deviation;
transaction costs determine **adjustment frequency**:

- Adjustments don't change expected return, only *dispersion* of
  outcomes. Frequent rehedging (cheap for a professional) concentrates
  results near the model prediction; a retail trader who adjusts less
  takes on more luck — same long-run EV.
- Two rehedging styles: fixed time intervals, or rehedge only when the
  delta drift exceeds a threshold (e.g., tolerate ±500–1,000 deltas).
  More tolerance → less cost, more variance.

## Breakeven volatility & early exit

- The hedge breaks even exactly at the option's **implied volatility at
  the trade price** (32.40% for the call bought at 5.00). Realized vol
  above it → adjustments out-earn time decay (profit); below → loss.
- If implied vol re-evaluates up to your target (37.62%), just sell the
  options and buy back the underlying: immediate 89.00, no need to ride
  to expiry. If implied vol moves *against* you (32.40 → 30.35, −35.00),
  that's a mark-to-market noise, not a verdict — hold and hedge if your
  forecast is right. You can rarely pick the bottom/top of implied vol.

## Futures-option variant (overpriced put)

- Futures 61.85, 10 weeks, r = 8%, true vol 21.48%. March 60 put value
  1.46, price 1.70 (implied 23.92%) → sell 100 puts (Δ−35) + sell 35
  futures, rehedge weekly. Same structure except: no upfront cash on
  futures (margin + daily variation), so interest accrues on *variation
  credits/debits* (e.g., 35 × (61.85−60.83) = 35.70 credit earning
  8%×63/365 = 0.49). Total PV 23.96 vs. predicted 24.00.
- Note the US vs. non-US convention: options on futures are stock-type
  settled in the US (paid in full up front), futures always futures-type.

## Replication principle

*Dynamic hedging replicates an option: the sum of all hedging cash
flows, discounted, equals the option's theoretical value.* Buying cheap
options + dynamic hedging is equivalent to selling them back at fair
value; selling rich options + hedging is equivalent to buying them back
at fair value.

## Key takeaways

1. Delta-neutral + periodic rehedging captures theoretical edge; the
   hedge P&L ≈ option value − price, provided the realized vol input was
   right.
2. Hedge adjustments = realized-vol exposure; you profit when realized
   vol exceeds the *implied* vol embedded in the trade price.
3. Adjustment frequency is a cost-vs-variance tradeoff, never a source
   of edge by itself.
