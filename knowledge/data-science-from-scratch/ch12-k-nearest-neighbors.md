# Ch12 — k-Nearest Neighbors

**Source:** Grus, *Data Science from Scratch*, Chapter 12.

## Purpose
The simplest predictive model: classify a new point by letting its nearest
labelled neighbours vote. Requires only a distance notion and the assumption
that *close points are similar*.

## The algorithm
```python
def knn_classify(k, labeled_points, new_point):
    by_distance = sorted(labeled_points,
                         key=lambda lp: distance(lp.point, new_point))
    k_nearest_labels = [lp.label for lp in by_distance[:k]]
    return majority_vote(k_nearest_labels)
```
- **`majority_vote`** breaks ties by dropping the *farthest* neighbour and
  re-voting until a unique winner emerges (reducing k one at a time is
  guaranteed to terminate).
- Choosing **k**: too small → outliers dominate; too large → you're just
  predicting the dataset's most common class. In production, choose k with a
  held-out **validation set**.
- Model makes **no mathematical assumptions** and no heavy training — the
  "training" is just storing the points (lazy learning).

## Example: Iris dataset
- 150 flowers, 4 measurements (sepal/petal length & width), 3 species.
- Parse into `LabeledPoint(measurements, label)`; split 70/30; k=5 classifies
  almost perfectly (one versicolor misread as virginica).
- Lesson: scatterplotting pairs of measurements first reveals the species
  cluster cleanly → plot before modelling.

## The curse of dimensionality — the chapter's key warning
- Simulated experiment: 10,000 random pairs of points in the d-dimensional
  unit cube, for d = 1..100. Track **avg distance** and **min distance**.
- As d grows:
  - average distance between random points grows;
  - crucially, the **ratio min/avg distance → 1**: the closest points are no
    longer much closer than average.
- Implication: in high dimensions "nearest" neighbours are barely nearer
  than random points, so their labels carry little signal (unless the data
  has strong low-dimensional structure).
- Also: 50 random points cover the unit interval fine, the unit square
  sparsely, the unit cube sparser still — high-D space is mostly empty;
  you'd need exponentially more data to fill it.
- **Fix**: do dimensionality reduction (PCA, ch10) before nearest-neighbour
  modelling in high dimensions.

## When to use / not use k-NN
- **Use**: simple, no assumptions, works well when data is low-dimensional
  and genuinely clustered.
- **Not for**: high-dimensional data (curse), or when you need to *explain*
  drivers — k-NN is a black box ("my neighbors vote" doesn't say why).

## Key takeaways
- k-NN = majority vote of the k closest points, with tie-breaking by
  dropping the farthest.
- Hyperparameter k must be tuned on validation data.
- In high dimensions, distances stop discriminating — reduce dimensions
  first.

## Notes
- Uses `distance` from ch4 (Euclidean) and `split_data` from ch11.
- The ratio min/avg ≈ 1 result is the quantitative face of the curse: keep
  it in mind for any distance-based method (clustering ch20, recommender
  similarities ch23).
