# Attribution — Phase 3 legs + paper journal

Model cost rate: 0.0010 (10 bps).

| leg | gross | costs | net | cost/gross | turnover | skew |
|---|---|---|---|---|---|---|
| donchian_50_20_QQQ | 1.2660 | 0.0920 | 1.1740 | 0.073 | 0.0241 | -0.760 |
| donchian_50_20_SPY | 0.8048 | 0.0960 | 0.7088 | 0.119 | 0.0254 | -1.062 |
| donchian_50_20_TLT | 0.4199 | 0.0680 | 0.3519 | 0.162 | 0.0180 | -0.094 |
| dual_sma_9_45_QQQ | 1.3650 | 0.0990 | 1.2660 | 0.073 | 0.0262 | -0.605 |
| dual_sma_9_45_SPY | 1.1044 | 0.0960 | 1.0084 | 0.087 | 0.0252 | -0.681 |
| dual_sma_9_45_TLT | 0.7413 | 0.1040 | 0.6373 | 0.140 | 0.0276 | 0.310 |
| vol_mom_252_60_10pct_QQQ | 1.2553 | 0.0492 | 1.2061 | 0.039 | 0.0130 | -0.683 |
| vol_mom_252_60_10pct_SPY | 1.0349 | 0.0716 | 0.9633 | 0.069 | 0.0190 | -1.030 |
| vol_mom_252_60_10pct_TLT | 0.2404 | 0.0858 | 0.1546 | 0.357 | 0.0227 | -0.134 |

## Paper journal integrity
- rows: 12, unit cost |cost/delta|: 166.666667
- relative spread of unit cost: 1.71e-16 (proportionality)
- implied capital per leg: 166666.67
- paper_only guard on every row: True
- verdict: PASS
