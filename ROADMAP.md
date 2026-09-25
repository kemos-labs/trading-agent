# ROADMAP.md

Exactly one phase is marked `[ACTIVE]` at any time. Work only inside the active
phase. Move the marker forward only when the current phase's checklist is
complete.

## Phase 0 — Environment [DONE]

- [x] Folder structure: AGENTS.md, ROADMAP.md, PROGRESS.md, skills/INDEX.md,
      knowledge/, library/raw/, src/, notebooks/
- [x] Python env: pandas, numpy, matplotlib, jupyter, vectorbt, yfinance
- [x] Books sorted into /library/raw/ by topic

## Phase 1 — Knowledge extraction [DONE]

- [x] Process every book into /knowledge/ per AGENTS.md rules (30/30
      books, distilled chapter notes)
- [x] Populate core skills: options-pricing, backtesting-framework,
      risk-metrics, data-pipelines (all four present; 33 skills total)
- [x] Start glossary.md

## Phase 2 — Core toolkit [DONE]

- [x] Build reusable Python modules in /src/ from Phase 1 skills: data loader,
      backtest engine, Greeks/IV calculator, position sizing (quantkit 0.2.0,
      all four modules + 95 unit tests passing)
- [x] Each module has a matching skill file

## Phase 3 — Strategy research [DONE]

- [x] Propose and backtest 2–3 strategy hypotheses using the Phase 2 toolkit — dual SMA 9/45, Donchian 50/20, vol-targeted momentum 252/60 (fixed, no OOS search) on real SPY/QQQ/TLT 2010–2024 via quantkit 0.3.0 (`src/quantkit/strategies.py`, 106 tests pass)
- [x] Log each experiment: hypothesis, params, result, verdict — `knowledge/strategy-research/phase3-results.md` (predeclared 2019 holdout, 10 bps, one-bar lag; inputs `data/research/phase3/`, harness `research/run_phase3.py`); assessed FMZ `fmzquant/strategies` catalog in `knowledge/fmz-strategies-assessment.md` (5,807 exports, useful only for fixed defaults, no code copied)

## Phase 4 — Live integration [DONE]

- [x] Connect toolkit to live data feeds — `src/quantkit/live.py` polls yfinance 1d bars, validates via `data_loader`, gap-detects (recent-only), atomic `data/live/*_1d.csv` stores; `research/paper_trade.py --offline` seeds from `data/research/phase3` caches for deterministic replay
- [x] Paper-trading only, no live capital — `src/quantkit/paper.py` (`PaperTrader`) reuses close-decided/next-bar-executed + 10 bps cost, `data/paper/state.json` + append-only `journal.csv` with `paper_only; execution next bar` guard; CLI `research/paper_trade.py` (`--dry-run`, `--reset-state`), demo `notebooks/paper_demo.ipynb` + `notebooks/paper_demo.py`, docs `knowledge/live-integration.md`; 119 tests pass

  Note: Phase 3 yielded 2/3 PASS (dual SMA and vol-mom) and 1/3 REJECT (Donchian) on a narrow 3-ETF, single-holdout protocol. A PASS is *not* tradable approval — broader purged walk-forward and cross-asset checks are still required before any real capital; Phase 4 is paper-only by design.

## Phase 5 — Maintenance (ongoing) [DONE]

- [x] Prune stale skills — audited 36 dirs, 5 leafs tagged [consolidated] (see `skills/INDEX.md`), 0 orphan
- [x] Re-verify formulas — `research/verify_formulas.py` 10 checks PASS + 119/119 tests (report `knowledge/maintenance-2026-08-31.md`)
- [x] Fold in new book material — `library/raw` 33 files / 31 books 0 pending; glossary updated (Paper trading, PTC)

## Phase 6 — Advanced engine (features / portfolio / risk / execution) [DONE]

- [x] T1 Validation lab — `src/quantkit/validation.py` (PurgedKFold + embargo + CPCV + PSR/DSR/deflated Sharpe) + `src/quantkit/factors.py` (IC + quantile spread, winsorize/z-score/neutralize) — re-run Phase 3 legs via it
- [x] T2 Feature + Portfolio labs — `src/quantkit/features.py` (FFD d* + triple-barrier/CUSUM/entropy) + `src/quantkit/portfolio.py` (HRP/risk parity + max-Sharpe/GMV via cvxpy/scipy) — depends T1
- [x] T3 Risk + Execution labs — `src/quantkit/risk.py` (VaR/cVaR, Kupiec/Christoffersen, stressed covariance + PSD, Cholesky scenarios) + `src/quantkit/execution.py` (Lee–Ready, quoted/effective/realized, Roll, Kyle/Amihud/OFI) — depends T2
- [x] T4 TSA + hardening — `src/quantkit/tsa.py` (ARMA/GARCH, CADF/Johansen, Kalman, HMM wrappers) + paper kill-switch (max-DD/position cap) + docs — depends T3

  Note: All 4 T done at once per your request — 5 new labs, quantkit 0.5.0→0.6.0, 134→159 tests green, SHAs 79d9cd/f584d0/cd13f1 preserved, paper-only guard + kill-switch. See `knowledge/engine-upgrade-research-2026-08-31.md` and `plans/phase6-advanced-engine.md`.

## Phase 7 — Maintenance (ongoing) [ACTIVE]

  Resting state (re-activated 2026-09-25 on Phase 8 completion).

  Note: Each T ships tests + `research/verify_formulas.py` check + green `research/run_phase3.py --offline` (SHAs 79d9cd/f584d0/cd13f1). Paper-only guard stays. See `knowledge/engine-upgrade-research-2026-08-31.md` (web + book synthesis, P0/P1/P2) and plan `plans/phase6-advanced-engine.md`.

## Phase 8 — Academic corpus integration (µ → Σ → optimization → attribution) [DONE]

  All 5 T complete 2026-09-25: 411 unique notes indexed, 7 skills, `xsec.py` +
  4 `portfolio`/`execution`/`factors` extensions, `attribute.py`, 180 tests
  green, 17 formula checks PASS, Phase-3 SHAs pinned, paper-only guard intact.
  Plan: `plans/phase8-academic-corpus.md`.

- [ ] T0: Corpus hygiene + index — dedupe 21 ` (1)/(2).md` copies, merge `papers/` overflow, tag book-notes, priority lists + bib join keys (`knowledge/corpus-inventory.md`)
- [ ] T1: µ-models lab — intermediate momentum (12-7), HMM momentum, reversal, BAB/low-vol (sample momentum 59 + anomalies 16 + abnormalreturns 107; mechanism label or no skill; candidate `quantkit/xsec.py`)
- [ ] T2: Σ + costs lab — Almgren impact calibration vs `execution.py`, country/industry neutralization for `factors.py` (marketimpact 10 + returnproperties 31)
- [ ] T3: Optimization lab — FLAM/IC·√BR, error-maximizer guards, shrinkage + norm caps for `portfolio.py`, universal/Kelly notes (portfolioconstruction 172 + universalportfolios 24)
- [ ] T4: Overlays + attribution — CTA convexity, futures carry, FI systematic; `strategy-attribution` skill + `research/attribute.py` on paper journal (trendfollowing 19 + derivatives 14 + yield 6)

  Spine: `knowledge/paleologo-quant-investing/lecture01.md`; plan: `plans/phase8-academic-corpus.md`. Move the marker here only after T0 lands (Phase 7 stays ACTIVE until then). Same gates: 159+ tests, `verify_formulas.py`, Phase-3 SHAs, paper-only guard.
