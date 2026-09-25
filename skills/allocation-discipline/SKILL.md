# Allocation discipline (FLAM + shrinkage before optimization)

- **description**: Research-budgeting and estimation discipline for portfolio
  construction: exact unconstrained IR `√(α'Ω⁻¹α)` (IC√N on diagonal alphas),
  transfer coefficient TC as the constraint-deadweight meter, Jorion
  Bayes-Stein mean shrinkage, Ledoit-Wolf covariance shrinkage, and Tu-Zhou
  1/N combination as the low-variance anchor. Ex-ante IR benchmarks:
  top-quartile practitioner ≈ 0.5, very good 0.75, exceptional 1.0.
- **when to use it**: Before every optimizer run and every research-hours
  decision. Shrink means AND covariances before optimizing; report TC for
  every constrained book; allocate research by `IR²` additivity across
  independent bets, not by backtest Sharpe alone.
- **method/formula/code**:
  - Exact law: `w* = Ω⁻¹α/(2λ)`, `IR = √(α'Ω⁻¹α)`;
    `TC = α'w/(IR·σ_A)`; attribution `R_A = (TC·ρ_α + √(1-TC²)·ρ_c)·√N·D·σ_A`
    — even TC = 0.67 leaves noise multiplier 0.74.
  - `IR ≈ IC·√BR`, `IR_total² = Σ IR_k²` (independent bets only; correlated
    signals share `IC²(com) = 2IC²/(1+γ)`).
  - Bayes-Stein: `μ̂ = (1-w)Ȳ + w·Y₀·1`,
    `w = min{1,(N-2)/(T(Ȳ-Y₀1)'Σ⁻¹(Ȳ-Y₀1))}` → `bayes_stein_means`.
  - Ledoit-Wolf: `S* = (1-δ*)S + δ*μI` → `ledoit_wolf_shrinkage` (PD even N>T).
  - 1/N anchor: `w_c = (1-δ)/N + δ·w` → `combine_with_1n`.
  - Code: `quantkit.portfolio.fundamental_law_ir / transfer_coefficient /
    bayes_stein_means / ledoit_wolf_shrinkage / combine_with_1n`.
- **known pitfalls**: Breadth = N only on diagonal Ω — correlated alphas
  collapse effective breadth (the most common FLAM inflation). Mean errors
  hurt more than variance errors (Chopra-Ziemba) — shrink means first.
  TC decay is silent value destruction: constraints imposed after
  optimization look free but multiply realized IR by TC. 1/N wins when
  estimation noise dominates — that is a fact about your sample length,
  not a refutation of theory.
- **source**: Clarke-de Silva-Thorley (2006) FLAM (exact laws + TC);
  Jorion (1986) Bayes-Stein; Ledoit-Wolf (2004) shrinkage; Tu-Zhou (2011)
  1/N combination; Grinold-Kahn (2000) benchmarks.
- **corpus**: `drive-download-20260925T215026Z-1-001/portfolioconstruction/The
  Fundamental Law of Active Portfolio Management ([Clarke, de Silva, Thorley]
  ...2006...).md`, `.../Bayes-Stein Estimation for Portfolio Analysis
  (1986).md`, `.../Markowitz Meets Talmud ... (2011).md`. Bib: no exact
  keys — cite corpus paths.
- **spine**: optimization. **mechanism**: estimation risk (not a return
  premium — a decision-theoretic guardrail).
- **implementation**: `src/quantkit/portfolio.py` additions
  (tests: `tests/test_portfolio.py::TestEstimationDiscipline`).
