# Ch6 — Bayesian Stochastic Volatility Model

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 6.

## Motivation
Estimate *historical volatility of asset returns* in a Bayesian way. Value to a quant: a
**risk filter** on trade signals. The model returns, at each t, a **full posterior distribution**
(hence credible intervals) of volatility instead of a single point estimate — quantifying
uncertainty in the latent vol process. It follows Hoffman & Gelman (NUTS) and the PyMC3
tutorial of Salvatier et al.

## Background: stochastic volatility
- Accounts for **volatility clustering** (heteroskedasticity): bouts of excess vol, e.g. the
  2008 crisis.
- Contrast with GARCH (later chapter) — both model time-varying vol but differently.
- The **continuous Heston model** is a pair of SDEs: dS (asset, geometric random walk) and
  dν for volatility, with ν a **mean-reverting** process having its own variance ξ:
  dν = κ(θ−ν)dt + ξ√ν dW. (Mentioned for context.)

## The simplified model (this chapter)
No mean reversion — the latent vol follows a **random walk**, and returns use a
**Student's t-distribution** with variance driven by ν (t gives fat tails / excess kurtosis).

Model priors (positive-support, high uncertainty):
- **σ** = scale of the volatility process, **ν** = Student-t degrees of freedom
  (controls kurtosis; higher ν ⇒ thinner tails). Both Exponential-distributed;
  σ gets a *larger* chosen rate to reflect high initial uncertainty about the vol scale.
- **Latent volatility**: **s_i ~ N(s_{i−1}, σ²)**  (6.3) — a Gaussian random walk, variance
  driven by σ.
- **Log-returns**: **log(y_i / y_{i−1}) ~ Student-t(ν, mean 0, variance exp(−2·s_i))** — variance
  depends on the latent vol variable, giving heavy tails.

Final Bayesian model (4 priors):
- σ ~ Exponential; ν ~ **Exponential**
- s ~ GaussianRandomWalk(σ², length of returns)
- log returns ~ StudentT(ν, λ = exp(−2·s))

## PyMC3 implementation (applied to AMZN)
- Pull AMZN adjusted close from Yahoo via `pandas_datareader`; compute
  **log returns** = log(AdjClose_t / AdjClose_{t−1}).
- Model via `with pm.Model()`, using `GaussianRandomWalk`, `pm.StudentT`, exponential priors.
- Sample with **NUTS** — 2000 draws is enough here (custom slow, ~15–20 min); uses
  `pm.sample`.
- Diagnostic plots:
  - **Traceplot** of logν, logσ posteriors (posterior distributions + trace series).
  - **Volatility estimate vs time**: plot every k-th sample per trading day (k=10, 3%
    opacity) to visualise the posterior *cloud* of vol; overlay absolute returns to confirm
    vol clustering.
- Automated use: detect higher-vol periods to trigger risk reduction (e.g. cut leverage).

## Takeaways / pitfalls
- Heavy-tailed (Student-t) returns + shrinking posterior is a more robust vol model than plain
  Gaussian for real financial data with fat tails.
- The posterior cloud conveys uncertainty — better than a volatility point estimate for
  risk-filtering and regime-style decisions.
- NUTS is the practical sampler here because conjugate (closed-form) posterior isn't available.
- "simulate-and-fit" discipline from the previous chapter carries over for validating the
  model before use.

This concludes the Bayesian Statistics part; the methods feed the Time Series and ML
sections.