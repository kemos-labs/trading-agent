# Ch4 — Markov Chain Monte Carlo (MCMC)

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 4.

## Why MCMC
Bayes' rule gives P(θ|D) = P(D|θ)P(θ)/P(D). The **evidence/normaliser** is an integral over all
parameter values: P(D) = ∫_Θ P(D,θ) dθ — usually analytically intractable. With many
(hierarchical) parameters, posteriors become high-dimensional, so data grows sparse in the
volume (the **curse of dimensionality**; data must grow exponentially with dimension to retain
significance). **MCMC** avoids the intractable evidence integral by *sampling* from the
posterior via an intelligent random search: "memoryless searches performed with intelligent
jumps". (MCMC is also used in physics/biology for approximating any high-dim integral.)

## The generic MCMC recipe
1. Start at a current position θ_curr in parameter space.
2. Propose a new position θ_new (via a proposal distribution).
3. Accept/reject θ_new *probabilistically* using the prior and data.
4. Repeat; collect accepted positions.
5. Return the (stationary) sequence of accepted positions = the posterior sample.

The difference between MCMC algorithms lies in *how they jump* and *how they accept/reject*.

## Metropolis Algorithm (1953)
- **Proposal**: normal distribution with mean μ = θ_curr (current position) and a **proposal
  width** σ. Larger σ jumps further / covers more space but may initially miss the high-prob
  region; smaller σ converges more slowly. A normal proposal is natural for continuous
  parameters (nearby points more likely, occasionally jumping far → explores space).
- **Acceptance**: compute the ratio of the proposal density at the new vs current position;
  generate a uniform random number U ∈ [0,1]; accept if U ≤ acceptance ratio.
- **Why it works (key trick)**: we need the ratio of posteriors, but the intractable evidence
  term P(D) *cancels* in the ratio — the ratio depends only on **likelihoods and priors**,
  both computable:
  ratio = [P(D|θ_new)P(θ_new)] / [P(D|θ_curr)P(θ_curr)]
  So we resample regions of higher posterior probability more often — no integral needed.

## Sampling variants noted
Metropolis → **Metropolis-Hastings** (Hastings 1970), **Gibbs sampler** (Geman & Geman),
**Hamiltonian Monte Carlo**, and **No-U-Turn Sampler (NUTS)** (Hoffman & Gelman). NUTS is
built into PyMC3 and can handle thousands of parameters.

## PyMC3 (probabilistic programming in Python, uses Theano)
- Specify the model straightforwardly, then run MCMC. Similar to JAGS/Stan. Support for
  Metropolis, NUTS, etc.
- Example: infer coin fairness.
  - Prior: `theta = pm.Beta('theta', alpha=12, beta=12)`.
  - Likelihood: `y = pm.Binomial('y', n=50, p=theta, observed=10)`.
  - `start = pm.find_MAP()` (MAP optimisation for a good starting point),
    `step = pm.Metropolis()`, `trace = pm.sample(100000, step, start)`.
- **Worked verification**: prior(α=12,β=12), N=50, z=10 ⇒ analytic posterior Beta(22,52)
  with mean 22/74 ≈ 0.297. MCMC histogram (100k samples) closely tracks this analytic
  posterior — confirming MCMC converges to the closed-form for this conjugate case. Far fewer
  samples suffice for such a simple model.
- **Trace plot**: the vector of accepted samples; used to assess convergence (series should
  look stationary) and to spot the burn-in period to discard initial samples.

## Takeaways / pitfalls
- MCMC is what makes Bayesian inference tractable when conjugacy fails.
- The acceptance ratio cancels the evidence term — this is the crux.
- Use trace convergence plots + burn-in before trusting posterior estimates.

## Source books
Metropolis (1953); Hastings; Geman & Geman (Gibbs); Duane et al (HMC); Hoffman & Gelman
(NUTS); modelled on the QuantStart/Probabilistic-Programming-Notes lineage.