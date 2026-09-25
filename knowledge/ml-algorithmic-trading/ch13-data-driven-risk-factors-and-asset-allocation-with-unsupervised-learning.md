# Ch13 — Data-Driven Risk Factors and Asset Allocation with Unsupervised Learning

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 13.

## Purpose
Unsupervised learning for markets: PCA and factor analysis to extract latent risk factors, clustering to group assets/similarity, and dimensionality reduction for feature engineering — plus hierarchical risk parity (HRP) for robust allocation.

## PCA for risk factors
- Eigen-decompose the covariance (or correlation) matrix: principal components = orthogonal directions of maximum variance; eigenvalue = variance explained.
- **Factor interpretation**: first PCs of equity returns act like market/industry factors; loadings identify systematic exposures (cf. GKX autoencoder risk factors in ch20, de Prado ch16).
- **Use**: risk decomposition, feature decorrelation before regression, visualization (2D projections).
- Standardize features (correlation vs. covariance matters when scales differ); decide component count by explained-variance elbow or eigenvalue > 1.

## Clustering assets
- **k-means**: partition into k clusters by Euclidean distance in feature space; scale features; choose k by inertia/elbow or silhouette score.
- **Hierarchical clustering**: dendrogram of asset similarity — groups assets by return correlation distance; no need to fix k; basis for HRP.
- **Similarity metric for assets**: correlation distance d = √(0.5·(1 − ρ)) maps correlations to a Euclidean-like metric.
- Use clusters for: diversification-aware portfolio construction, regime identification, peer-group relative-value analysis.

## Dimensionality reduction
- PCA, t-SNE, UMAP for visualization and as features; autoencoders (ch20) are the nonlinear generalization.
- t-SNE preserves local structure (good for clusters), UMAP is faster and preserves more global structure; both are for exploration, not model features.

## Hierarchical Risk Parity (HRP)
- **Motivation**: Markowitz optimization (ch5) is unstable with estimated inputs — HRP is the robust, purely data-driven alternative.
- **Three stages** (full detail in `advances-financial-ml` ch16):
  1. Build a correlation-distance matrix; hierarchical clustering → dendrogram.
  2. Quasi-diagonalize: reorder assets along the dendrogram.
  3. Recursive bisection: split the ordered list in half repeatedly, allocate risk inversely proportional to cluster variance within each branch.
- Result: weights that are long-only, diversification-aware, and robust to estimation error — no optimizer, no inverse-covariance blow-up.

## Practical notes
- Unsupervised outputs are *features and structure*, not predictions — validate them downstream with supervised evaluation.
- Covariance estimation is noisy: use shrinkage (Ledoit-Wolf) or factor models before PCA/clustering.
- Clustering needs the right distance (correlation, not raw return distance) and careful scaling.

## Key takeaways
- PCA/clustering turn a large asset universe into interpretable structure: factors and groups.
- HRP is the practical robust allocation method — strongly preferable to unstable mean-variance on noisy estimates.
- Unsupervised learning is a feature-engineering and risk-management layer; supervised models still do the predicting.
