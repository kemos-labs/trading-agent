# SESSION-HANDOFF.md
Read this first, before AGENTS.md and ROADMAP.md. This explains what
the project is, what's been decided, what's done, and what's next.
Written for a new AI agent picking this up cold.

## What this project is
A persistent knowledge base that turns ~30 downloaded trading/quant
books into distilled notes and reusable skill files, so any AI coding
agent (regardless of provider/model) can read a few files at session
start and continue exactly where the last session stopped. This is
NOT model fine-tuning — it's an external memory system. AGENTS.md is
the master prompt; ROADMAP.md gates which phase is active; PROGRESS.md
is the append-only session log; skills/ holds the reusable output.

## Current state (as of this handoff — refresh this on every session)
- ROADMAP.md: Phase 0 [DONE], Phase 1 [ACTIVE]
- Books: 30 distinct books inventoried in knowledge/book-inventory.md.
  5 fully processed: Natenberg (Option Volatility & Pricing, 25 ch),
  Leshik & Cralle (Introduction to Algorithmic Trading, 39 ch + appx),
  Halls-Moore (Advanced Algorithmic Trading, 32 ch), Chan (Quantitative
  Trading, 6 ch — notes were found already-written during the 2026-08-04
  audit; they had never been logged/reconciled), Vibe Coding (2 ch,
  O'Reilly Early Release). 25 remain pending.
- skills/INDEX.md: 6 skill files — bayesian-updating, arma-garch-modeling,
  cointegration-testing, kalman-filter-pairs, hmm-regime-detection (all
  Halls-Moore), ai-pair-programming (Vibe Coding). Each has verified
  formulas, code patterns, and pitfalls, not just prose summaries.
- Known gap (from 2026-08-04 audit): the `options-pricing` skill suggested
  in the first PROGRESS entry was never created; ROADMAP Phase 1's core
  skills (options-pricing, backtesting-framework, risk-metrics,
  data-pipelines) are all still missing. PROGRESS.md is authoritative for
  current state; this section is only a snapshot.
- Tools installed: markitdown (PDF→md), pandoc (epub→md, installed as
  a static binary in .venv/pandoc/ since no root/sudo access was
  available for apt/brew).
- Python env: .venv on Python 3.12 (NOT 3.14 — numba/llvmlite, which
  vectorbt depends on, has no 3.14 support). pandas, numpy, matplotlib,
  jupyter, vectorbt, yfinance all confirmed working, including a real
  end-to-end vectorbt backtest.

## The standing per-book loop (use this every session, unless told otherwise)
```
Read AGENTS.md, ROADMAP.md, and the last 5 entries of PROGRESS.md.
Process the next unprocessed book from knowledge/book-inventory.md
(convert epub with pandoc or PDF with markitdown first if needed).
Write chapter notes as usual, AND promote any reusable technique to a
skills/<topic>/SKILL.md file before finishing — don't leave skill
promotion for a later pass. Update skills/INDEX.md if any were added.
Stop after one book.
```

## Decisions already made — do not re-litigate these
- Python 3.12, not 3.14 (dependency support).
- Pandoc installed as a static binary, not via system package manager
  (no root access on this machine).
- No local LLM fine-tuning has happened yet — it is planned but gated
  behind having enough skill files to build a real training dataset
  (see "Fine-tuning plan" below). Do not suggest starting from a
  from-scratch/uninitialized model (e.g. any "toy" or
  architecture-test checkpoint) — it has no language ability to build
  on and cannot be meaningfully fine-tuned on a small dataset.
- Fine-tuning base model choice: Qwen2.5-3B-Instruct (open, ungated,
  fits 6GB VRAM at 4-bit via Unsloth). Llama-3.2-3B-Instruct was the
  alternative but requires a gated Hugging Face license acceptance.
- Fine-tuning tool choice: Unsloth (lowest VRAM footprint of the
  available options).
- Hardware: Ryzen 5 4800H (CPU, 8-core/16-thread), no dedicated GPU
  confirmed — assume 6GB VRAM ceiling for any local model work until
  told otherwise. This is enough to RUN a small quantized model but
  NOT enough to pretrain one from scratch.

## Fine-tuning plan (not started — do not begin without explicit go-ahead)
1. Confirm Unsloth + Qwen2.5-3B-Instruct (4-bit) loads and report VRAM
   usage — no training, just a load test.
2. Once more skill files exist (target: after several more books are
   processed, not just the current 5), convert every skills/<topic>/
   SKILL.md into 3-5 instruction/output JSON training pairs, saved to
   training/dataset.json.
3. Run a LoRA fine-tune (rank 16, 3 epochs as a starting point) on
   that dataset, save the adapter to models/trading-lora-v1/.
Purpose of the fine-tune: make a local model that talks in the
project's terminology/style more consistently. It does NOT add new
knowledge beyond what's already in the skill files, and it does NOT
replace the knowledge-base system — it's an optional additive layer.

## What "closing the gaps" means for the next agent
Before continuing blindly, audit the project against this document and
flag anything that's drifted or is missing. Specifically check:
- Does ROADMAP.md still show Phase 1 [ACTIVE] with exactly one phase
  marked active? If not, fix it and log why in PROGRESS.md.
- Does book-inventory.md match what's actually in library/raw/? Books
  can be added between sessions without the inventory being updated —
  re-scan and reconcile if counts don't match.
- Are new skill files actually being promoted per book, or is the
  agent drifting back to chapter-notes-only? Spot check the last 2-3
  processed books' worth of skills/ output against their knowledge/
  notes to confirm reusable techniques aren't being left un-promoted.
- Is PROGRESS.md being appended to every session, append-only, with
  Did/Next/Blockers? Flag any session that skipped logging.
- Any book that repeatedly fails to convert cleanly (garbled OCR,
  broken epub structure, etc.) — flag it in PROGRESS.md rather than
  silently skipping or producing low-quality notes from bad extraction.
Give me a short recommendation list for anything found broken or
drifted, then resume the standing per-book loop above.
