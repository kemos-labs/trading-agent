# Chapter I.2 — Essential Linear Algebra for Finance

## Core idea
Matrix algebra for portfolio analysis: matrices, eigenvalues/eigenvectors,
the covariance matrix (at the heart of portfolio risk), matrix
decompositions (Cholesky), and principal component analysis (PCA).

## Matrix basics
- Matrix: rectangular array of real numbers, m rows × n columns; square if
  m=n; **transpose** A' swaps rows/columns; symmetric if A = A'.
- Vector: column by convention; n-dimensional Cartesian space.
- **Laws**: addition/subtraction element-wise (same dimension); zero matrix;
  multiplication (row × column); identity; **inversion**.
- **Linear equations in matrix form**: Ax = b — used to solve hedging
  equations (e.g., gamma/vega hedges of an options portfolio) and in OLS.
- **Quadratic forms**: x'Ax — represents the variance of a linear portfolio.

## Eigenvalues and eigenvectors
- For square A, eigenvalue λ and eigenvector v satisfy Av = λv.
- Used to find the most important sources of variability in highly
  correlated systems (futures of different maturities).
- **Positive definiteness**: a matrix is positive definite iff all its
  eigenvalues are positive — guarantees every portfolio has positive
  variance (no arbitrage in risk).

## The covariance matrix
- Portfolio return in matrix notation: `R_p = w'·R`; variance
  `σ_p² = w'·Σ·w`.
- **Covariance matrix Σ**: from volatilities and correlations of asset
  returns; must always be positive definite.
- Lies at the heart of portfolio risk analysis: measures risk as a function
  of weights.

## Decompositions
- **Cholesky decomposition**: Σ = LL' for positive definite Σ — the tool for
  simulating correlated returns (I.5.7.4), fundamental for Monte Carlo
  VaR models (Volume IV).
- Eigen-decomposition of covariance/correlation matrices → principal
  components.

## PCA
- Eigenvectors of the covariance/correlation matrix form new uncorrelated
  variables (principal components) ordered by eigenvalue (variance).
- Case study: European equity index returns — a few PCs explain most of the
  variation.
- Applications: risk modelling of fixed-income portfolios and portfolios
  with many futures of different maturities.

## Pitfalls
- Not every matrix is invertible — check the determinant/rank.
- A covariance matrix that is not positive definite signals bad data or
  redundant assets (arbitrage-like).
- Correlations of nearly identical assets make the matrix ill-conditioned —
  PCA regularizes this.

## Bottom line
The algebra layer: how to express portfolio risk (w'Σw), test positive
definiteness via eigenvalues, simulate correlated returns via Cholesky, and
reduce dimension via PCA. Cross-refs:
`skills/correlated-scenario-simulation` (Cholesky), and the PCA material in
`knowledge/pythonic-quant/ch03`.
