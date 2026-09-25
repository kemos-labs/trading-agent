# Ch17 — Structural Breaks

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 17.

## Purpose
Methods to detect regime changes and bubbles (structural breaks) in
financial series — the events around which profitable ML features can
be built, since most participants are caught off guard at transitions.

## Types of tests
- **CUSUM tests**: do cumulative forecasting errors deviate from white
  noise? (level/regime shifts)
- **Explosiveness tests**: does the process exhibit exponential growth
  or collapse — inconsistent with random walk/stationarity and
  unsustainable long-run?
  - Right-tail unit-root tests (autoregressive specification):
    SADF/CADF.
  - Sub/super-martingale tests (various functional forms).

## CUSUM tests
- **Brown–Durbin–Evans (1975) on recursive residuals**: fit recursive
  least squares β on expanding subsamples [1,k+1], [1,k+2], ...;
  standardized 1-step-ahead recursive residuals; CUSUM statistic
  S_t = Σ standardized residuals. Under H0 (β constant), S_t ~ N[0,
  t−k−1]. Caveat: arbitrary starting point.
- **Chu–Stinchcombe–White on levels**: drop features, assume no-change
  forecast (β = 0); compute standardized log-price departures
  S_{n,t} = (y_t − y_n)/√(t−n)·σ... ~ N[0,1] under H0. Time-dependent
  one-sided critical value (b₀.₀₅ ≈ 4.6). Reference level y_n is
  arbitrary → compute on backward-shifting windows and take the max.

## Explosiveness tests (bubbles)
- **SADF (supremum ADF)**: for each t, compute the ADF t-stat over
  backward-shifting windows n ∈ [1,t] and take the supremum. Detects a
  single bubble; sensitive to outliers (single big move inflates it).
- **CADF/SADF on sub-samples**: more robust to multiple
  bubble-burst-bubble cycles (a cycle makes the series appear
  stationary to single-bubble tests).
- Implementation: ADF regression on log-prices with a constant and
  optional time trends ('nc', 'ct', 'ctt'), min sample length,
  lags; inner loop backshifts the window, outer loop advances t.

## Key takeaways
- Structural breaks are where the money is: transitions between
  regimes (mean-reversion → momentum) catch the crowd off guard.
- Use CUSUM for regime shifts and SADF/CADF for bubble detection; be
  aware of the arbitrary-reference weakness in level-based CUSUM.
- Use structural-break tests as *event triggers* for event-based
  sampling (ch2) and as features (e.g., a rising SADF → explosiveness
  risk feature).
