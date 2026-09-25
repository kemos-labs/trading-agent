# Ch05 — Support Vector Machines

**Source:** Géron, *Hands-On Machine Learning*, Chapter 5.

## Purpose
SVM: large-margin classification/regression. Great for small-to-medium
nonlinear datasets; doesn't scale to huge data.

## Linear SVM & margins
- Idea: fit the **widest possible street** between classes (large-margin
  classification); the decision boundary is fully determined by the
  instances on the street's edge — the **support vectors**. Instances off
  the street don't affect the boundary.
- **Sensitive to feature scales** — always `StandardScaler` first.
- **Hard margin**: all instances strictly off the street on the correct
  side — only works if linearly separable and fragile to outliers.
- **Soft margin**: allow **margin violations**, balanced by hyperparameter
  **C**. Small C ⇒ wider street, more violations, less overfitting; large C
  ⇒ fewer violations, more overfit. Overfitting ⇒ reduce C.

## Nonlinear SVMs
- **Polynomial features** can make data separable (add x², etc.) — works
  with any algorithm, but explodes combinatorially.
- **Kernel trick** (SVC `kernel="poly"`): get the effect of high-degree
  polynomial features WITHOUT adding them (no explosion). `coef0` balances
  high- vs low-degree influence.
- **Similarity features**: Gaussian RBF `exp(−γ||x−landmark||²)` per
  landmark; landmark-per-instance ⇒ m features, linearly separable, but
  expensive.
- **Gaussian RBF kernel** (`kernel="rbf"`, default): same effect without
  materialising features. **γ** acts like a regulariser: small γ ⇒ smooth
  boundary; large γ ⇒ wiggly. Overfit ⇒ reduce γ; underfit ⇒ increase γ.

## SVM regression (SVR)
- SVR fits as many instances as possible *within* an ε-wide tube around the
  predictions; margin violations outside the tube are penalised (C).
  `LinearSVR`/`SVR`; wider tube ⇒ fewer support vectors, smoother model.

## Under the hood
- **Hard margin objective**: minimise ½wᵀw subject to
  `t⁽ⁱ⁾(wᵀx⁽ⁱ⁾ + b) ≥ 1` (t = ±1). Smaller ‖w‖ ⇒ wider margin; b shifts
  the margin but doesn't change its size.
- **Soft margin**: add slack ζ⁽ⁱ⁾ ≥ 0 and minimise
  `½wᵀw + C·Σζ⁽ⁱ⁾` subject to `t⁽ⁱ⁾(wᵀx⁽ⁱ⁾+b) ≥ 1 − ζ⁽ⁱ⁾`.
- Both are convex **quadratic programs** (QP); solvable off-the-shelf, or
  via gradient descent on the **hinge loss**
  `max(0, 1 − t·s)` (linear penalty) / squared hinge (quadratic, outlier-
  sensitive but faster on clean data).
- **Dual problem**: equivalent optimisation over α⁽ⁱ⁾ whose solution makes
  predictions depend only on dot products of training instances —
  `w = Σα⁽ⁱ⁾t⁽ⁱ⁾x⁽ⁱ⁾`; this is exactly what enables the kernel trick
  (replace xᵀx by K(x,x′)).
- **Kernelised SVMs are inefficient on large training sets** (fitting is
  between O(m²) and O(m³)); use LinearSVC or SGD for large data. Online SVM
  exists (SGDClassifier with hinge loss, `partial_fit`).

## Key takeaways
- SVM = max-margin classifier; C controls the margin-vs-violations trade.
- Kernel trick = implicit feature expansion via dot products — poly, RBF,
  sigmoid kernels.
- γ (RBF) and degree (poly) are regularisers; tune with (randomised) search.
- Prefer LinearSVC at scale; SVC for small nonlinear data.

## Notes
- The dual formulation + kernel trick is the conceptual bridge to kernel
  methods in finance (e.g. SVR for volatility forecasting).
- Probability outputs need `probability=True` (extra CV fit, slower).
