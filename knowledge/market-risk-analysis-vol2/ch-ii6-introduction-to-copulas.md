# II.6 Introduction to Copulas

Source: Carol Alexander, *Market Risk Analysis*, Vol. II (Practical Financial
Econometrics), ch II.6.

## Core idea

Volatility and Pearson correlation are only adequate risk/dependence metrics
when returns follow a multivariate normal i.i.d. process (elliptical
distributions). Real returns are skewed and fat-tailed, so we model the
**entire joint distribution** by combining *marginal* distributions with a
**copula** — a function that imposes a dependence structure on the marginals.
This two-stage construction (specify marginals, then the copula) separates
dependence from marginal behavior: each marginal can be a different
distribution (Student-t, chi-squared, gamma, ...).

Critically, **Pearson correlation is only a symmetric, linear dependence
metric**: two copulas can be calibrated to the same correlation yet produce
different joint distributions — e.g., one with strong lower-tail dependence
(riskier by downside measures) and one without.

## Concordance metrics

A concordance metric m(X, Y) in [-1, 1] is based on the proportion of
concordant pairs (x1-x2 and y1-y2 have the same sign). Rank-based metrics:
- **Spearman's rho**: correlation of the ranks.
- **Kendall's tau**: difference between concordant and discordant pair
  proportions.

These are copula-consistent (depend only on the joint distribution, not the
marginals) — the natural calibration inputs for copulas.

## Copula families

- **Gaussian (normal) copula**: from a multivariate normal via inversion —
  captures linear correlation but has **zero tail dependence** when
  correlation < 1 (understates joint extremes).
- **Student-t copula**: elliptical, symmetric, but with **tail dependence**
  governed by the degrees of freedom — better for simultaneous extreme moves.
- **Normal mixture copula**: mixture of two Gaussian copulas (e.g., one
  positive, one negative correlation) — captures complex asymmetric
  association patterns in all four tails.
- **Archimedean copulas** (built from a generator function phi(u)):
  - **Clayton**: `C(u1,...,un) = (sum u_i^-alpha - n + 1)^(-1/alpha)` —
    **lower-tail dependence** (assets crash together).
  - **Gumbel**: `C = exp(-(sum (-ln u_i)^theta)^(1/theta))` —
    **upper-tail dependence** (booms together).
  Nelsen lists 22 one-parameter Archimedean copulas; the independent copula
  arises from the generator phi(u) = -ln u.

## Calibration

- For one-parameter copulas there is often an **analytic link between the
  parameter and a rank correlation** (e.g., Clayton alpha from Kendall's tau:
  tau = alpha/(alpha+2); Gumbel: tau = 1 - 1/theta) — trivial calibration.
- Otherwise use **maximum likelihood** on the copula density; or construct an
  **empirical copula** from the sample and use it to choose the best
  parametric family (e.g., Kole et al.'s criteria).
- Marginal parameters are typically estimated first, then the copula — a
  two-step (inference for margins) procedure.

## Simulation and risk applications

Simulate correlated returns: draw uniform copula samples, then invert through
each marginal CDF. Applications:
- **Monte Carlo VaR** of portfolios with non-normal joint distributions.
- **Convolution over the copula** to aggregate dependent returns.
- Portfolio optimization with more realistic joint dependence.

## Key takeaways

- Copulas isolate dependence from marginals; use rank correlations (Kendall's
  tau, Spearman's rho) rather than Pearson to describe/couple them.
- Gaussian copula ⇒ no tail dependence; choose Clayton (lower tail) or Gumbel
  (upper tail) when joint extremes matter — common in equity returns.
- Student-t copula balances tractability with symmetric tail dependence.
- Calibrate one-parameter Archimedean copulas analytically from tau where
  possible; fall back to ML or the empirical copula.

Related skills: `skills/correlated-scenario-simulation`,
`skills/risk-metrics` (VaR), `knowledge/market-risk-analysis-vol1/ch-i3`
(distributions).
