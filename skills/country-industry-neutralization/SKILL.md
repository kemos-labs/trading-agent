# Country-industry neutralization (Heston-Rouwenhorst)

- **description**: Split any international return cross-section into pure
  country and pure industry effects with a constrained dummy regression.
  The empirical prior (1978–1992 Europe): pure-country variance ≈ 4.5×
  pure-industry variance, so country neutralization comes first — but
  Cavaglia-Brightman-Aked show the ranking reversed by the late 1990s, so
  re-estimate, don't memorize.
- **when to use it**: Any cross-border screen, hedge, or attribution:
  neutralize country before industry; decompose index returns into
  mix-effects vs pure effects before claiming stock-picking skill.
- **method/formula/code**:
  - `R_i = α + β_{j(i)} + γ_{k(i)} + e_i`, identified by
    `Σ W_j β_j = 0`, `Σ V_k γ_k = 0` (cap-weighted; count-weighted = EW
    market α). Code: `quantkit.factors.pure_factor_returns`
    (constrained WLS via last-dummy substitution; exact reconstruction).
  - Readout: `α` = cap-weighted market; `α + β_j` = geographically
    diversified industry j; `α + γ_k` = industrially diversified country k.
  - Variance check: `Var(pure country)/Var(pure industry)` ≈ 4.5 is the
    1978–1992 reference, not a constant.
- **known pitfalls**: No industry×country interaction allowed — misses
  local-industry shocks. Raw country/industry indices confound composition
  with effect (the mistake this method fixes). 7-industry/12-country
  granularity is coarse for concentrated books. The country-dominance
  result decayed after the 1990s (integration, tech) — verify on your
  sample before sizing hedges off it.
- **source**: Heston-Rouwenhorst (1994 JFE companion; 1995 JPM popularization);
  Cavaglia-Brightman-Aked (2000) reversal update.
- **corpus**: `drive-download-20260925T215026Z-1-001/returnproperties/Industry
  and Country Effects in International Stock Returns (...1995...).md`.
  Bib: no exact key — cite corpus path.
- **spine**: Σ + costs (risk-model factors). **mechanism**: information
  (local policy/legal/regional shocks dominate industry comovement).
- **implementation**: `src/quantkit/factors.py::pure_factor_returns`
  (tests: `tests/test_factors.py::TestPureFactorReturns`).
