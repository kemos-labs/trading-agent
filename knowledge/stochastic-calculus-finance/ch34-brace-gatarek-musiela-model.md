# Ch34 — Brace-Gatarek-Musiela (BGM) Model

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, Part II)
— Steven Shreve

## Review: HJM forward rates

HJM models the entire forward-rate curve f(t,T) (rate at time t for
borrowing at T). Under the risk-neutral measure:

```
df(t,T) = σ(t,T)·σ*(t,T) dt + σ(t,T) dW(t),   σ*(t,T) = ∫ₜᵀ σ(t,u) du
```

The drift is *determined by the volatility* (HJM drift condition) — the
no-arbitrage restriction. Bond prices follow dB/B = r dt − σ* dW. The
classic lognormal choice σ(t,T) = σ_f·f(t,T) makes the drift grow like
the square of the forward rate (σ² f ∫f du): the solution **explodes
before T** (like the ODE f' = f², whose solution blows up at 1/c). So
plain lognormal HJM is unstable.

## BGM (a.k.a. LIBOR Market Model, LMM)

BGM fixes the explosion by modeling **discrete forward LIBOR rates**
L(t, τ_i) (over successive tenor dates) instead of the continuum, with
**lognormal volatilities of the rates themselves**:

- Working with the BGM variables (time-to-maturity τ = T − t, forward
  rates over the tenors), each forward rate L(t, τ) is lognormal under
  its own forward measure.
- Rates are positive (lognormal, no explosion), and the model is
  calibrated to **caps and swaptions** (Black's formula per caplet —
  market quotes are in Black-lognormal terms, which the model matches by
  construction).
- Dynamics couple rates through the forward-rate drifts (convexity
  adjustments), with a Libor-style numéraire / spot-LIBOR measure; the
  drift of each L involves covariances with the other forward rates.

## Implementation

- **Caplets**: each caplet = call on a single forward LIBOR → priced with
  Black's formula under the caplet's own forward measure — exact and fast.
- **Caps**: sums of caplets. Swaptions require simulation or
  approximations (drift terms make them non-lognormal jointly).
- **Calibration**: choose the per-tenor volatilities to match caplet
  (cap) prices and the correlation matrix to match swaption prices.
- Simulation: simulate the vector of forward rates under the spot-LIBOR
  measure (drift = covariance-weighted sums), then price path-dependent
  payoffs (swaptions, exotic structures).

## Key takeaways

- HJM: df = σσ*dt + σdW; drift fixed by vol; plain lognormal forward
  rates explode — motivating BGM.
- BGM/LMM: lognormal discrete forward LIBOR rates under their own forward
  measures — positive, stable, market-calibratable (caps/swaptions).
- Caplets are Black-formula-priced under the T-forward measure; the
  numéraire machinery (ch33) is the foundation.
- The standard practical market model for interest-rate exotics; drift
  coupling and calibration are the hard parts.
