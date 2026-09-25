# Impact calibration (Almgren closed forms)

- **description**: Pre-trade cost estimation with fitted universal
  coefficients: permanent impact linear in size/ADV (`γ = 0.314`), temporary
  impact concave in trade rate (`η = 0.142`, exponent `3/5` — square-root
  rejected). Permanent leg is schedule-free; temporary leg shrinks with
  slower (longer-T) execution. The hurdle every µ-signal must clear.
- **when to use it**: Before sizing any strategy: convert target positions
  into expected implementation shortfall via `almgren_impact`, compare
  against the signal's expected alpha, and reject (or slow down) trades
  where cost ≥ edge. Re-estimate coefficients on your own fills — the
  2001–2003 S&P 500 numbers drift.
- **method/formula/code**:
  - `I = γ·σ·(X/V)·(Θ/V)^{1/4}` — permanent (fraction of pre-trade price);
    linear in `X/V`, independent of execution time `T`.
  - `J = I/2 + sgn(X)·η·σ·|X/(V·T)|^{3/5}` — realized average execution cost.
  - Code: `quantkit.execution.almgren_impact` (warns above 25% ADV;
    calibrated ≤ ~10% ADV, intraday active schedules, large-cap US).
  - Reference magnitudes: X/V = 10%, σ = 2%, Θ/V = 100 → I ≈ 20 bps,
    J ≈ 38 bps at T = 0.1 volume-time.
- **known pitfalls**: Single-order R² < 1% — volatility noise dominates any
  single fill; the model is for averages and schedules, not fill-by-fill
  prediction. Fat-tailed residuals → Gaussian cost confidence bands are
  optimistic. No cross-impact, no leakage effects beyond 10% ADV, buy/sell
  symmetry assumed. Volume-time (not clock-time) scheduling is load-bearing.
- **source**: Almgren-Thum-Hauptmann-Li (2005) "Direct Estimation of Equity
  Market Impact" (WP).
- **corpus**: `drive-download-20260925T215026Z-1-001/marketimpact/Direct
  Estimation of Equity Market Impact (2005).md`. Bib: no exact key — cite
  corpus path.
- **spine**: Σ + costs. **mechanism**: liquidity (concession for immediacy) +
  information (permanent drift).
- **implementation**: `src/quantkit/execution.py::almgren_impact`
  (tests: `tests/test_execution.py::TestAlmgrenImpact`).
