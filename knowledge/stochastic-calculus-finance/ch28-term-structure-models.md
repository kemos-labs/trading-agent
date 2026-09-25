# Ch28 — Term-Structure Models

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, Part II)
— Steven Shreve

## Setup

A term-structure model takes zero-coupon bonds of all maturities as the
primitive assets (default-free, pay $1 at maturity). Given an adapted
short-rate process r(t), the accumulation factor is β(t) = exp(∫₀ᵗ r du),
and bond prices are

```
B(t, T) = E_Q[ e^{−∫ₜᵀ r(u)du} | F(t) ]
```

## Fundamental theorem of asset pricing (term structure)

A term-structure model is **arbitrage-free iff there is an equivalent
measure Q** (risk-neutral) under which every discounted bond price
B(t,T)/β(t) is a martingale.

Model each bond as

```
dB(t,T) = μ(t,T)B dt + σ(t,T)B dW
```

Then Q is risk-neutral iff the mean rate of return μ(t,T) equals the
short rate r(t) for every t and T (the drift is pinned to the money-market
rate). If not, change measure so it is; if no such measure exists, there
is an arbitrage trading zero-coupon bonds.

## Building arbitrage-free bond prices

Two methods:

**1. Factor-model method (short-rate models).** Start with a factor SDE
dX = a(t,X)dt + b(t,X)dW (one or more factors). Set r(t) = r(X(t)) — e.g.
one-factor: r(t) = X(t) (CIR, Hull-White — ch30/31). Then compute bond
prices by the Q-expectation above; the drift a is chosen (via the market
price of risk) so that everything is consistent.

**2. Forward-rate method (HJM).** Specify the forward-rate curve
f(t,T) directly (ch34). The no-arbitrage condition links the forward-rate
drift to its volatility — the HJM drift condition.

## The market price of risk

Bond price dynamics under the *market* measure carry an extra drift
μ(t,T) − r(t) = "risk premium". The market price of risk θ converts:
under Q the premium vanishes (drift = r). Different choices of θ give
different Q — the term structure's version of incompleteness (only the
short rate is the "risk factor" driving all bonds in one-factor models,
which is complete for bonds but the drift choice is still a modeling
input).

## Key takeaways

- Bonds are priced as discounted Q-expectations of $1; arbitrage-free ⇔
  discounted bond prices are Q-martingales ⇔ bond drift = r.
- Bond price dynamics: dB/B = r dt + σ(t,T) dW under Q; the volatility
  σ(t,T) is the model's free input (term-structure vol).
- Two construction routes: short-rate factor models (r = r(X)) and
  forward-rate models (HJM) — ch30–31 and ch34 respectively.
- The market price of risk is what separates market-measure drift from
  risk-neutral drift; it's a modeling choice that shows up as the risk
  premium in bond yields.
