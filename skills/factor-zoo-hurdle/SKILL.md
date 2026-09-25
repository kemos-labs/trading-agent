# Factor-zoo hurdle (multiple-testing discipline for new signals)

- **description**: A newly mined factor must clear far more than t = 2.0.
  Harvey-Liu-Zhu's catalog of 316 factors implies a hurdle near **t ≈ 3.0**
  (higher under family-wise error control); most published "anomalies" are
  likely false. Pair with McLean-Pontiff post-publication decay: haircut
  in-sample Sharpe before any capital or sizing decision.
- **when to use it**: Before promoting ANY corpus signal to a strategy,
  module, or paper trade. Gate: |t| ≥ 3.0 on the OOS leg, DSR-corrected
  significance (validation lab), and an explicit decay haircut.
- **method/formula/code**:
  - Hurdle: new factor needs `|t| ≳ 3.0` (HLZ), not 2.0; Bonferroni/Holm/FDR
    for families of tried variants — count every tried variant, not every
    reported one (file-drawer `M` matters).
  - Decay haircut: shrink in-sample Sharpe ~30–50% (McLean-Pontiff magnitude)
    for the ex-ante IR used in sizing; re-check FLAM math post-haircut.
  - Code: combine `quantkit.validation.deflated_sharpe` (trials = variants
    tried) with `quantkit.validation.probabilistic_sharpe_ratio`; reject if
    DSR < 0.95 at the haircut Sharpe.
- **known pitfalls**: Theory-derived factors earn a lower hurdle than
  data-mined ones — but never 2.0. Unconditional insignificance can hide
  state-conditional value (HLZ caveat) — route those to regime-gated designs,
  not the main book. Tried-but-unreported variants are the bias; log every
  trial in the experiment report (embargo width + trial count).
- **source**: Harvey-Liu-Zhu (2015) "...and the Cross-Section of Expected
  Returns" (RFS); McLean-Pontiff (2015) post-publication decay (background).
- **corpus**: `drive-download-20260925T215026Z-1-001/anomalies/and the
  Cross-Section of Expected Returns (AbnormalReturnsReview_HarveyLiuZhu_2015.pdf).md`.
  Bib: no exact key — cite corpus path.
- **spine**: µ-models (evidence filter). **mechanism**: none claimed — this is
  a skepticism gate, not a signal.
- **implementation**: existing `src/quantkit/validation.py` (no new module);
  enforced in every Phase 8 experiment report.
