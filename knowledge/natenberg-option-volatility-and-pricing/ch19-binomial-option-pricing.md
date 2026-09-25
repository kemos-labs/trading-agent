# Chapter 19 — Binomial Option Pricing (Cox-Ross-Rubinstein)

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## Risk-neutral world

A stock can go to Su or Sd. Risk-neutral probability makes expected
value equal the forward:

```
p = (1 + r·(t/n) − d) / (u − d)      (r=0: p = (1−d)/(u−d))
```

p and 1−p are *pseudoprobabilities* — with extreme rates they can leave
[0,1] (r = 40%, u = 1.05 → p = 1.59, 1−p = −0.59); the up-move must
exceed the financing cost (u > 1 + r·t/n) for sensible values. The tree
is recombining (u·d = 1, driftless).

## Pricing

- One period: `C = [p·max(Su−X,0) + (1−p)·max(Sd−X,0)] / (1 + r·t/n)`.
- n periods: terminal prices `S·u^j·d^(n−j)` with binomial-path weights;
  work **backwards** from expiry, discounting each node:
  `C_{i,j} = [p·C_{i+1,j+1} + (1−p)·C_{i+1,j}] / (1 + r·t/n)`.
- Tree parameters from vol: `u = e^(σ·√(t/n))`, `d = 1/u` (a one-σ move
  per interval). Example: u = 1.05, t/n = 0.25 → ln(1.05) = 0.0488 =
  σ·0.5 → σ = 9.76%.
- Worked 3-period example (S = 100, t = 9 mo, r = 4%, u = 1.05, p =
  0.59): 100 call = 5.22, 100 put = 2.28. Put-call parity check:
  F = 100×(1.01)³ = 103.03; (F−X)/(1+rt) = 3.03/1.03 = 2.94 = C − P ✓.

## Greeks from the tree

- `Δ = (C_{1,1} − C_{1,0}) / (S_{1,1} − S_{1,0})` = (7.75−1.71)/(105−95.24)
  = 6.04/9.76 → **62**.
- `Γ = (Δ_{1,1} − Δ_{1,0}) / (S_{1,1} − S_{1,0})` ≈ (81−31)/9.76 ≈ **5.1**.
- Θ: needs two periods (only then does the price return to a level):
  (C_{2,1} − C_{0,0}) / (2·period days).
- Vega and rho: no closed form — bump σ or r and reprice the tree.

## Why it works (gamma rent)

Delta-neutral + rehedging at every node breaks even *including interest*
(option +0.62-stock hedge: −0.57 loss both ways + 0.57 interest =
0). The break-even move each interval is exactly **one standard
deviation** — theta is the rent you pay for gamma. Buying below value /
selling above value at any node is captured by the rehedging (ch. 8
principle).

## American options

At each node, replace the backward-inducted value with **intrinsic
value** if higher, then continue. Effects propagate:
- American 100 put (P_{2,0}: 8.31 → 9.30 intrinsic) changes the initial
  value and the Greeks — European put Δ −38 → American −42; gamma
  changes too.
- Calls only benefit with a dividend: at S = 110.25 pre-ex-div,
  European 100 call = 9.26 < intrinsic 10.25 → exercise. No dividend →
  American = European for calls.
- Dividends paid *between* periods break recombination (each node
  spawns a new tree); common approximation: build the no-dividend tree,
  then subtract total dividends from all downstream nodes (slightly
  overvalues).

## Convergence & accuracy

- Binomial → Black-Scholes as n → ∞; error oscillates sign with n and
  shrinks in magnitude. 3-period example: C = 5.22 vs BS 5.01.
- 50–100 periods is the usual accuracy/speed tradeoff; **half-step
  averaging** (mean of n and n+1 period values) cuts error
  dramatically (9½-period error ≈ 0.01 vs. 0.07–0.09).
- Parameter variants (b carry) extend the tree to futures, FX, etc.,
  exactly like the Black-Scholes family.

## Key takeaways

1. Binomial = risk-neutral backward induction on a recombining u/d tree
   with u = e^(σ√(t/n)); it handles American early exercise, which BS
   cannot.
2. Greeks fall out of node values; vega/rho need repricing bumps.
3. Break-even gamma rent = one σ per interval; 50–100 steps (or
   half-step averaging) ≈ BS accuracy for Europeans.
