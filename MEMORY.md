# MEMORY.md — Project Memory

Durable snapshot of what this project is, its current state, and standing
decisions. Read this first on every new session, then ROADMAP.md, PROGRESS.md,
and skills/INDEX.md. Update this file whenever the state it describes changes.

## What this project is

A persistent knowledge base and quantitative trading toolkit. ~30 trading/quant
books are distilled into chapter notes (`knowledge/`) and reusable skill files
(`skills/<topic>/SKILL.md`), and those skills are compiled into a working
Python toolkit (`src/quantkit`). The whole system is an external memory: any AI
coding agent can read a few files at session start and continue where the last
session stopped. This is NOT model fine-tuning — the fine-tune is a separate,
optional additive layer that is gated and has not started.

## Current state (as of 2026-09-25 — Phase 8 DONE, Phase 7 ACTIVE)

- **Phase 8 complete (2026-09-25, T0→T4 single session)**: 634 → 411 unique notes (`knowledge/corpus-inventory.md`, 223 quarantined w/ manifest); Lecture 1 distilled (`knowledge/paleologo-quant-investing/lecture01.md`); 7 skills (intermediate-momentum, residual-reversal, factor-zoo-hurdle, impact-calibration, country-industry-neutralization, allocation-discipline, strategy-attribution); new `src/quantkit/xsec.py` (module 15) + `execution.almgren_impact` + `factors.pure_factor_returns` + 5 `portfolio` fns (FLAM/TC/Bayes-Stein/Ledoit-Wolf/1N) + `research/attribute.py` → `knowledge/strategy-research/attribution-2026-09-25.md`. **180 tests green, 17 checks PASS, Phase-3 SHAs pinned, paper-only guard intact.** Plan all checked; ROADMAP Phase 8 [DONE], Phase 7 [ACTIVE] resting.
- **AGENTS.md upgraded**: corpus access rules (never bulk-load, ≤5 notes/turn), paper-promotion traceability (corpus path + spine block + mechanism), engine rule covers Phase 8 plan, test gate 180.
- **ROADMAP**: Phase 7 — Maintenance (ongoing) still `[ACTIVE]`; Phase 8 — Academic corpus integration (µ → Σ → optimization → attribution) `[PROPOSED]` per `plans/phase8-academic-corpus.md`. Marker moves only after T0 hygiene lands.

- **ROADMAP**: Phases 0–6 `[DONE]`; Phase 8 corpus integration `[DONE]` (T0→T4, 411 notes, 7 skills, xsec + 8 fn extensions, attribution); Phase 7 `[ACTIVE]` resting. `AGENTS.md` corpus-ready (never bulk-load, ≤5 notes/turn, spine+mechanism traceability, 180-test gate).
- **Books**: 31 books fully processed and distilled into `knowledge/`; 0 pending. Inventory lives in `knowledge/book-inventory.md`.
- **Skills**: 44 skill files in `skills/`, indexed in `skills/INDEX.md`. Phase 8 additions (all with corpus path + spine + mechanism): `intermediate-momentum`, `residual-reversal`, `factor-zoo-hurdle`, `impact-calibration`, `country-industry-neutralization`, `allocation-discipline`, `strategy-attribution` — plus `fresh-data` (terminal-backed pulls). Core ones: options-pricing, backtesting-framework, risk-metrics, data-pipelines.
- **Toolkit**: `src/quantkit` v0.8.0 — data loader, backtest engine, Greeks/IV, sizing, strategies, live + paper, validation + factors, `features`/`portfolio`/`risk`/`execution`/`tsa` + paper kill-switch **+ Phase 8: `xsec`, Almgren impact, HR dummy regression, FLAM/TC/shrinkage suite + `fresh` (terminal-backed pulls, 454 fresh bars/symbol → 2026-09-24)**. All 190 unit tests pass.
- **Strategy research**: 3 fixed hypotheses tested on real SPY/QQQ/TLT 2010–2024 (equal-weight, 10 bps, one-bar lag, predeclared 2019 holdout). Results in `knowledge/strategy-research/phase3-results.md`, harness `research/run_phase3.py`, inputs `data/research/phase3/`: **2 PASS** (dual SMA 9/45, vol-mom 252/60) and **1 REJECT** (Donchian 50/20). A PASS is not tradable approval.
- **FMZ catalog**: `fmzquant/strategies` cloned at `strategies/` (commit 7853bb2, ~5,807 Markdown exports, 98 MB) and assessed in `knowledge/fmz-strategies-assessment.md`. No license file found; no code copied; only fixed idea defaults were taken.
- **Live integration**: `src/quantkit/live.py` polls yfinance 1d bars into `data/live/*_1d.csv` (validated, atomic, recent-gap warn, fail-closed); `src/quantkit/paper.py` (`PaperTrader`) steps paper-only with `data/paper/state.json` + append-only `journal.csv` (`paper_only; execution next bar`); CLI `research/paper_trade.py` supports `--offline` deterministic replay from `data/research/phase3` and `--dry-run`; docs in `knowledge/live-integration.md`, demo in `notebooks/paper_demo.ipynb` + `.py`. Paper run on 2024-12-31 bar: 6 legs, equity 999,607 after ~393 in costs (10 bps). No real orders, no credentials. Phase 4 is paper-only by design; real capital still gated on broader walk-forward checks.

## Standing decisions — do not re-litigate

- Python 3.12, NOT 3.14 (numba/llvmlite, which vectorbt depends on, has no
  3.14 support). Env: `.venv` with pandas, numpy, matplotlib, jupyter,
  vectorbt, yfinance.
- Pandoc installed as a static binary at `.venv/pandoc/pandoc` (no root
  access for apt/brew). markitdown at `.venv/bin/markitdown` converts PDFs.
- No local LLM fine-tuning has happened. If it ever starts: base model
  Qwen2.5-3B-Instruct, tool Unsloth, 6GB VRAM ceiling (Ryzen 5 4800H, no
  dedicated GPU). Gated behind having enough skill files to build a real
  training dataset. Do NOT suggest a from-scratch/untrained base model.

## Data integrity & performance rules

- Never present mock/simulated data as real; fail closed if a data source is
  unavailable.
- Verify every formula against a known reference value before trusting it.
- Prefer vectorized pandas/numpy over loops.

## Session bookkeeping (mandatory, every session)

- Append a dated entry to `PROGRESS.md` (Did / Next / Blockers).
- Update `skills/INDEX.md` if skills changed.
- Update the `ROADMAP.md` phase marker if the current phase is complete.
- Update this file if the state above changes.
