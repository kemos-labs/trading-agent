# Ch13 — Semi-automatic Trader

**Source:** Carver, *Systematic Trading*, Chapter 13. (Example 1 of 3:
discretionary forecasts inside the systematic framework.)

## Who it's for
You make your own market calls (discretionary forecasts), but let the
framework handle stops, risk targeting, and position sizing — "the best of
both worlds." Hard part: the system forces trades (or prevents them) against
your instincts; design a system you trust, then don't deviate. Example setup:
£100,000 trading capital, quarterly spread bets (£1–£10/point), part-time.

## Framework choices specific to semi-automatic trading
- **Instruments**: check any potential bet has max position ≥ 4 blocks (at
  forecast 20); standardised cost ≤ 0.01 SR (spread bets); avoid ultra-low
  vol.
- **Forecasts**: quantified −20..+20 (table 37: Very strong sell −20 …
  Very strong buy +20). **Never change a forecast once a bet is open.**
- **Exit: trailing stop only** — no profit targets (no evidence they work;
  they exit trends early). Stop = X × daily price volatility (in price
  points) from the high/low since entry; trailing stops move with new
  highs/lows and updated vol. **X=4** recommended for spread bets: average
  holding ~6.5 weeks, turnover 8 round trips/yr, max standardised cost 0.01
  SR (X=1 → 4 days/64 turnover/0.0013 cost … X=10 → 26 weeks/2.0/0.04). Use
  one X for all instruments, set by the most expensive one. Update the vol
  estimate only if it moved >25% (cheapness); eyeball a 1-month chart.
- **Volatility target**: assume SR 0.30 after costs (≤ the 0.50 cap) → 15%
  target (table 26 col D) → £15,000 annual / £937.50 daily. Costs: 8 × 0.01
  = 0.08 SR/yr ≈ 1.2% drag at 15% vol + ~0.6% roll costs.
- **Position sizing**: daily cash target ÷ instrument value vol → volatility
  scalar; position = scalar × forecast ÷ 10. Spread bets: block value = bet
  size × price ÷ 100; FX = 1 (betting in £/point regardless of underlying
  currency).
- **Portfolios**: instrument weight = 100% ÷ max bets; diversification
  multiplier = max ÷ average bets (≤2.5). Example: max 4, avg 3 → weight
  25%, multiplier 1.33. Max bets = hard cap (no new bets until one stops
  out). Pyramiding allowed as *separate* bets (own stop; can't reduce or
  reverse an existing position; total |forecast| per instrument ≤ 40).
- **Risk per bet check**: (X × forecast × %target) ÷ (10 × 16 × avg bets) —
  example: (4×10×15%)/(10×16×3) = 1.25% of capital average, 2.5% max.

## Daily process
1. **Housekeeping**: check stops (close if hit); get account value → trading
   capital → annual/daily cash targets; eyeball vol on positions & candidates
   (update only if >25% change for existing); recalculate/trail stops; vol
   scalars; desired subsystem positions (forecast × scalar ÷ 10); portfolio
   positions (× weight × multiplier); round; trade if >10% away (position
   inertia).
2. **Intra-day** (full-time only): check stops; check setups.
3. **New position**: forecast → check max-bets cap & instrument limits →
   instrument value vol → stop (X × vol from entry) → scalar → subsystem
   position → portfolio position → round → trade.

## Trading diary highlights (Oct–Nov 2014)
- 15 Oct: long crude 31 blocks (£10/pt, stop 79), long S&P 5 blocks (£5/pt,
  stop 1800), short Euro Stoxx 6 blocks (£1/pt, stop 3100) from forecasts
  +10/+15/−10.
- 29 Oct: trailing S&P stop raised to 1900; added a *second* +25 S&P bet
  (total +40, max reached — no more bets). Position inertia kept crude at 31
  (target 32).
- 4 Nov: crude stopped out at 79 (loss £1,333). Tempted to take S&P profits
  — "can't, it isn't part of the system!"
- 21 Nov: Euro Stoxx stopped (loss £1,380).
- 28 Nov: crude vol doubled ($1→$2) → stop doubled to $8 away, position cut
  from −32 to −17 (buy 15) — **same capital at risk**: the system was
  rebalancing risk, not taking profits.
- Lesson: the system repeatedly overruled instincts (close winners early,
  hold losers) — exactly its purpose.

## Notes
- This is the "human forecast + machine discipline" archetype: no back-test
  possible, so SR assumptions are deliberately conservative (0.30 → 15%
  target).
- The stop-loss rule is the ch1 early-loss-taker made systematic: risk stays
  constant, returns keep benign positive skew.
