# Chapter 11 — Mathematical Tools

## Core idea
The numerical toolbox finance relies on: **approximation** (regression,
interpolation), **convex optimization**, **integration**, and **symbolic
computation** — all in Python.

## Approximation
- **Regression** (least-squares fit): given basis functions
  `b_d(x)`, `d=1..D`, minimize `(1/I) Σ_i (y_i - Σ_d α_d b_d(x_i))²`.
  - Monomials: `np.polyfit(x, y, deg)` + `np.polyval(p, x)` — vectorized
    polynomial regression.
  - scipy least-squares / `np.linalg.lstsq` for general basis sets.
  - Higher degree → closer fit, but overfitting risk (Runge's phenomenon).
- **Interpolation**: pass exactly through the data points —
  `scipy.interpolate.interp1d` (linear, cubic splines); used for yield
  curves and vol surfaces. Regression smooths, interpolation reproduces.

## Convex optimization
- Minimize a convex objective subject to constraints — the backbone of
  portfolio optimization (ch13) and model calibration (ch21).
- `scipy.optimize.minimize` with methods (SLSQP) for constrained problems;
  `spo.fmin` for unconstrained (Nelder-Mead).
- Financial applications: mean-variance optimization, calibrating option
  models to market quotes (MSE in model params).

## Integration
- Valuation of derivatives = evaluating integrals (risk-neutral expectations).
- `scipy.integrate.quad` for 1-D; `quad`/`dblquad` for higher dimensions;
  Monte Carlo integration as the general fallback (ch12).

## Symbolic computation (SymPy)
- `sympy.symbols`, `sympy.diff`, `sympy.solve` — derivative of a payoff,
  solving equations symbolically before coding numerically.
- Use symbolic derivatives to verify hand-derived Greeks, then plug into
  numeric code.

## Pitfalls
- Polynomial degree too high → oscillation between points; prefer splines.
- Local optima in non-convex calibration: do a coarse grid search first,
  then a local minimizer from the best grid point (the ch21 recipe).
- Integration over infinite domains needs care (variable transform or
  truncation).

## Quick reference of the main calls
- Regression: `np.polyfit(x, y, deg)`, `np.polyval(p, x)`; general least
  squares via `np.linalg.lstsq`.
- Interpolation: `scipy.interpolate.interp1d(x, y, kind='cubic')`.
- Optimization: `scipy.optimize.minimize(fun, x0, method='SLSQP')`,
  `scipy.optimize.fmin(fun, x0)` for unconstrained Nelder-Mead.
- Integration: `scipy.integrate.quad(f, a, b)` (1-D), `dblquad` (2-D).
- Symbolic: `sympy.symbols`, `sympy.diff`, `sympy.solve`.

## Bottom line
The applied-math layer: fit, optimize, integrate, and derive symbolically —
each with scipy/SymPy one-liners that the valuation chapters use constantly.
Cross-refs: `knowledge/python-for-finance/ch13` (portfolio optimization),
`ch21` (model calibration).
