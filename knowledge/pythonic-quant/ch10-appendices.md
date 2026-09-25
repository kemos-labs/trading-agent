# Appendices — Financial Mathematics and Automation Guides

## Core idea
Reference appendices: the options/Greeks formulas (Black-Scholes, Greeks,
stochastic calculus) and a set of practical Python automation recipes for
daily finance work.

## Black-Scholes model
- European call: `C = S0·N(d1) - X·e^(-rT)·N(d2)`
- European put: `P = X·e^(-rT)·N(-d2) - S0·N(-d1)`
- where `d1 = (ln(S0/X) + (r + 0.5·σ²)T) / (σ·√T)`, `d2 = d1 - σ·√T`,
  `N(·)` the standard-normal CDF.
- Inputs: S0, strike X, time to expiry T, risk-free rate r, volatility σ.
- Assumptions: constant volatility and rates, no dividends.

## The Greeks
- **Delta (Δ)**: price sensitivity to underlying — call `N(d1)`, put
  `N(d1)-1`.
- **Gamma (Γ)**: delta's sensitivity to underlying —
  `N'(d1)/(S0·σ·√T)` — stability of the hedge.
- **Theta (Θ)**: time decay — call
  `-S0·N'(d1)·σ/(2√T) - r·X·e^(-rT)·N(d2)`; put with `+r·X·e^(-rT)·N(-d2)`.
- **Vega (ν)**: volatility sensitivity — `S0·√T·N'(d1)`.
- **Rho (ρ)**: rate sensitivity — call `X·T·e^(-rT)·N(d2)`, put negative.
- N'(d1) is the standard-normal density.

## Stochastic calculus essentials
- **Brownian motion / Wiener process**: W(0)=0, independent normal
  increments with mean 0, variance t; martingale; quadratic variation t.
- **Itô's lemma**: differential of a function of a stochastic process — the
  engine behind BS.
- **SDEs**: `dX(t) = μ(t,X)dt + σ(t,X)dW(t)`.
- **GBM**: `dS = μS·dt + σS·dW`, solution
  `S(t) = S(0)·exp((μ - 0.5σ²)t + σW(t))`; expected value `E[S(t)] =
  S(0)·exp(μt)` (the -0.5σ² correction shows in the median/log form).
- **Martingales**: `E[X(t+s) | F_t] = X(t)` — fair games; coin-toss
  winnings example.

## Automation recipes (sample)
- Task scheduling (`schedule`), file conversion (CSV→Excel via pandas),
  database backup (`subprocess` + `mysqldump`), network scanning (nmap),
  voice commands (`speech_recognition`/`pyttsx3`), PDF/email/web-scraping
  automations, monitoring, alerts, and reporting.

## Bottom line
The reference appendix. The BS/Greeks/stochastic-calculus formulas are the
classic derivations already distilled across the knowledge base —
`knowledge/natenberg-option-volatility-and-pricing/ch18`,
`knowledge/stochastic-calculus-finance/` (ch13–17), and
`skills/monte-carlo-option-pricing` — and the automation recipes are
general Python utility patterns.
