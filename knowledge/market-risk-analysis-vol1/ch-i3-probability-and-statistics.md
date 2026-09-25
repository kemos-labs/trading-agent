# Chapter I.3 — Probability and Statistics

## Core idea
The probabilistic and statistical machinery for analyzing financial returns:
probability laws, distributions (normal, lognormal, Student t, normal
mixtures, extreme value), joint/conditional distributions and dependence,
statistical inference, maximum likelihood, and stochastic processes in
discrete/continuous time.

## Basic concepts
- Random variables in finance: prices, returns, rates, P&L.
- Continuous vs discrete RVs; for continuous variables, probabilities are
  over intervals, not points.
- **Classical (frequentist) vs Bayesian**: classical = relative frequency,
  prior uniform; Bayesian allows subjective priors. Classical dominates in
  practice; Bayesian is better suited to market risk (history ≠ future).
- **Laws of probability**: P(A) ∈ [0,1]; mutually exclusive events sum;
  complement; joint/conditional/marginal probabilities.

## Moments and distributions
- Expectation, variance, skewness, kurtosis and higher moments; percentiles
  and quantiles.
- **Univariate catalog**:
  - **Normal**: benchmark; symmetric; used for i.i.d. assumptions.
  - **Lognormal**: prices (returns normal ⇒ prices lognormal); GBM.
  - **Normal mixture**: fat tails via mixing normals (EM estimation, I.5).
  - **Student t**: heavier tails; used in inference and dependence.
  - **Extreme value distributions**: tails and extremes.
  - **Stable distributions**: sum-stable, aggregate risks over time.
  - **Empirical distributions**: non-parametric via **kernel estimators**.
- **Joint distributions**: marginal vs conditional; independence ⇔ joint
  distribution = product of marginals.
- **Covariance**: `Cov(X,Y) = E[(X-μx)(Y-μy)] = E[XY] - E[X]E[Y]`.
- **Correlation**: standardized covariance; limitations as a dependency
  measure (linear only; zero correlation ≠ independence) — motivates
  copulas (Volume II ch6).

## Statistical inference
- **Confidence intervals**: quantiles, critical values; Student t based CIs
  for small samples.
- **Hypothesis testing**: critical regions, significance levels.
- Volatility/var inference is key for market risk (vol forecast CIs in
  Volume II ch3).

## Maximum likelihood estimation (MLE)
- Likelihood function of a sample given a distributional form; maximize to
  estimate parameters.
- Required for GARCH parameter estimation (Volume II ch4) and distribution
  fitting (Johnson, EM).

## Stochastic processes
- **Discrete time**: stationary vs integrated processes (random walks).
- **Continuous time**: Brownian motion, GBM; the discrete–continuous
  translation is critical — a continuous-time SDE has a discrete-time
  analogue used for estimation and simulation.

## Bottom line
The statistical core of the volume: distribution families, dependence,
inference, MLE, and stochastic processes. It underpins the regression
chapter (I.4) and later volumes' GARCH, copulas, and VaR. Cross-refs:
`knowledge/market-risk-analysis-vol1/ch-i4` and the knowledge base's
`skills/bayesian-updating`, `skills/arma-garch-modeling`.
