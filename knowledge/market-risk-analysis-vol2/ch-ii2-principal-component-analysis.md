# II.2 Principal Component Analysis

Source: Carol Alexander, *Market Risk Analysis*, Vol. II (Practical Financial
Econometrics), ch II.2.

## Core idea

PCA builds **statistical factor models** with no economic interpretation:
principal components (PCs) are orthogonal factors extracted from the
eigen-decomposition of a covariance or correlation matrix. Unlike the
regression factor models of ch II.1, curve PCA models capture a portfolio's
**P&L as a linear function of risk-factor *changes*** (not percentage
returns), which makes them ideal for interest-rate-sensitive books and any
term structure (yields, forwards, futures, implied volatility surfaces).

Three aims: (1) reduce many risk factors to a manageable few (e.g., 60 yields
→ 3 PCs); (2) identify the key sources of risk; (3) construct hedges against
the most common curve movements.

## PCA mechanics

Given data matrix X (T observations x n series, each column a return or rate-
change series) and its covariance/correlation matrix V:

```
V = W * Lambda * W'   (eigen-decomposition)
P = X * W             principal components (orthogonal, uncorrelated)
X = P * W'            reconstruction (W orthogonal: W^-1 = W')
```

- Eigenvectors of a symmetric matrix are orthogonal; eigenvalues positive iff
  the matrix is positive definite.
- The first PC carries the largest eigenvalue (most variance), the second the
  next, etc.
- Reduced-k approximation: `X ~ P* * W*'` using only the first k components;
  accuracy improves with k. In a highly correlated system (a yield curve),
  k = 3 typically captures >99% of variation.

## Curve factor models

For term structures the first few PCs have stable, interpretable shapes —
**shift** (parallel movement, PC1), **tilt/slope** (PC2), **curvature/
convexity** (PC3). Scenario analysis and hedging use this structure: a hedge
that zeroes the portfolio's exposure to the first three PCs protects against
the overwhelming majority of historically observed curve moves. Multiple
curves (e.g., two currencies) are handled by PCA on the full cross-curve
correlation matrix, capturing both within-curve and between-curve dependence.

## Equity applications

PCA on the correlation matrix of many stock returns gives a statistical
factor model for equities; commercial products (e.g., APT) derive component
representations for thousands of stocks. Choosing the number of components
lets the investor control the level of specific risk retained.

## Key takeaways

- PCA = eigenvalue decomposition of the covariance/correlation matrix; PCs
  are uncorrelated by construction.
- Use the **correlation** matrix when series have very different scales
  (mixing yields and spreads), covariance otherwise.
- Term-structure PCA reduces dimensionality massively (60 rates → 3 factors)
  and yields interpretable shift/tilt/curvature factors.
- Works best on highly correlated systems; for weakly correlated systems the
  small-k approximation is poor.
- The same machinery underlies O-GARCH (ch II.4): GARCH on each PC's
  variance reconstructs a full positive semi-definite covariance matrix.

Related skills: `skills/cointegration-testing` (a related form of
dimensionality reduction via common trends), `knowledge/market-risk-analysis-
vol1/ch-i2` (linear algebra).
