# Chapter 12 — Bull and Bear Spreads

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## Directional bias in option positions

- Naked directional views: buy calls / sell puts = bullish; sell calls /
  buy puts = bearish. Works but leaves little margin for error (buyers
  bleed theta; sellers face unlimited risk).
- **Ratio spreads with bias can invert their delta**:
  - Sell-more-than-buy (frontspread, −γ): initially bullish at 2×3
    (+28 deltas), but if the market runs to 130–140 both calls go deep
    ITM (Δ→100) leaving −100 deltas — the *negative gamma* flips the
    direction on a fast move.
  - Buy-more-than-sell (backspread, +γ): 3×1 at +28 deltas inverts to
    −25 as time passes/vol falls (100 call Δ rises to 70, 110 call
    falls to 15) — wrong on volatility flips the direction.
- **Bull/bear butterflies & calendars**: a butterfly is bullish when the
  body strike is above spot, bearish when below; a calendar is bullish
  when its strike is above spot. Both have −γ, so the delta inverts if
  the underlying crosses the body/strike. Direction is a *secondary*
  feature of these structures.

## Vertical spreads (the pure directional tool)

One option each, same type, same expiry, different strikes — the spread
never changes its bullish/bearish character (the lower-strike call
always has higher delta than the higher-strike call; likewise for puts).

- **Rule**: buy the lower strike + sell the higher = **bullish** (calls
  *and* puts); sell the lower + buy the higher = **bearish**. Both legs
  same type.
- Expiration value ∈ [0, distance between strikes] (0 if both OTM,
  max if both ITM).
- Same-strike call vs. put verticals have ~identical delta, P&L, and
  value (European assumption; put-call parity family).

## Choosing the strike: the ATM rule

Volatility sensitivity (ch. 6): in *total points* the at-the-money
option moves most with vol. Therefore:

> **If implied volatility is low, buy the at-the-money option; if high,
> sell it.**

Worked example (r = 0, ATM = 100, own vol est. 25%):
- IV 20%: 95/100 bull call costs 3.06 (worth 2.91, edge −0.15);
  100/105 costs 1.82 (worth 1.92, edge **+0.10**) → buy the ATM 100
  call, sell 105.
- IV 30%: 95/100 costs 2.81 (worth 2.91, edge **+0.10**); 100/105 costs
  1.98 (worth 1.92, edge −0.06) → sell the ATM 100 call, buy 95.

Why: the ITM-including spread (95/100) profits whenever the market
*doesn't fall* (positive theta, −γ); the OTM-including spread (100/105)
needs the market to rise (negative theta, +γ). Since the ATM option is
the most vol-sensitive, it's the one to buy when vol is cheap and sell
when vol is rich. In practice: use the strike closest to the money
(or, for stock options, the **at-the-forward** strike when rates are
high and time is long).

## Other design levers

- Wider strikes → bigger delta and bigger max P&L (95/110 > 95/105 >
  95/100). Deep-OTM spreads (e.g., 115/120) are cheap, low-delta, and
  hugely leverageable via size.
- Position delta = spread delta × size (e.g., 500 deltas = 25 spreads ×
  Δ20, or 5 underlying). Vertical spreads cap risk where underlying
  positions don't — the classic reason to trade direction via spreads.
- Spread graphs: max gamma/vega/theta occur just below the lowest or
  just above the highest strike; value/Δ/γ/vega all respond similarly to
  time and vol.

## Key takeaways

1. Buy lower/sell higher = bullish; sell lower/buy higher = bearish —
   for calls *and* puts.
2. Anchor every vertical on the ATM option: buy it when IV is low, sell
   it when IV is high.
3. Non-vertical "directional" structures (ratio, butterfly, calendar)
   are volatility trades first — their deltas invert when the market or
   vol moves against the thesis.
