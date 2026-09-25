# Ch33 — Change of Numéraire

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, Part II)
— Steven Shreve

## The idea

Prices are relative: the money-market account β(t) = exp(∫₀ᵗ r du) is the
usual numéraire, and Q is the measure under which *discounted* (deflated)
prices S/β are martingales. But **any strictly positive traded asset can
serve as the numéraire**, each carrying its own equivalent martingale
measure. Choosing the right numéraire can make pricing dramatically
simpler.

## Mechanics

Stock dS = rS dt + σS dW under Q (money-market numéraire). The T-forward
measure: use the zero-coupon bond B(t,T) as numéraire. The change-of-
measure density (Radon-Nikodym between the two martingale measures) is

```
dQ^T/dQ = B(T,T)/β(T) · β(0)/B(0,T) = β(t)·B(T,T)/(B(t,T)β(T))-type ratio
```

The forward price F(t,T) = S(t)/B(t,T) is a **martingale under Q^T**
(the T-forward measure) — no discounting needed. Pricing a claim whose
payoff is at T:

```
V(t) = B(t,T) · E_{Q^T}[ V(T) | F(t) ]
```

The bond factor handles all discounting; expectations are taken under the
forward measure.

## Why it helps

- **Interest-rate derivatives** (caps, swaptions, LIBOR): payoffs are
  functions of rates at fixed dates; under the forward measure those rates
  have simpler (often martingale or lognormal) dynamics — this is the
  engine behind the Black-76 formulas for caps/floors and the BGM/LMM
  market models (ch34).
- **Quanto/foreign-currency claims**: choose the foreign or domestic
  money-market/equity numéraire to absorb FX drift terms.
- **Equity claims with dividends**: the dividend-adjusted forward measure
  makes the underlying a martingale in its own units.

## Key formula

Under Q^T (T-forward measure), the numéraire is B(t,T). For any traded
asset price process A(t):

```
A(t)/B(t,T)  is a Q^T-martingale
```

Pricing: V(t)/B(t,T) = E_{Q^T}[V(T)/B(T,T)|F(t)] = E_{Q^T}[V(T)|F(t)] since
B(T,T) = 1 — clean.

## Key takeaways

- Numéraire = unit of account; each positive traded asset defines an
  equivalent martingale measure.
- T-forward measure (numéraire = T-bond): forward prices are martingales;
  V(t) = B(t,T)·E_{Q^T}[V(T)].
- Change-of-numéraire = change of measure with the numéraire ratio as the
  density — Girsanov at the asset level.
- Master tool for rate derivatives (caps/swaptions), quantos, and any
  claim with awkward discount factors.
