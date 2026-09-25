# Ch04 — Linear Algebra

**Source:** Grus, *Data Science from Scratch*, Chapter 4.

## Purpose
The minimum linear algebra needed for the book: **vectors** (lists of
numbers) and **matrices** (lists of vectors), implemented from scratch in
pure Python.

## Vectors
- A vector is `List[float]` — a list of numbers. In data science, a vector
  is one *data point*: each position is a feature/attribute.
- **Vector addition** (componentwise): `[v1[i] + w1[i] for i in range(len(v1))]`.
- **Scalar multiply**: `[scalar * v[i] for i in range(len(v))]`.
- **Dot product** — the workhorse:
  `dot(v, w) = sum(v_i * w_i for i in range(len(v)))`.
  - Length of a vector: `sum_of_squares = dot(v, v)`; `magnitude = sqrt(sum_of_squares)`.
  - Distance between two vectors: `sqrt(sum((v_i - w_i)**2))` (Euclidean).
- **Vector mean**: the average vector of a collection (componentwise mean) —
  `vector_mean(vectors)`.
- **Cosine similarity** — the angle between two vectors, not just their
  distance:
  `cosine_similarity(v, w) = dot(v, w) / (magnitude(v) * magnitude(w))`.
  Value in [−1, 1]; 1 = same direction. Used for user/interest similarity
  (ch23) and word embeddings (ch21).
- **dot product as "similarity"**: when both vectors are 0/1 indicator
  vectors, `dot(v, w)` counts shared features (used for shared interests).

## Matrices
- A matrix is `List[List[float]]`: `A[i][j]` = element in row i, column j.
  In data science: rows = data points, columns = attributes.
- **Shape**: `num_rows = len(A)`, `num_cols = len(A[0])`.
- **Matrix construction** helpers: `shape`, `get_row`, `get_column`,
  `make_matrix(num_rows, num_cols, entry_fn)` — build a matrix from a
  function `entry_fn(i, j)`.
- The book doesn't implement matrix multiplication here (it appears in the
  deep-learning chapter via tensors); the emphasis is on the *shapes* and
  the row/column access patterns used by every later algorithm.

## Why it matters
- Almost every algorithm in the book is expressed in terms of vectors:
  distances (k-NN, ch12), dot products (regression predictions, ch14–16;
  neural nets, ch18), cosine similarity (recommendations, ch23).
- The "data as matrix" framing (rows = points, columns = features) is the
  conceptual backbone for the whole book.

## Key takeaways
- Dot product = projection/similarity; use it to combine features with
  weights (predictions) or to compare vectors (similarity).
- Euclidean distance works in any dimension, but see the curse of
  dimensionality (ch12) for why high-D distances mislead.
- Normalise vectors before comparing directions (cosine) when magnitude
  doesn't matter.

## Notes
- Matrix multiplication and inversion are deferred/elided; the book uses
  gradient descent instead of closed-form linear algebra (ch14–15).
- Known pitfalls: Python lists alias when reused — the book uses
  comprehensions to build fresh vectors; `row[:] = ...` slice assignment
  mutates in place (emphasised in ch18).
