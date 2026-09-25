# Chapter 17 — Valuation Framework

## Core idea
The theoretical foundation of the DX derivatives library: the **Fundamental
Theorem of Asset Pricing**, **risk-neutral discounting**, and a
**market-environment** container class.

## Fundamental Theorem of Asset Pricing
- No-arbitrage ⇔ existence of an equivalent **martingale (risk-neutral)
  measure** under which discounted prices drift at the risk-free rate.
- Worked example: stock 10 → 20 or 0 (60/40). Call with strike 15.
  - Naive expectation under the real-world measure: `0.6*5 = 3` — wrong,
    because it embeds the stock's 20% risk premium.
  - Replication: buying 0.25 of the stock perfectly hedges the option
    (0.25*20 = 5) → option value 2.5, not 3.
  - Under the martingale measure (50/50), the stock's expected return is
    zero and `0.5*5 + 0.5*0 = 2.5` — the correct arbitrage-free price.
- Lesson: price by **no-arbitrage/replication** (or risk-neutral
  expectation), never by real-world expectation.

## Risk-neutral discounting
- `constant_short_rate` class: discount a future payoff `V(T)` as
  `V0 = V(T) * exp(-r*(T-t))`.
- In Monte Carlo valuation: `V0 = exp(-r*T) * mean(payoff(paths))`.

## Market environments
- `market_environment` class: a container for everything needed to price an
  instrument — constants (strike, maturity, currency, initial value), lists,
  and curves (vols, rates).
- One environment per instrument; the same environment is shared between
  simulation and valuation objects — the glue of the DX architecture.

## The pricing-by-expectation recipe
1. Model the underlying under the risk-neutral measure (ch18).
2. Simulate paths.
3. Discount the average payoff.

## Pitfalls
- Pricing under the real-world measure (with risk premia) overvalues
  derivatives — always use the risk-neutral measure.
- Discounting must use the same curve as the model's drift (consistency).
- Incomplete markets (jumps, stochastic vol) have multiple martingale
  measures — the choice must be justified (e.g., calibrated to market, ch21).

## Bottom line
The theory chapter: why risk-neutral pricing works, the discounting class,
and the market-environment container. It grounds the DX library built in
ch18–21. Cross-ref: `knowledge/stochastic-calculus-finance/ch17-girsanov...`
and `ch22` (arbitrage pricing summary).
