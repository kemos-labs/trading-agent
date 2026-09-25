# Ch27 — Go Forth and Do Data Science

**Source:** Grus, *Data Science from Scratch*, Chapter 27.

## Purpose
The bridge from toy from-scratch implementations to production tooling: the
libraries and next topics that turn understanding into practice.

## The message
- Implementing from scratch **builds understanding** but not performance,
  convenience, or error handling. In real work, **use battle-tested
  libraries** — the from-scratch code was pedagogy, not production.

## The essential Python stack
- **NumPy**: real `ndarray`s and matrices (fast, vectorised) — the building
  block under everything else.
- **pandas**: `DataFrame` — the production version of the book's `Table`/
  `NotQuiteABase`: munging, slicing, grouping, joins at scale.
- **scikit-learn**: the standard ML library — every model in this book and
  many more (better decision trees, real optimisers), with a uniform
  fit/predict API.
- **matplotlib / seaborn**: static visualisation; seaborn beautifies
  matplotlib.
- **D3.js / Bokeh**: interactive, web-shareable visualisation (D3 is the
  reference; Bokeh brings it to Python).
- **IPython / Jupyter**: IPython's shell is endorsed; the book is openly
  skeptical of notebooks ("confuse beginners, encourage bad habits") —
  worth reading as a dissenting voice even if you end up using them.

## Deep learning
- **PyTorch** (the book's recommendation: easier, beginner-friendlier) or
  **TensorFlow** (older, more widespread). Both have endless tutorials of
  wildly varying quality.
- Deep learning is optional ("you can be a data scientist without it") but
  the trendy path.

## Beyond Python
- **R**: worth familiarity to read other people's analyses and blog posts —
  not required to do data science.
- **Math depth**: real data science needs deeper linear algebra, statistics,
  and probability than the book covered (ch4–6 are appetisers); study the
  textbooks listed at each chapter's end.

## Finding data
- Work usually provides your data. Otherwise: public datasets, scraping
  (ch9) with etiquette, and the general principle that data quality
  dominates modelling choices.

## The overarching advice
- Continue the book's habits: **plot first, question everything, hold out
  test data, understand the math under the library calls, and code
  reproducibly** (seeded, documented).
- Read the Python Data Science Handbook (VanderPlas) next for the library
  layer.

## Key takeaways
- Understanding (from scratch) → then libraries (NumPy/pandas/sklearn/
  PyTorch) for real work.
- The book's spirit: never use a tool you don't understand — even in
  production, keep the underlying math in view.
- Notebook skepticism and seed-everything reproducibility are deliberate
  professional opinions worth absorbing.

## Notes
- Effectively a reading list + philosophy chapter; no formulas.
- Closes the loop on ch1's promise: the whole book was "data science from
  scratch" so the library layer makes sense.
