# Ch08 — Dimensionality Reduction

**Source:** Géron, *Hands-On Machine Learning*, Chapter 8.

## Purpose
Fight the **curse of dimensionality**: high-D spaces are sparse, distances
become uninformative, and training slows. Reducing dimensions speeds
training and enables visualisation — but loses information and adds pipeline
complexity, so **try the full data first**.

## The manifold assumption
- Real high-D data (e.g. digit images) usually lies near a much
  lower-dimensional **manifold** (a smoothly embedded subspace).
- The manifold hypothesis: the task becomes simpler in manifold
  coordinates — but not always (a split at x₁ = 5 is simple in 3D, complex
  when unrolled). Reduction speeds training; it doesn't guarantee better
  solutions.

## PCA
- **Idea**: project onto the hyperplane that preserves maximum variance
  (= minimum mean squared projection distance).
- **Principal components**: orthogonal unit vectors (c₁, c₂, …) capturing
  successively maximal variance. From **SVD**: center X, then
  `U, s, Vt = np.linalg.svd(X_centered)`; PCs = rows of Vt.
- **Projection**: `X_proj = X_centered @ W_d` (first d PCs as columns).
- **Choosing d**: `explained_variance_ratio_`; pick d for ~95% cumulative
  variance (or a knee in the curve). Inversely recoverable:
  `X_recovered ≈ X_proj @ W_dᵀ` (loses only the discarded variance).
- **Variants**: `IncrementalPCA` (out-of-core, `partial_fit`, works on
  `np.memmap`), `PCA(svd_solver="randomized")` (fast approximate for big m/n;
  O(m·d²)+O(d³)), `KernelPCA` (nonlinear via kernel trick).
- PCA is linear — fails on curved manifolds like the Swiss roll.

## Random projection
- Project with a random matrix P of shape [d, n], entries ~ N(0, 1/d).
  No training, data-independent.
- **Johnson–Lindenstrauss lemma**: d ≥ 4·log(m)/(½ε² − ⅓ε³) dimensions
  suffice to preserve all pairwise distances within tolerance ε with high
  probability (independent of n!). `johnson_lindenstrauss_min_dim`.
- `GaussianRandomProjection` / **`SparseRandomProjection`** (sparse matrix,
  ~25 MB vs ~1.2 GB, 50% faster, keeps sparsity; density default 1/√n) —
  prefer the sparse one for large/sparse data.

## Manifold learning (nonlinear, for visualisation)
- **LLE**: for each point, reconstruct it as a linear combo of its k
  nearest neighbours (weights W); then find low-D coordinates zᵢ
  preserving those local relationships. Unrolls the Swiss roll; O(dm²)
  doesn't scale.
- **Others**: MDS (preserve pairwise distances), Isomap (preserve
  geodesic distances on a neighbour graph), **t-SNE** (keep similar close,
  dissimilar apart; amplifies clusters — great for visualising MNIST
  clusters, not for real reduction), LDA (supervised: axes that separate
  classes — good pre-classification reduction).

## Key takeaways
- PCA via SVD is the default; pick d by explained variance.
- Curse of dimensionality is real: neighbour distances stop discriminating
  (ch3/ch9 of Grus show the ratio min/avg → 1).
- Manifold methods (LLE/t-SNE) are for understanding, not production
  pipelines.
- Random projection is the cheap, surprisingly effective large-data trick.

## Notes
- PCA on 154 dimensions captures 95% of MNIST variance (784 → 154).
- Randomised/incremental PCA + random projection are the scalable choices
  when data doesn't fit memory.
