# Intermediate-horizon momentum (12-7 vs 6-2)

- **description**: Cross-sectional momentum sorts on intermediate-horizon past
  returns (`r_{12,7}`), skipping both the most recent month (reversal,
  bid-ask bounce) and relying less on the recent `r_{6,2}` leg, which
  Novy-Marx shows is weak and unstable. Includes the Daniel-Jagannathan-Kim
  crash overlay: cut exposure when the ex ante turbulent-state probability
  (loser leg distressed → WML short a call on the market) is high.
- **when to use it**: Any cross-sectional equity momentum screen. Use 12-2 as
  the baseline, report the 12-7 / 6-2 split as a spanning check, and gate
  exposure with a drawdown/volatility crash filter before sizing.
- **method/formula/code**:
  - Formation: rank on cumulative return months `t-12..t-2`; split
    `r_{12,2} = (1+r_{12,7})(1+r_{6,2})-1`. Winner-minus-loser = long top
    decile, short bottom decile (value- or equal-weight, NYSE breakpoints).
    Code: `quantkit.xsec.formation_returns` + `wml_weights`.
  - Skip-month: never include month `t-1` in formation (short-term reversal
    contamination). Holding: 1 month, or Jegadeesh-Titman overlapping
    K-cohorts via `quantkit.xsec.overlapping_weights`.
  - Crash filter (DJK 2019): `R_MOM = α + β·R_MKT + β⁺·max(R_MKT,0) + ε`;
    estimate β⁺ after drawdowns; when turbulent probability
    `P(S_t=turbulent|F_{t-1})` (or a vol/drawdown proxy) is high, scale WML
    exposure down — the short loser leg rallies violently on rebounds.
- **known pitfalls**: Recent-return (`6-2`) momentum has little alpha once
  `12-7` is controlled — don't ship a 6-2-only signal. Momentum crashes
  cluster after market drawdowns (2009-style); unfiltered WML has a deep
  left tail. Industry momentum contaminates single-sort WML — neutralize or
  report within-industry sorts. Post-publication decay: haircut Sharpe via
  the factor-zoo-hurdle skill.
- **source**: Novy-Marx (2012) "Is Momentum Really Momentum?" (JFE);
  Daniel-Jagannathan-Kim (2019) HMM of momentum (WP).
- **corpus**: `drive-download-20260925T215026Z-1-001/momentum/Is Momentum Really
  Momentum (2012).md`, `.../momentum/A Hidden Markov Model of Momentum
  (2019).md` (canon; two alt distillations quarantined-kept).
  Bib: no exact key (weak join) — cite corpus path.
- **spine**: µ-models. **mechanism**: information (slow diffusion,
  Hong-Stein-style) + funding (distress leverage → crash convexity).
- **implementation**: `src/quantkit/xsec.py` (tests: `tests/test_xsec.py`).
