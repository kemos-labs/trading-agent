# Ch17 — Decision Trees

**Source:** Grus, *Data Science from Scratch*, Chapter 17.

## Purpose
Interpretable classification: a tree of yes/no questions that partition data
into classes. Built greedily with **ID3** using **entropy**.

## Entropy — the split criterion
- **Entropy** of a labelled set S measures uncertainty:
  `H(S) = −Σ pᵢ log₂ pᵢ` (pᵢ = proportion of class i; 0·log 0 = 0).
  - All one class ⇒ H = 0; evenly split ⇒ H = 1; in between otherwise.
  - `entropy([0.5, 0.5]) == 1`; `entropy([1.0]) == 0`.
- **Partition entropy**: after splitting S into subsets S₁…Sₘ with
  proportions q₁…qₘ:
  `H = Σ qⱼ H(Sⱼ)` — the size-weighted average of the subsets' entropies.
  Lower = better split (subsets are purer).
- **Pitfall**: splitting on an attribute with many values (e.g. SSN) gives
  one-point subsets, entropy ≈ 0 — pure overfitting. Bucket or avoid
  high-cardinality attributes.

## ID3 algorithm (greedy)
1. If all data share one label → **leaf** with that label.
2. If no attributes remain → **leaf** with the most common label.
3. Else try partitioning on each attribute; pick the one with the **lowest
   partition entropy**; recurse on each subset with the remaining
   attributes.
- Greedy: chooses the best split now; may miss a better tree whose first
  split looks worse (accepted trade-off for simplicity).

## Representation
- `Leaf(value)` or `Split(attribute, subtrees, default_value)`:
  ```python
  class Leaf(NamedTuple): value
  class Split(NamedTuple):
      attribute: str
      subtrees: dict          # value -> subtree
      default_value: Any = None  # for unseen attribute values
  ```
- **classify**: descend `Split`s by the input's attribute value; hit a
  missing value → return `default_value` (the most common label at build
  time).
- **build_tree_id3**: stop on pure labels or exhausted attributes; else
  pick min-entropy attribute, recurse.

## Worked example (hiring)
- Attributes: level, language, tweets, phd → did_well.
- First split on `level` (lowest entropy ~0.69); `Mid` → True immediately;
  `Senior` splits on `tweets` (0.4 → 0.0 entropy: tweet/no-tweet perfectly
  separates); `Junior` splits on `phd`. Resulting tree is small, pure, and
  fully explains the 14 candidates.

## Key takeaways
- Decision trees = greedy entropy-minimising partitioners, perfectly
  interpretable.
- Entropy (not error rate) drives split choice; weight subset entropies by
  size.
- High-cardinality attributes overfit — restrict/bucket them.
- `default_value` handles unseen values gracefully.

## Notes
- No pruning or impurity alternatives (Gini) here — that's a scikit-learn
  production concern (ch27).
- Ties naturally to ch11's overfitting: an unconstrained tree will keep
  splitting until every leaf is pure — a memorised training set.
