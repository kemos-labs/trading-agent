# Ch10 — Bayesian ML: Dynamic Sharpe Ratios and Pairs Trading

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 10.

## Purpose
Bayesian inference for finance: treat parameters as probability distributions, update beliefs with data, and apply it to Sharpe-ratio estimation and pairs trading — with MCMC and variational inference as the computational engines.

## Bayesian inference recap
- Posterior ∝ Likelihood × Prior: p(θ|x) ∝ p(x|θ)·p(θ).
- **Priors** encode existing beliefs; **posterior** is the updated belief; **posterior predictive** p(x_new|x) generates new data.
- Point estimates (posterior mean/mode) plus full uncertainty (credible intervals) — uncertainty quantification is the payoff (see `bayesian-updating`).

## Inference methods
- **Conjugate analysis**: closed-form posteriors for simple models (normal-normal, beta-binomial).
- **MCMC** (Metropolis-Hastings, Hamiltonian MC/NUTS): sample from the posterior for arbitrary models; PyMC3 workflow — model definition, sampling, diagnostics (trace plots, R-hat ≈ 1).
- **Variational inference (ADVI)**: approximate the posterior by optimization; faster but approximate — for large datasets.

## Bayesian Sharpe ratio
- Treat the mean return μ (and its precision) as unknown; with a normal likelihood + normal-gamma prior, the posterior mean is a precision-weighted blend of prior and data mean.
- Result: a posterior *distribution* over Sharpe — you can answer "P(Sharpe > 0 | data)" and see how prior skepticism shrinks estimates. This is the honest way to evaluate short backtests (cf. deflated Sharpe in `purged-cross-validation`).
- Model Sharpe of a strategy conditioned on a factor model (Bayesian regression with shrinkage priors on factor loadings).

## Bayesian pairs trading
- Estimate the cointegration/spread parameters (β, spread mean and vol) with uncertainty via Bayesian regression (normal likelihood, priors on β and σ).
- The posterior gives a distribution over the spread's current deviation → probability the spread is stretched; trade thresholds informed by posterior quantiles.
- **Dynamic learning**: update the posterior as new spread observations arrive (online/sequential Bayesian updating) — the spread regime changes and beliefs track it (see `bayesian-updating` for the update formulas).

## Practical notes
- Priors are both a feature (regularization, domain knowledge) and a risk (bad priors bias results) — run sensitivity checks.
- MCMC is slow: for production use conjugate updates or variational methods; monitor convergence diagnostics.
- Report credible intervals, not just point estimates — the spread's posterior quantiles directly set entry/exit bands.

## Key takeaways
- Bayesian methods add exactly what finance needs: rigorous uncertainty around estimated Sharpe, betas, and spread parameters.
- Sequential updating fits markets' non-stationarity — beliefs adapt as regimes shift.
- Pair the Bayesian spread model with the classical cointegration test (ch9) for a robust pairs workflow.
