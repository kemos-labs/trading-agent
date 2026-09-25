# Chapter 18 — Stock Personality Clusters

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## Clustering

- **Definition** (restricted usage): assembling stock symbols into
  groups of varying tightness/proximity based on chosen properties,
  metrics, or traits. Usually one metric at a time (multi-metric gets
  complex).
- **Uses**: understand data structure, summarize, define useful
  subsets, and — central conjecture — *stocks of close proximity
  exhibit similar trading characteristics*: solve the price-trajectory
  problem for one member and you're closer to solving it for the
  cluster. No rigorous proof, but "the parallelism of behavior is
  sometimes quite remarkable."
- **Caveats**: clustering is an *ill-posed* problem (many possible
  partitions, no objective reason to prefer one); results depend on the
  analyst's bias, skill, and experience. "Eyeballability" beats the
  math (paraphrasing Mandelbrot: use your eyes).
- **Input**: backtested historical tick data, 20–60 sessions of NASDAQ/
  NYSE watchlist symbols (100 stocks × 60 sessions = 6,000 files — be
  prepared). Method: **Euclidean distance**
  `D_ij = √((X_i − X_j)²)` between two stocks' metric values — works
  with Excel scatter diagrams.
- The idea: different stocks appeal to different trader psychologies;
  cluster members should respond to the same algos and move together →
  homogeneous *cohorts* with higher probability of excess returns, and
  clustering itself suggests new strategies.

## Key takeaways

1. Cluster on single standardized metrics (e.g., %Range) and treat
   membership as a hypothesis, not proof.
2. Euclidean distance on a metric + scatter plots is the minimal viable
   clustering tool.
3. Personality → cohort → algorithm-fit: same algo for same-cluster
   stocks, new strategy ideas from cluster peculiarities.
