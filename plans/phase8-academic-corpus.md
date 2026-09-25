# Plan: Phase 8 — Academic corpus integration (µ → Σ → optimization → attribution)

Goal: turn the 634-note paper corpus (`drive-download-20260925T215026Z-1-001/`,
`bibliography.bib`, FINC-B8420 Lecture 1) from a file dump into executable
knowledge — prioritized skills and a small number of new `quantkit` modules —
without breaking the 159-test, SHA-pinned, paper-only discipline.

Spine: Paleologo pipeline (see `knowledge/paleologo-quant-investing/lecture01.md`).
Every T names its spine block; every promoted skill names its claimed mechanism
(risk / liquidity / funding / flow / information). No mechanism → no skill.
Corpus index: `knowledge/corpus-inventory.md`.

Rules for all Ts (from AGENTS.md Corpus section):
one note at a time, ≤5 notes per turn for synthesis; cite corpus path + bib key;
dedupe ` (1).md` copies before use; formulas verified against a reference value.

## DAG

- [x] **T0: Corpus hygiene + index** — DONE 2026-09-25: 634 → 425 unique notes,
  merge `papers/portfolioconstruction/` into the top-level namespace; ignore
  `papers/Untitled/` + `Welcome.md`; tag `yield/` book-notes vs paper-notes;
  build a per-topic priority list (notes with Approach(detailed) formulas first);
  record bib join keys where filenames embed source PDFs. No code. Depends: none.
  - Exit: `knowledge/corpus-inventory.md` updated with canonical counts + priority
    lists; dupe set deleted or quarantined with a log line in PROGRESS.md.
  - DONE: 209 byte-identical dupes quarantined (`_quarantine_dupes/` + MANIFEST,
    nothing deleted); 12 same-name DIFFER groups kept as alt distillations;
    bib join WEAK (~6/131) so corpus path is primary citation; formula-density
    priority index in `knowledge/corpus-inventory.md`.

- [x] **T1: µ-models lab** — DONE 2026-09-25: read Novy-Marx 12-7, DJK-HMM crash
  overlay, Da-Liu-Schaumburg reversal ×2, HLZ t≈3.0 hurdle. 3 skills
  (`intermediate-momentum`, `residual-reversal`, `factor-zoo-hurdle`) + new
  `src/quantkit/xsec.py` (log formation, Novy-Marx split identity, decile/WML
  incl. within-industry, JT overlapping, residual score; 10 tests) + checks
  10–11. 169 tests green, Phase-3 SHAs unchanged.

- [x] **T2: Σ + costs lab** — DONE 2026-09-25: read Almgren direct-estimation
  (γ=0.314/η=0.142 closed forms) + Heston-Rouwenhorst dummy regression (4.5×
  country variance). `execution.almgren_impact` + `factors.pure_factor_returns`
  with 6 tests + checks 12–13 vs paper numbers. 2 skills (`impact-calibration`,
  `country-industry-neutralization`). Depends: T1 (µ-leg defines what costs
  must beat).
  - Exit: skills + `verify_formulas.py` checks comparing module outputs to at
    least one paper-reported number each (impact coefficient, variance share).

- [x] **T3: Optimization lab** — DONE 2026-09-25: read CDT-2006 FLAM (exact IR,
  TC, attribution), Jorion Bayes-Stein (w formula), Tu-Zhou 1/N anchor.
  `portfolio.py` +5 fns (fundamental_law_ir, transfer_coefficient,
  bayes_stein_means, ledoit_wolf_shrinkage, combine_with_1n) with 5 tests +
  checks 14–16. Skill `allocation-discipline`. 180 tests green.

- [x] **T4: Overlays + attribution close-out** — DONE 2026-09-25: read trend
  convexity (variance-spread identity), Erb-Harvey commodities (+4.5% divers.
  return, roll ±9pp), Grinold attribution. Skill `strategy-attribution` +
  `research/attribute.py` (per-leg gross/cost/net, cost/gross flag, turnover,
  skew + journal proportionality/guard PASS) →
  `knowledge/strategy-research/attribution-2026-09-25.md`. Check 17 (identity
  to 1e-9). Exit gates: 180 tests green, verify PASS, SHAs pinned, guard intact.

## Risks
- Corpus scale tempts bulk ingestion — enforce ≤5 notes/turn; the index is the
  memory, not the context.
- Alpha-Zoo overfitting — abnormalreturns/ (107) is evidence for skepticism, not
  signals; every T1 candidate needs a mechanism + OOS net-of-costs check.
- Scope creep across 172 portfolio notes — T3 samples FLAM/shrinkage/norm-cap
  notes first; the rest stay indexed, unprocessed.
- Dependency bloat — no new `.venv` deps without a textbook/paper reference
  check first (per AGENTS.md Tools rule); Python stays 3.12.

## Verify (must stay green at every T)
- `PYTHONPATH=src .venv/bin/python -m unittest discover -s tests` — 180 pass
- `PYTHONPATH=src .venv/bin/python research/verify_formulas.py` — PASS
- `PYTHONPATH=src .venv/bin/python research/run_phase3.py --offline` — SHAs
  79d9cd/f584d0/cd13f1, verdicts unchanged
- `PYTHONPATH=src .venv/bin/python research/paper_trade.py --offline --dry-run` —
  `paper_only; execution next bar`, idempotent per bar_date
- Each new module/skill cites corpus path + bib key + spine block + mechanism

## Plan rule
T0 first, alone (hygiene before synthesis). T1→T4 in spine order since costs
gate µ-claims and net-IR gates optimization claims. Keep Phase 7 ACTIVE until
T0 lands; then move the marker.
