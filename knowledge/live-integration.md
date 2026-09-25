# Live integration — paper-trading only (Phase 4)

## What it is
A thin live-feed + paper-trading layer on top of quantkit that **never places real orders**. It polls Yahoo Finance 1d bars via `quantkit.live`, validates with `data_loader`'s fail-closed checks, and steps a `quantkit.paper.PaperTrader` that reuses Phase 3's cost/lag discipline (close-decided → next-bar-executed, 10 bps per unit turnover by default).

State is persisted locally so the process can restart:
- `data/live/*_1d.csv` — per-symbol append-only daily stores (atomic write via `*.tmp` → `*.csv`)
- `data/paper/state.json` — equity, peak, per-leg target/exposure/bar_date
- `data/paper/journal.csv` — append-only decisions (timestamp, symbol, strategy, bar_date, close, target, exposure, delta, cost, equity, peak, note)

No brokerage credentials, no order API, `paper_only` guard on every journal row.

## When to use
- Daily paper run for the two Phase 3 PASS legs (`dual_sma_9_45`, `vol_mom_252_60_10pct` on SPY/QQQ/TLT) before broader walk-forward validation.
- Offline replay for tests/docs: copy `data/research/phase3/ohlcv_*.csv` into `data/live/` without touching the network.

## How to run
```bash
# offline deterministic replay (no network, uses Phase 3 caches)
PYTHONPATH=src .venv/bin/python research/paper_trade.py --offline --dry-run
PYTHONPATH=src .venv/bin/python research/paper_trade.py --offline

# online poll + paper step (fails closed on feed outage — use --offline to replay)
PYTHONPATH=src .venv/bin/python research/paper_trade.py
# custom universe / fresh start
PYTHONPATH=src .venv/bin/python research/paper_trade.py --symbols SPY QQQ --strategies dual_sma_9_45 --reset-state --offline
```

Cron example (1x/day after close, e.g. 22:00 UTC):
```
0 22 * * * cd /home/kalde/trading-agent && PYTHONPATH=src .venv/bin/python research/paper_trade.py >> data/paper/cron.log 2>&1
```

## Feed adapter (`quantkit.live`)
- `update_store(symbol, store_dir, lookback_days=10)` fetches the last N 1d bars, merges with the existing store (dedup keep-last), validates via `normalize_columns`/`validate_ohlcv`, detects business-day gaps (`B` freq) and warns, then atomic-writes.
- `load_store`, `store_path`, `detect_gaps`, `fetch_many` are the public helpers.
- Intraday (`!=1d`) is warned and not used for Phase 4 stores.

Fail-closed: fetch/validation exceptions propagate; the CLI exits 2 and suggests `--offline`. No mock data is ever invented.

## Paper engine (`quantkit.paper`)
- `PaperTrader(capital, ptc, symbols, strategies, store_dir, state_path, journal_path)` — capital is split equally across `len(symbols)*len(strategies)` legs for cost accounting.
- `step(dry_run=False)`:
  - Loads each `store_dir/SYM_1d.csv` (error if missing/short).
  - `close, rets = store["close"], compute_returns(close, log=False)`; `target = STRATEGY_MAP[name](close, rets).iloc[-1]` (point-in-time safe, same functions as Phase 3).
  - `delta = target - prev_target`, `cost = ptc * |delta| * (equity / n_legs)`, equity `−= cost`, `exposure = target` for next bar (execution next bar, same as vectorized `shift(1)`).
  - Skips legs already at `bar_date` (idempotent), appends one row per new leg to `journal.csv`, persists `state.json` unless `dry_run`.

Paper view: `trader.positions_df()`, `trader.equity()`.

## Verification
- `PYTHONPATH=src .venv/bin/python -m unittest discover -s tests` — 119 tests (incl. `test_live` 6, `test_paper` 7) pass.
- `PYTHONPATH=src .venv/bin/python research/paper_trade.py --offline --dry-run` — deterministic replay from `data/research/phase3` without network.
- Journal rows always contain `paper_only; execution next bar`.

## Limitations & next steps
- Single holdout (2019–2024) and 3-ETF universe are insufficient for capital — broader purged walk-forward and cross-asset checks still required before any real trading (see Phase 3 report).
- Daily only; corporate actions are auto-adjusted by yfinance — verify `store` SHAs against `data/research/phase3` when replaying.
- No risk kill-switch yet — add max-DD or max-position guard before longer paper runs.
