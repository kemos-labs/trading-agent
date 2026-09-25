# Chapter 12 — Math Toolkit

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## Philosophy

Keep the toolkit sparse — complex math didn't yield commensurate
returns. Most algo construction uses the simplest tools. Moving
averages (of price, volatility, return density, inter-trade duration)
are the key ingredients; the book concentrates on stock price as input.

## Moving averages (the building blocks)

- **SMA/LMA**: arithmetic moving averages (note: here SMA = *Short*
  Moving Average, LMA = *Long* Moving Average — not "simple").
  `MA = Σ(T₀…T_n)/(n+1)` where n = lookback; a fixed-size window slides
  over the series. Longer lookback ⇒ smoother but laggier line.
  Conventions: SMA white, LMA red, EMA violet, trigger green.
- **EMA (exponential)**: `EMA_t = EMA_{t−1} + (2/(n+1))·(S_t −
  EMA_{t−1})`; seeded with the earliest trade price. Oldest data never
  drops out — its influence decays exponentially with a speed set by
  the lookback n (the **ALPHA constant**; later tuned in 100-tick
  steps). EMAs are *recursive*.
- **Filter interpretation (DSP)**: long MAs = *low-pass* filters
  (attenuate high frequencies); short MAs = *high-pass*. Convolution of
  the tick series with a moving-average window is the formal operation;
  the green line = LMA subtracted from SMA is an early (unparameterized)
  version of the ALPHA-1 trigger line.
- Excel tip: Format Data Series → Add Trendline → Moving Average (up to
  255) for fast short-MA prototyping.

## Other tools

- **Exponents/logs**: ln(x) natural logs dominate; logs convert
  multiplication→addition, division→subtraction, powers→multiplication;
  log(price) for wide-range axes; logs of exponential series produce
  straight lines (log returns as the default).
- **Curves**: y = x² parabola; power law Y = a·x^b; nonlinear
  exponential Y = α·e^(βX). Price trajectory = an "ultra-convolution"
  of interacting equations/parameters.
- **Derivatives/slopes**: slope = Δy/Δx (keep deltas small) = tangent
  line slope; first derivative = instantaneous speed, second =
  acceleration; Leibniz notation dy/dx.
- **Sets/clusters**: define collections freely (e.g., "stocks priced
  $70+", "stocks with %Range > N") and intersect them to filter stock
  candidates — sets and clusters underpin stock selection (ch. 18–20).

## Key takeaways

1. SMA/LMA/EMA on tick price with tick-based lookbacks are the raw
   materials of the authors' algos; EMA's alpha = decay speed.
2. MA pairs act as DSP filters; the SMA−LMA difference is the classic
   trigger construct.
3. Simple math + set-based filtering is the design philosophy — not
   heavy quant.
