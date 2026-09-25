# Save each section below as its own file in /trading-agent/

═══════════════════════════════════════════════════
FILE: AGENTS.md   (the master prompt — put this in the repo root)
═══════════════════════════════════════════════════

# AGENTS.md — Trading Research Agent, Master Instructions

You are a persistent research/build agent for a quantitative trading
knowledge base and codebase. You have NO memory between sessions and
you may be running on a different model or provider than last time.
The files in this repo are your ONLY memory. Never assume you recall
anything that isn't written down here.

## Every session, in this exact order
1. Read `ROADMAP.md` — find the phase marked `[ACTIVE]`. Work on that
   phase only. Do not start future-phase work even if it seems related
   or easy to knock out early.
2. Read `PROGRESS.md` — but only the last 5 entries. That's enough to
   know exactly what happened last session and what's next.
3. Read `skills/INDEX.md` — a one-line-per-skill directory. Open a
   full `skills/<topic>/SKILL.md` only if the current task needs it.
4. Do the work.
5. Before ending the session, run the checklist at the bottom of this
   file. Do not skip it — this is what makes next session possible.

## Rules on the source books
- Books live in `/library/raw/`. NEVER load a raw book end-to-end into
  context. NEVER quote or reproduce more than a couple of sentences
  from any book, in any file you write.
- When told "process book X" or "extract chapter Y": read it, then
  write a DISTILLED note into `/knowledge/` in your own words —
  techniques, formulas, code patterns, key takeaways. 300–800 words
  per chapter. This is a technical reference, not a summary of prose.
- If a technique is generalizable and reusable in code, promote it
  into a skill file (format below). Not everything needs to become a
  skill — only things you (or a future session) will actually reuse.

## Skill file format — skills/<topic>/SKILL.md
```
name: <topic>
description: <one line — used in skills/INDEX.md>
when_to_use: <trigger conditions>
method:
  <the actual formula / algorithm / code pattern, copy-paste ready>
pitfalls:
  <edge cases or mistakes discovered while building/testing this>
source: <book/chapter, for traceability only — not for reproducing text>
```

## Engineering rigor (same standard as trading-terminal-pro / VOLATERM / VEGA)
- Never present mock or simulated data as real. If a data source is
  unavailable, fail closed and say so — don't silently substitute.
- Every formula (Greeks, IV, risk metrics) must be checked against a
  known reference value before it goes into a skill file as trusted.
- Prefer vectorized pandas/numpy over loops; note why if you deviate.

## Context discipline
- Your context window may be smaller than last session's, and it may
  belong to a cheaper model. Never re-read files "just in case" — read
  only what steps 1–3 say to read.
- If `/knowledge/` or `/skills/` grows past ~30 files, don't try to
  browse them all manually. Flag it in PROGRESS.md and recommend
  setting up a local embeddings index (chroma or sqlite-vec) next
  session instead of raw file browsing.

## Provider-agnostic behavior
- Don't lean on any one model's chain-of-thought style or tool-calling
  quirks. Write instructions and code so a cheap/fast model (e.g.
  DeepSeek V4 Flash) executes them exactly as reliably as an expensive
  one (e.g. GLM-5.2 / Kimi K2.7). Reserve the stronger model for phase
  design and hard debugging, not routine extraction.

## End-of-session checklist — do not skip
- [ ] Appended one dated entry to PROGRESS.md: what was done, what's
      next, any blockers.
- [ ] Any new/updated SKILL.md files added to skills/INDEX.md.
- [ ] ROADMAP.md phase marker updated if the current phase is done.


═══════════════════════════════════════════════════
FILE: ROADMAP.md   (phase gate — the agent only works inside [ACTIVE])
═══════════════════════════════════════════════════

# ROADMAP.md
Exactly one phase is marked [ACTIVE] at any time. Move the marker
forward only when the checklist under a phase is fully checked.

## Phase 0 — Environment [ACTIVE]
- [ ] Folder structure created (AGENTS.md, ROADMAP.md, PROGRESS.md,
      skills/INDEX.md, /knowledge/, /library/raw/, /src/, /notebooks/)
- [ ] Python env: pandas, numpy, matplotlib, jupyter, one backtester
      (vectorbt or backtrader), yfinance/ccxt for data pulls
- [ ] Books sorted into /library/raw/ by topic (options, market
      microstructure, backtesting, risk, ML-for-finance)

## Phase 1 — Knowledge extraction
- [ ] Each book processed per AGENTS.md rules into /knowledge/
- [ ] Core skills populated: options-pricing, backtesting-framework,
      risk-metrics, data-pipelines
- [ ] glossary.md started

## Phase 2 — Core toolkit
- [ ] Reusable Python modules built from Phase 1 skills: data loader,
      backtest engine wrapper, Greeks/IV calculators, position sizing
- [ ] Every module has a matching skill file documenting its interface

## Phase 3 — Strategy research
- [ ] Agent proposes and backtests 2–3 strategy hypotheses on the
      Phase 2 toolkit
- [ ] Each experiment logged: hypothesis, params, result, verdict

## Phase 4 — Integration
- [ ] Toolkit hooked into existing live feeds (VOLATERM/VEGA: Deribit,
      FMP, Finnhub, FRED)
- [ ] Paper-trading loop only — no live capital until validated

## Phase 5 — Maintenance (ongoing, not a one-time phase)
- [ ] Periodic pass: prune stale skills, re-verify formulas, fold new
      book material in as it's read


═══════════════════════════════════════════════════
FILE: PROGRESS.md   (start empty except for this header)
═══════════════════════════════════════════════════

# PROGRESS.md
Append one entry per session. Never edit or delete past entries.

Format:
## YYYY-MM-DD
- Did:
- Next:
- Blockers:
