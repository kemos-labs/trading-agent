# Chapter 22 — Stock Index Futures and Options

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## Index mechanics

- **Price-weighted** (DJIA): Σ prices / divisor — high-priced stocks
  dominate (Stock A at 80 = 53% of a 150 sum vs. B = 13%). Each point
  move in *any* component changes the index by 1/divisor (0.67 for
  divisor 1.5).
- **Cap-weighted** (S&P 500): Σ (price × shares) / divisor, using the
  **free float** — large-cap stocks dominate. **Equal-weighted**: ratios
  of current/initial price, periodically rebalanced (divisor/continuity
  adjusted by the prior period's growth); geometric-weighted: nth root
  of the price-ratio product.
- **Divisor** = target/raw value, set so the index opens at a round
  number; adjusted for splits (price-weighted only — caps are
  unaffected), component replacement, and (for **total-return indexes**
  like DAX) dividends.
- Key identity: `%Δ index = Σ (%Δ stock_i × weight_i)` — used to
  estimate the index when a component is halted (e.g., 1,425.50 × [1 +
  0.025 × (67.75−63)/63] ≈ 1,428.2). Closing index values may use VWAP
  over the last period.

## Index futures

- All index futures are **cash-settled** (final variation only).
- Fair value approximation: `F = S × [1 + (r − d)·t]` with d = average
  annualized index dividend yield. Fine for long-dated; **short-dated
  contracts are distorted by dividend lumpiness** (Dow example: annual
  estimate 2.75% vs. near-zero payout if the cycle's dividends are
  already paid).
- **Index arbitrage / program trading**: buy program (buy basket, sell
  rich futures) or sell program; carried to expiry, liquidated via
  market-on-close → exchanges moved to **AM expiration** (opening
  prices) to avoid closing imbalances. Risks: variable rates, dividend
  estimates, short-sale frictions.
- **Hedge ratio is not 1:1** (settlement risk, cf. ch. 15): the futures
  delta ≈ **1 + r·t** index units; the stock basket must exceed exact
  replication by r·t, shrinking as expiry nears (4 mo @ 6% → hold 1.02×
  the index; 3 mo → 1.015×). Rates up hurt buy programs (they borrow);
  dividends up help buy programs.
- **Structural downward bias**: equity portfolio managers are almost
  always long stocks and hedge by *selling* futures; the offsetting
  arbitrage side requires shorting a basket (harder, costly), so index
  futures persistently trade below fair value.

## Index options

- **Options on index futures** (CME, 1983): exercise/assignment →
  futures position (margin + variation; e.g., exercise Feb 1,000 call,
  futures 1,025, multiplier $100 → long March future + $2,500 credit).
  At quarterly expiry (futures + options + cash options all settle —
  **triple witching**, 3rd Friday) in-the-money options cash-settle.
  American; early-exercise value only under stock-type settlement.
- **Options on the cash index** (OEX 1983; now European — early
  exercise proved problematic): cash-settled at AM expiration from
  opening prices; hedged with the same-index futures.
- **Underlying price for valuation = the futures (forward) price**; at
  quarterly expiry cash-option and futures-option prices converge (the
  option is on the forward). For serial months with no matching future,
  back out the forward from put-call parity:
  `F = (C − P)·(1 + r·t) + X`. Example: Nov 1,000 combo 34.80 − 29.85,
  2 mo @ 6% → F_Nov ≈ (4.95)(1.01) + 1,000 = **1,005**; with Dec
  futures at 1,010, Nov options price off Dec futures − 5.00. Check the
  Dec combo: (1,010−1,000)/1.015 = 9.85 → Dec 1,000 put = 44.60 − 9.85
  = 34.75; Nov/Dec 1,000 roll = 9.85 − 4.95 = **4.90**.
- ETFs trade like equity options (PM expiration).

## Key takeaways

1. Futures delta ≈ 1 + r·t index units (not 1) — index-arb baskets
   must be scaled and rebalanced.
2. Short-dated index forwards are dividend-timing-sensitive; long-dated
   are fine with a dividend-yield approximation.
3. Trade index options against the futures/forward price, not the spot
   index; serial-month forwards come from put-call parity.
