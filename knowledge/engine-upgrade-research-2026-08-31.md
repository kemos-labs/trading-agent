# Engine upgrade research — expert web + book synthesis (2026-08-31)

## Executive summary
Current `quantkit 0.4.0` covers 7 modules (data_loader, backtest, options, sizing, strategies, live, paper) and 119 tests, but the knowledge base (31 books → 36 skills) already distills **~29 production techniques that have no code module**. The Phase 3→4 holdout (SPY/QQQ/TLT, 3774 bars, 2 PASS) proved the discipline works, but the narrow 3-ETF/309-day OOS and equal-weight portfolio are insufficient for capital. Web research confirms the cutting edge is *structure-aware* ML (de Prado) + *landmark portfolio* (Hudson & Thames) + *microstructure execution* (Harris/Aldridge) — all present in `knowledge/` but not yet in `src/quantkit/`.

This note is the “full advanced quant research” you asked for before upgrading `AGENTS.md` and the working plan.

## Web research (fetched 2026-08-31, fail-closed)
- **Hudson & Thames** (`https://hudsonthames.org`): Home + `/portfoliolab/` explicitly markets **PortfolioLab** (“landmark implementations regarding portfolio optimization… latest techniques”), **MlFinLab** (“reproducible, interpretable tools… machine learning”), **ArbitrageLab** (“exploit mean-reverting portfolios… complete set of algorithms from best academic journals”). Product names found: *Black-Litterman, Hierarchical Risk Parity (HRP), Risk Parity, Hierarchical* — all in our `portfolio-optimization` skill but not in `src/quantkit`.
- **CrossRef API** (`api.crossref.org`): query `quantitative trading` returns >500k works; Wiley `Quantitative Trading` ch1/ch7 (Chan) confirms the *What/Whos/Whys* taxonomy we already distilled (toll-taker vs position-taker).
- **Quantpedia** (`https://quantpedia.com`): title *“The Encyclopedia of Algorithmic and Quantitative Trading Strategies”* — confirms the cross-sectional factor zoo (anomaly factors) we cover in `alpha-factor-evaluation` but not in code.
- **arXiv `q-fin.ST` recent** (2026-08): 10+ new stat-arb titles (`arXiv:2608.27xxx`) — confirms statistical arbitrage / HFT remains active research, matching our `automated-market-making` + `spread-decomposition` skills.
- **Vercel Web Interface Guidelines** (fetched via `curl raw.githubusercontent`): used for dashboard a11y — confirms our live-paper skill already follows modern web a11y (focus-visible, aria-label, semantic HTML).
- **Chart.js 4.4.0 CDN** (fetched): live, MIT — used for equity curves.

No web source was presented as mock data; fetches that failed (QuantStart 404, MlFinLab readthedocs 302) were noted as fail-closed and not used.

## Book trail — what we already know but haven’t built
All 31 books are distilled in `knowledge/` (see `book-inventory.md` 0 pending). The following skills have **no `src/quantkit/` implementation** (grep `Implementation:.*src/quantkit` → 36 dirs, only 7 have code; 10 are pure-process skills like `ai-pair-programming` that intentionally stay docs-only):

### Must-build (highest expert consensus + Phase 3 gap)
1. **Features & labeling lab** — `fractionally-differentiated-features` (FFD, `d*` search, Ch.5 AFML), `triple-barrier + meta-labeling` (Ch.3), `CUSUM/SADF structural breaks` (Ch.17), `entropy features` (plug-in/LZ, Ch.18), `microstructural features` (tick rule, Roll, Kyle/Amihud, VPIN, Ch.19), `time-series-feature-engineering` (pandas shift/rolling/resample). *Why now:* de Prado’s Ch.2–5 are the core of MlFinLab; our current `strategies.py` uses only raw SMA/Donchian — no stationarity or sample-weight awareness.
2. **Portfolio lab** — `portfolio-optimization` (Markowitz max-Sharpe/GMV/target-return via `cvxpy`/`scipy.optimize`, long-only, estimation error), `HRP` (de Prado Ch.16, tree clustering, recursive bisection — the PortfolioLab flagship), `risk parity / Black-Litterman`. *Why now:* Phase 3 equal-weight is a placeholder; Hudson & Thames explicitly sells this as “essential for quants who want to be ahead.”
3. **Risk lab** — `parametric-var` (norm.fit → `ppf`), `var-backtesting` (Kupiec/Christoffersen), `stress-testing` (stressed covariance + PSD repair, PCA stress), `correlated-scenario-simulation` (Cholesky vols×corr), `downside-risk-measures` (Sortino/Omega/Kappa), `bond-price-sensitivities` (duration/convexity/PV01). *Why now:* Risk.net and Vol. IV (Alexander) stress that historical VaR alone is non-subadditive; we only have `backtest.performance_summary`.
4. **Execution & microstructure lab** — `spread-decomposition` (Lee–Ready, quoted/effective/realized, Roll), `automated-market-making` (Kyle lambda, Amihud, OFI, rebate threshold), `market-microstructure-execution` (maker-taker, Reg NMS, SIP, colocation). *Why now:* Phase 4 polls daily close only; real execution is the next live-paper upgrade (Almgren-Chriss, capacity).

### Keep docs-only (intentionally not code)
- `ai-pair-programming`, `ai-evaluation-pipeline`, `market-structure-risk` — process/audit skills.
- `loss-function-design`, `data-pipelines`, `statistical-significance-testing` — partially in tests but not a standalone module.

## What the engine must upgrade (prioritized)
### P0 — before any broader walk-forward (blocks capital)
- **Purged CV + CPCV + walk-forward as code** (`src/quantkit/validation.py`): the `purged-cross-validation` skill describes embargo + CPCV + PSR/DSR but `research/run_phase3.py` uses a single 2019 split. Must implement `PurgedKFold` + `CPCV` + `deflated Sharpe` and re-run Phase 3 legs via it.
- **Alpha-factor evaluation as code** (`src/quantkit/factors.py`): IC + quantile spread screen (winsorize/z-score/neutralize per cross-section) — the only cross-sectional check before claiming 3-ETF results generalize.

### P1 — engine labs (new `src/quantkit/` modules, each with tests + skill)
- `src/quantkit/features.py` — FFD, triple-barrier, CUSUM, entropy (from AFML Ch.2–5, Ch.17–18)
- `src/quantkit/portfolio.py` — HRP + risk parity + max-Sharpe/GMV (with `cvxpy` optional, fallback `scipy`)
- `src/quantkit/risk.py` — VaR/cVaR, stress, Cholesky scenarios (from MRA Vol. IV)
- `src/quantkit/execution.py` — spread decomposition + Kyle/Amihud estimators (from Harris/Aldridge)
- `src/quantkit/tsa.py` — ARMA/GARCH, cointegration/Kalman/HMM wrappers (from Halls-Moore Ch.10–14)

### P2 — hardening
- **Live:** add 1-min/1-h polling + `to_bars` resample edge tests, and a max-DD kill-switch in `paper.py` (currently paper equity only tracks costs).
- **deps:** add `arch`, `statsmodels`, `hmmlearn`, `pykalman` (optional), `cvxpy`; keep `numba/llvmlite` pinned to py3.12 (AGENTS.md standing decision).

## Upgrade working plan proposal
Add **Phase 6 — Advanced engine (features/portfolio/risk/execution)** as the next `[ACTIVE]` after Phase 5 maintenance sweep, with a DAG:
- T1: `validation.py` + `factors.py` (purged CV + IC screen) — no deps
- T2: `features.py` + `portfolio.py` — depends T1 (needs CPCV to validate)
- T3: `risk.py` + `execution.py` — depends T2
- T4: `tsa.py` re-verification + kill-switch + docs — depends T3

Each T ships tests, updates `skills/INDEX.md`, and re-runs `research/verify_formulas.py` + `research/run_phase3.py --offline` (must stay green).

## AGENTS.md upgrade proposal (diff summary)
- **Memory model:** add `knowledge/engine-upgrade-research-YYYY-MM-DD.md` as a durable decision log.
- **Source books:** note `library/raw/` → `knowledge/` is complete (0 pending) but new `src/quantkit/` modules must cite their skill + web source (Hudson & Thames, de Prado, etc.) for traceability.
- **Tools:** add `cvxpy`, `arch`, `statsmodels`, `hmmlearn` to `.venv` (keep pandoc/markitdown, keep py3.12 gate).
- **Performance:** keep vectorized pandas/numpy; add `numba` only for validated hot loops (e.g., FFD).
- **Data integrity:** extend fail-closed to *feature* pipelines (FFD `d*` must be fit on train only, purged CV embargo must be honored).
- **End-of-session:** also update `knowledge/engine-upgrade-research-*.md` if Phase 6 decisions change.

No brokerage, no live capital change — Phase 6 stays paper-only, same `paper_only; execution next bar` guard.

## Risks if not upgraded
- Single-split OOS (2019–2024) is indistinguishable from luck without CPCV/PSR/DSR — de Prado Ch.11–14 calls this “the 7 sins of backtesting.”
- Equal-weight without HRP/risk parity misstates portfolio risk — Hudson & Thames positions HRP as the efficient-frontier fix.
- Daily-close-only execution understates spread/cost — Aldridge Ch.5/Harris Ch.14 show 1–3 bps spread can erase SMA turnover (2.5% daily → ~2.5 bps/day at 10 bps).

## Next step for you
Approve Phase 6 DAG (or edit it) and I will proceed one T at a time, keeping 119 tests green and every new formula verified against a textbook reference before trusting it.

---
*Sources fetched 2026-08-31; local counts: 31 books done, 36 skills, 7 code modules, 119 tests, 3 live stores 3774 bars, journal 12+1, dashboard white at `dashboard/index.html`.*
