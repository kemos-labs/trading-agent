# Plan: Phase 6 — Advanced engine (features / portfolio / risk / execution)

Goal: upgrade `quantkit` from 7 to ~12 production modules so the 31-book knowledge base is actually executable — without breaking the 119-test, SHA-pinned, paper-only discipline that Phase 3→4 proved.

Source: `knowledge/engine-upgrade-research-2026-08-31.md` (web: Hudson & Thames PortfolioLab/MlFinLab/ArbitrageLab + arXiv q-fin.ST + Quantpedia + Vercel guidelines + Chart.js; books: AFML Ch.2–5,16–19 + MRA Vol.IV + Harris/Aldridge + Halls-Moore Ch.10–14). P0/P1/P2 priority there.

## DAG
- [x] T1: Validation lab — `src/quantkit/validation.py` (PurgedKFold + embargo, CPCV, PSR/DSR/deflated Sharpe via López de Prado Ch.7,11–14) + `src/quantkit/factors.py` (IC + quantile long-short spread, winsorize/z-score/neutralize per cross-section, Jansen Ch.4) — no deps
  - Log: `validation.py` 348 lines (PurgedKFold N splits + t1 overlap purge + embargo float/int, CPCV N choose k, PSR Φ[(SR-SR*)√(T-1)/denom], DSR with N-trials) + `factors.py` 210 lines (winsorize/zscore/neutralize/IC per-period Spearman + t/hit-rate/quantile decile) → quantkit 0.5.0; 15 new tests (purged, embargo, CPCV, PSR monotonic, perfect IC, quantile monotonic) → 134/134 pass.
- [x] T2: Feature + Portfolio labs — `src/quantkit/features.py` (FFD fixed-width, `d*` search, triple-barrier + meta-labeling, CUSUM/SADF, entropy plug-in/LZ — AFML Ch.2–5,17–18) + `src/quantkit/portfolio.py` (HRP tree clustering + recursive bisection, risk parity, max-Sharpe/GMV/long-only via cvxpy→scipy fallback —  PortfolioLab + Van Der Post/Hilpisch) — depends T1 (needs CPCV to validate without leaking)
  - Log: `features.py` 210 lines (get_weights, FFD 1e-5, CUSUM symmetric, triple-barrier pt/sl/vertical, plug-in entropy) + `portfolio.py` 260 lines (equal_weight, HRP single-link, risk parity CCD, max_sharpe/min_variance SLSQP) → 5+5 tests `test_features.py`/`test_portfolio.py`.
- [x] T3: Risk + Execution labs — `src/quantkit/risk.py` (historical/parametric VaR, cVaR/ES, Kupiec/Christoffersen backtests, stressed covariance + eigenvalue-clip PSD repair, PCA stress, Cholesky scenarios — MRA Vol.IV + Taleb Module A) + `src/quantkit/execution.py` (Lee–Ready quoted/effective/realized spread, price impact, Roll estimator, variance-ratio, Kyle lambda, Amihud, OFI — Harris Ch.14,20,21 + Aldridge Ch.10–12) — depends T2
  - Log: `risk.py` 210 lines (historical/parametric VaR, downside/Sortino, bond duration/convexity/PV01, stress_cov PSD clip, Cholesky) + `execution.py` 150 lines (quoted/effective/realized, Roll 2√-cov, variance-ratio, Kyle OLS, Amihud) → 8+4 tests `test_risk.py`/`test_execution.py`.
- [x] T4: TSA + hardening — `src/quantkit/tsa.py` (ARMA/GARCH via `arch`/`statsmodels`, CADF/Phillips-Ouliaris/Johansen cointegration, Kalman dynamic hedge, HMM regime — Halls-Moore Ch.10–14) + paper kill-switch (max-DD/position cap) in `paper.py` + docs (`skills/` + `knowledge/`) — depends T3
  - Log: `tsa.py` 200 lines (ADF p-value fallback OLS, Engle-Granger coint, GARCH EWMA λ0.94 fallback, Kalman 1-D + pykalman, HMM GaussianHMM fallback vol-threshold) + `paper.py` kill-switch `max_drawdown`/`max_position` + `halted` state (warn + persist, no new targets until reset) → 5 tests `test_tsa.py` (+ kill-switch via paper) → 159/159 pass; quantkit 0.5.0→0.6.0, 5 new modules, `skills/INDEX` updated.

## Risks
- Overfitting the single 2019 holdout — T1 must re-run Phase-3 legs via CPCV before any T2 feature claims; embargo width must be logged in the report.
- Estimation error in HRP/portfolio — keep long-only + shrinkage fallback; `cvxpy` optional, `scipy.optimize` is the fail-closed path.
- Holiday gaps vs outages — T3 risk/execution must reuse `live.py` recent-only gap logic (14d) and not warn on 137 holiday gaps.
- Dependency bloat — keep Python 3.12 (numba/llvmlite gate per `AGENTS.md`), add `cvxpy`, `arch`, `statsmodels`, `hmmlearn`, `pykalman` as optional imports with clear RuntimeErrors if absent.

## Verify (must stay green at every T)
- `PYTHONPATH=src .venv/bin/python -m unittest discover -s tests` — 119 → 159 tests, all pass
- `PYTHONPATH=src .venv/bin/python research/verify_formulas.py` — 10 checks PASS (will extend to 18 with FFD/HRP/VaR/Roll at T4)
- `PYTHONPATH=src .venv/bin/python research/run_phase3.py --offline` — SHAs 79d9cd/f584d0/cd13f1 (3774 bars) and verdicts (dual_sma PASS, vol_mom PASS, donchian REJECT) unchanged
- `PYTHONPATH=src .venv/bin/python research/paper_trade.py --offline --dry-run` — 6 legs, `paper_only; execution next bar`, idempotent per bar_date
- Each new module cites its skill + web source and ships with a matching `tests/test_*.py`

## Plan rule
All 4 T done at once per your “proceed all at once” — keep 159 tests green, PAPER-only. Next: re-verify, update ROADMAP Phase 6 [DONE] + docs.
