# Ch04 — Training Models

**Source:** Géron, *Hands-On Machine Learning*, Chapter 4.

## Purpose
Open the black box: linear regression fit by closed form and by gradient
descent (batch/stochastic/mini-batch), polynomial regression,
regularisation (Ridge/Lasso/ElasticNet), and logistic/softmax regression.

## Linear regression
- Model: `ŷ = θ₀ + θ₁x₁ + … + θₙxₙ = θᵀx` (x₀ = 1 dummy for bias).
- Fit = minimise MSE over θ.
- **Normal equation** (closed form): `θ̂ = (XᵀX)⁻¹ Xᵀy`. Exact, but O(n³)
  and slow for many features; use `np.linalg.inv(X.T@X)@X.T@y` or better
  SVD-based `LinearRegression` (computes pseudo-inverse, faster, no
  invertibility issue).
- **Complexity**: normal eqn/SVD fast for large m, slow for large n.

## Gradient descent
- Step: `θ ← θ − η·∇MSE(θ)`; the MSE gradient is `(2/m)·Xᵀ(Xθ − y)`.
- **Feature scaling is mandatory** for GD (else it zigzags and converges
  slowly); `StandardScaler`.
- **Batch GD**: full dataset per step — precise, but slow for large m.
- **Stochastic GD**: one random instance per step — fast, jumps around the
  minimum; use a **learning schedule** (η decays over time: η = η₀/(t +
  t₀) etc.); shuffle instances (IID assumption) or results drift.
  `SGDRegressor` with `tol`, `n_iter_no_change`, `eta0`.
- **Mini-batch GD**: small random batches per step — best of both; uses
  matrix/GPU hardware efficiently; the practical workhorse (and the basis
  of all neural-net optimisers in ch11).
- GD variants generalise to any differentiable model; normal equation only
  fits linear regression.

## Polynomial regression
- Add powers (and cross-products) of features via `PolynomialFeatures`,
  then run linear regression — fits nonlinear data with a linear model.
- **Combinatorial explosion**: degree d over n features ⇒ (n+d)!/(d!n!)
  features. Beware.

## Learning curves & the bias/variance trade-off
- **Learning curves**: training & validation error vs training-set size.
  - Underfitting: both curves plateau close together and high; more data
    will NOT help — need a better model.
  - Overfitting: big gap (train low, validation high); more data closes the
    gap.
- **Generalization error = bias + variance + irreducible error**.
  High bias ⇒ underfit; high variance ⇒ overfit; complexity ↑ ⇒ bias ↓,
  variance ↑. The sweet spot balances them.

## Regularised linear models
- **Ridge (Tikhonov)**: MSE + α·Σθᵢ² (ℓ₂ penalty on weights). Shrinks
  weights toward 0; closed form exists: `θ̂ = (XᵀX + αI)⁻¹Xᵀy`. α↑ ⇒ flatter
  model. Regularisation must be added during training only; evaluate with
  plain MSE.
- **Lasso**: MSE + α·Σ|θᵢ| (ℓ₁) — drives unimportant weights to exactly 0
  (sparse, feature selection); derivative discontinuous at 0 → subgradient.
- **Elastic Net**: α·r·ℓ₁ + α·(1−r)/2·ℓ₂ — middle ground; prefer when
  features are many or correlated; pure Lasso can behave erratically with
  correlated features.
- **Rule of thumb**: plain linear → Ridge; few useful features → Lasso;
  correlated features → Elastic Net.

## Logistic (binary) & Softmax (multiclass) regression
- **Logistic**: `p = σ(θᵀx)` with sigmoid `σ(t) = 1/(1+e⁻ᵗ)`; predicts
  probability, not a raw score. **Log loss** cost
  `−[y·log p + (1−y)·log(1−p)]`; convex → GD works. Gradient per point:
  `(σ(θᵀx) − y)·x` (same shape as linear regression's).
- **Decision boundary**: p ≥ 0.5 ⇒ positive class (θᵀx ≥ 0).
- **Softmax regression** (multinomial logistic): one score per class k,
  `pₖ = softmax(s(x))ₖ = exp(sₖ)/Σexp(sⱼ)`; loss = cross-entropy over
  classes; output is a probability distribution. Labels must be exclusive
  (one-hot). `LogisticRegression(multi_class="multinomial")` /
  `SGDClassifier(loss="log_loss")`.

## Key takeaways
- Scaling matters for every gradient-based method.
- Learning curves diagnose under/overfitting definitively.
- Regularisation (ℓ₂ Ridge / ℓ₁ Lasso / Elastic Net) trades bias for
  variance; tune α on validation.
- Logistic/softmax = linear model + sigmoid/softmax + log-loss — the
  probability-output pattern that generalises to neural nets.

## Notes
- The ℓ₁ vs ℓ₂ distinction (Lasso sparsity, Ridge shrinkage) carries into
  ch11's neural-net regularisation and into quantitative finance's
  penalised regressions.
- `add_dummy_feature` adds the bias column for manual normal-equation work.
