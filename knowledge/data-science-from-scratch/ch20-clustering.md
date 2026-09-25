# Ch20 — Clustering

**Source:** Grus, *Data Science from Scratch*, Chapter 20.

## Purpose
Unsupervised learning: group unlabelled points into clusters. Two
algorithms: **k-means** (flat, spherical) and **bottom-up hierarchical
clustering** (tree).

## k-means
- **Idea**: choose k cluster centres (means); assign each point to the
  nearest centre; recompute each centre as the mean of its assigned points;
  repeat until assignments stabilise.
```python
class KMeans:
    def __init__(self, k): self.k = k
    def train(self, inputs):
        # 1. pick k random distinct points as initial means
        # 2. loop:
        #    assign each point to closest mean (argmin distance)
        #    recompute means = vector_mean of assigned points
        #    stop when means stop changing (or max iterations)
    def classify(self, input): return argmin(distance(input, mean))
```
- **Choice of k**: not known a priori. The book's pragmatic approach: choose
  k so that adding another cluster doesn't dramatically reduce total
  squared distances — "the value of k where the curve starts to flatten"
  (an elbow heuristic).
- **Sensitivity to init**: random starting means can give bad local optima;
  results vary with the seed. Run multiple times / pick good seeds in
  practice (k-means++).
- **Example: image compression** — cluster all pixel RGB values into 5
  colours, then recolor each pixel with its cluster's mean. 5-means decolors
  a photo into a palette poster — a neat demonstration that clustering finds
  dense regions of a distribution.

## Bottom-up (agglomerative) hierarchical clustering
- Start with each point as its own leaf cluster; repeatedly merge the two
  **closest** clusters until one giant cluster remains; record **merge
  order**; unmerge to get any desired number of clusters.
- Cluster distance with an aggregation function over all pairwise point
  distances:
  - `min` (single linkage): merges clusters closest to touching — produces
    **chain-like**, elongated clusters;
  - `max` (complete linkage): merges the pair that fits in the smallest
    ball — **tight, spherical** clusters (looks like k-means output);
  - `average`: in between.
- `generate_clusters(base, n)`: repeatedly split the cluster with the
  *smallest* merge order (most recently merged) until n clusters remain.
- **Efficiency warning**: the naive version recomputes every pairwise
  distance at every merge — precompute the distance matrix and remember
  prior results for production use.

## Comparing the two
- k-means: fast, requires choosing k up front, assumes convex/spherical
  clusters.
- Hierarchical: no k needed (choose after by unmerging), gives a dendrogram
  of structure, but O(n²)-ish and linkage choice changes the result
  dramatically.

## Key takeaways
- k-means = assign-to-nearest-mean, recompute means, repeat; sensitive to k
  and init.
- Hierarchical = merge closest clusters; min-linkage → chains, max-linkage →
  tight balls.
- Clustering is unsupervised: no labels to validate against — inspect the
  clusters' meaning yourself.

## Notes
- Uses `vector_mean` (ch4) and `distance` (ch4); 3-means on the user-
  location data groups users into city clusters.
- scikit-learn's `KMeans`, `Ward`, and SciPy's hierarchy are the production
  equivalents (ch27).
