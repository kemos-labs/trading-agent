# Ch16 — Machine Learning Asset Allocation

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 16.

## Purpose
Introduces **Hierarchical Risk Parity (HRP)**, a portfolio-construction
method from graph theory and ML that avoids the instability,
concentration, and underperformance problems of Markowitz-style
quadratic optimizers — and works even on singular covariance matrices.

## Why convex optimization fails
- **Markowitz's curse**: the condition number of the covariance matrix
  (max/min eigenvalue) grows with correlation among assets. The more
  correlated the investments, the greater the need for diversification
  — yet the more ill-conditioned the matrix inversion, so the more
  unstable the weights. Diversification benefits are offset by
  estimation error.
- Estimating an invertible N×N covariance requires ≥ N·(N+1)/2 IID
  observations (e.g., 5 years of daily data for N=50) — and correlation
  structures don't stay invariant that long.
- Quadratic optimizers (CLA, mean-variance) are also sensitive to
  return forecasts (Michaud), and even 1/N portfolios beat mean-variance
  out-of-sample (De Miguel et al.).

## HRP: from geometry to hierarchy
- A correlation matrix is a *complete graph*: every asset is a
  substitute for every other. Instead, treat relationships
  **hierarchically** (tree): stocks cluster by industry, size, region —
  J.P. Morgan substitutes with Goldman Sachs, not with a Caribbean real
  estate holding.
- HRP pipeline (3 stages):
  1. **Tree clustering**: compute a correlation-distance matrix
     (d_ij = √(0.5·(1−ρ_ij))), then single-linkage hierarchical
     clustering → dendrogram.
  2. **Quasi-diagonalization**: reorder the covariance matrix by the
     dendrogram leaves so similar assets are adjacent — blocks of
     substitutes appear.
  3. **Recursive bisection**: allocate weights top-down; at each
     bisection split the weight between the two sub-clusters in inverse
     proportion to each cluster's variance (computed via inverse
     variance weights on the quasi-diagonal block). Guarantees weights
   in [0,1] summing to 1; runs in best-case logarithmic, worst-case
   linear deterministic time.
- No matrix inversion needed — singular or ill-conditioned covariances
  are fine.

## Evidence
- Monte Carlo: HRP delivers *lower out-of-sample variance* than CLA
  (even though min-variance is CLA's objective), and lower variance
  than naive risk parity.
- HRP allocations are more stable (less weight oscillation) and more
  diversified (less concentration) than quadratic solutions.

## Key takeaways
- Markowitz's curse: more correlated assets → less reliable optimizers
  exactly when you need them most. HRP sidesteps inversion entirely.
- Use HRP to allocate across ML strategies (and across assets): it
  needs only a covariance/correlation matrix, produces robust,
  diversified weights, and is fast.
- HRP is a natural portfolio-construction companion to the rest of the
  book: strategies are clustered by return correlation, then
  risk-budgeted hierarchically.
