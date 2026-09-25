# Chapter I.5 — Numerical Methods in Finance

## Core idea
Numerical methods when no analytic solution exists: iteration/root-finding,
interpolation and extrapolation, optimization, finite differences, lattice
(binomial tree) methods, and Monte Carlo simulation.

## Why numerical methods
- Analytic solutions exist only under simple assumptions (i.i.d. normal
  returns), but real returns are skewed, leptokurtic, and volatility-
  clustered.
- Examples needing numerics: implied volatility (invert BSM), constrained
  min-variance portfolios, VaR, bond yields, American options under
  stochastic volatility.

## Iteration / root finding
- Solve f(x) = 0 (e.g., bond yield PV(y) - P_market = 0; implied volatility
  f_BSM(σ) - f_market = 0).
- **Bisection**: halve an interval bracketing a sign change — simple,
  slow, needs continuity.
- Newton-Raphson-type and other iterative schemes refine a starting guess.
- Excel: Goal Seek (root finding), Solver (optimization).

## Interpolation and extrapolation
- Fill gaps where data are missing: yield curves, implied volatility
  surfaces.
- Linear, polynomial interpolation (e.g., for currency options); splines.
- Extrapolation beyond observed data — with caution.

## Optimization
- Three areas: efficient resource allocation (portfolio capital
  allocation); model calibration to market data; fitting distributions to
  data (maximize likelihood).
- Solver-based: GARCH parameter estimation, Johnson distribution fitting,
  cash-flow mapping.

## Finite differences
- Approximate first/second derivatives of functions — used for the
  **Greeks** of exotic/path-dependent options, local volatility
  calibration, anywhere no analytic derivative exists.
- Central differences: f'(x) ≈ (f(x+h) - f(x-h))/2h.

## Lattice methods
- Binomial tree discretizes time and space to approximate path-dependent
  option prices; European and American options via backward induction.
- Cross-ref: `skills/binomial-tree-pricing`.

## Simulation (method of last resort)
- Always provides a solution; used where optimization/discretization fails:
  barrier option risk, options-portfolio VaR, worst-case loss.
- Simulate from empirical or given distributions; lognormal asset price
  series; **correlated normal returns** via Cholesky (from I.2).
- Caution: don't keep simulation spreadsheets open while running Solver —
  it re-simulates at each iteration.

## Pitfalls
- Bisection is slow; Newton can diverge without good starting values.
- Extrapolation is dangerous beyond the data range.
- Simulation converges slowly (~1/√N); use variance reduction and enough
  paths.
- Finite-difference step h must balance truncation vs roundoff error.

## Bottom line
The numerical toolbox: bisection/Newton for roots, interpolation for
curves, optimization for calibration, finite differences for Greeks,
binomial trees for American options, and Monte Carlo as the universal
fallback. Cross-refs: `skills/binomial-tree-pricing`,
`skills/monte-carlo-option-pricing`, `skills/correlated-scenario-simulation`.
