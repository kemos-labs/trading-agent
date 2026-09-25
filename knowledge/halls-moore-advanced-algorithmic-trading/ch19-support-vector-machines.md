# Ch19 — Support Vector Machines (SVM)

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 19.

## Motivation & framing
SVM = one of the best "out-of-the-box" **supervised binary classification** techniques. Set up:
labelled feature data x=(x₁..x_p), class label y ∈ {+1, −1} (e.g. spam/not, sentiment +/−).
It's a **non-probabilistic** classifier: a (possibly non-linear) separation plane partitions the
feature space into two subspaces; new objects are categorised by which side they fall on
(deterministic since feature values → position).
Key benefit: the separating boundary need not be a linear hyperplane — via the **kernel trick**
it handles non-linear decision boundaries needed for real data.

## Advantages
- **High-dimensionality**: works well in huge spaces (document/sentiment, dim ≥10⁶).
- **Memory-efficient**: only **support vectors** (points on the margin) matter for decisions; only
  those are stored/computed.
- **Versatility**: applying new kernels gives flexible decision boundaries.

## Disadvantages
- **p >> n**: if #features p >> #samples n, few effective support vectors → poor performance.
- **Non-probabilistic**: no probabilistic class-membership; a proxy = distance from decision
  boundary.

## Linear separating hyperplane
An affine (p−1)-dim space dividing R^p. Defined by:
**f(x) = β·x + β₀ = 0** (β·x = dot product / inner product).
- For an element x: sign(f(x)) decides the side (β·x+β₀ > 0 ⟹ class +1; < 0 ⟹ −1).

## Classification model
n training obs (x_i, y_i, y∈{−1,1}); goal: hyperplane separating them, then classify test x*
by sign of **f(x) = β₀ + Σ β_j x*_j**.
Separating hyperplanes aren't unique; want the **optimal** one.

## Maximal Margin Classifier (MMC)
- **Margin** = smallest perpendicular distance from training obs to the hyperplane.
- **Maximal Margin Hyperplane (MMH)** = separator with the **largest margin** (the mid-plane of
  the "widest block" that perfectly separates the classes).
- Relies only on **support vectors** = training points lying on the margin boundary (not the
  plane) — see points A,B,C. Consequence: MMH location is very sensitive to support-vector
  positions (a single added point can shift it a lot). Also why SVM is memory-light.
- Optimisation: max M subject to each obs being on the correct side ≥ distance M, and
  constrained so the hyperplane solution is bounded (β·β=1). Requires **perfect linear
  separability** — unrealistic for most real data.

## Support Vector Classifier (SVC) — soft margin
Relax perfect separation using **slack variables ε_i ≥ 0** and a **budget C ≥ 0**. Meaning:
- ε_i = 0 → obs correctly on the margin side; 0<ε_i<1 → wrong side of margin but right side of
  hyperplane; ε_i > 1 → wrong side of the hyperplane.
- **C controls violations**: C=0 forbids violations (→ MMC); larger C = wider margin, allows up
  to Σε_i ≤ C violations of the hyperplane.
- **C is the bias–variance control** (chosen by cross-validation): small C = low-bias /
  high-variance; large C = high-bias / low-variance.
- A test point is classified by sign of f(x*).

## Tree SVM — the kernel trick
For non-linear separation, enlarge the feature space via a transformation (e.g.
x → (x, x², …)) — linear in the expanded space, non-linear in the original — but this blows up
dimension. **Kernel**: the SVC optimisation only needs **inner products ⟨x_i, x_k⟩** between
training pairs (really only support vectors). Replace the inner product with a more general
kernel **K(x_i, x_k)** to get non-linear SVMs (still computationally efficient).

Common kernels:
- **Linear**: K = Σ x_ij·x_kj → recovers the SVC.
- **Polynomial of degree d**: K = (1 + Σ x_ij x_kj)^d → SVC in a higher-dim d-degree-polynomial
  feature space.
- **Radial**: K = exp(−γ Σ (x_ij − x_kj)²). **Localized**: if x* is far from x_i in Euclidean
  distance, K is tiny → that training obs barely influences placement of x*; only nearby points
  matter. (Popular; behaviour like local/near-neighbour.)

Formally: **SVM = support vector classifier with a non-linear kernel** (Vapnik originally;
Cortes for the modern soft-margin approach).

## Takeaways / pitfalls
- SVMs shine in high-dim, non-linear classification; memory-efficient (support vectors only).
- Avoid in low-sample/high-feature regimes (p >> n).
- The kernel confines computation to support-vector inner products — the computational
  advantage.
- C (budget/regularisation) is the key tuning knob → cross-validate.
- Later applied for document classification & sentiment (NLP chapter).