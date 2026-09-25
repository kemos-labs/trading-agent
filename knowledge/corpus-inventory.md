# Corpus inventory — academic paper notes + bibliography + FINC-B8420 Lecture 1

New research corpus received 2026-09-25. NOT books — distilled academic-paper
notes (structured: Metadata / Problem statement / Approach short + detailed,
with formulas). This file is the index; never bulk-load the corpus into context.

## Locations

- Paper notes: `drive-download-20260925T215026Z-1-001/` — **634 .md files, ~12 MB**
- Bibliography: `bibliography.bib` — **748 entries** (articles, books, techreports,
  unpublished; Almgren/Amihud/Cochrane/Fama-type asset-pricing core)
- Course lecture: `FINC_B8420_1_simple.pdf` — Columbia FINC-B8420 Quantitative
  Investing, Lecture 1 (Paleologo, 43 slides). Distilled in
  `knowledge/paleologo-quant-investing/lecture01.md`.

## Per-topic counts (folder = signal family)

| Folder | Files | Role on the Paleologo spine |
|---|---|---|
| portfolioconstruction | 172 | Optimization + risk-model block |
| abnormalreturns | 107 | µ-model evidence (alpha Zoo audit) |
| momentum | 59 | µ-model: cross-section + time-series momentum |
| returnproperties | 31 | Return stylized facts (feeds Σ + cost models) |
| universalportfolios | 24 | Online/Kelly growth-optimal allocation |
| trendfollowing | 19 | µ-model: trend/CTAs, convexity |
| anomalies | 16 | µ-model: accruals, BAB, low-vol, liquidity |
| derivatives | 14 | Futures/options overlays, hedging legs |
| marketimpact | 10 | Transaction-cost block (Almgren, Bouchaud) |
| yield | 6 |Rates/credit/carry (Tuckman, Richardson, CDS/Lando) |
| papers/ (+portfolioconstruction sub) | 6 | Loose overflow, mostly portfolio |

## Hygiene issues (fixed in Phase 8 T0, 2026-09-25)

- **209 duplicate files quarantined** to `drive-download-.../_quarantine_dupes/`
  (manifest `MANIFEST.txt`, hash-named files; nothing deleted): 21 same-dir
  ` (1).md`/`(2).md` copies + 196 cross-folder byte-identical copies
  (`papers/portfolioconstruction/` was a full shadow of top-level
  `portfolioconstruction/`; ~35 momentum notes shadowed in `abnormalreturns/`),
  plus a second sweep (14 `)(1).md`-style suffixes without a space).
  Canonical kept = topical folder over `papers/`, shorter/alpha-first path.
  Live corpus: **634 → 411 unique notes**.
- 12 same-basename DIFFER groups kept (alternative distillations of one paper
  in different topics, e.g. HMM-Momentum trio, Cover 1991 vs 1996, Patton
  market-neutral in `returnproperties/` + `papers/`): consult, don't promote twice.
- `papers/` leftovers: Patton note (alt distillation) + `Welcome.md` boilerplate
  (ignore). Empty `papers/Untitled/`, `papers/portfolioconstruction/` removed.
- `yield/` notes are partly book distillations (Tuckman, Lando, Jha, Richardson)
  — tag `type: book-note` vs `type: paper-note` when promoting.
- **Bib join: WEAK.** Only ~6/131 filename-embedded PDF stems fuzzy-match
  `bibliography.bib` — the bib is a background asset-pricing pool, not the
  notes' source list. Cite corpus path primarily; bib key only on real matches.

## Priority index (formula-density scan, Phase 8 T0)

Top formula-dense notes per spine block (read these first):

- µ: `momentum/Understanding and Exploiting Momentum in Stock Returns`,
  `abnormalreturns/Identifying Small Mean Reverting Portfolios`,
  `momentum/Is Momentum Really Momentum (2012)` (12-7 vs 6-2).
- Σ+costs: `marketimpact/Execution Risk Optimal Trading`,
  `returnproperties/Industry and Country Effects (Heston-Rouwenhorst 1995)`.
- Optimization: `portfolioconstruction/The Fundamental Law of Active Portfolio
  Management (Clarke-de Silva-Thorley)`, `.../Markowitz Meets Talmud (1/N)`,
  `.../Bayes-Stein Estimation`, `.../Optimal Turnover Liquidity and
  Autocorrelation (Garleanu-Pedersen/Ritter 2022)`.
- Overlays: `derivatives/The Volatility Surface (Gatheral)`,
  `universalportfolios/A New Interpretation of Information Rate (Kelly 1956)`.
- Attribution: `portfolioconstruction/Attribution Modeling Asset Characteristics
  as Portfolios (Grinold 2006)`.

## Access rules (see AGENTS.md Corpus section)

- One note at a time; max ~5 notes per session turn for synthesis tasks.
- Always record `corpus path + bib key (if any)` when promoting to a skill.
- Prefer notes with Approach(detailed) formulas over Metadata-only notes.
