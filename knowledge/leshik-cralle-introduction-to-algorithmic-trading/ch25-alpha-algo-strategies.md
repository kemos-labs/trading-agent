# Chapter 25 — Our Trading Algorithms: The ALPHA ALGO Strategies

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

The six ALPHA algos + the LC Adaptive Capital Protection Stop — all
Excel-function-language, tick-based, designed for individual traders
seeking immediate profit (≈25 bp net target).

## ALPHA-1 (DIFF)

- **Concept**: convolve low-pass (SMA, white) and high-pass (LMA, red)
  filters on the price tick series; the difference (SMA − LMA) is the
  green *trigger line* on the secondary axis.
- **Parameterization** (empirical, per stock, reset daily): SMA lookback
  = (5-day avg TXN count) ÷ integer 4–7; LMA lookback = SMA × integer
  (usually 6); on a longer 5-day (3-day) lookback chart, set a straight
  valley-penetration line so 5–8 valleys cross it (parameterized).
- **Triggers**: Buy on a valley of the trigger line; Sell when the up-
  peak exceeds the red zero line.
- **Excel code**: SMA at Col G Row 400 =
  `=IF(ROW()>G$1, AVERAGE(OFFSET($F4,-(G$1-1),0,G$1)),"")` (relative
  copy-down); LMA parallel in Col H; trigger = `=G-H` in Col I.
- **Heuristics**: trigger line fits parabolas; the deeper the valley,
  the better the trade; you only see half the parabola in real time.
- Characteristics: fairly consistent but parameter-sensitive; rare 300
  bp "gifts"; "no triggers" sessions are common — verify connectivity,
  UPS, Time & Sales before worrying. Win/loss ratios of 8/10 for
  several days in a row are achievable.

## ALPHA-1a — ALPHA-1 expressed in Excel function language

Full source on the CD ('BUILDING ALPHA-1'); columns G/H/I for
SMA/LMA/DIFF with parameter cells in Row 1, formula starts at the
lookback row. Helper: spare columns AA–AC with 200T/1200T alternatives.

## ALPHA-2 (EMA PLUS) V1 & V2

- V1: single EMA (start ~300T) — Buy at valleys, Sell when the line
  rises above the red zero line and forms an up-peak.
- V2: three EMAs (200T, 300T, 500T) with the third running on the
  difference of the first two; Col M = signal line, Col N = a 200T EMA
  on the signal line (the trigger).
- EMA constant α = 2/(n+1) (0.009950 for n=200); `EMA_t = EMA_{t−1}
  + α·(S_t − EMA_{t−1})`.
- **Valley-detection code** (3-tick lag):
  `=IF(AND((M27<MIN(M24:M26)),(M27<MIN(M28:M30)),M27<−0.04),1,"")` —
  TRUE writes 1 (Buy signal); adjacent column fetches trade price.
- ALPHA-2 fires *earlier* than ALPHA-1; comparison lets you study how
  trigger math shifts entries.

## ALPHA-3 (Leshik-Cralle Oscillator)

- Adaptive lookback (300–600T default) on a tick series driven by
  recent %Range; center the envelope off the standard deviation over
  the LMA lookback; compute an oscillator for triggers.
- Default lookback = median or LMA-based (auto-adaptive in software,
  preset limits; %Range over the latest 50% fraction of the median
  lookback). Prefer the **median** (robust to outliers).
- Bands at **1.65 × σ** for a ~90% likelihood envelope; anything at or
  outside the bands = trigger; oscillator steepness indicates signal
  quality. Down-swings are more aggressive than up-swings (stock-
  specific).

## ALPHA-4 (High-Frequency Real-Time Matrix)

- Stocks must be highly correlated (≥0.7 on 200T %returns over two
  sessions). Basic grid = 4 stocks (larger grids need automation; the
  "curse of dimensionality" — pairs AB, AC, AD, AE, BC, BD, BE, CD,
  CE, DE for 4+1 symbols).
- Divergence/convergence baseline = %Range over the previous 300T; a
  20% increase above baseline = trading signal.
- On divergence: short the riser, long the faller; on subsequent
  reversion, close with a 35 bp profit target per leg.

## ALPHA-5 (Firedawn)

- Surrogate for *slope* on the LMA to capture long continuous up-
  trends; suited to the energy sector (OIH, RIG, drilling) — rarer
  signals but longer trades with bigger dollar returns.
- Buy trigger: LMA (or EMA) rises AND return > 5 bp per 50T AND
  SMA > LMA for two consecutive 50T periods (TRUE).
- Sell: SMA crosses below LMA.

## ALPHA-6 (General Pawn)

- **Lead-lag** within a sector + topological maps (Vandewalle;
  impactopia.com / market-topology.com).
- General = sector's largest market-cap stock with %Range > 0.0075
  averaged over the last 3 sessions EOD; Pawns = 4 more sector stocks
  with the largest %Range over 3 sessions EOD.
- Buy/sell trigger threshold: General 25–35 bp at 50T "boxcar"; when
  TRUE, fire market orders for the Pawns (you don't have to go long
  the General — use the lead/lag property). Pawn lag ≈ the integrated
  market reaction time.
- Four Pawns: best put them all on trailing-sell orders or use a 30 bp
  profit stop. Capital-protection stops always.

## 7. LC Adaptive Capital Protection Stop

Every trade gets an *adaptive* stop placed milliseconds after the fill;
fixed-percentage stops don't fit high-speed trading.

- **Version 1**: (1) set lookback ~100T from the trade timestamp
  (adjust for high-activity stocks); (2) compute the Standard Median
  Deviation (SMD) of price over the lookback — median = less bias
  from outliers; (3) for a long, subtract 2×SMD from the buy price;
  (4) place a LIMIT SELL order at that value.
- **Version 2** (more frequently used): (1) compute $Range over 100T;
  (2) subtract $Range from the buy price; (3) place a LIMIT SELL.
- Test all stop parameters per stock and current conditions.

## Key takeaways

1. Every ALPHA algo = a moving-average/EMA/Oscillator-based *trigger
   line* with parameterized valley/peak detection; ALPHA-1/2/3 are the
   bread and butter.
2. ALPHA-4 (correlated matrix) and ALPHA-6 (bellwether lead-lag) are
   the cross-sectional/cross-stock variants.
3. The LC adaptive stop (SMD- or $Range-based) is non-negotiable risk
   management — adapt to the stock's recent volatility, not a fixed
   percentage.
