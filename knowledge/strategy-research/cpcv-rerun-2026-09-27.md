# CPCV re-run — Phase 3 legs (embargo + HLZ hurdle)

Protocol: N=6 groups, k=2 -> 15 OOS paths; label horizon = next-bar return; embargo = 5 bars; equal-weight SPY/QQQ/TLT, 10 bps, one-bar lag; pinned bars 2010-01-01 -> 2024-12-31 (3774 bars).

Predeclared verdict rule: ROBUST = mean OOS Sharpe > 0 AND t >= 3.0 AND DSR > 0.95 AND >= 12/15 paths positive; FRAGILE = positive mean but below hurdle; REJECT = non-positive mean.

| strategy | full SR | mean OOS SR | path SD | t-stat | pos paths | PSR | DSR | paired vs BH t | paired pos | verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| buy_hold | 1.04 | 1.11 | 0.33 | 13.18 | 15/15 | 0.009 | 1.000 | nan | 0/15 | **ROBUST** |
| dual_sma_9_45 | 0.81 | 0.81 | 0.21 | 15.26 | 15/15 | 0.381 | 1.000 | -3.82 | 3/15 | **ROBUST** |
| vol_mom_252_60_10pct | 0.84 | 0.85 | 0.33 | 9.91 | 15/15 | 0.374 | 1.000 | -3.86 | 3/15 | **ROBUST** |
| donchian_50_20 | 0.75 | 0.76 | 0.18 | 16.78 | 15/15 | 0.336 | 1.000 | -4.82 | 1/15 | **ROBUST** |

## OOS Sharpe per path

| strategy | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 | P11 | P12 | P13 | P14 | P15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| buy_hold | 1.65 | 1.22 | 1.40 | 0.81 | 1.17 | 1.42 | 1.61 | 0.85 | 1.28 | 1.17 | 0.60 | 0.96 | 0.76 | 1.12 | 0.69 |
| dual_sma_9_45 | 1.00 | 0.45 | 0.80 | 0.73 | 0.73 | 0.85 | 1.21 | 1.03 | 1.05 | 0.63 | 0.57 | 0.57 | 0.87 | 0.87 | 0.81 |
| vol_mom_252_60_10pct | 1.26 | 0.43 | 0.86 | 0.49 | 0.95 | 0.97 | 1.32 | 0.98 | 1.44 | 0.64 | 0.31 | 0.68 | 0.67 | 1.06 | 0.71 |
| donchian_50_20 | 0.85 | 0.82 | 1.12 | 0.80 | 0.83 | 0.56 | 0.93 | 0.56 | 0.60 | 0.90 | 0.54 | 0.57 | 0.82 | 0.86 | 0.60 |

## Paired per-path comparison vs buy&hold
Paired t = t-stat of (strategy SR - BH SR) across the same 15 paths; paired pos = paths where the rule beat the baseline.

| strategy | paired t | paired pos |
|---|---|---|
| dual_sma_9_45 | -3.82 | 3/15 |
| vol_mom_252_60_10pct | -3.86 | 3/15 |
| donchian_50_20 | -4.82 | 1/15 |

## Headline
All three rules are STABLE (t >= 9.9, 15/15 positive) but NONE beats buy&hold across the 15 OOS paths: paired pos 3/15 (dual_sma), 3/15 (vol_mom), 1/15 (donchian), paired t all < -3.8. The 2019+ holdout PASS was regime-dependent — buy&hold itself did exceptionally well in that window (mean OOS SR 1.11 vs 0.81/0.85). **CPCV downgrades both PASS legs: stable, positive, but no edge over the baseline net of costs across the full window.**

## Notes
- The rules are fixed (no fitted parameters): CPCV measures Sharpe stability across OOS paths, not selection bias.
- t-stat = mean / (SD/sqrt(15)) across paths; HLZ hurdle t >= 3.0 (Harvey-Liu-Zhu 2015 factor-zoo multiple-testing bar).
- PSR/DSR from quantkit.validation vs the CPCV null distribution.
- CPCV does NOT overturn the Phase 3 verdicts on their own terms (the 2019+ holdout stands as measured); it adds the missing context — the holdout was a favorable BH regime, and no rule shows a paired OOS edge over the baseline.
- Read-only over pinned stores; Phase 3 verdicts/SHAs untouched.
