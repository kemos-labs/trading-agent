# Ch12 — Cointegrated Time Series

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 12.

## Mean-reversion / pairs trading motivation
A classic "pairs trade" longs one asset and shorts another that shares underlying factors (e.g.
long MCD, short BKW — hamburger producers). Long-term relative prices are in equilibrium; a
temporary dislocation (e.g. a supply-chain hit to one firm) makes the pair long-short
profitable as it reverts to equilibrium. We want a rigorous way to find pairs/baskets that mean-
revert → the concept of **cointegration**.

## Cointegration definition
Let {x_t}, {y_t} be two **non-stationary** series. If a linear combination **a·x_t + b·y_t**
(a, b ∈ R) is **stationary**, the pair is *cointegrated*. (Intuition: two random-walk-like assets
can have a stationary synthetic combination such that disruptions revert to the mean.)

## Unit-root tests (detecting non-stationarity)
Series with a **unit root** (AR process root =1, e.g. random walk) are non-stationary. Tests:
1. **Augmented Dickey-Fuller (ADF)** — H0: unit root (α=1); Ha: α<1 (stationary). Fits an AR(p)
   approximation to handle higher-order autocorrelation.
2. **Phillips-Perron** — no AR(p) assumption; uses non-parametric kernel smoothing on w_t to
   handle unspecified autocorrelation & heteroscedasticity. Asymptotically ≈ ADF but can differ
   in finite samples (they treat autocorrelation/heteroscedasticity differently).
3. **Phillips-Ouliaris** — tests for cointegration *among residuals of two series*. Because ADF
   distributions don't hold on estimated cointegrating residuals, it uses **Phillips-Ouliaris
   distributions** under the null.

**Pitfalls**: unit-root tests poorly separate highly-persistent-stationary from
non-stationary processes; and mean-reversion relationships can break down under **regime
change** — be very careful with these tests on financial series.

### Simulated cointegrated pair verification
Create random walk z (DWN steps); build x=0.3z+w, y=0.6z+w.
- Correct combination a·x+b·y stationary when **ap+bq=0**; pick p=0.3,q=0.6 ⇒ a=2,b=−1 gives
  stationary comb (ADF, PP, and PO all reject unit root → cointegrated ✓).
- Wrong combination (e.g. arbitrary a,b) → ADF fails to reject unit root (not cointegrated). ✓

## CADF — Cointegrated ADF (determining the hedge ratio)
ADF alone doesn't give the regression (hedge) ratio β. **CADF**:
1. Linear regression between the two series → intercept α & slope β (the hedge ratio).
2. ADF-test the regression **residuals**; stationary residuals ⇒ cointegrated pair.
- Doesn't say which series is dependent/independent — so do BOTH regressions (swap Y,X) and
  pick the one with the *more negative (more significant)* ADF statistic (the "optimal" ratio).

### Simulated CADF
Series with known combination: regression gives β ≈ 0.5 (since q is twice p); residuals ADF
rejects unit root → confirms cointegration. ✓

### Real data — EWA/EWC (Chan's classic example)
- EWA (Aussie equities) & EWC (Canadian equities) baskets, both commodities-dependent;
  historic period Apr 2006–Apr 2012.
- Regression HEDGE ratios differ by direction: EWA-roll gives β~... vs EWC relation. Use ADF
  statistic to pick optimal (EWC-as-independent has the more negative ADF → chosen).

### Real data — RDS-A / RDS-B (Royal Dutch Shell share classes)
Tight cointegration (same underlying equity). Use `get()` to handle hyphenated tickers in R.
Both directions yield stationarity; first combination has the smallest Dickey-Fuller statistic
→ optimal.

## Johansen test (≥3 series / portfolio cointegration)
- Built on **Vector Autoregressive (VAR)** (multivariate AR; not VaR) and the **Vector Error
  Correction Model (VECM)**: Δx_t= μ + A·x_{t−1} + ΣΓ_i Δx_{t−i} + w_t.
- Tests for **cointegration rank r** (number of cointegrating relations) by eigenvalue
  decomposition of A: H0 r=0 (none) → r=1 … up to r=n−1.
- The eigenvector (largest eigenvalue) components give the **coefficients of the stationary
  linear combination** — estimated *as part of* the test (unlike CADF's a-priori OLS
  regression). Trade-off: less statistical power than CADF; sometimes can't reject when
  CADF can.
- R: `urca::ca.jo(...)` with `type="trace"` (or max-eigen), K lags, ecdet, spec.

### Simulated 3-series
p=0.3z, q=0.6z, r=0.9z → Johansen trace: reject r=0, r≤1, r≤2 (statistic 8161.48 >> 1% crit
37.22) → rank r=3; eigenvector (1, 1.791, −1.717) forms stationary combination. ✓

### Real 3-asset baskets
- **EWA/EWC/IGE** (natural resources): R's `ca.jo` gives slightly different stats/critical
  values than MatLab `jplv7` → **implementation differences matter**; results can flip the
  cointegration conclusion. Be wary of differing test implementations.
- **SPY/IVV/VOO** (all S&P500 trackers): reject r=0 strongly, r≤1 at 1%, r≤2 only at 5%
  (weaker). **Caveat**: only ~1 year (~250 trading days) of data — too small a sample to trust;
  possible r=2 rather than 3.

## Takeaways / pitfalls
- Confirm cointegration with residual ADF; choose hedge-ratio direction by ADF statistic.
- Same financial series can yield different test verdicts across R vs MatLab implementations →
  verify, don't blindly trust a tool's p-values.
- Watch out for short samples and regime changes undermining mean-reversion relationships.
- Johansen estimates the (multi-asset) weights directly; CADF needs a chosen regression.