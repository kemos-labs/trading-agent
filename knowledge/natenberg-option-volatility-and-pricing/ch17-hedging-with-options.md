# Chapter 17 — Hedging with Options

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## Options as insurance

Futures transfer *all* risk of an underlying position; options transfer
only part — like insurance (premium = option price; strike gap below/
above spot = deductible). Hedgers are natural longs/shorts (producers,
users, lenders, borrowers) or voluntary positions needing temporary
protection. Every hedge trades off: upside participation for downside
protection.

## The basic toolkit

- **Protective put** (long position) / **protective call** (short
  position): unlimited profit potential in your favor, hard floor/ceiling
  against adverse moves. Simple and complete (no downside risk beyond
  the premium). Interest-rate analogs: **caps** (borrowers buy calls,
  cap the rate) and **floors** (lenders buy puts).
- Synthetically: long underlying + long put ≈ **long call**; short
  underlying + long call ≈ **long put**. So a protective put is really a
  synthetic long call.
- **Covered write** (sell against the position): immediate credit,
  limited protection only.
  - Stock 100, sell 95 call @6.50: break-even down to 93.50; called away
    above 95 (still keeps the 1.50 time premium). Sell 105 call @2.00:
    protection only to 98, upside participation to 105.
  - ATM options = most time premium → most popular covered writes.
  - **Buy/write**: buy stock + sell call as one transaction (single
    quote, e.g., 98.00 for stock 100 − call 2.00); tracked by the CBOE
    BXM index.
  - Selling a call at your target price locks in an exit; a
    **cash-secured put** at your target price locks in a purchase
    (company buy-backs; European version needs only PV(X) on deposit).
- Decide buy vs. sell purely on price-vs-value (implied vs. expected
  vol) — but practical needs (a price beyond which your business is
  threatened) override theory: buy the insurance even if "expensive."

## Collars

- Buy a protective option + sell a covered option against the same
  position: **long collar** = long underlying + long put + short call =
  a *bull vertical spread*; short collar = *bear vertical spread*.
  Known limited risk and reward at low or zero cost (zero-cost collar
  when premiums match). Gamma/theta/vega follow whichever leg the spot
  is nearer, and can be neutralized by strike choice. Names: fence,
  tunnel, cylinder, range forward, split-strike conversion.

## Complex hedging (vol-aware)

- Rule: **high implied vol → buy as few options as possible, sell as
  many as possible; low implied vol → the reverse** — anchored to the
  ATM option (ch. 12) and delta targets.
  - Hedging 50% of a long position: one ATM put (Δ−50) is theoretically
    cheaper than several OTM puts summing to −50 when IV is high.
  - Ratio writes (sell multiple calls vs. one position) create
    unlimited risk *both* directions — acceptable only if you're
    deliberately taking a volatility view, not truly hedging.
  - Calendar spreads and bear/bull verticals with chosen deltas hedge
    fractionally while letting you buy/sell vol as conditions warrant.

## Hedging reduces portfolio volatility (compound returns)

Worked example (annual returns): PM1 {+19,−14,+27,−9,+22} → avg +9%,
5-yr product 1.4429 (+44.3%) vs. PM3 {+35,+15,−35,+65,−20} → avg +12%
but 5-yr 1.3320 (+33.2%). Volatility destroys compounded wealth; a
steady 8% beats volatile arithmetic-mean winners. Measure with the
**Sharpe ratio** = average return / std dev of returns.

## Portfolio insurance (option replication)

When no market exists for the put you want, replicate it: long stock +
long put ≡ long call, so dynamically trade the stock to match the
call's delta (start 75% → sell 25%; rebalance to 60%, etc.) — the
dynamic-hedging process of ch. 8 run in reverse, usually via index
futures for transaction-cost reasons. Pre-1987, firms like Leland,
O'Brien, Rubinstein marketed this as cheap "synthetic puts."

- **Why it failed in the 1987 crash**: the volatility input was wrong
  (the crash was an unprecedented vol spike) and the continuous-hedging
  assumptions broke down; replication cost far exceeded the price of a
  real put. Widespread forced selling of futures during the crash may
  have amplified the decline.

## Key takeaways

1. Buy protective options when you need *defined* worst-case protection
   regardless of price; sell covered options when vol is rich and you
   accept one-sided risk.
2. Collars give defined risk/reward at minimal cost and are just
   vertical spreads.
3. Hedging is about survival and compounding (Sharpe), not maximizing
   arithmetic returns.
4. Delta-replication of options (portfolio insurance) works only while
   vol and hedging assumptions hold — it fails exactly when you need it
   most.
