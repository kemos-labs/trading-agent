# Ch22 — Unsupervised Clustering with K-Means (incl. OHLC regime detection)

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 22.

## K-Means clustering (recap + formal)
Clustering = partition observations into subgroups so points *within* a cluster are similar and
*different* from points in other clusters. K-Means is a **hard clustering** technique: every
observation is forced into exactly one of **K non-overlapping clusters** (contrast soft/
probabilistic clustering). Must pre-specify K.

**Objective — minimise Within-Cluster Sum of Squares (WCSS / WCV):**
min over cluster index sets S₁..S_K of  Σ_{k=1..K} Σ_{i∈S_k} ‖x_i − μ_k‖²
where μ_k = mean feature vector (centroid) of cluster k. This is a hard global minimisation
→ not solvable globally; heuristic gives a **local optimum**.

**K-Means algorithm (two steps, iterated):**
1. Randomly assign each observation to cluster k ∈ {1..K}.
2. (a) Compute each cluster's centroid μ_k (mean of its members).
   (b) Reassign each observation to the *closest* centroid (Euclidean distance).
3. Repeat until centroids stop changing.

Because initial assignment is random, the found local optimum depends on it → **run multiple
times (sklearn default: 10) and keep the best local optimum** (lowest WCSS).

## Known flaws (important for finance)
- **Low SNR in financial data**: forced to produce K clusters even if data is pure noise → the
  "clusters" may be artifacts, not true separated distributions.
- **Outliers** get assigned to a cluster anyway (hard boundary) — bad ticks, flash crashes.
- **Sensitive to dataset variations**: splitting one series in two and fitting K-Means with same
  K on each half commonly yields *different* cluster assignments for similar data → robustness
  question on small samples; more data helps.

More sophisticated (beyond scope): Gaussian Mixture Models (soft), Vector Quantisation,
autoencoders / Restricted Boltzmann Machines (deep-learning alternatives).

## Simulated-data demo
Sample 3 separate 2D Gaussians (100 pts each), fit KMeans with K=3 and K=4.
- K=3: largely recovers the three clusters (hard boundary trouble only near overlaps).
- K=4: **splits one true Gaussian into two** (yellow/red) → wrong; demonstrates K choice
  matters hugely for interpretation.
- Lesson: choice of K has significant implications for usefulness, esp. in trading.

## OHLC clustering application (S&P500, 2013–2015)
Goal: identify **market regimes** from daily bars. Normalisation: High, Low, Close each divided
by **Open** → 3 dims (H/O, L/O, C/O); automatically accounts for splits/dividends & allows
like-for-like candle comparison. (4 dims → 3.)
- Download 2 years S&P500 OHLC; fit KMeans (K=5); colour 3D scatter of (H/O, L/O, C/O).
- Plot candles ordered by cluster membership, with blue dotted cluster boundaries
  (`clust_change = Cluster.diff()` finds boundary indices).
- **Follow-on matrix**: K×K matrix where element (i,j) = % frequency that *tomorrow's* cluster
  is j given *today's* cluster i (built with `shift`, `value_counts` on (today,tomorrow)
  tuples). Shows **uneven transitions** — some candles more likely to follow others → motivates
  predictive trading strategies around cluster membership.

Findings: majority of bars cluster near (1.0,1.0,1.0) (normal low-volatility days); distinct
clusters for big-gain days (C/O high) and big-dip days (L/O low); membership highly unequal
(calm days dominate).

## Cautions / next steps (explicitly in book)
- All analysis is **in-sample**; using clusters predictively assumes the cluster *distribution*
  stays similar over time → prefer a **rolling / online clustering** tool.
- The follow-on matrix must not drift too often (else poor predictive power) but must update
  often enough to detect **market regime changes**.
- K choice is asset-dependent and unclear — needs further experimentation (elbow etc.).

## Takeaways / pitfalls
- Hard clustering + K pre-specified; local optimum depends on initial random assignment → run
  several restarts.
- Financial data low SNR → clusters may be noise artifacts; outliers always assigned.
- Normalise OHLC by Open before clustering (accounts for splits/dividends).
- Cluster transitions (follow-on matrix) are a *starting point* for regime-aware strategies —
  must be validated out-of-sample / rolling.