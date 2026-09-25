# Chapter 10 — Introduction to Spreading

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## What a spread is

Opposing positions in different but related instruments. The positions
move in opposite directions to changes in conditions; a profitable
spread assumes the *rates* of change differ (if they matched exactly,
the spread would never move). Many spreads are arbitrage relationships;
they can also isolate a single risk dimension (gamma, vega, rho
spreads).

## Non-option spread examples (with numbers)

- **Cash-and-carry**: commodity $700, r = 6%, storage+insurance $5/mo.
  Fair 2-month forward = 700×(1+0.06×2/12) + 5×2 = 707 + 10 = **717**.
  Market forward at 725 → buy cash, sell forward, carry to maturity:
  cash flow −7 (interest) −700 (buy) −10 (carry) +725 = **+8** = exactly
  the mispricing; immune to price moves in either leg. (Reverse —
  shorting the commodity — usually impossible in physicals.)
- **Calendar spread** (same commodity, two maturities): 4-month forward
  compounds: 700 → 717 → 734.17 (second period on 717 + 2×$5 storage),
  so fair 2v4 spread = 734.17 − 717 = **17.17**. If the spread trades at
  20, sell 4-month / buy 2-month: profit 2.83 via convergence or carry.
  Risks: rates and carry costs can move after initiation, widening the
  spread.
- **Intermarket / ratio spread**: B = 3×A historically. A = 120, B = 390
  (3.25×) → B rich. Buy 3 A + sell 1 B; when the ratio reverts, close at
  zero cost for **+30**. Ratio trades on statistically-observed
  relationships (gold/silver, corn/soybeans, S&P/DJIA) carry more
  uncertainty than arbitrage-implied spreads. Energy **crack spread**
  3:2:1 = (2×gasoline)+(1×heating oil)−(3×crude); soybean **crush
  spread** analogous.
- **Execution**: execute the *difficult* leg first (less liquid) to
  avoid a naked position; spread bids/asks are often tighter as one
  transaction than the sum of the legs.

## Why option traders spread

1. **Relative mispricing in volatility terms**: option A value 7.00 /
   price 8.00 (overpriced 1.00, IV 26%); option B value 6.00 / price
   6.75 (overpriced 0.75, IV 28%) → B is *more* overpriced in vol
   terms even though it's cheaper in points.
2. **Express a specific market view** with defined loss limits (ch. 4
   parity graphs).
3. **Control risk / survive the short run**: models are long-run
   probability statements; a single short-run disaster (the casino's
   $70,000 loss on one $2,000 roulette bet) ends the game before
   probability evens out. Two $1,000 bets on different numbers cut max
   loss to $34,000 *with the same 5% edge*; the perfect spread (bets on
   all 38 numbers) locks a sure profit. Spreading preserves expected
   edge while shrinking variance — and lets a trader size up positions
   (e.g., a 400×100 vol-spread) beyond what a naked view would allow.

## The margin-for-error argument

A spread is also insurance against wrong model inputs. Example: sell 4
calls @ 4.00 (value 3.50 at assumed 35% vol, Δ25), hedge 1 underlying;
if real vol is 45% the calls are worth 4.50 → the hoped-for 2.00 profit
becomes a 2.00 loss. A spread that raises the *breakeven* volatility
(e.g., 35% → 45%) buys you a 10-point margin for error and justifies
much larger size. Traders price option mispricing in *volatility
points*, not currency points, precisely because vol is the error-prone
input.

## Key takeaways

1. Spreads monetize relative mispricing while hedging away shared
   (directional) risk; options allow spreads along any risk dimension
   (delta, gamma, vega, theta, rho).
2. Same edge, lower variance: spread risk off rather than take a single
   large directional bet.
3. Evaluate every option trade's breakeven volatility (position implied
   vol from ch. 7) and size so you survive your input errors.
