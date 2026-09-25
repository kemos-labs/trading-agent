# Ch16 — Logistic Regression

**Source:** Grus, *Data Science from Scratch*, Chapter 16.

## Purpose
Classification via probabilities: predict `P(y = 1 | x)` with a number in
[0, 1]. Applied to predicting which users pay for premium accounts.

## Why not linear regression for classification?
- Linear predictions can be hugely negative or above 1 — uninterpretable as
  probabilities (the chapter's fits produced many negative predictions).
- Residual structure is wrong: near the boundaries (y fixed at 0/1), errors
  correlate with x, biasing the coefficient estimates.
- Fix: squeeze `dot(x, β)` through the **logistic (sigmoid) function**:
  `logistic(z) = 1/(1 + exp(−z))` ∈ (0, 1), with derivative
  `logistic'(z) = logistic(z)·(1 − logistic(z))`.

## The model
- `P(yᵢ = 1 | xᵢ, β) = logistic(dot(xᵢ, β))`.
- **Fit by maximum likelihood**, not least squares (the two are no longer
  equivalent once the link function is nonlinear).
- Per-point log-likelihood (Bernoulli):
  - if y = 1: `−log(logistic(dot(x, β)))`;
  - if y = 0: `−log(1 − logistic(dot(x, β)))`.
  I.e. maximise `Σ [yᵢ log fᵢ + (1−yᵢ) log(1−fᵢ)]` — **log loss /
  cross-entropy**. Gradient descent minimises the *negative* log likelihood.
- **Gradient** (nicely simple after the sigmoid derivative cancels):
  `∂/∂βⱼ [−log L] = (logistic(dot(x,β)) − y)·xⱼ` per point — the prediction
  error times the feature. Same shape as linear regression's gradient, which
  is why the same GD machinery (ch8) fits both.

## Practicalities
- **Rescale features first** (ch10) so gradient descent converges cleanly
  across salary-scale vs experience-scale inputs.
- Interpretable output: `logistic(...)` = predicted probability; threshold
  at 0.5 (or elsewhere) to classify.
- The fitted model: salary and experience both raise the probability of a
  premium account.

## Key takeaways
- Logistic regression = linear combination → sigmoid → probability, fit by
  maximising Bernoulli log-likelihood.
- Log loss is the right objective for probabilities; least squares is wrong
  for binary targets.
- Gradient = `(predicted − actual) · x` per point — a pattern shared with
  linear regression, so one optimiser serves both.

## Notes
- The sigmoid's derivative identity `σ' = σ(1−σ)` is what makes the gradient
  clean; this same convenience drives backpropagation in ch18.
- Probability calibration note for later: predicted probabilities are
  calibrated only if the model is well-specified.
