# Ch09 — Unsupervised Learning Techniques

**Source:** Géron, *Hands-On Machine Learning*, Chapter 9.

## Purpose
Unlabelled data: clustering (k-means, DBSCAN), density estimation + anomaly
detection (Gaussian mixtures). LeCun's framing: unsupervised is the cake,
supervised the icing, RL the cherry.

## k-means
- Algorithm: pick k centroids (random instances) → assign each instance to
  the nearest centroid → recompute centroids as means → repeat until
  centroids stop moving. Guaranteed finite convergence (MSE to centroids
  only decreases). Complexity O(m·k·n) — fast.
- **Hard vs soft clustering**: `transform()` returns distances to every
  centroid — usable as k-dimensional feature (nonlinear dim-reduction) or
  RBF-style affinity features (used for geo clusters in ch2).
- **Choosing k**: use **inertia** (sum of squared distances to centroids)
  + **silhouette score**; look for an elbow / peak. k-means can't find the
  right k itself.
- **Pitfalls**: bad init → local optima (run several seeds, or k-means++);
  centroids ≠ cluster membership on elongated/uneven blobs; sensitive to
  scaling (standardise first); degenerate solutions (empty clusters).
  KMeans algorithm converges to local minima — inertia can't tell you
  k is right.
- Uses: customer segmentation, image colour quantisation (k=5 recolors a
  photo), semi-supervised label propagation, anomaly detection (low
  affinity).

## DBSCAN
- Density-based: instances within distance ε of each other form clusters;
  points with fewer than `min_samples` neighbours in ε are **noise**.
- No k needed; finds arbitrary-shaped clusters; robust to outliers;
  **density-based** so it handles non-convex clusters k-means can't.
- **Choosing ε**: k-distance graph (sorted distance to kth neighbour; look
  for the knee).
- Complexity O(m²) naive (metric-tree indexing helps). `eps`,
  `min_samples` are the knobs. Good default alternative to k-means when
  clusters are irregular or data has outliers.

## Gaussian mixture models (GMM)
- Model data as a weighted sum of k Gaussians with means/covariances;
  trained by **EM** (expectation–maximisation): assign soft responsibilities
  (E step), re-estimate parameters (M step), iterate.
- Soft clustering via `predict_proba`; **generative**: `sample()` new
  instances; **density estimation** via `score_samples()` (log-PDF).
- **Choosing k**: use **BIC/AIC** — `BIC = log(m)·p − 2·log ℒ`,
  `AIC = 2p − 2·log ℒ` (p = #params, ℒ = max likelihood) — pick the model
  minimising the criterion (BIC tends simpler; inertia/silhouette don't
  work for GMMs with nonspherical clusters).
- **Covariance constraints**: `covariance_type` = "full" (any shape; costly
  O(kmn²+kn³)) | "spherical" | "diag" (axes-parallel ellipsoids) | "tied"
  (shared covariance) — reduce parameters when data/EM struggles.
- **Anomaly detection**: instances in low-density regions (below a density
  percentile threshold, e.g. 2nd) are anomalies — tune threshold via the
  precision/recall trade-off. Novelty detection = trained on clean data;
  anomaly detection assumes contamination.
- **GMM pitfall**: outliers bias the model's view of normality — fit, remove
  extreme outliers, refit; or use robust covariance (EllipticEnvelope).

## Key takeaways
- k-means: fast, spherical, needs k (inertia/silhouette). DBSCAN: arbitrary
  shapes, no k, noise-labelled, ε-sensitive. GMM: soft, generative, density
  estimation + anomaly detection, k via BIC/AIC.
- All three are sensitive to feature scaling.
- Clustering = the engine for segmentation, quantisation, label
  propagation, and unsupervised feature engineering.

## Notes
- Anomaly detection connects to ch17 autoencoders (reconstruction error as
  anomaly score) — same "learn normal, flag deviations" philosophy.
- In finance: regime detection, outlier/fraud detection, and
  feature-generation all use these tools (see hmm-regime-detection skill).
