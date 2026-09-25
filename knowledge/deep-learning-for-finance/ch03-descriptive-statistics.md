# Ch03 — Descriptive Statistics

**Source:** Sofien Kaabar, *Deep Learning for Finance* (O'Reilly, 2024), Chapter 3.

## Purpose
Covers the descriptive statistics used to summarize and characterize
financial series — central tendency, dispersion, distribution shape,
correlation, and stationarity — the preprocessing knowledge needed
before any ML model is fit.

## Central tendency and dispersion
- **Mean** (average), **median** (middle value), **mode** (most
  frequent). The median is robust to outliers; the mean is not.
- **Variance** σ² = E[(X−μ)²] and **standard deviation** σ measure
  dispersion; in finance, σ of returns is *volatility*.
- **Interquartile range** (IQR = Q3−Q1) is a robust dispersion measure;
  values beyond 1.5·IQR from the quartiles are common outlier flags.

## Distribution shape
- **Skewness** measures asymmetry: positive skew (long right tail) is
  desirable in returns; negative skew (long left tail) means
  occasional large losses — bad for compounding.
- **Kurtosis** measures tail weight: excess kurtosis > 0 (leptokurtic)
  means fat tails and a peaked center, exactly what real return series
  show versus the normal distribution.
- The **Jarque–Bera test** combines skewness and kurtosis to test
  normality: JB = (n/6)·(S² + (K−3)²/4). Large JB rejects normality.

## Correlation
- **Pearson correlation** r ∈ [−1,1] measures linear association.
  Caveat: r = 0 does not mean independence (nonlinear relationships
  are invisible to it), and correlation is not stable across regimes.
- Correlation matrices are inputs to portfolio construction and
  features for ML models; watch for multicollinearity when feeding
  correlated features to regressions.

## Stationarity
- A series is **stationary** if its mean and variance are constant over
  time — a requirement for many models (ARMA, regressions).
- Prices are typically non-stationary (random walk); **returns** and
  log-returns are usually stationary.
- The **Augmented Dickey–Fuller (ADF) test** checks for a unit root:
  a large negative test statistic (or p < 0.05) rejects a unit root,
  supporting stationarity. If a series is non-stationary, difference it
  or use returns before modeling.

## Key takeaways
- Always characterize a series (mean, σ, skew, kurtosis, stationarity)
  before modeling — this determines which models are valid.
- Skewness and kurtosis tell you the risk is in the tails; don't size
  positions as if returns were normal.
- Test stationarity explicitly (ADF) instead of assuming it — feeding
  a random walk into a regression produces spurious results.
