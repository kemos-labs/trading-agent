# Strategy attribution + trend convexity

- **description**: The Lecture 1 close-out template — signal P&L vs cost drag
  vs sizing — plus the trend-convexity diagnostic: a trend rule earns
  long-horizon variance minus short-horizon variance
  (`G_T = λ/2·[(S_T−S₀)² − ΣD²]`), so convex payoffs and positive skew are
  mechanical, while average profitability is a separate question. Overlay
  notes: rebalanced commodity portfolios earn a diversification return
  (~4.5% where constituents average ~0); roll explains the cross-section;
  GSCI history is an energy bet, not a policy weight.
- **when to use it**: After every backtest and every paper-trade batch. Run
  `research/attribute.py`; reject legs where cost/gross is fragile
  (TLT-vol_mom 0.36 is the live example); check skew sign against the
  strategy's claimed shape (trend legs should skew positive at their own
  horizon — negative monthly skew on equity-momentum legs is the crash-tail
  warning from the HMM skill).
- **method/formula/code**:
  - Attribution columns per leg: gross, costs, net, cost/gross, turnover
    (mean |Δexposure|), skew. Journal integrity: unit cost |cost/δ|
    constant (= ptc × capital-per-leg) + `paper_only` guard on every row.
  - Convexity identity (verify check 17): direct P&L vs variance-spread RHS
    must match to 1e-9 on any price path — it is algebra, not a model.
  - Commodity overlay math: EW-rebalanced excess ≈ +4.5% vs ≈ −0.5% mean
    constituent; roll-return spread ±9pp cross-sectionally.
  - Code: `research/attribute.py` → `knowledge/strategy-research/
    attribution-*.md` (read-only over paper stores).
- **known pitfalls**: Attribution is ex-post accounting, not a license to
  re-optimize (route changes through purged-CV + HLZ hurdle). Cost/gross on
  a single holdout is noisy — compare across legs, don't threshold one leg
  alone. Trend convexity needs the matching horizon to be visible (CTA
  smile emerges ~180d aggregation, not monthly scatter). Diversification
  return requires continued low correlations + disciplined rebalancing.
- **source**: Grinold (2006) attribution-as-portfolios (framework);
  Moscou-Potters-Bouchaud (2016) trend convexity; Erb-Harvey commodity
  futures (diversification return + roll); Paleologo Lecture 1 close-out.
- **corpus**: `drive-download-20260925T215026Z-1-001/trendfollowing/Tail
  Protection for Long Investors Trend Convexity at Work (2016).md`,
  `.../derivatives/Strategic and Tactical Value of Commodity Futures
  (Futures_ErbHarvey.pdf).md`, `.../portfolioconstruction/Attribution
  Modeling Asset Characteristics as Portfolios ([Grinold] ... 2006...).md`.
  Bib: no exact keys — cite corpus paths.
- **spine**: overlays + attribution. **mechanism**: variance harvesting
  (convexity/diversification return are mechanical) + liquidity (roll).
- **implementation**: `research/attribute.py` (no new quantkit module;
  check 17 in `research/verify_formulas.py`).
