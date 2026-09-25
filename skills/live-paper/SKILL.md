# Live feed + paper trading — paper-only, fail-closed

## Name
live-paper

## Description
Daily live polling from yfinance into validated per-symbol stores and an incremental paper-trading runtime that reuses Phase 3's cost/lag discipline. Never places real orders; append-only journal.

## When to use
- Daily paper run after close for Phase 3 PASS legs (or any `STRATEGY_MAP` subset).
- Offline replay from `data/research/phase3` caches when Yahoo is unavailable or for tests.

## Method / formula / code

### Feed adapter (`quantkit.live`)
```python
from quantkit.live import update_store, load_store, detect_gaps
df = update_store("SPY", store_dir="data/live", lookback_days=10)  # validated, atomic
# gaps are business-day diffs; only recent (last 14d) gaps warn — holidays are expected
```

Store is `data/live/SYM_1d.csv` (CSV with `date,open,high,low,close,volume`). Merges fresh fetch with existing store, dedup keep-last, `validate_ohlcv` (fail-closed), `detect_gaps` (B freq). `fetch_many` loops symbols. Inject `fetcher` for tests.

### Paper engine (`quantkit.paper`)
```python
from quantkit.paper import PaperTrader
tr = PaperTrader(capital=1_000_000, ptc=0.001,
                 symbols=("SPY","QQQ","TLT"),
                 strategies=("dual_sma_9_45","vol_mom_252_60_10pct"),
                 store_dir="data/live",
                 state_path="data/paper/state.json",
                 journal_path="data/paper/journal.csv")
out = tr.step()  # dry_run=True to not persist
# out rows: timestamp,symbol,strategy,bar_date,close,target,exposure,delta,cost,equity,peak,note
```

Discipline: `target = strategy(close, rets).iloc[-1]` at last close, `delta = target - prev_target`, `cost = ptc * |delta| * (equity / n_legs)`, `exposure = target` for next bar (next-bar execution, same as `vectorized_backtest` `shift(1)`). Idempotent per `bar_date`; journal always contains `paper_only; execution next bar`.

### CLI
```bash
PYTHONPATH=src .venv/bin/python research/paper_trade.py --offline --dry-run
PYTHONPATH=src .venv/bin/python research/paper_trade.py --offline
PYTHONPATH=src .venv/bin/python research/paper_trade.py  # online poll, fail-closed
```

Offline seeds `data/research/phase3/ohlcv_*.csv` → `data/live/*_1d.csv` for deterministic replay.

## Known pitfalls
- yfinance is adjusted (`auto_adjust=True`); compare live store SHAs against Phase 3 caches when debugging corporate actions.
- `detect_gaps` with `B` freq flags holidays — only recent gaps warn; don't treat 100+ holiday gaps as outages.
- Capital is split equally across legs for cost accounting; equity is paper cash, not brokerage value.
- No risk kill-switch yet; add max-DD or position cap before long-running paper.

## Source book / traceability
Reuses `data-loader` (Chan ch3 validation) and `trend-following` signals; live polling is Phase 4 glue. No FMZ execution code copied.

## Implementation
`src/quantkit/live.py` (tests `tests/test_live.py`), `src/quantkit/paper.py` (tests `tests/test_paper.py`), CLI `research/paper_trade.py`, docs `knowledge/live-integration.md`, demo `notebooks/paper_demo.ipynb`.

## Verification
- `PYTHONPATH=src .venv/bin/python -m unittest discover -s tests` — 119 tests pass
- `research/paper_trade.py --offline --dry-run` — no network, journal rows carry `paper_only` note
