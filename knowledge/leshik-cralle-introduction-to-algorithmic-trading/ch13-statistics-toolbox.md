# Chapter 13 — Statistics Toolbox

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## Philosophy

Statistics are used to *describe* data characteristics, not to fit
assumed distributions: **no distributional assumptions** — the price
trajectory is a convolution of an unknown number of fluctuating
factors. This is especially important at "high resolution" (tick level).

## Key concepts

- **Normal/Gaussian distribution**: historically the workhorse
  (Gauss/De Moivre 1733, Laplace). Mandelbrot's cotton-price studies
  showed *fat legs* — the Gaussian understates tail risk. Classic tools
  assume **IID** data (independent, identically distributed) — financial
  data is hardly ever IID; watch out for any computation built on it.
- **Variance σ²** = sum of squared deviations from the mean; **standard
  deviation σ** = √variance (sample: Σ(x−x̄)²/(n−1); Excel `STDEV`).
  In a Gaussian, ±2σ covers ~95%, ±3σ ~100% — but "Gaussianity is
  assumed with clenched white knuckles".
- **Correlation R** (Excel `CORREL`): unitless, −1…+1; requires paired
  equal-length series. **Autocorrelation**: financial series are
  dependent on earlier values — for a *short* window (up to ~5
  minutes) this stylistic anomaly of the market is the essence of the
  authors' high-frequency, short-holding-time edge (afterwards it
  vanishes).
- **Data manipulation**:
  - *Smoothing* = low-pass filter (moving average).
  - *Differencing* (first-differencing, lag ≥ 1) = high-pass filter /
    detrending — but keeps high-frequency *noise* too.
  - *Standardizing*: (x − mean)/σ — makes series comparable.
- Population vs. sample vs. stratified samples; mean, mean deviation
  (absolute), mode, median (50th percentile / 2nd quartile; robust to
  outliers), 1st/3rd quartiles (25th/75th percentiles).

## Key takeaways

1. Don't assume a distribution; describe the actual tick stream
   (variance, σ, correlation, quantiles).
2. Autocorrelation over short windows (minutes) is the exploitable
   anomaly for short-holding-time trading; treat IID-based statistics
   with suspicion.
3. MA smoothing, differencing, and standardization are the three
   standard data transforms (DSP view: low-pass/high-pass filters).
