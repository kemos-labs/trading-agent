# Ch01 — The Machine Learning Landscape

**Source:** Géron, *Hands-On Machine Learning*, Chapter 1.

## What ML is
Three definitions, from loose to rigorous:
- Arthur Samuel (1959): "field of study that gives computers the ability to
  learn without being explicitly programmed."
- Tom Mitchell (1997): "A computer program is said to learn from experience
  E with respect to some task T and some performance measure P, if its
  performance on T, as measured by P, improves with experience E."
- Data alone (e.g. downloading Wikipedia) is not learning — learning is
  improvement on a task from experience.

## Why ML (vs hand-coded rules)
- Traditional programming fails when: solutions need long lists of
  fine-tuned rules (spam filter); no known algorithm exists (speech
  recognition); the environment fluctuates and rules go stale (spammers
  adapt); or you want insights/mining from large data.
- ML adapts automatically (spammers writing "For U" after "4U" is blocked).

## Types of ML systems (three orthogonal axes)
1. **Training supervision**: supervised (labels; classification +
   regression), unsupervised (clustering, anomaly detection, density
   estimation), self-supervised (labels generated from the data itself —
   e.g. predict next token/masked word), semi-supervised (small labelled +
   large unlabelled), reinforcement (agent maximises reward in an
   environment).
2. **Learning mode**: batch (train once offline) vs online/incremental
   (learn on the fly from data streams; sensitive to bad data, needs
   monitoring).
3. **How they generalise**: instance-based (memorise examples, compare new
   points by similarity — k-NN) vs model-based (fit parameters to a model,
   then predict with it — the common case).

## Main challenges: bad data and bad algorithms
- **Insufficient data**: even simple problems need thousands of examples.
  "The Unreasonable Effectiveness of Data" (Banko & Brill 2001, Norvig
  2009): with enough data, simple algorithms rival complex ones.
- **Nonrepresentative data / sampling bias**: the 1936 Literary Digest poll
  (2.4M responses, predicted Landon, Roosevelt won 62%) failed because its
  sample favoured wealthy Republicans and had nonresponse bias. Small
  samples give sampling noise; large flawed samples give sampling bias.
- **Poor-quality data**: outliers and missing values must be cleaned.
- **Irrelevant features**: feature engineering = selection, extraction
  (e.g. PCA), and gathering new data.
- **Overfitting**: model too complex for the data; learns noise (the "w in
  country name ⇒ satisfaction > 7" example). Fixes: simplify (fewer
  params/features), regularise (constrain), more data, clean noise.
- **Underfitting**: model too simple. Fixes: more powerful model, better
  features, less regularisation.
- **Regularization**: constraining a model's degrees of freedom, controlled
  by a **hyperparameter** (set before training, not learned).

## Testing and validation
- Split into training + **test set**; test error ≈ **generalization error**
  (out-of-sample). 80/20 typical; large datasets can hold out less.
- **Hyperparameter tuning needs a third set** — a **validation set** (or
  k-fold cross-validation): tune on validation, evaluate once on test.
  Otherwise the test set leaks into your choices and overestimates
  performance.
- **Data mismatch** (e.g. web images vs app photos): keep validation/test
  representative of production data; add a **train-dev set** (drawn from
  training distribution) to tell overfitting apart from data mismatch.
- **No Free Lunch theorem** (Wolpert 1996): with no assumptions about the
  data, no model is a priori best — evaluate a few reasonable models.

## Key takeaways
- Learn the vocabulary (instance, model, feature, label, hyperparameter)
  cold — it's used everywhere in the book.
- Bias–variance framing: too-simple → high bias (underfit); too-flexible →
  high variance (overfit); irreducible noise always remains.
- Always hold out a test set and never tune on it.

## Notes
- This is the book's only near-code-free chapter; it's a vocabulary and
  workflow map for the rest.
- The ML project checklist in Appendix A operationalises this chapter.
