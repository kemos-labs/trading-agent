# Ch23 — Recommender Systems

**Source:** Grus, *Data Science from Scratch*, Chapter 23.

## Purpose
Recommend items (interests, movies) users will like, from sparse
user–item preference data. Three approaches: user-based collaborative
filtering, item-based collaborative filtering, and matrix factorisation.

## The data
- Binary matrix (users × interests) of 0/1 likes, or numeric ratings
  (MovieLens 100k: 943 users × 1682 movies, ratings 1–5).
- **Cosine similarity** (ch4) measures similarity between users (rows) or
  interests (columns) — dot product of indicator vectors counts shared
  likes, normalised by magnitudes.

## User-based collaborative filtering
- For user u: find the most similar *other* users (cosine > 0, sorted);
  score each candidate item by the **sum of similar users' similarities**
  who like it; sort and recommend the top new items.
- Weights aren't meaningful — only ordering matters.
- **Fails at scale (curse of dimensionality, ch12)**: with thousands of
  items, most users' vectors are nearly orthogonal — the "most similar"
  shopper on Amazon isn't similar at all. User-based CF breaks down when
  item counts grow.

## Item-based collaborative filtering
- Transpose the matrix (rows = interests, columns = users); compute
  **interest–interest** similarity: two interests are similar if the *same
  users* like both.
- Recommend by summing the similarities of interests similar to the user's
  current interests.
- **Scales better**: item–item similarity is more stable than user–user
  (item neighbourhoods change slowly); this is the classic Amazon approach.

## Matrix factorisation (MF)
- **Idea**: assume users and items have hidden **latent "types"**
  (dimension-k vectors); ratings ≈ `user_matrix @ item_matrix.T`
  (users×k times k×items). Learning the factors = factorising the sparse
  ratings matrix — the same latent-vector philosophy as word embeddings
  (ch21).
- **Training** (the book's implementation):
  - Split ratings into train (70%) / validation (15%) / test (15%).
  - `dot(u, v) = Σ factors` predict a rating; use **gradient descent**
    (ch8) on the squared error of *known* ratings, taking gradient steps in
    both `u` and `v` vectors; regularisation terms keep factors bounded.
  - Iterate over epochs; on validation, pick the number of factors/epochs
    that generalise best; finally score on test with RMSE (book gets
    ~1.10–1.13 — decent for a from-scratch MF).
- **Cold-start problem**: new users/items have no ratings to factorise —
  MF can't recommend for them (fall back to popularity/other signals).

## Key takeaways
- Collaborative filtering = "similar people's likes" (user-based) or
  "similar items" (item-based); item-based survives scale better.
- MF = learn latent user/item vectors so that `u·v ≈ rating`; train with
  SGD on observed ratings, validate to pick dimensionality.
- Cold start and sparsity are the structural limits of all three; the book's
  train/validation/test split is the correct discipline.

## Notes
- MovieLens IDs are non-consecutive — the book maps them to dense indices /
  strings to avoid wasted dimensions.
- Production: `surprise`/`implicit`/`lightfm` libraries (ch27).
