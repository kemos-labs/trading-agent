# Plan: Phase 3 strategy research

Goal: assess the FMZ strategy repository and complete reproducible, cost-adjusted Phase 3 tests of three hypotheses on real data.

## DAG

- [x] T1: Record an evidence-based FMZ repository assessment (files: `knowledge/fmz-strategies-assessment.md`) — no deps
  - Log: catalog is useful for fixed SMA/Donchian hypotheses, not reusable execution code; no license found and multiple leakage/validation hazards documented.
- [x] T2: Implement leakage-safe signal functions and unit tests (files: `src/quantkit/strategies.py`, `tests/test_strategies.py`) — depends T1
  - Log: 106/106 tests pass (11 new point-in-time checks); SMA, Donchian and vol-targeted signals all shift-safe and vectorized.
- [x] T3: Build and run the real-data OOS experiment harness; save immutable inputs/results and experiment log (files: `research/run_phase3.py`, `data/research/phase3/*.csv`, `knowledge/strategy-research/phase3-results.md`) — depends T2
  - Log: harness built with predeclared 2019 holdout, 10 bps cost, one-bar lag; real SPY/QQQ/TLT 3774 bars each (hashes 79d9cd/f584d0/cd13f1); 2 PASS (dual SMA, vol-mom), 1 REJECT (Donchian); offline rerun deterministic.
- [x] T4: Critique results, run the full suite, and update project state/bookkeeping (files: `ROADMAP.md`, `MEMORY.md`, `PROGRESS.md`, this plan) — depends T3
  - Log: 106/106 tests pass; offline rerun deterministic; ROADMAP Phase 3→DONE / Phase 4→ACTIVE with PASS≠approval guard; MEMORY/PROGRESS updated; skills/trend-following added and INDEX bumped; critic passed (no credential or mock-data paths, leakage tests green).

## Predeclared protocol

- Adjusted daily data: SPY, QQQ, TLT, 2010-01-01 through 2024-12-31.
- Development period: through 2018-12-31. Held-out OOS: 2019-01-01 onward.
- Equal-weight portfolio across the three instruments; 10 bps proportional cost per unit turnover; one-bar execution lag via quantkit.
- Fixed hypotheses/parameters (no search on OOS): dual SMA 9/45; Donchian entry/exit 50/20; 252-day momentum with 60-day realized-vol scaling to 10% annual volatility, capped at 1.5x.
- PASS requires positive OOS return, OOS Sharpe > equal-weight buy-and-hold Sharpe, shallower maximum drawdown than buy-and-hold, and positive OOS return on at least 2/3 instruments. Otherwise REJECT; report results regardless.

## Risks

- Yahoo data can be revised or unavailable; cache the successfully validated observations and fail closed on download failure.
- FMZ examples may contain look-ahead or ambiguous order semantics; implement independent close-decision/next-bar-execution rules.
- Three ETFs are not broad evidence of generality; passing means “candidate for further validation,” not tradable approval.

## Verify

- `PYTHONPATH=src .venv/bin/python -m unittest discover -s tests`
- `PYTHONPATH=src .venv/bin/python research/run_phase3.py`
- Re-run from saved CSV inputs and confirm identical reported metrics.
