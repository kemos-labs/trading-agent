# Plan: Phase 5 — Maintenance (ongoing)

Goal: keep the knowledge base and toolkit truthful — prune/consolidate stale skills, re-verify every formula against a known reference, and confirm book inventory is complete.

DAG:
- [x] T1: Skill audit — de-duplicate/consolidate leaf skills now covered by `options-pricing`, `backtesting-framework`, `trend-following`, `live-paper` (files: `skills/INDEX.md`, skill headers) — no deps
  - Log: 36 dirs audited, 0 orphan, 5 leaf skills tagged [consolidated] (binomial, MC, vectorized, walk-forward, purged); maintenance header added.
- [x] T2: Formula re-verification — run `research/verify_formulas.py` against textbook references and existing unit-test oracles, write `knowledge/maintenance-2026-08-31.md` — depends T1
  - Log: 10 checks PASS (BSM ATM 10.45, parity, delta FD, IV roundtrip, no-lookahead, Sharpe/DD, split invariance, Kelly, vol weight, point-in-time); 119/119 tests pass; report `knowledge/maintenance-2026-08-31.md`.
- [x] T3: Book-inventory & glossary sweep — confirm 0 pending, update glossary if gaps, log completion — depends T2
  - Log: `library/raw` 33 files / 31 distinct books 0 pending verified; `knowledge/glossary.md` added Paper trading + PTC (189→192 lines); `knowledge/book-inventory.md` unchanged; Phase 5 checklist now satisfied (ongoing).

Risks: over-pruning traceability (keep leaf files, just mark consolidated); verification drift from yfinance revisions (use cached SHAs).

Verify:
- `PYTHONPATH=src .venv/bin/python -m unittest discover -s tests` (119 pass)
- `PYTHONPATH=src .venv/bin/python research/verify_formulas.py` (all checks pass)
- `skills/` count and `INDEX.md` leaves no orphan skill.
