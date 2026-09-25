# Plan: Phase 4 — Live integration (paper-trading only)

Goal: connect quantkit to live Yahoo Finance feeds with a paper-trading runtime that reuses Phase 3's cost/lag discipline and never places real orders.

DAG:
- [x] T1: Live-feed adapter — `src/quantkit/live.py` + `tests/test_live.py` — no deps
  - Log: yfinance polling with validate_ohlcv, gap detection (B freq), atomic store write, fail-closed; 6 tests pass.
- [x] T2: Paper-trading engine — `src/quantkit/paper.py` + `tests/test_paper.py` — depends T1
  - Log: close-decided/next-bar-executed, 10 bps cost per leg, append-only journal, JSON state, paper_only guard, idempotent bar handling; 7 tests pass; 119 total tests green.
- [x] T3: CLI / demo + integration proof — `research/paper_trade.py`, `notebooks/paper_demo.ipynb` (or md), `knowledge/live-integration.md` — depends T2
  - Log: CLI with --offline/--dry-run/--reset-state, offline seeds Phase-3 caches, paper step is idempotent per bar_date and journals paper_only; demo notebook + py, live-integration docs; offline dry_run replay verified (6 legs → cost-aware equity), online path fail-closed.
  - Verify: 119/119 tests pass; `research/paper_trade.py --offline --dry-run` deterministic; live store gap detection now recent-only (1 holiday 2024-12-25).

Risks: Yahoo gaps/revisions, clock skew, no live capital. Mitigations: fail-closed validation (reuse data_loader), gap detection, cached fallback only in paper replay mode, explicit paper-only guard.

Verify:
- `PYTHONPATH=src .venv/bin/python -m unittest discover -s tests` (all 106 + new)
- `PYTHONPATH=src .venv/bin/python -m research.paper_trade --dry-run --offline` replays cached Phase 3 bars without network
- No credentials, no `order.*live` calls, `paper` journal is append-only CSV.

Notes: Expands on Phase 3 PASS notes — broader walk-forward still required before any capital. FMZ clone remains docs-only.
