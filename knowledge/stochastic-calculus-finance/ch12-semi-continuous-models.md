# Ch12 — Semi-Continuous Models

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes) — Steven
Shreve

## Discrete-time Brownian motion

Let Y₁,...,Y_n be independent standard normals under P. Define

```
B₀ = 0,   B_k = Y₁ + ... + Y_k
```

This is **discrete-time Brownian motion** — the bridge from the binomial
model to continuous Brownian motion. F_k = σ(Y₁,...,Y_k) = σ(B₁,...,B_k).

Properties:
- **Martingale**: E[B_{k+1} | F_k] = E[Y_{k+1} + B_k | F_k] = B_k.
- **Markov**: E[h(B_{k+1}) | F_k] = g(B_k) for g(b) = E[h(Y_{k+1}+b)] — the
  future depends only on the current value (Independence Lemma).
- **Gaussian increments**: B_{k+1} − B_k = Y_{k+1} ~ N(0,1), independent of
  the past — normal, independent increments.
- **Quadratic variation**: Σ (ΔB_k)² = Σ Y_k² → n as n → ∞ (law of large
  numbers), i.e. the process accumulates quadratic variation at rate 1 per
  unit time. (Discrete analog: the coin-toss walk accumulates (log u)² per
  step.)

## The stock price process

Log-normal dynamics: S_k = S₀·exp(μ·k + σ·B_k), or in returns form
log(S_{k+1}/S_k) = μ + σ·Y_{k+1} with Y ~ N(0,1). μ is the mean rate of
return, σ the volatility (per period). Returns are i.i.d. normal here —
the "semi-continuous" step toward geometric Brownian motion: time is
discrete, states are continuous.

## Risk-neutral version

Under Q, the drift changes: log(S_{k+1}/S_k) = r − σ²/2 + σ·Ỹ_{k+1} with
Ỹ standard normal under Q, so that the discounted stock is a martingale
(mean E_Q[log return] = r − σ²/2 — the Itô correction, appearing here in
discrete form).

## Where this is heading

- Scaling B_k/√k → standard normal (CLT); as step size → 0 the discrete
  walk converges to **continuous Brownian motion** (ch13).
- The stock dynamics become geometric Brownian motion
  dS = μS dt + σS dB, and the r − σ²/2 term becomes the Itô-formula
  drift correction.
- The machinery of martingales/Markov/quadratic variation established here
  (discrete) is exactly what ch13–15 define rigorously (continuous).

## Key takeaways

- Discrete-time Brownian motion = sum of i.i.d. normals: martingale,
  Markov, independent normal increments, quadratic variation per unit time.
- The log-normal stock model with i.i.d. normal returns is the
  semi-continuous bridge to GBM.
- Risk-neutral drift r − σ²/2: the discount-adjusted mean return — the
  Itô correction in embryo.
- Quadratic variation accumulation (rate σ² per unit time) is the single
  most important quantity for what comes next (Itô calculus).
