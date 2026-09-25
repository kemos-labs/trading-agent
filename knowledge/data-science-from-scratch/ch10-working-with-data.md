# Ch10 — Working with Data

**Source:** Grus, *Data Science from Scratch*, Chapter 10.

## Purpose
Data munging: cleaning, exploring, and **dimensionality reduction** so raw
data becomes a usable matrix of features.

## Exploring one- and two-dimensional data
- One dimension: histogram, min/max, mean, variance, number of distinct
  values.
- Two dimensions: scatterplot + `correlation(x, y)` — always *look* first.
- The chapter repeats the book's discipline: **inspect distributions and
  relationships before modelling**.

## Cleaning and rescaling
- Real datasets have missing values, junk rows, and mixed types. Filter
  obviously-bad rows (e.g. blank salary), coerce types, decide on missing
  data.
- **Rescaling**: when features live on very different scales (salary in
  thousands vs experience in years), standardise each column to mean 0 /
  std 1:
  `rescaled = [(x − mean) / std for x in column]`.
  The book's `rescale()` maps each row so every *column* has mean 0 and std
  1. Needed before distance-based and gradient-based methods (k-NN ch12,
  logistic regression ch16) so no single feature dominates.

## Dimensionality reduction: PCA
- **Why**: high-dimensional data is sparse and distances are uninformative
  (ch12's curse of dimensionality); plotting is limited to 2–3 dims.
- **Principal Component Analysis (PCA)** finds the directions of greatest
  variance in the data.
  - **Center** the data: subtract the column means.
  - The **principal components** are the eigenvectors of the covariance
    matrix, ordered by eigenvalue (variance explained).
  - The first PC is the direction capturing the most variance; each
    subsequent PC is orthogonal and captures the next most.
- The book's from-scratch PCA:
  ```python
  def pca(data, k):
      # data rows are points; subtract vector_mean
      # compute covariance matrix, then its eigenvectors
      # return the k eigenvectors with largest eigenvalues
  def transform(v, components):  # project vector v onto components
      return [dot(v, direction) for direction in components]
  ```
- **Eigenvectors** via power iteration: repeatedly multiply a random vector
  by the matrix and normalise — converges to the top eigenvector; deflate to
  get the next.
- Result: project points onto the top-2 components and plot a 2-D view that
  preserves most variance (used for word embeddings in ch21).

## Key takeaways
- **Rescale before modelling** whenever features have different units or
  magnitudes — gradient descent converges faster and distances are
  meaningful.
- PCA = "find the few orthogonal directions of max variance, then project";
  eigenvalues rank the directions.
- Dimensionality reduction is the standard escape from the curse of
  dimensionality before distance-based methods.

## Notes
- Matrix covariance and eigenvector code is approximate (power iteration)
  but correct enough for teaching; production code would use
  sklearn's `PCA`/`SVD`.
- `rescale` is reused in ch16 before fitting logistic regression.
