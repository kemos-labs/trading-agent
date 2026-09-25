# Chapter 3 — Fundamentals of NumPy for Quants

## Core idea
NumPy's `ndarray` is the matrix workhorse of quantitative finance: fast
C-backed N-dimensional arrays, random generation, boolean/masking
operations, linear algebra (eigen/PCA), and a finance case study
(distribution fitting + VaR).

## The ndarray
- Homogeneous, fixed-size multidimensional container; `shape` (tuple) and
  `dtype` describe it.
- `np.array([[1,2,3],[4,5,6]], dtype=np.int32)`; `.shape`, `.size`, `.dtype`,
  `.ndim`.
- **Views vs copies**: an ndarray can be a *view* of another — changes
  propagate to the base; use `.copy()` for independence.
- **1D arrays**: creation, indexing, slicing, `np.arange`, `np.linspace`,
  `np.reshape`, `np.split`/`hsplit`/`vsplit`, `np.concatenate`, `np.tile`.
- **Special arrays**: zeros, ones, identity, NaN and Inf handling, clipping,
  flattening.
- **2D and N-D**: matrix construction, sub-array views (dependent vs
  independent), conditional scanning; 3D/4D arrays as stacks of simulations
  (e.g., K experiments × time steps × N×M matrices); `np.vstack` for
  growing a time stack.

## Arrays of randomness
- `np.random.randn` (standard normal), `rand`, `randint`, `random`,
  `permutation`, `choice` (with `replace=False` for unique draws).
- **Distribution zoo**: `beta`, `binomial`, `chisquare`, `exponential`,
  `gamma`, `gumbel`, `hypergeometric`, `laplace`, `lognormal`,
  `multivariate_normal`, `pareto`, `poisson`, `uniform`, etc.
- Backed by the **Mersenne Twister**; seed with `np.random.seed` for
  reproducibility.
- Example: LOTTO simulation — drawing 6-of-49 and counting iterations to a
  match (probability ≈ 2.65e-05 per draw).

## Finance case study: MA returns → fit → VaR
```python
import pandas_datareader.data as web
from scipy.stats import norm
data = web.DataReader("MA", 'yahoo', start='2010-05-13', end='2015-05-13')['Adj Close']
cp = np.array(data.values)
ret = cp[1:]/cp[:-1] - 1                      # daily returns
mu_fit, sig_fit = norm.fit(ret)               # fit N(mu, sig)
# annualised: mu = (mu_fit+1)**364 - 1; sig = sig_fit * sqrt(252)
# (the book uses 364 trading days; 252 is the common convention)
pdf = norm.pdf(x, mu_fit, sig_fit)            # density; sum(pdf*dx) == 1
cdf = norm.cdf(x, mu_fit, sig_fit)
# Value-at-Risk: quantile of the fitted Normal at significance 0.05
var = norm.ppf(0.05, mu_fit, sig_fit)         # parametric VaR (daily, negative)
```
- `norm.fit` gives ML estimates of mean/std; PDF/CDF come from the same
  fitted distribution; the parametric quantile is the VaR.
- Empirical VaR: order returns, take the 5th-percentile value directly.

## Element-wise (boolean) analysis
- Comparisons (`>`, `==`, `!=`, `>=`) produce boolean arrays — ufuncs with
  operator aliases (`np.greater_equal` ⇔ `>=`).
- Compound conditions: `&` (and), `|` (or), `~` (not) on boolean arrays.
- `np.where(cond)` returns indices; `np.where(cond, a, b)` selects values.
- **Masking**: boolean array selects the matching elements
  (`x[x > 4]`); search/replace/filter patterns.
- Aggregates: `any`, `all`, counts of matches; central tendency measures
  (mean, median, std).

## Linear algebra & PCA
- Matrix multiply, transposes, eigenvalues/eigenvectors
  (`np.linalg.eig`); **PCA** via eigendecomposition of the covariance of
  simulated asset returns — the first principal component captures common
  movement, later PCs are noise for random data.

## Pitfalls
- Views vs copies: mutations leaking through views.
- Inexact float comparisons; NaN/Inf contamination propagating through
  aggregates.
- `np.reshape` requires compatible sizes — verify `sqrt(size)` integrality
  for square reshaping.
- Seeding: a single global seed; reset per experiment for independence.

## Bottom line
The NumPy foundation — arrays, randomness, masking, linear algebra — with a
complete quant workflow (download → returns → fit → PDF/CDF → VaR). This
is the seed of the knowledge base's simulation/VaR toolkit:
`skills/risk-metrics` (historical VaR) and `skills/monte-carlo-option-pricing`.
