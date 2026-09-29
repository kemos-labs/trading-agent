# Skills Index

> Maintenance 2026-08-31: 36 dirs, 0 orphan. Leaf skills marked `[consolidated]` are intentionally kept for traceability — see `options-pricing`, `backtesting-framework`, `trend-following`, `live-paper` for the consolidated entry points. No stale-skill deletions this cycle; re-verification passed (see `knowledge/maintenance-2026-08-31.md`).

## bayesian-updating
Bayesian updating with conjugate priors (Beta-Binomial posterior updates).
Source: Halls-Moore ch02–03. `skills/bayesian-updating/SKILL.md`

## arma-garch-modeling
ARMA/GARCH time-series modeling for return forecasting (AIC order search,
GARCH(1,1), rolling direction signals, look-ahead fix).
Source: Halls-Moore ch10–11, ch26. `skills/arma-garch-modeling/SKILL.md`

## cointegration-testing
Cointegration testing (CADF/ADF, Phillips-Ouliaris, Johansen) and
mean-reverting Bollinger-band pairs trading.
Source: Halls-Moore ch12, ch27. `skills/cointegration-testing/SKILL.md`

## kalman-filter-pairs
Kalman-filter dynamic hedge-ratio pairs trading (state-space update rules,
±√Q_t entry/exit, TLT/IEI parameters).
Source: Halls-Moore ch13, ch28. `skills/kalman-filter-pairs/SKILL.md`

## hmm-regime-detection
HMM market-regime detection (GaussianHMM, regime-gated risk manager,
retraining caveats).
Source: Halls-Moore ch14, ch31. `skills/hmm-regime-detection/SKILL.md`

## ai-pair-programming
AI-assisted development workflow (70/30 model, first-drafter / pair-programmer /
validator patterns, AI-commit hygiene, human review checklist).
Source: Osmani, Vibe Coding ch1–2. `skills/ai-pair-programming/SKILL.md`

## volatility-targeted-position-sizing
Volatility-targeted position sizing & risk management (Half-Kelly vol target,
volatility scalar → subsystem position pipeline, diversification multipliers,
speed/cost limits).
Source: Carver, Systematic Trading ch5, ch7–12. `skills/volatility-targeted-position-sizing/SKILL.md`

## ai-evaluation-pipeline
Evaluation-driven development for AI/ML systems (exact vs AI-judge metrics, eval-set
sizing rule: ~3× smaller diff → ~10× more samples, judge bias pitfalls).
Source: Huyen, AI Engineering ch3–4. `skills/ai-evaluation-pipeline/SKILL.md`

## statistical-significance-testing
Hypothesis testing & A/B comparison (z-test, pooled-SE two-proportion test, confidence
intervals, sample-size math, multiple-testing warnings).
Source: Grus, Data Science from Scratch ch7. `skills/statistical-significance-testing/SKILL.md`

## data-pipelines
ML data-preprocessing pipelines (fit-on-train-only, scaling, categoricals, custom
transformers, ColumnTransformer/Pipeline, tf.data, training/serving skew).
Source: Géron, Hands-On ML ch2, ch13. `skills/data-pipelines/SKILL.md`

## loss-function-design
Loss-function-first modeling (mean⇔squared / median⇔absolute / mode⇔0-1, custom
asymmetric losses for asymmetric error costs, Huber robust loss, constant-model baseline).
Source: Lau/Gonzalez/Nolan, Learning Data Science ch4, ch18, ch20. `skills/loss-function-design/SKILL.md`

## time-series-feature-engineering
pandas time-series features for trading models (returns/lags via shift, rolling/expanding/ewm
windows, resample to OHLC bars with closed/label edge conventions, seasonal grouping, no-look-ahead discipline).
Source: McKinney, Python for Data Analysis ch11. `skills/time-series-feature-engineering/SKILL.md`

## market-structure-risk
Market-structure risk audit (toll-taker vs position-taker, embedded optionality,
tranching as risk reallocation, commitment/bridge-loan liquidity risk, information
asymmetry, incentive corruption).
Source: Lewis, Liar's Poker ch3, ch5–7, ch11. `skills/market-structure-risk/SKILL.md`

## market-microstructure-execution
Execution-layer market microstructure (maker-taker fee math, order types, Reg NMS
best-price routing, SIP latency, colocation, tick-size economics, Flash-Crash fragility
checklist).
Source: Patterson, Dark Pools ch3–4, ch8, ch11, ch13–15, ch20–22, ch24. `skills/market-microstructure-execution/SKILL.md`

## spread-decomposition
Spread decomposition and transaction-cost measurement (Lee–Ready classification,
quoted/effective/realized spread, price impact, Roll's estimator, variance-ratio test
for fundamental vs. transitory volatility).
Source: Harris, Trading and Exchanges ch14, ch20, ch21. `skills/spread-decomposition/SKILL.md`

## automated-market-making
Automated market making (limit-order fill simulation, fixed/volatility-dependent quote
offsets, Kyle's lambda, Amihud illiquidity, order-flow imbalance OFI prediction, rebate-capture
profitability threshold).
Source: Aldridge, High-Frequency Trading ch10–12. `skills/automated-market-making/SKILL.md`

## walk-forward-validation — [consolidated → backtesting-framework]
Walk-forward / leakage-free evaluation of time-series ML (sequential splits,
fit-on-train-only scaling, TimeSeriesSplit loop, multiple-testing/data-snooping
awareness, cost-adjusted backtests).
Source: Kaabar, Deep Learning for Finance ch7, ch11. `skills/walk-forward-validation/SKILL.md`

## purged-cross-validation — [consolidated → backtesting-framework; now code in quantkit 0.5.0]
Purged k-fold CV with embargo + Combinatorial Purged CV (CPCV) for
overlapping/path-dependent labels; multiple OOS backtest paths, PSR/DSR
significance (deflated Sharpe). Implementation: `src/quantkit/validation.py`
(tests: `tests/test_validation.py`). Source: López de Prado, Advances in Financial ML ch7, ch11–14. `skills/purged-cross-validation/SKILL.md`

## alpha-factor-evaluation — [now code in quantkit 0.5.0]
Information coefficient (IC) + quantile long-short spread screening for
cross-sectional factors/features: winsorize, z-score, neutralize, then
period-by-period rank correlation with forward returns, t-stat, hit rate.
Implementation: `src/quantkit/factors.py` (tests: `tests/test_factors.py`).
Source: Jansen, Machine Learning for Algorithmic Trading ch4. `skills/alpha-factor-evaluation/SKILL.md`

## correlated-scenario-simulation
Cholesky decomposition for correlated multi-asset simulation: covariance
matrix from vols × corr, lower-triangular factor, mixed normals,
lognormal paths — for Monte Carlo pricing, option-book scenario grids,
and portfolio stress tests (incl. PSD checks and crisis correlation).
Source: Taleb, Dynamic Hedging Module A. `skills/correlated-scenario-simulation/SKILL.md`

## kelly-position-sizing
Kelly criterion and fractional-Kelly / volatility-targeting position
sizing: discrete (f* = p − q/b) and continuous (f* = m/σ²) Kelly, the
over-betting trap (negative growth past ~2f*), fat-tail/skew cautions,
and the vol-target approximation for noisy edge estimates.
Source: Sinclair, Volatility Trading ch8; corpus addendum (Kelly 1956:
growth = mutual information, track-take withholding, ignore-odds-for-proportions).
`skills/kelly-position-sizing/SKILL.md`

## optimal-turnover-liquidity
Cost-aware turnover target (Baldacci-Benveniste-Ritter 2022): optimal
steady-state turnover `γ√(φ/γ+1)` and steady-state IR net of quadratic
costs, from alpha half-life φ, Kyle λ, risk aversion κ; residual-asset
√N breadth restoration. Implementation: `src/quantkit/portfolio.py::
optimal_turnover / steady_state_ir` (tests: `TestOptimalTurnover`; checks
20). Corpus: `portfolioconstruction/Optimal Turnover Liquidity and
Autocorrelation (OptimalTrading_RitterBaldacciBenveniste_2022.pdf).md`.
Mechanism: liquidity + information. `skills/optimal-turnover-liquidity/SKILL.md`

## execution-risk
Engle-Ferstenberg (2006): investment + execution = one mean-variance
problem with a single λ; TC variance and Cov(TC, gain) in ex-ante Sharpe;
risk-averse front-loading (three-period closed form); hedge unfinished
execution with futures; liquidity risk = ES of liquidation cost.
Implementation: `src/quantkit/execution.py::ef_midpoint` (tests:
`TestEFMidpoint`; check 21). Corpus: `marketimpact/Execution Risk
Optimal Trading (optimaltrading_Engle_2006.pdf).md`. Mechanism: liquidity.
`skills/execution-risk/SKILL.md`

## binomial-tree-pricing — [consolidated → options-pricing]
Binomial tree (CRR) option pricing and hedging: build a recombining tree
(u = e^{σ√Δt}, d = 1/u), discount backward under risk-neutral probabilities
p̃ = (e^{(r−q)Δt} − d)/(u − d), apply the American early-exercise max at
every node, and extract the delta as value-difference over
price-difference. Vectorized numpy example; converges to Black-Scholes.
Source: Shreve, Stochastic Calculus and Finance ch1–5. `skills/binomial-tree-pricing/SKILL.md`

## vectorized-backtesting — [consolidated → backtesting-framework]
Vectorized (array-based) backtesting of signal strategies: log returns →
position → position.shift(1) × returns (the no-look-ahead discipline) →
cumulative performance, plus proportional/fixed transaction costs and
ffill-based holding. The fast first-pass skeleton for SMA, momentum,
mean-reversion, and ML-direction strategies before event-based engines.
Source: Hilpisch, Python for Algorithmic Trading ch4–5. `skills/vectorized-backtesting/SKILL.md`

**Risk metrics** — Drawdown, historical VaR, cVaR/Expected Shortfall, the
VaR/cVaR tail diagnostic, and portfolio risk contributions, vectorized in
pandas. The standard "how bad can it get" report card pairing with
Sharpe/Sortino for any strategy or portfolio. Source: Inglese, Python for
Finance and Algorithmic Trading 2ed ch5. `skills/risk-metrics/SKILL.md`

**Monte Carlo option pricing** — [consolidated → options-pricing] Vectorized GBM/jump-diffusion/CIR path
simulation, antithetic variates + moment matching (variance reduction),
European valuation by discounted payoff expectation, and American
valuation via Least-Squares Monte Carlo (Longstaff-Schwartz) with numeric
Greeks. Source: Hilpisch, Python for Finance 2ed ch12, ch18–19.
`skills/monte-carlo-option-pricing/SKILL.md`

**Parametric VaR** — Value-at-Risk from a fitted return distribution:
scipy.stats norm.fit → PDF/CDF validation → norm.ppf(alpha, mu, sig)
quantile, with daily/annualization conventions and the empirical
(order-statistic) VaR cross-check. Complements the historical VaR in
risk-metrics. Source: Lachowicz, Python for Quants Vol. I ch3.5.
`skills/parametric-var/SKILL.md`

**Portfolio optimization (mean-variance)** — Markowitz efficient frontier:
max-Sharpe, global-min-variance, and target-return solutions via
scipy.optimize/cvxpy, with long-only constraints, the frontier sweep, and
estimation-error/robustness guardrails. Source: Van Der Post, Pythonic
Quant ch6; Hilpisch, Python for Finance 2ed ch13.
`skills/portfolio-optimization/SKILL.md`

**Downside risk measures** — Lower partial moments, downside deviation,
the Sortino ratio, the omega statistic, and the kappa index family for
skewed/fat-tailed returns, with threshold-choice guidance. Source:
Alexander, Market Risk Analysis Vol. I ch I.6.
`skills/downside-risk-measures/SKILL.md`

**VaR / forecast backtesting (coverage tests)** — Statistical validation of
VaR and interval forecasts: Kupiec's unconditional coverage LR test,
Christoffersen's conditional (independence) coverage test, and the
rolling-window VaR backtest procedure. Source: Alexander, Market Risk
Analysis Vol. II ch II.8. `skills/var-backtesting/SKILL.md`

**Bond price sensitivities** — Macaulay/modified duration, convexity, dollar
duration, PV01/PVBP, and bond-portfolio immunization via the Taylor-series
price sensitivities, plus PV01-invariant cash-flow mapping. Source:
Alexander, Market Risk Analysis Vol. III ch III.1 & ch III.5.
`skills/bond-price-sensitivities/SKILL.md`

**Stress testing and scenario analysis** — Formal stress testing for market
risk: single-case vs distribution scenarios, scenario VaR/ETL, stressed
covariance matrices with PSD repair, PCA-focused stress, sensitivity grids,
and liquidity-adjusted VaR. Source: Alexander, Market Risk Analysis Vol. IV
ch IV.7. `skills/stress-testing/SKILL.md`

**Options pricing (consolidated)** — Vanilla options toolkit: BSM closed
forms with the carry adjustment b (stocks/futures/FX), put-call parity,
Greeks (delta/gamma/vega/theta/rho), implied volatility by root-finding,
and when to switch to numerical methods (CRR tree, Monte Carlo/LSM).
Consolidates binomial-tree-pricing + monte-carlo-option-pricing. Source:
Natenberg ch18; Alexander MRA Vol. III ch III.3.
`skills/options-pricing/SKILL.md`

**Backtesting framework (consolidated)** — Two-tier backtesting: vectorized
first pass + event-driven engine (QSTrader-style events queue, price
handler, strategy, portfolio, sizer, risk manager, execution), wrapped in
the data-quality (splits/dividends, survivorship, H/L noise) and
performance-measurement discipline (Sharpe annualization, drawdown,
MAR, OOS-only). Consolidates vectorized-backtesting + walk-forward-
validation + purged-cross-validation. Source: Hilpisch PAT ch4–5;
Halls-Moore ch24; Chan ch3. `skills/backtesting-framework/SKILL.md`

**Data loader (quantkit module 1)** — Market-data loading and cleaning:
canonical OHLCV frames from CSV/yfinance, Chan multiplier split/
dividend adjustment (returns invariant across ex-dates), log/simple
returns, OHLC bar resampling with edge conventions, z-sigma outlier
flags; fails closed on bad feeds. Implementation: `src/quantkit/
data_loader.py` (tests: `tests/test_data_loader.py`). Source: Chan ch3.
`skills/data-loader/SKILL.md`

**Backtest engine (quantkit module 2)** — Two-tier backtesting code:
vectorized `position.shift(1) × returns` screen with proportional/flat
costs; bar-by-bar engine with guaranteed one-bar lag, exposure clamps,
cash costs at order time, and equity stop-loss halt; performance
summary (CAGR, Sharpe, max DD + duration, MAR). Implementation:
`src/quantkit/backtest.py` (tests: `tests/test_backtest.py`). Source:
Hilpisch PAT ch4–5; Halls-Moore ch24. `skills/backtesting-framework/SKILL.md`

**Options pricing (quantkit module 3)** — Generalized BSM with carry b,
five Greeks, put-call parity solver, fail-closed implied vol by
bisection. Verified against textbook ATM reference ($10.45) and finite
differences. Implementation: `src/quantkit/options.py` (tests:
`tests/test_options.py`). Source: Natenberg ch18; Alexander MRA Vol.
III ch III.3. `skills/options-pricing/SKILL.md`

**Position sizing (quantkit module 4)** — Kelly (continuous f* = m/σ²,
discrete p − q/b), fractional-Kelly/vol-target weights, Carver pipeline
(vol scalar → subsystem position in blocks). Fail-closed variance
checks. Implementation: `src/quantkit/sizing.py` (tests:
`tests/test_sizing.py`). Source: Sinclair ch8; Carver ch5/9/10.
`skills/kelly-position-sizing/SKILL.md`,
`skills/volatility-targeted-position-sizing/SKILL.md`

**Trend following (quantkit module 5)** — Leakage-safe trend targets:
dual SMA (9/45), Donchian breakout (50/20 with prior-bar channels),
vol-targeted momentum (252/60, 10% target, cap 1.5×); one-bar execution
lag, equal-weight portfolio, predeclared 2019 holdout. Verified by
point-in-time invariance tests and real-data OOS (SPY/QQQ/TLT,
10 bps). Implementation: `src/quantkit/strategies.py` (tests:
`tests/test_strategies.py`; harness: `research/run_phase3.py`).
Source: FMZ `fmzquant/strategies` (see
`knowledge/fmz-strategies-assessment.md`) + consolidated backtesting
skills. `skills/trend-following/SKILL.md`

**Live feed + paper trading (quantkit modules 6–7)** — yfinance polling
into validated daily stores (`data/live/*_1d.csv`, atomic writes, B-freq
gap detection, fail-closed) and incremental paper runtime
(`data/paper/state.json` + append-only `journal.csv`) reusing Phase 3's
close-decided/next-bar-executed + 10 bps discipline. No real orders;
every journal row carries `paper_only; execution next bar`. Offline replay
from `data/research/phase3` caches is deterministic. Implementation:
`src/quantkit/live.py` + `src/quantkit/paper.py` (tests:
`tests/test_live.py`, `tests/test_paper.py`; CLI: `research/paper_trade.py`;
docs: `knowledge/live-integration.md`; demo: `notebooks/paper_demo.ipynb`).
`skills/live-paper/SKILL.md`

**Validation + factor screening (quantkit modules 8–9)** — Purged K-Fold /
CPCV (purged + embargo, N choose k OOS paths) + PSR/DSR deflated Sharpe
and factor IC (Spearman per cross-section, t-stat/hit-rate) + quantile
long-short spreads (winsorize/z-score/neutralize). The P0 lab that makes
Phase-3 holdout honest. Implementation: `src/quantkit/validation.py` +
`src/quantkit/factors.py` (tests: `tests/test_validation.py`,
`tests/test_factors.py`). Source: López de Prado AFML Ch.7,11–14 +
Jansen Ch.4. `skills/purged-cross-validation/SKILL.md`,
`skills/alpha-factor-evaluation/SKILL.md`

**Feature + Portfolio labs (quantkit modules 10–11)** — FFD (fixed-width
`d*` search, weight generation), CUSUM sampler, triple-barrier labeling
(pt/sl/vertical), plug-in entropy + HRP (single-link, quasi-diagonal,
recursive bisection), risk parity (CCD), max-Sharpe/min-variance (SLSQP,
long-only, cvxpy fallback). Implementation: `src/quantkit/features.py` +
`src/quantkit/portfolio.py` (tests: `tests/test_features.py`,
`tests/test_portfolio.py`). Source: de Prado AFML Ch.2–5,16 + Hudson &
Thames PortfolioLab. `skills/time-series-feature-engineering/SKILL.md`,
`skills/portfolio-optimization/SKILL.md`

**Risk + Execution labs (quantkit modules 12–13)** — Historical/parametric
VaR, cVaR, Kupiec/Christoffersen, downside/Sortino, bond duration/convexity/PV01,
stressed PSD covariance, Cholesky scenarios + quoted/effective/realized spread,
Roll 2√-cov, variance-ratio, Kyle λ OLS, Amihud. Implementation:
`src/quantkit/risk.py` + `src/quantkit/execution.py` (tests:
`tests/test_risk.py`, `tests/test_execution.py`). Source: Alexander MRA Vol.IV
+ Harris Ch.14,20,21 + Aldridge Ch.10–12. `skills/risk-metrics/SKILL.md`,
`skills/spread-decomposition/SKILL.md`

**TSA + kill-switch (quantkit modules 14 + paper hardening)** — ADF/Engle-Granger,
GARCH(1,1) EWMA fallback, Kalman hedge (pykalman/manual 1-D), HMM regimes
(hmmlearn/vol-threshold) + paper `max_drawdown`/`max_position` halt (persisted
`halted` flag, warn, no new targets). Implementation: `src/quantkit/tsa.py`
+ `src/quantkit/paper.py` kill-switch (tests: `tests/test_tsa.py`,
`tests/test_paper.py` + new kill-switch check). Source: Halls-Moore Ch.10–14.
`skills/arma-garch-modeling/SKILL.md`, `skills/cointegration-testing/SKILL.md`,
`skills/kalman-filter-pairs/SKILL.md`, `skills/hmm-regime-detection/SKILL.md`

**Cross-sectional momentum + reversal (quantkit module 15, Phase 8 T1)** — Log formation returns with skip-month discipline, Novy-Marx 12-7/7-2 split identity, decile/WML sorts (ungrouped dollar-neutral + within-industry group-neutral), Jegadeesh-Titman overlapping cohorts, Da-Liu-Schaumburg residual score, HLZ t≈3.0 factor-zoo hurdle as the promotion gate. Implementation: `src/quantkit/xsec.py` (tests: `tests/test_xsec.py`; checks 10–11 in `research/verify_formulas.py`). Source: Novy-Marx 2012 + Daniel-Jagannathan-Kim 2019 + Da-Liu-Schaumburg 2011/2014 + Harvey-Liu-Zhu 2015. `skills/intermediate-momentum/SKILL.md`, `skills/residual-reversal/SKILL.md`, `skills/factor-zoo-hurdle/SKILL.md`

**Σ + costs (execution + factors extensions, Phase 8 T2)** — Almgren-Thum-Hauptmann-Li closed-form impact (`I = γσ(X/V)(Θ/V)^1/4`, `J = I/2 + sgn·ησ|X/VT|^3/5`, γ = 0.314 / η = 0.142) as the pre-trade hurdle every µ-signal must clear; Heston-Rouwenhorst constrained dummy regression for pure country/industry effects (country-first prior ≈ 4.5×, re-estimate per sample). Implementation: `src/quantkit/execution.py::almgren_impact` + `src/quantkit/factors.py::pure_factor_returns` (tests: `TestAlmgrenImpact`, `TestPureFactorReturns`; checks 12–13 in `research/verify_formulas.py`). Source: Almgren et al. 2005 + Heston-Rouwenhorst 1994/1995 (+ Cavaglia-Brightman-Aked 2000 update). `skills/impact-calibration/SKILL.md`, `skills/country-industry-neutralization/SKILL.md`

**Optimization estimation discipline (portfolio extensions, Phase 8 T3)** — Exact unconstrained IR `√(α'Ω⁻¹α)` (= IC√N on diagonal), transfer coefficient TC with signal/noise attribution, Jorion Bayes-Stein mean shrinkage, Ledoit-Wolf covariance shrinkage (PD even N>T), Tu-Zhou 1/N combination; ex-ante IR benchmarks 0.5/0.75/1.0. Implementation: `src/quantkit/portfolio.py::fundamental_law_ir / transfer_coefficient / bayes_stein_means / ledoit_wolf_shrinkage / combine_with_1n` (tests: `TestEstimationDiscipline`; checks 14–16 in `research/verify_formulas.py`). Source: Clarke-de Silva-Thorley 2006 + Jorion 1986 + Ledoit-Wolf 2004 + Tu-Zhou 2011 + Grinold-Kahn benchmarks. `skills/allocation-discipline/SKILL.md`

**Attribution + trend convexity (Phase 8 T4, no new module)** — Lecture 1 close-out template as code: per-leg gross/costs/net, cost/gross fragility flag, turnover, skew + paper-journal integrity (unit-cost proportionality + `paper_only` guard). Trend identity `G = λ/2·[(S_T−S₀)² − ΣD²]` (check 17); commodity overlay math (EW-rebalanced +4.5% vs ≈0 constituents, roll ±9pp). Implementation: `research/attribute.py` → `knowledge/strategy-research/attribution-2026-09-25.md` (read-only over paper stores). Source: Grinold 2006 + Moscou-Potters-Bouchaud 2016 + Erb-Harvey. `skills/strategy-attribution/SKILL.md`

**Fresh-data pulls (quantkit module 16)** — Terminal-backed daily OHLCV (Massive aggs → Alpha Vantage → fail-closed; Finnhub quote as staleness check only): runtime keys from TERMINAL_ENV, quota ledger + headroom gates, TTL file cache, 13 s Massive self-throttle, adjusted-data splice via median anchor ratio, `validate_ohlcv` before staging. Implementation: `src/quantkit/fresh.py` (tests: `tests/test_fresh.py`, mocked) + `research/pull_fresh.py` + `research/fresh_extension.py` (fixed-rule 2010→2026 diagnostic → `knowledge/strategy-research/fresh-extension-2026-09-25.md`). Reference (patterns only, no code copied): trading-terminal-pro `api/deskFeeds.js` + `api/upstreamCache.js`. `skills/fresh-data/SKILL.md`
