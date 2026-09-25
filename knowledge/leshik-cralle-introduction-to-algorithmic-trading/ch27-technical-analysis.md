# Chapter 27 — Technical Analysis (TA)

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## TA defined

The discipline of identifying patterns in historical data with the
conjecture that they will repeat (at least to some extent) in the
future. History: Sakata rice market (1600s) — Kosaku Kato's "Sakata
constitution" rules; Charles Dow (1880s) the "father of modern TA".
Grudging academic acceptance now; the "chartist" stigma is fading.

**Key point**: TA uses *daily homogeneous* time series; the authors'
methodology uses *inhomogeneous tick series* (asynchronous, very
short time periods). Adaptation is non-trivial — some long-timeframe
properties don't translate to ticks/seconds (different time constants).

**Profitability condition**: strategies work only if prices are either
**mean-reverting** or **trending** (think across resolutions,
durations, frequencies, slopes, amplitudes).

## Reviewed indicators (Excel formulas)

- **Crossing Simple Moving Averages**: oldest TA pillar — short MA
  crosses down through long MA ("Black Cross") = sell signal;
  crosses up = buy.
- **Stochastic Oscillator** (%K/%D):
  `%K = 100·(close − 12-day low)/(12-day high − low)`.
  Default lookbacks 26/19/12. %K raw + %D = MA of %K (5-period,
  dotted). Oscillator 0–100 (0 = at the 12-day low; 100 = at the peak).
- **Bollinger Bands**: 20-day EMA ± 2σ envelope (the authors prefer
  **1.65σ** for ~90%, fewer missed trades). Bands widen/narrow with
  volatility; buy when the upper band is touched/penetrated; narrowing
  bands signal reduced volatility and possible reversal. Live traders
  often act on rate-of-change before the band is hit.
- **Williams %R** (momentum, oversold/overbought): anticipates price
  reversals — peaks/turns before the stock price does.
  `%R = ((MAX_n − close)/(MAX_n − MIN_n))·100`, swings 0 (highest) to
  −100 (lowest); 0 to −20 overbought, −80 to −100 oversold.
- **Momentum**: `MOM = price now − price n periods ago` (% or bp);
  trend-following oscillator — buy at bottoms, sell at peaks when it
  turns down (don't miss the turn after a long plateau).
- **Arms Index / TRIN** (Richard Arms, 1967):
  `TRIN = (advancing/declining stocks)/(advancing/declining volume)`.
  <1 ⇒ volume flowing into rising stocks; >1 ⇒ into declining stocks.
  Used as a real-time market sentiment indicator.

## Key takeaways

1. TA's value is inspiration for adaptation to tick/second scales, not
   direct copy — beware time-constant mismatches.
2. The profitability filter: any TA strategy is only valid where prices
   are mean-reverting or trending at the chosen resolution.
3. Excel implementations of stochastic/Bollinger/%R/momentum/TRIN are
   straightforward; experiment empirically, not on faith.
