# Chapter 11 — Volatility Spreads

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## Hedging with options instead of the underlying

10 calls at Δ50 (+500 deltas) can be hedged with: sell 5 underlying,
buy puts totalling −500 deltas, sell *other* calls totalling −500, or a
combination. Hedging with options yields volatility spreads: ~delta
neutral, sensitive to underlying moves, implied vol, and time.

## Symmetrical spreads

- **Straddle**: call + put, same strike & expiry, usually 1×1 ATM
  (Δ≈50/−50 → neutral). Long = +γ, −θ, +vega (wants movement); short =
  −γ, +θ, −vega (wants stillness). Off-ATM strikes make a *bull/bear
  straddle* (e.g., 95 calls Δ75 + 95 puts Δ−25 = +50; use 3 puts per
  call for a *ratio straddle*).
- **Strangle**: same expiry, different strikes — by convention OTM
  (90/110 = 90 put + 110 call; ITM version = *guts*). Same risk profile
  as the straddle.
- **Butterfly**: 3 equally spaced strikes, fixed **1×2×1** ratio, one
  type. Long = buy wings, sell body. Expiration value: max at the body
  strike = distance between strikes (10.00 for 90/100/110), min 0 → long
  butterfly is always a debit, and it can *never* lose more than the
  cost. Delta neutral when body ≈ ATM; long butterfly ≈ short straddle
  with limited loss (hence tradable in huge size: 300×600×300 carries
  less risk than 100 short straddles). European call butterfly ≡ put
  butterfly → any price difference is a riskless arbitrage.
- **Condor**: 4 options, **1×1×1×1**, long = buy two outer wings, sell
  two inner; max value between the inner strikes, min 0.

**Symmetry summary**: long straddle/strangle and short butterfly/condor
→ +γ/−θ/+vega; the mirrors → −γ/+θ/−vega.

## Asymmetrical spreads

- **Ratio spread / backspread** (buy more than sell): +γ, −θ, +vega;
  unlimited profit on one side, worthless beyond the opposite extreme;
  typically executed for a *credit* under the model. **Frontspread**
  (sell more than buy): −γ, +θ, −vega with one-sided limited risk.
  Common ratios 2:1, 3:1, 4:1, 3:2.
- **Christmas tree / ladder**: 1 long + 2 shorts (or reverse) at three
  strikes → strangle-like profile, one side limited.
- **Calendar (time/horizontal) spread**: same strike, different
  expiries; long = buy far month, sell near month (debit; short-term
  ATM theta is bigger, so *time passing with the market flat widens the
  spread* — April loses 0.96 vs. June 0.61 over the first month, spread
  1.34→1.69). Long-term options have higher vega, so *rising implied
  volatility widens* it; a big underlying move collapses it (both legs
  lose time value). Net: **long calendar = −γ, +θ, +vega** — the one
  case where realized-vol preference (quiet) and implied-vol preference
  (up) are *opposite*. This happens when pending news raises IV while
  the spot sits still (CEO announcement scenario).
- **Diagonal**: calendar with different strikes; 1×1 same-type,
  similar-delta ≈ a calendar spread.
- Futures calendars can span different futures months → hedge the
  futures spread separately (10 June calls (+500) + 10 Mar calls
  (−500) → buy 5 March futures, sell 5 June futures). Not an issue for
  stocks, where all months share one underlying.

## Rates and dividends (stock calendars)

- Rates up → the longer-dated forward moves more → call calendar
  widens (**+rho**), put calendar narrows (**−rho**); effect ∝ months
  between expiries. (Futures-option calendars are rate-insensitive.)
- Dividends up → forward down → call calendar narrows, put calendar
  widens (call = negative dividend risk, put = positive dividend risk).
  A no-dividend call calendar has a floor ≈ cost of carry — unless the
  stock can't be borrowed (*short squeeze*) and you're forced to
  exercise the long leg early.

## Classification framework

- **Long premium** = +γ (want volatile market); **short premium** = −γ
  (want quiet market). γ and θ always have opposite signs — movement and
  time are irreconcilable.
- Four categories by (γ, vega): (+γ,+vega), (+γ,−vega) [calendar],
  (−γ,+vega) [calendar], (−γ,−vega). Vega in practice = implied-vol
  sensitivity.
- Magnitudes: straddles/strangles = largest γ/vega (biggest swings both
  ways); butterflies/condors = smallest (limited everything); ratio
  spreads/Christmas trees in between.

## Key takeaways

1. Every volatility spread is a (γ, θ, vega) trade; read off its
   preferences from those three signs.
2. Butterflies/condors cap both risk and reward at the strike
   spacing — the arbitrage between call and put versions pins their
   price.
3. Calendars are the exception that decouples realized from implied
   volatility preference — their +vega/−gamma signature.
