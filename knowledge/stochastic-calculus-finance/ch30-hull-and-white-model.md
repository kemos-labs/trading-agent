# Ch30 — Hull and White Model

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, Part II)
— Steven Shreve

## The model

Hull-White short-rate SDE (mean-reverting with time-dependent target):

```
dr(t) = (α(t) − β(t)r(t)) dt + σ(t) dW(t)
```

α, β, σ are nonrandom functions of time. β(t) is the mean-reversion
speed, α(t)/β(t) the (time-varying) long-run level, σ(t) the vol. The
time dependence lets the model be **calibrated to the current yield
curve** — a key practical advantage.

## Solving the SDE

Integrating factor K(t) = ∫₀ᵗ β(u) du:

```
d(e^{K(t)} r(t)) = e^{K(t)} α(t) dt + e^{K(t)} σ(t) dW(t)
```

hence

```
r(t) = e^{−K(t)} [ r(0) + ∫₀ᵗ e^{K(u)} α(u) du + ∫₀ᵗ e^{K(u)} σ(u) dW(u) ]
```

- r(t) is a **Gaussian process** (ch29): the integral of a nonrandom
  function against dW is Gaussian.
- Mean: m(t) = e^{−K(t)}[r(0) + ∫e^{K}α du]; Variance:
  v(t) = e^{−2K(t)}∫e^{2K(u)}σ(u)² du.
- Consequence: **interest rates can go negative** with positive
  probability — HW's known weakness (CIR fixes this, ch31).

## Bond prices

The zero-coupon bond price is the Q-expectation of e^{−∫ₜᵀ r du}. For the
Gaussian short rate, the integral is also Gaussian, so bond prices are
**exponential-affine**:

```
B(t, T) = exp( −A(t,T) + ... )   →   B(t,T) = exp(−A(t,T) r(t) + C(t,T))
```

(affine in the current short rate). The functions A, C are computed from
the ODEs that result from the Feynman-Kac/PDE approach; A(t,T) = ∫ₜᵀ
e^{−∫ₜˢ β du} ds-type expressions. Exponential-affine form makes yields
and derivatives tractable and gives closed-form formulas for bond
options.

## Calibration

α(t) is chosen so model bond prices match the observed term structure
exactly (fit the yield curve). σ(t) is then calibrated to swaption/caplet
volatilities. The model is *internally consistent*: drift α absorbs the
curve shape, so the model prices at-the-market bonds by construction.

## Key takeaways

- HW: dr = (α(t) − β(t)r)dt + σ(t)dW — mean-reverting Gaussian short
  rate, calibratable to the current curve.
- Solution via integrating factor: Gaussian process; negative rates
  possible.
- Bond prices exponential-affine in r → closed-form yields and bond
  option prices.
- Use when you need exact yield-curve fit and analytic tractability; be
  aware of the negative-rate tail.
