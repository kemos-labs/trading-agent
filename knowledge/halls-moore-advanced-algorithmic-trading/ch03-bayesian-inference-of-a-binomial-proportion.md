# Ch3 — Bayesian Inference of a Binomial Proportion

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 3.

## Goal
Estimate the **proportion** (e.g. coin fairness θ = P(head)) of a two-outcome process and
make future predictions, extending the ch2 example. Applications: engine-blade defect rate,
survey "yes" responses, patient recovery rate, error rate in transactions, click-through rate.

## Procedure (Bayesian workflow for a binomial proportion)
1. **Assumptions**: two outcomes; flips independent and identically distributed (IID);
   fairness θ **stationary** (time-invariant); θ ∈ [0,1].
2. **Quantify prior belief**: pick a probability distribution over θ — here the **Beta**.
3. **Experimental data / likelihood**: run N flips, count z heads; define the **likelihood**.
4. **Compute posterior** with Bayes' rule (Beta prior + Bernoulli likelihood → Beta conjugate).
5. **Infer**: estimate θ, predict probability of next head, assess parameter sensitivity.

## Bernoulli distribution vs likelihood

For a single coin outcome k ∈ {1 (head), 0 (tail)}:
- Bernoulli distribution (discrete, over outcomes): **P(k|θ) = θ^k (1−θ)^(1−k)**
  - P(k=1|θ)=θ; P(k=0|θ)=1−θ.
- **Likelihood function** (of θ, treating k fixed, varying θ as continuous): same formula but
  read the other way; it is *not* a probability — its integral over all θ ≠ 1.

Multiple flips (independence) — probability of seeing z heads in N flips:
**P(z, N | θ) = θ^z (1−θ)^(N−z)**   (3.9)

## Choosing the prior — the Beta distribution

The Beta PDF (normalised by B(α,β)):   **P(θ|α,β) = θ^(α−1)(1−θ)^(β−1) / B(α,β)**   (3.10)
- Support [0,1] matches θ; two free shape parameters α, β give flexibility.
- Larger α shifts mass toward heads; larger β toward tails; equal large α=β narrows and peaks at
  θ=0.5 (fair coin).

**Conjugate prior** definition: a prior whose family is preserved in the posterior when combined
with a chosen likelihood. Beta prior ⊗ Bernoulli likelihood ⇒ **Beta posterior**, giving a
closed-form posterior — no numerical integration needed. (A prior is conjugate *only w.r.t. a
specific likelihood*.)

**Why Beta is conjugate to Bernoulli** (sketch): the Beta PDF and Bernoulli likelihood share the
θ^(a)(1−θ)^(b) form, so multiplying them (per Bayes rule) keeps the same functional form.

## Specifying prior via mean & variance

The Beta's mean μ and variance σ² relate to α, β:
- **μ = α / (α+β)**
- **σ² = αβ / ((α+β)²(α+β+1))**

Rearranged to in-piece practical elicitation: given desired prior mean μ and sd σ, solve for
α, β. **Caveat**: do not specify σ > 0.289 — that's the sd of the uniform θ∈[0,1] (i.e. no
prior information); larger is impossible. Example: μ=0.5, σ=0.1 ⇒ α=12, β=12.

## Posterior update rule (the key takeaway)

**P(θ|z,N) = P(z,N|θ)·P(θ) / P(z,N)**  (3.18), where P(z,N) is the beta-function normaliser.

Closed-form: with prior  **Beta(α, β)** and z heads in N flips:
**posterior ~ Beta(α + z, β + N − z)**   (3.22-ish)

- Straightforward: sum the observed counts onto the prior shape parameters.
- **Posterior mean** μ_post = (α+z)/((α+z)+(β+N−z)); **posterior sd** = sqrt(αβ-mean form),
  shrinking as α, β grow with data ⇒ uncertainty falls with sample size.

## Worked example verification
Prior μ=0.5, σ=0.1 ⇒ α=β=12. Observe N=50, z=10 heads:
- Posterior = Beta(12+10, 12+40) = Beta(22, 52).
- Mean = 22/(22+52) = 22/74 = **0.297**; sd = sqrt(22·52/(74²·75)) = **0.053**.
  (Matches the book's 0.297 / 0.053.) Mean shifted toward 0.3, sd roughly halved → more
  certainty. The posterior Beta can serve as the new prior for further updates — iterative
  conjugate updating.

## Takeaways / pitfalls
- Always normalise the prior belief sd (≤0.289) to keep it a valid density over [0,1].
- Conjugate choice removes numerical integration — a core speed-up in Bayesian tooling.
- The posterior-as-new-prior property is the engine behind online/sequential Bayesian learning.