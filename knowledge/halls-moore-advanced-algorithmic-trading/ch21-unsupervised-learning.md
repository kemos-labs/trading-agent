# Ch21 — Unsupervised Learning (intro: PCA & K-Means)

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 21.

## Supervised vs unsupervised
- **Supervised**: feature/response pairs (x_i, y_i); training has *ground truth* labels; model
  p(y_i | x_i, θ); goal = predict response from features.
- **Unsupervised**: features x_i only, **no response labels**; no ground truth → interest in
  *structure of the features themselves*: do they form clusters/subgroups? Can the data be
  described in lower dimension? Models are of the form **p(x_i | θ)** (density estimation).

Motivations for unsupervised: labelling data is expensive/time-consuming; images, video, NLP
documents, gene data are **extremely high-dimensional** (needs many DoF → overfitting risk
for supervised). Downside: **no objective, widely-agreed performance metric** → assessment is
heuristic, case-by-case, subjective.

Uses: anomaly detection, purchase-habit analysis, recommendation systems, NLP. In quant
finance: **de-noising datasets, portfolio/asset clustering, market-regime detection, risk**.

## Curse of Dimensionality
High-dim data (e.g. 1080p image ≈ 2×10⁷ possible b/w images; ×2²⁴ colours). Even with huge
N, "training data cannot be expected to populate the space" → with p >> N there are large
feature-space regions about which we know nothing. → **dimensionality reduction**: describe key
variation with a lower-dimensional **manifold of dimension q < p** embedded in R^p
(linear PCA, non-linear kernel PCA).

## Principal Components Analysis (PCA)
Standard linear dimensionality-reduction tool for a set of correlated variables.
- **Orthogonal coordinate transformation** → new linearly **uncorrelated** variables:
  the **principal components**.
- PCs = **eigenvectors of the data covariance matrix**; mutually orthogonal (by construction);
  each explains successively less dataset variability. First few PCs usually capture a large
  fraction of variability → big dimension cut.
- Interpretation: a **change of basis**; subset of basis vectors spans a linear subspace within
  the feature space.
- For non-linear data: apply the **kernel trick** → (kernel) PCA in a higher-dim transformed
  space, then project back.
- In quant finance: **factor analysis** — reduce a large set of correlated stocks to a few
  latent factors/dimensions.

## Cluster Analysis & K-Means
Goal: assign each of N elements a cluster label, partitioning feature space into **K separate,
non-overlapping clusters**; unambiguous when subgroups are distinct, ambiguous when clusters
overlap.

**K-Means** (canonical, iterative):
1. Randomly assign every element to cluster k ∈ {1..K}.
2. Iterate: compute the **centroid** (mean vector) of each cluster.
3. Reassign each element to the cluster with the **nearest centroid** (Euclidean distance).
4. Repeat until centroids stop moving (within tolerance).

In quant finance: clustering finds assets with similar characteristics → **diversified
portfolios**; also **market-regime detection** → risk management tool.

## Takeaways / pitfalls
- No ground truth ⇒ performance assessment is heuristic (no single "best" unsupervised model).
- p >> N ⇒ curse of dimensionality ⇒ prefer PCA (or kernel PCA) before supervised fitting.
- PCA: uncorrelated, ordered-by-variance components from covariance eigenvectors.
- K-Means needs K chosen a priori and is sensitive to the random initial assignment
  (heuristic; e.g. pick K by elbow/regime reasoning); clusters may overlap in practice.
- Finance uses: de-noising, asset clustering for diversification, regime detection, risk.