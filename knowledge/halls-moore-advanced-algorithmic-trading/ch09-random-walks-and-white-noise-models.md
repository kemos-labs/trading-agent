# Ch9 — Random Walks and White Noise Models

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 9.

## Time-series modelling process (recurring recipe)
1. Obtain the correlogram, assess serial correlation.
2. Fit a model that *reduces* the serial correlation.
3. Refine until no correlation remains; run statistical tests.
4. Use the model's **second-order properties** (mean, variance, autocovariance) to forecast.

A good model is the *simplest* that explains the serial correlation. **Residual error series**
x_t = y_t − ŷ_t: if the model explains the serial correlation, residuals are serially uncorrelated
(i.i.d.) — the confirmation target of a good fit.

## Operators
- **Backward Shift Operator (BSO)** B: Bx_t = x_{t−1}; repeated: B^n x_t = x_{t−n}.
- **Difference Operator** ∇: ∇x_t = x_t − x_{t−1} = (1−B)x_t; ∇^n = (1−B)^n. Used to handle
  non-stationary series later.

## Discrete White Noise (DWN)
A series {w_t} with elements i.i.d., mean 0, variance σ², and **no serial correlation**
(Cor(w_i,w_j)=0 for all i≠j). Standard-normal DWN: w_t ~ N(0, σ²).
- Second-order properties: mean 0; autocorrelation ρ_k = 1 if k=0, else 0. Single parameter σ².
- Used as the **model for residuals** (confirmation that serial correlation is gone).
- Useful to simulate *synthetic* series → many "histories" → statistics on parameters.
- Correlogram of 1000 normals: a few lags (k=6,15,18) exceed 5% purely by sampling variation —
  expect ~5%, don't over-interpret.
- Variance from R `var()`: simulated σ²=1 → sample 1.071.

## Random Walk
**x_t = x_{t−1} + w_t** (plus BSO form). Simply the cumulative sum of DWN increments:
a sum of white-noise steps = a "walk".
- Mean still 0, but **covariance is time-dependent**: Cov(x_t, x_{t+k}) = σ²·t — grows linearly
  with time.
- **Autocorrelation ≈ 1 for short lags** in a long series; decays very slowly — extreme,
  persistent autocorrelation.
- Implication: never extrapolate "trends" from a random walk over the long term — they're
  literally random walks.

### Fitting & validating a RW
- Simulate a RW from DWN draws; to validate, **difference the series** and check the result is
  DWN: `acf(diff(x))` → near-white-noise correlogram (one marginal peak at k=10, within the
  expected ~5%). Confirms the RW model fits (because we built it that way) — the
  *simulate-and-fit-check* pattern.

## Fitting to real financial data (R + quantmod)
- Download adjusted close via `quantmod` (`getSymbols`). Take first differences, run `acf()`,
  look for white-noise residuals.

### MSFT daily adjusted close
Correlogram of differences mostly within 5% bands; the few marginal peaks are far from lag 0
→ plausibly stochastic; conclude daily adjusted close of MSFT is roughly consistent with a
**random walk**.

### S&P500 (^GSPC)
More interesting: a **negative correlation at lag 0/1** (i.e. slight negative first-order
autocorrelation in returns — brief mean reversion / reversal) plus peaks at k=15,16,18
(possible longer-lag process). Harder to accept RW → motivates more sophisticated models
(AR/MA/ARMA).

## Takeaways / pitfalls
- "White noise à minus" is the gold standard for residuals; a good model leaves white noise.
- Difference a series (if stationary-in-mean violated) before judging its structure.
- Don't over-read 5% ACF bands; correlated lags cluster.
- Financial indices often show *weak negative* short-lag autocorrelation (reversal) and
  longer-lag structure — beyond simple random walk.