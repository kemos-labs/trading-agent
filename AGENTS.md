# AGENTS.md — Master Instructions

You are a persistent research/build agent for a quantitative trading knowledge
base and codebase. Engine upgrades (Phase 6+) follow `knowledge/engine-upgrade-research-*.md` and the plan DAG before coding.

## Memory model

- You have no memory between sessions; the files in this repo are your only
  memory.
- You may be a different model/agent each session. Never assume you recall
  anything that isn't written down in this repo.
- `MEMORY.md` is this project's canonical memory file: a durable snapshot of
  what this project is, its current state, and standing decisions. Keep it
  truthful and up to date — it is the first thing every new session reads.
- `knowledge/engine-upgrade-research-*.md` is the durable log for Phase 6+ engine upgrade decisions (web + book synthesis, P0/P1/P2 priority). Read the latest one alongside `MEMORY.md` when Phase 6 is active.

## Every session, in this order

1. Read `MEMORY.md` (the project memory) and internalize its contents.
2. Read `ROADMAP.md` and find the phase marked `[ACTIVE]`.
3. Read the last 5 entries of `PROGRESS.md`.
4. Read `skills/INDEX.md`.
5. If Phase 8 (or any corpus phase) is active, read `knowledge/corpus-inventory.md`.
6. Work only inside the active phase. Do not start future-phase work.

## Source books

- Books live in `/library/raw/`.
- NEVER load a raw book fully into context.
- NEVER quote more than a couple of sentences from any book.
- When processing a book/chapter, write a distilled technical note in your own
  words into `/knowledge/`: formulas, code patterns, key takeaways, 300–800
  words per chapter.

## Research corpus (Phase 8+)

- Paper notes live in `drive-download-20260925T215026Z-1-001/` (634 notes,
  ~12 MB, 11 topic folders). Index: `knowledge/corpus-inventory.md`.
- Citations live in `bibliography.bib` (748 entries). Quote bib keys, not PDFs.
- NEVER bulk-load the corpus. One note at a time; max ~5 notes per turn for
  synthesis tasks. Prefer notes with Approach(detailed) formulas.
- Dedupe first: 21 files carry ` (1).md` / `(2).md` suffixes — hash content,
  keep one canonical copy, never promote a dupe to a skill.
- Course spine: `knowledge/paleologo-quant-investing/lecture01.md` (FINC-B8420
  Lecture 1). Every corpus work item names its spine block: µ-models
  (momentum / anomalies / abnormalreturns), Σ + costs (marketimpact /
  returnproperties), optimization (portfolioconstruction / universalportfolios),
  overlays (trendfollowing / derivatives / yield).

## Tools

- `markitdown` is installed in `.venv` and converts PDFs to markdown (e.g.
  `.venv/bin/markitdown <file.pdf> -o <out>.md`). PDFs in `/library/raw/` can
  be converted to markdown before processing if a book is scanned/image-heavy
  and hard to read directly.
- `pandoc` is available at `.venv/pandoc/pandoc` (static binary; apt/brew
  installs aren't possible in this env without root). `.epub` files in
  `/library/raw/` get converted via pandoc before processing, same as PDFs go
  through markitdown (e.g. `.venv/pandoc/pandoc book.epub -o book.md`).
- Phase 6+ engine labs add `.venv` deps: `cvxpy` (portfolio), `arch` + `statsmodels` (GARCH), `hmmlearn` + `pykalman` (HMM/Kalman) — keep Python 3.12 (numba/llvmlite gate) and verify every new dep against a textbook reference before trusting it.

## Skills

If a technique is reusable in code, promote it into
`skills/<topic>/SKILL.md` with:

- name
- description
- when to use it
- the method/formula/code
- known pitfalls
- source book (for traceability only)

Paper-note promotions (Phase 8+) additionally record:

- corpus path (`drive-download-.../<topic>/<note>.md`) + `bibliography.bib` key
- spine block (µ / Σ-costs / optimization / overlay)
- claimed mechanism (risk / liquidity / funding / flow / information) —
  no-alpha-without-a-counterparty rule; a note that names no mechanism
  earns no skill.

## Data integrity

- Never present mock/simulated data as real; fail closed if a data source is
  unavailable.
- Verify every formula against a known reference value before trusting it.
- For Phase 6+ feature/CV pipelines: `d*` (FFD), triple-barrier, and purged-CV embargo must be fit on train only — never on the holdout; log the embargo width in the experiment report.

## Performance

- Prefer vectorized pandas/numpy over loops.
- Keep `numba` only for validated hot loops (e.g., FFD fixed-width) after a vectorized baseline exists.

## Engine upgrade rule (Phase 6+)

- Engine upgrades (Phase 6+) follow `knowledge/engine-upgrade-research-*.md`
  and the plan DAG before coding; corpus upgrades (Phase 8+) follow
  `plans/phase8-academic-corpus.md` and the Paleologo spine before coding.
- New `src/quantkit/` modules must cite their skill + web source (Hudson & Thames, de Prado, etc.) for traceability and ship with a matching `tests/test_*.py` + `research/verify_formulas.py` check.
- Corpus-derived modules additionally cite corpus path + bib key and state the
  claimed mechanism; no new live path without an OOS check net of costs.
- Keep 190 tests green and re-run `research/run_phase3.py --offline` (SHAs `79d9cd`/`f584d0`/`cd13f1`) before declaring any engine upgrade done.
- Paper-only guard stays: every new live path must journal `paper_only; execution next bar` and fail-closed on feed gaps.

## End of every session

- Append a dated entry to `PROGRESS.md`: what was done, what's next, blockers.
- Update `skills/INDEX.md` if skills changed.
- Update the `ROADMAP.md` phase marker if the current phase is complete.
- Update `knowledge/engine-upgrade-research-*.md` if Phase 6 decisions changed.
