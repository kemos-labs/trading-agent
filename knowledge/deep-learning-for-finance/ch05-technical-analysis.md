# Ch05 — Technical Analysis

**Source:** Sofien Kaabar, *Deep Learning for Finance* (O'Reilly, 2024), Chapter 5.

## Purpose
Covers technical analysis — reading price history through charts and
indicators — and explains why its patterns often become ML features
later in the book: indicators encode momentum, mean reversion, and
volatility as numbers a model can consume.

## Charts and patterns
- **Candlestick charts** encode open, high, low, close per period;
  patterns like engulfing and doji are visually recognized but hard to
  quantify reliably — one reason ML models struggle to learn them from
  raw OHLC data alone.
- **Trendlines and support/resistance** mark price levels where buyers
  or sellers historically step in. Breakouts above resistance or below
  support often produce momentum signals.

## Core indicators (with formulas)
- **Simple Moving Average (SMA)**: SMA(n) = mean of last n closes.
  Crossovers (fast SMA crossing slow SMA) are classic trend signals.
- **Exponential Moving Average (EMA)**: weights recent prices more:
  EMA_t = α·P_t + (1−α)·EMA_{t−1}, with α = 2/(n+1). EMA reacts
  faster than SMA and is the basis of MACD.
- **RSI (Relative Strength Index)**: RSI = 100 − 100/(1 + RS), where
  RS = average gain / average loss over n periods (usually 14).
  RSI > 70 = overbought, < 30 = oversold; divergences between RSI and
  price are trend-reversal warnings.
- **Bollinger Bands**: middle band = SMA(20); bands = SMA ± k·σ
  (usually k = 2). Price touching the upper/lower band signals
  overextension; band width measures volatility.
- **MACD**: MACD line = EMA(12) − EMA(26); signal = EMA(9) of MACD;
  histogram = MACD − signal. Crossovers signal momentum shifts.
- **ATR (Average True Range)**: mean of true range
  (max of high−low, |high−prev close|, |low−prev close|) over n
  periods — the standard volatility/stop-distance measure.

## Key takeaways
- Indicators are *derived features*: they compress raw price into
  momentum, volatility, and mean-reversion quantities — the same
  quantities ML models need as inputs. Hand-crafted indicator features
  often beat raw OHLC sequences in small-data regimes.
- All indicators lag; none predict — they describe what already
  happened. Use them to define entry/exit rules or model features, not
  as oracles.
- Optimizing indicator parameters on past data overfits; validate on
  out-of-sample data (a recurring theme for the ML chapters).
