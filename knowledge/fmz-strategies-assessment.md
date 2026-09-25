# FMZ `fmzquant/strategies` assessment for quantkit

Assessed clone: `strategies/`, commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (2025-04-30). The repository contains roughly 5,800 Markdown exports (about 98 MB), usually combining a strategy description, parameters, platform-specific source, and an FMZ link. No license file was present at assessment time, so none of its source is copied into quantkit.

## Where it helps

The collection is useful as a large **hypothesis catalog**. It confirms that simple trend families recur across markets and provides concrete defaults worth testing without searching the held-out sample. Two examples align with the existing Phase 3 roadmap:

- `Dual-SMA-Momentum-Strategy双SMA动量策略.md` describes fast/slow SMA trend detection with default windows 9 and 45.
- `Donchian渠道趋势跟踪策略Donchian-Channel-Trend-Following-Strategy.md` describes long-channel entry and shorter-channel exit, including a 50/20 parameter pair and volatility-aware sizing.

These ideas can be expressed cleanly as point-in-time pandas signals and evaluated with quantkit's mandatory one-bar execution lag. The repository also supplies a useful checklist of practical concerns—turnover, stop placement, position caps, and trend whipsaw—even when its implementation is not reusable.

## Where it does not help

The repository is not a validated strategy library. Most files are PineScript, JavaScript, MyLanguage, or FMZ runtime snippets rather than standalone Python. There is no shared test suite, reproducible data snapshot, portfolio-level evaluation protocol, or consistent transaction-cost model. Many examples declare only a short backtest interval, expose numerous optimization knobs, or make unverified profitability claims.

Several patterns are unsafe for direct adoption. The SMA example requests prior daily values with PineScript `lookahead_on`; channel examples compare the close with extrema containing the current bar; and numerous files use DCA, grids, or martingale sizing whose loss exposure is not bounded by evidence. Such code requires independent semantics and leakage tests. The OKX pairs example computes a rolling average raw price ratio and trades deviations, but does not test stationarity/cointegration, estimate a hedge ratio, or provide an offline backtest. It therefore does not justify a pairs-trading experiment.

## Decision

Use FMZ only to source two transparent hypotheses and fixed defaults. Independently implement leakage-safe signals; combine them with the already planned vol-targeted momentum hypothesis; test all three on adjusted real SPY/QQQ/TLT data with costs and a fixed 2019–2024 holdout. Do not import execution code, credentials, DCA/martingale logic, or reported returns. A favorable result is only a candidate for broader walk-forward and asset-universe validation, never authorization for live trading.
