# Residual (decomposed) short-term reversal

- **description**: One-month reversal sorted not on raw prior returns but on
  the residual nonfundamental component: strip industry, expected return
  (factor model), and cash-flow news (analyst revisions); sort within
  industry on the leftover. Da-Liu-Schaumburg report ~3–4× the alpha of
  raw-return reversal, with asymmetric legs (long = liquidity provision,
  short = sentiment correction under short-sale constraints).
- **when to use it**: Monthly contrarian screens in universes with industry
  codes and analyst coverage. Always report the raw-reversal baseline
  alongside — the uplift from residualizing is the test that the
  decomposition works.
- **method/formula/code**:
  - Decompose: `r_{i,t-1} = r_{j,t-1} + μ̃ + CF̃ + DR̃` (industry mean,
    expected return from rolling FF3 betas, cash-flow news from consensus
    forecast revisions, residual). Signal: `Residual = r − μ̂ − CF`
    (code: `quantkit.xsec.residual_score`).
  - Trade: within each industry, sort prior-month residuals into deciles;
    buy bottom, short top; hold one month. Exclude prices < $5 at formation
    (microstructure noise). Across-industry term is continuation —
    never sort raw returns across industries for reversal.
- **known pitfalls**: Residual is "everything left over" — broad by
  construction; validate with double sorts on CF news (residual must win).
  Needs analyst coverage (large-cap bias). Illiquidity drives the long leg
  — net-of-costs check is mandatory (use execution-lab Kyle/Amihud).
  One-month holding + monthly turnover → costs dominate weak implementations.
- **source**: Da-Liu-Schaumburg (2011) NY Fed Staff Report (decomposition);
  Da-Liu-Schaumburg (2014) Management Science (residual strategy, ~1%/mo alpha).
- **corpus**: `drive-download-20260925T215026Z-1-001/momentum/Decomposing
  Short-Term Return Reversal (2011).md`, `.../momentum/A Closer Look at the
  Short-Term Return Reversal (2014).md`. Bib: no exact key — cite corpus path.
- **spine**: µ-models. **mechanism**: liquidity (long leg — price pressure /
  fire sales) + information/frictions (short leg — sentiment + short-sale
  constraints).
- **implementation**: `src/quantkit/xsec.py::residual_score` +
  `wml_weights(..., groups=industry)` (tests: `tests/test_xsec.py`).
