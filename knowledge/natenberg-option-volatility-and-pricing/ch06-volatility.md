# Chapter 6 — Volatility

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## Volatility = speed of the market

Options require a *speed* estimate because only the portion of the price
distribution past the strike generates value. Higher volatility spreads
the distribution → **all** options (calls and puts, any strike) gain
value; lower volatility cuts all values.

## Normal distributions (quincunx / random walk)

- Symmetric, bell-shaped; fully described by **mean** (peak location) and
  **standard deviation** (spread).
- Empirical rules: ±1σ ≈ 68.3% (~2/3), ±2σ ≈ 95.4% (~19/20), ±3σ ≈
  99.7% (~369/370) of occurrences. "Unlikely ≠ impossible" (15 heads in
  a row has odds < 1/32,000).
- The mean of the price distribution = the **forward price** (arbitrage
  constraint from ch. 5). The various Black-Scholes forms differ mainly
  in forward-price calculation.
- σ is additive in price-distance terms: with mean 7.5 and σ = 3, troughs
  5–10 are within 1σ (≈2/3 of balls); a 30:1 bet on troughs 14–15 is bad
  because 2σ covers ±6 → beyond-2σ total is 1/20, split by symmetry →
  1/40 per tail.

## Volatility as annualized standard deviation

- **Working definition**: volatility = one σ *percent* price change over
  one year. E.g., forward 100, vol 20% → 68% probability of finishing in
  80–120, 95% in 60–140, 99.7% in 40–160. With dividends/rates, scale
  the mean to the forward first: S = 100, r = 8% → forward 108, 1σ =
  20% × 108 = 21.60.
- **Time scaling (square-root rule)**: σ_t = σ_annual·√t (t in years) —
  unlike interest, volatility scales with √time. Daily: divide annual by
  16 (√256 trading days); weekly: divide by 7.2 (√52). Example: $45 at
  37% vol → daily 1σ = 45 × 0.37/16 = $1.04; weekly = 45 × 0.37/7.2 =
  $2.31. Same probabilities apply to scaled σ.
- **Realized volatility** = annualized σ of log price changes
  (settlement-to-settlement; ln(P_t/P_{t−1}) is standard; business days
  only for daily sampling). Choice of sampling interval (daily/weekly/
  monthly) barely changes the result. Distinguish historical vs. **future
  realized** vol — the future value is what a model actually needs.
  Checking: 5 daily moves of ~±0.7–1.0 on a 45 stock are inconsistent
  with 37% (realized was 27.8%) — you'd expect a >1σ day about 1 in 3.
- **Implied volatility** = the vol that makes model value equal to market
  price (run the model backwards). It is the market's consensus future
  volatility for that expiry and is treated as the option's *price*
  ("sold the 105 call at 28.50"). Pitfalls: results depend on the model
  and on contemporaneous inputs (a stale 3.60 quote from two hours ago
  at stock 99.25 instead of 98.50 gives 26.95% instead of 28.50%).
  Composite market IVs weight ATM options / volume / open interest.

## Value vs. price

- Option *value* ← future realized volatility; option *price* ← implied
  volatility. Buy when implied < expected realized; sell when implied >
  expected realized (the weather analogy: forecast vs. what the crowd is
  wearing).
- Mispricing is best expressed in volatility points (3.60 vs. 2.94 =
  3.50 vol points overpriced), enabling cross-strike comparisons (100
  call at 5.40 = 27.51% vs. 105 call at 3.60 = 28.50% → 100 call is
  cheaper in vol terms).

## Volatility sensitivity principles (preview of vega)

1. In *total points*, a vol change moves **at-the-money** options most
   (1600 call +9.95 when vol 14→18 vs. 1800 call +2.27).
2. In *percent terms*, it moves **out-of-the-money** options most (1800
   call +291%, 1400 put +585%).
3. **Long-term** options move more than short-term at the same strike.
4. In-the-money options are the least vol-sensitive (they trade more like
   stock — sensitivity shifts to underlying moves).

Most volume therefore concentrates in ATM/OTM options. Calls and puts at
the same strike/expiry move nearly identically with vol and carry
similar implied vols — the put-call parity signature (ch. 15).

## Interest-rate contract quirk

Eurodollar/Euribor futures quote as 100 − rate (93.00 = 7% LIBOR). Use
**rate volatility** (not price volatility); index strikes from 100 too,
and swap calls ↔ puts (a 93.00 call = a 7.00% put). Bonds/notes don't
need this; they have both yield-volatility and price-volatility
conventions.

## Key takeaways

1. σ_t = σ_ann·√t; daily ≈ vol/16, weekly ≈ vol/7.2.
2. Compare implied vol (price) with your expected realized vol (value);
   express option prices in vol terms.
3. Lognormal (continuous compounding) is the realistic distribution —
   bounded below at zero, mean right of the peak, and symmetric
   percentage OTM calls worth more than puts (110 call > 90 put).
