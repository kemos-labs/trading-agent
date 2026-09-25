# Ch5 — Bayesian Linear Regression

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 5.

## Frequentist (classical) multiple linear regression — recap
Assume a model with response y, predictors X, coefficients β, and normal measurement error:
 **y = Xβ + ε**, ε ~ N(0, σ²).
- Goal: estimate β giving the best linear (hyperplane) fit to training data, by minimising a
  loss. Standard is **Ordinary Least Squares (OLS)** minimising the **Residual Sum of Squares**
  RSS = Σ(y_i − X_i β)².
- **Maximum Likelihood estimate** of coefficients:
  **β̂ = (XᵀX)⁻¹ Xᵀ y**   (5.4)
- Prediction for new data x: y_pred = x·β̂.
- **Point estimate**: β̂ is a single point in R^(p+1). Key limitation: gives no measure of
  uncertainty on the coefficients.

## Bayesian reformulation — probabilistic regression
The whole model is recast probabilistically: response values y are samples from a multivariate
normal with mean = Xβ and variance σ² (an identity matrix scales because it's multivariate):
 components as samples from a normal error term; Bayesian recasts *the entire problem* as a
 distribution over y.

**Benefit**: 
1. You can inject **prior knowledge** via prior distributions on β (or use uninformative priors).
2. Instead of a single point estimate β̂, you get a **full posterior distribution** over the
   coefficients, so uncertainty can be quantified via the variance of the posterior.

## Generalised Linear Models (GLM) — brief
GLM extends ordinary linear regression to other response-error distributions (logistic,
Poisson, etc.). The linear predictor Xβ links to the response via a **link function g**, with the
response from an **exponential-family distribution**; variance is often a function of the mean:
 **Var(y) = V(E(y)) = V(g⁻¹(Xβ))**  (5.7). Introduced because PyMC3's `pm.glm` module
(Wiecki) uses R-like formula syntax for clean Bayesian model specification.

## Simulate-then-fit methodology (key, reusable)
Simulate data with *known* parameter values, fit the model, then verify it recovers them — a
test that the model is set up correctly before trusting it on real data (same trick used later
for ARMA/GARCH). 
- Simulated N=100 points: intercept β₀=1, slope β₁=2, noise ε~N(0, σ²=1).

## PyMC3 GLM fit
- Use `with pm.Model()`, `pm.glm.glm('y ~ x', df, family=pm.glm.families.if(data))`,
  `start = pm.find_MAP()`, `step = pm.NUTS()`, sample ~5000 draws, discard first 500 as
- Traceplot per parameter:
  - Intercept posterior mode ≈ **1** (true 1),
  - Slope posterior mode ≈ **1.98** (true 2),
  - Noise sd ≈ **0.465** (true 1 σ √...  ≈ consistent as it's the residual sd of the noise).
  Each has a reasonable variance = quantified uncertainty.
- **Posterior predictive**: sample likely regression lines via `plot_posterior_predictive`;
  the thin band of lines near the true line demonstrates the location-uncertainty inherent in
  the Bayesian fit (not a single "best" line).

## Takeaways / pitfalls
- Bayesian regression outputs a *distribution of lines* (uncertainty), a core advantage over
  the single OLS line.
- Use the *simulate-and-recover* check whenever coding new Bayesian models; it validates the
  fit pipeline before trusting it on real data.
- MAP init helps NUTS start near the mode; burn-in is discarded for cleaner traces.