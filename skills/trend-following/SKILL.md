# Trend following — leakage-safe SMA, Donchian and vol-targeted momentum

## Name
trend-following

## Description
Fixed-hypothesis trend rules expressed as close-decided, next-bar-executed targets for quantkit's vectorized backtester. Evaluated as equal-weight portfolios with proportional costs and a predeclared holdout.

## When to use
- Screening a price series for a slow-trend bias without searching thresholds on the evaluation window.
- Comparing simple trend baselines (SMA cross, channel breakout, momentum) on the same cost and lag discipline before adding filters.

## Method / formula / code

### No-look-ahead discipline
All signals are targets decided at bar close `t` and held from `t+1` only. The caller must pass them to `vectorized_backtest`, which does `position.shift(1) * returns`. Channels use `rolling(...).max().shift(1)` so the current close cannot define its own breakout level.

### Dual SMA (long/flat)
```python
from quantkit.strategies import dual_sma_position
pos = dual_sma_position(close, fast=9, slow=45, long_only=True)
# pos[t] = 1 if SMA_fast(t) > SMA_slow(t) else 0, 0 during warm-up
bt = vectorized_backtest(returns, pos, ptc=0.001)
```

### Donchian breakout (long/flat, 50/20)
Enter when close exceeds the prior 50-bar high; exit when close falls below the prior 20-bar low. Position persists between events.
```python
from quantkit.strategies import donchian_breakout_position
pos = donchian_breakout_position(close, entry_window=50, exit_window=20)
```

### Vol-targeted momentum (252/60, 10% target, cap 1.5x)
Direction from 252-day price change, exposure scaled by trailing realized vol:
```python
from quantkit.strategies import vol_targeted_momentum_position
pos = vol_targeted_momentum_position(close, returns, momentum_lookback=252,
                                     vol_lookback=60, target_vol=0.10, max_weight=1.5)
# weight = target_vol / (rolling_std(60) * sqrt(252)), clipped; direction = sign(momentum)
```

Portfolio construction tested in Phase 3: mean of per-asset `net` returns (equal weight), 2010-01-01 → 2024-12-31, development ≤ 2018-12-31, holdout ≥ 2019-01-01.

## Known pitfalls
- SMA and Donchian are whipsaw-prone in range-bound regimes; turnover (≈2–2.5% daily for the defaults) still costs 10 bps per unit shift.
- Donchian `close == highest(close, N)` tests that include the current bar coincide with the close by construction — they are not breakouts. Always shift channels by one bar.
- `vol_target_weight` needs ≥ lookback valid returns; early bars are zero weight. Momentum can be positive while vol is unmeasured — the product is correctly zero.
- Three-ETF, single-holdout evidence is not tradable validation. A PASS only means the fixed hypothesis survived one real-data screen.

## Source book / traceability
FMZ `fmzquant/strategies` catalog (commit 7853bb2, 2025-04-30) supplied the fixed defaults (SMA 9/45, Donchian 50/20) assessed in `knowledge/fmz-strategies-assessment.md`; implementation is independent and leakage-tested (`tests/test_strategies.py`). Vol scaling follows the Kelly/vol-targeting skill (Sinclair ch8, Carver ch5/9/10). Phase 3 numbers in `knowledge/strategy-research/phase3-results.md`.

## Implementation
`src/quantkit/strategies.py` (tests: `tests/test_strategies.py`; harness: `research/run_phase3.py`).
