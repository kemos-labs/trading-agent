# Ch05 — Fractionally Differentiated Features

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 5.

## Purpose
Resolves the stationarity-vs-memory dilemma: standard integer
differentiation (returns) makes a price series stationary but erases
all memory. Fractional differentiation keeps the series stationary
while preserving as much memory (predictive information) as possible.

## The dilemma
- Prices have memory (long-run dependence) but are non-stationary;
  returns are stationary but memory-less. Integer differentiation is
  arbitrary — 0 (prices) and 1 (returns) are just two points in a
  continuum of possible differentiation orders d ∈ [0, 1].
- ML requires stationary features (to map new observations to training
  examples), but stationarity is necessary, not sufficient: erasing too
  much memory destroys the basis of predictive power (e.g., mean
  reversion needs memory to know how far price has drifted).

## The method
- Generalize the difference operator: Δ^d X_t = Σ_{k=0}^∞ ω_k X_{t−k},
  where ω_0 = 1 and
  ω_k = −ω_{k−1}·(d − k + 1)/k  (binomial series expansion).
  For d = 1 this recovers integer differencing; 0 < d < 1 is a
  weighted infinite sum of past values — memory is never fully erased.
- Weights decay hyperbolically (unlike integer differencing's hard
  cut-off), so the series retains long memory while becoming
  stationary.

## Implementation — two windows
- **Expanding window** (standard fracdiff): applies the full weight
  vector from the series start; produces a negative drift from the
  accumulating negative weights — undesirable.
- **Fixed-width window (FFD)**: drop weights once |ω_k| < τ (a small
  threshold, e.g., 1e−5). Same weight vector used everywhere; yields a
  driftless, stationary blend of level + noise. This is the recommended
  method.

## Choosing d* (maximum memory preservation)
- Compute the minimum d* such that the FFD series passes a stationarity
  test (e.g., ADF): d* quantifies how much memory must be removed.
- d* = 0 → series already stationary; d* > 1 → explosive (bubble-like);
  0 < d* ≪ 1 → "mildly non-stationary" — exactly the interesting case
  where integer differentiation would over-remove memory.
- Known reference: an IID Normal sequence with d = 0.4, τ = 1e−5, on
  E-mini S&P 500 futures, produces a stationary series with preserved
  memory (skew/kurtosis retained).

## Key takeaways
- Returns (d = 1) are usually suboptimal features: they throw away the
  memory that mean-reversion and equilibrium models need.
- Use fixed-width-window fracdiff and search d* by testing
  stationarity; the fractionally differentiated series is
  driftless-but-stationary with fat tails (not Gaussian).
- Fractional differentiation is a preprocessing step applicable to any
  feature, not just prices — cumulative tick series, volumes, etc.
