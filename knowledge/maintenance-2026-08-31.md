# Maintenance — 2026-08-31

Re-verification run at 2026-09-25T22:32:23.051897+00:00 — all checks PASS.

## Formula checks
- BSM ATM call/put vs Hull reference — PASS (tol 0.02)
- Put-call parity — PASS
- Greeks delta vs finite diff (eps 1.0) — PASS (tol 0.01)
- Implied vol roundtrip — PASS (tol 1e-4)
- Vectorized backtest no-lookahead — PASS
- Sharpe / DD — PASS
- Split/dividend adjustment invariance — PASS
- Discrete + continuous Kelly — PASS
- Vol target weight bounds — PASS
- SMA / Donchian point-in-time — PASS

## Tests
- `PYTHONPATH=src .venv/bin/python -m unittest discover -s tests` — 190/190 pass (180 Phase 8 + 10 fresh-data)

## Phase 8 T1 checks
- xsec 12-2 log-split identity F(12,2)==F(12,7)+F(7,2) — PASS (tol 1e-12)
- xsec skip-month exclusion — PASS
- xsec WML dollar-neutrality — PASS
- residual identity Resid = r − mu − CF — PASS

## Skills
- Audited 36 dirs, 5 leafs tagged [consolidated], 0 orphan (see skills/INDEX.md header).

## Books
- 33 files in library/raw (31 distinct books, 0 pending per knowledge/book-inventory.md); FMZ catalog (strategies/ 7853bb2) remains docs-only.

## Data stores
- `data/research/phase3` SHAs: SPY 79d9cd3695cc / QQQ f584d023aa16 / TLT cd13f15ccd35 (3774 bars)
- `data/live/*_1d.csv` seeded offline, paper journal `data/paper/journal.csv` (paper_only guard).

No stale-skill deletions this cycle; re-verification passed.
