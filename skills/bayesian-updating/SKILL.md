# Bayesian Updating (Conjugate Priors)

## name
Bayesian updating with conjugate priors

## description
Sequentially update a belief distribution about an unknown parameter (e.g. an
unknown probability, a mean) as new data arrives, using Bayes' rule with a
conjugate prior so the posterior stays in the same family as the prior.

## when to use it
- You have a prior belief about a probability/parameter (e.g. a win rate, a
  signal hit rate, a coin bias) and want to update it with new observations.
- You want a principled way to combine prior domain knowledge with data, and a
  full posterior (not just a point estimate) for uncertainty quantification.
- Useful in quant contexts: estimating hit rates of signals, binomial event
  probabilities, and Bayesian linear regression with Normal-Inverse-Gamma priors.

## method / formula / code

Bayes' rule:
```
p(θ | D) = p(D | θ) · p(θ) / p(D)
```
p(θ) = prior, p(D|θ) = likelihood, p(D) = marginal likelihood (evidence,
normalising constant; cancels in MCMC ratio computations).

**Beta-Binomial conjugacy** (the workhorse for binomial proportions):
```
Prior:      θ ~ Beta(α, β)
Likelihood: z successes in N trials: θ^z (1−θ)^(N−z)
Posterior:  θ | D ~ Beta(α + z, β + N − z)
```
Posterior mean = (α+z) / (α+β+N). A uniform prior = Beta(1,1); a "flat-ish"
prior = Beta(1/2, 1/2).

**Verified example**: prior α=β=12, N=50 trials, z=10 successes →
posterior Beta(22, 52): mean 0.297, sd 0.053. (Verify any formula against a
known reference value before trusting it.)

```python
from scipy import stats
a, b, N, z = 12, 12, 50, 10
post = stats.beta(a + z, b + N - z)
mean, sd = post.mean(), post.std()
# 0.297, 0.053
```

Recursive updating: today's posterior is tomorrow's prior — update as each
batch of data arrives.

## known pitfalls
- The prior is a modelling choice: a strong (informative) prior can dominate
  the data; a mis-specified prior biases the posterior.
- Evidence p(D) is a normalising constant — in MCMC you only need the
  *ratio* of posteriors, so it cancels.
- Conjugacy only holds for chosen likelihood/prior pairs; don't force a
  conjugate model where the likelihood isn't right (see Beta-Binomial vs
  Poisson-Gamma vs Normal-Normal choices).

## source book
Halls-Moore, *Advanced Algorithmic Trading*, ch02–ch03 (Bayesian statistics;
Bayesian inference of a binomial proportion).
