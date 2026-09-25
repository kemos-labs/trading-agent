# Ch17 — Linear Regression (supervised, sklearn)

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 17.

## Probabilistic formulation
Formalize linear regression under a probabilistic supervised-learning view so extensions (e.g.
SVMs) fit the same framework.

**Model (multiple linear regression)**:
**y = β^T x + ε**, with β, x ∈ R^(p+1) (the "+1" admits the **intercept**; x=(1, x₁,…,x_p), the
lone "1" is a notation trick for the intercept), and ε ~ N(μ, σ²). ε is the difference between
predicted and actual values.

Interpreted as a **joint-probability / conditional-probability (CPD) model**:
p(y | x; θ) with θ = (β, σ²). Assumptions:
- Mean is linear: E[y|x] = β^T x.
- **Fixed variance**: σ²(x)=σ² constant (does NOT depend on x). This constant-variance is
  visible in the 3-D density plot (spread of the normal does not widen with x).

**Non-linear extension**: choose a feature map φ so y is linear in *expanded* features but
nonlinear in the original x; e.g. x=(1,x₁,x₂,x₃) → add higher-order terms x₁², x₁x₂, etc. Still
linear in β — the basis of the **kernel trick** in SVMs.

## Maximum Likelihood Estimation (MLE) → OLS
MLE = what parameters most likely *generated* the data. We maximise the likelihood
∏ p(y_i|x_i;θ) — equivalently maximise the **log-likelihood** (product → sum via log),
equivalently minimise the **Negative Log-Likelihood (NLL)**:
**NLL = (1/2σ²) Σ(y_i − β^T x_i)² + const**.

Derivation steps:
1. Expand NLL using the normal-density formula.
2. Logs → reformulate as **Residual Sum of Squares (RSS) = Σ residuals²** (SSE equivalent).
3. Write residuals in matrix form using the N×(p+1) data matrix **X**.
4. **Differentiate RSS w.r.t. β, set to 0 = 0**.
5. Solve → **β̂_OLS = (XᵀX)⁻¹ Xᵀ y**, the Ordinary Least Squares estimate.

**Key condition**: XᵀX must be **positive-definite** → requires *more observations than
dimensions* (N > p+1). In high-dimensional data (N ≤ p) no solution exists — the matrix
equation breaks.

## Scikit-Learn implementation (univariate simulation)
- Simulate N=500: features X ~ N(0,10), true intercept α=2, slope β=3, noise ε~N(0, 30²)
  → y = α + βX + ε.
- Split: 400 train / 100 test.
- `lr_model = linear_model.LinearRegression(); lr_model.fit(X_train, y_train)`.
- Read params: `lr_model.intercept_`, `lr_model.coef_[0]` (coef is an array, generalises to
  multivariate); predict on test: `lr_model.predict(X_test)`.
- API is generic and identical across later models (Random Forests, SVMs, boosted trees).
- Contrast: this returns a *point* estimate (a line) — compare to the Bayesian linear
  regression chapter which returns a *posterior distribution* of lines (uncertainty).

## Notes / sources
- James, Witten, Hastie, Tibshirani (2013) — intro incl. shrinkage/regularisation,
  dimensionality reduction.
- Hastie et al (2009), Murphy (2012) — rigorous, Bayesian + MLE-via-OLS + regularisation.
- Kuhn & Johnson (2013) — high-collinearity/real-world, PLS.

## Takeaways / pitfalls
- Constant-variance (homoscedastic) + linearity are the two central assumptions.
- OLS = MLE for normal linear regression; requires XᵀX positive-definite (N > p).
- High-dimensional (p ≥ N) breaks OLS → motivates regularisation/shrinkage (later).