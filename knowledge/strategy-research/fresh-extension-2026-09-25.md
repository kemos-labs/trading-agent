# Fresh extension diagnostic — 2026-09-25

Fixed Phase 3 rules (same params, 10 bps, next-bar) on spliced base+fresh.
Diagnostic only — phase3 verdicts/SHAs untouched.

| sym | anchor ratio | base bars | fresh bars | full range |
|---|---|---|---|---|
| SPY | 1.02054 | 3774 | 433 | 2010-01-04 → 2026-09-24 |
| QQQ | 1.00907 | 3774 | 433 | 2010-01-04 → 2026-09-24 |
| TLT | 1.07666 | 3774 | 433 | 2010-01-04 → 2026-09-24 |

Common bars: 4207 (2010-01-04 → 2026-09-24)

| strategy | window | total | CAGR | Sharpe | MaxDD |
|---|---|---|---|---|---|
| dual_sma_9_45 | full | 174.32% | 6.23% | 0.79 | -13.62% |
| dual_sma_9_45 | 2025+ | 9.44% | 5.39% | 0.66 | -6.98% |
| donchian_50_20 | full | 105.27% | 4.40% | 0.68 | -18.51% |
| donchian_50_20 | 2025+ | 0.82% | 0.47% | 0.11 | -6.69% |
| vol_mom_252_60_10pct | full | 119.67% | 4.83% | 0.79 | -11.23% |
| vol_mom_252_60_10pct | 2025+ | 4.28% | 2.47% | 0.38 | -10.00% |
| buy_hold | full | 589.59% | 12.26% | 1.02 | -30.06% |
| buy_hold | 2025+ | 21.07% | 11.77% | 0.86 | -14.36% |

## Caution
2025+ Sharpe ratios rest on ~433 bars (~1.7 y) — wide confidence intervals; treat as a freshness check, not a verdict change. The anchor splice carries a ≤0.3% December seam (December distributions); return-based rules are invariant to it except at the seam bar. Massive free answers DELAYED; Alpha Vantage compact was superseded by Massive windows (3 AV calls burned, within budget).
