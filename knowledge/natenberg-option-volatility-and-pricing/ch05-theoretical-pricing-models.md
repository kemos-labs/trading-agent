# Chapter 5 — Theoretical Pricing Models

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## Direction vs. speed

An option trader must be right about both *direction* and *speed* of the
underlying. A stock trader who's right about direction is assured of
profit; an option trader who's right about direction can still lose if
the move is too slow to overcome time-value decay. Strategies that
depend only on speed (not direction) exist — this is the core of
volatility trading.

## Probability machinery

- **Expected value**: Σ pᵢ·outcome. Die: (1+2+…+6)/6 = 3.5. Roulette:
  $36/38 = $0.9474 for a $1 bet on one number → ~5¢ casino edge.
- **Theoretical value** = present value of expected value:
  95¢/(1 + 0.12·2/12) ≈ 93¢ for a payout 2 months later at 12% — the
  interest you forgo while holding the bet. Dividends/bonuses are
  additive corrections (like a 1¢ early payment).
- Probability is only reliable *in the long run*; the short run can
  bankrupt the house → risk management matters as much as pricing.

## Building a pricing model (4 steps)

1. Propose possible prices for the underlying at expiration.
2. Assign probabilities such that the market is *arbitrage-free*:
   **E[underlying] = forward price** (the forward price is the market's
   consensus future value). Probabilities need not be symmetric (book
   example: 6%/15%/39%/33%/7% over 83/90/99/110/123 sums to 102 = the
   two-month forward of 100 at 12%).
3. Compute expected option payoff: `E[call] = Σ pᵢ·max(Sᵢ − X, 0)`,
   `E[put] = Σ pᵢ·max(X − Sᵢ, 0)`.
4. Discount to present value per the settlement convention.

The forward price is central — for European options the current spot
matters only through the forward. Distinguish **at the money** (X =
spot) from **at the forward** (X = forward); the latter are often the
most liquid benchmark options.

## Black-Scholes family

- Lineage: Castelli 1877 (covered-write, straddle) → Bachelier 1900
  (*Theory of Speculation*) → Black-Scholes 1973 (European options on
  non-dividend stocks) → Black 1976 (futures options) →
  Garman-Kohlhagen 1983 (FX options). All share the same structure;
  they differ only in how the forward price is computed and the
  settlement convention. Merton co-credited (Black-Scholes-Merton).
- **Five inputs**: exercise price, time to expiration, underlying price,
  interest rate, **volatility** (the speed/probability input — ch. 6).
- **Riskless hedge**: for each option there's a theoretically equivalent
  underlying position; the **hedge ratio** gives the proportion. You
  hedge long-market positions (buy calls / sell puts) by selling the
  underlying, and short-market positions (sell calls / buy puts) by
  buying it. Mnemonic: *opposite* with calls, *same* with puts.
  Adjusting the hedge as the underlying moves implicitly reprices the
  changing outcome probabilities.

## Inputs in practice

- **Underlying price**: use the *bid* when you'll hedge by selling, the
  *ask* when hedging by buying; midpoint only if the market is liquid.
- **Time**: annualized (days/365). Business days matter for price
  movement; calendar days for interest. Model reliability degrades very
  near expiration.
- **Interest rate**: risk-free (T-bill) theoretically; LIBOR/Eurodollar
  in practice; rates are the *least* influential input. FX needs two
  rates.
- **Dividends**: use ex-dividend date for ownership questions; if the
  ex-date falls after expiry the dividend is irrelevant to the option.
- **Volatility**: the hardest and most important input — next chapter.

## Key takeaways

1. Option value = discounted expected payoff under probabilities that
   must be consistent with the forward price.
2. Always hedge model-driven option trades with the corresponding
   underlying position; use executable (bid/ask) prices for the hedge.
3. Models are candles in a dark room — useful, but garbage-in
   garbage-out, and reliance grows dangerous as position size grows.
