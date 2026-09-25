# Ch31 — HMM Market-Regime Filter as Risk Manager (QSTrader)

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 31 (QSTrader application).

## Idea
Use the **Hidden Markov Model** (from ch14) as a **risk-managing market-regime filter**:
disallow trades when a high-volatility regime is predicted, eliminating unprofitable trades
during turbulent periods. Paired with a deliberately simple **moving-average crossover
trend-following strategy** (the filter is the point of the chapter).

**HMM recap**: stochastic state-space model with *hidden/latent* states (here: market regimes
such as changing regulation or excess volatility) influencing *observations* (the returns of a
financial series). Fitting an HMM to returns → predict regime states → risk management.

## Trend-following strategy (MovingAverageCrossStrategy)
- At every bar compute **10-day SMA** (short) and **30-day SMA** (long) of adjusted close
  (rolling windows via `collections.deque`).
- 10-day SMA > 30-day SMA & not invested → **long** base_quantity (10,000) shares.
- 30-day SMA > 10-day SMA & invested → **close**.
- Plain version: weak — Sharpe 0.37 (≈ benchmark), max daily DD slightly above benchmark,
  slight CAGR increase; it's a lagged filter, 41 trades, doesn't avoid large downward moves.

## Training the HMM (regime_hmm_train.py, hmmlearn)
- Data: **SPY adjusted close returns**, 1993-01-29 → 2004-12-31 (training only).
- `obtain_prices_df`: read CSV, `Close.pct_change()`, truncate end date, drop NaN.
- `plot_in_sample_hidden_states`: per-state subplots of adjusted close masked by hidden state —
  sanity check; mostly captures "trending" periods and 2008-like high-vol periods (majority of
  2008 lands in Hidden State #1).
- **`GaussianHMM(n_components=2, covariance_type="full", n_iter=1000)`** — 2 states, full
  covariance; `np.column_stack` because hmmlearn wants a matrix of series even for univariate.
  Fit, print score, **pickle → hmm_model_spy.pkl** (state = 0 desirable/low-vol, 1
  undesirable/high-vol).

## PriceHandler change (calc_adj_returns)
New boolean flag on the bar price handler: when true, `_store_event` also stores
previous/current adjusted close (PriceParser-adjusted) and appends **percentage returns** to
`price_handler.adj_close_returns` — the list the risk manager consumes. (In current QSTrader.)

## RegimeHMMRiskManager (AbstractRiskManager subclass)
- Holds deserialised HMM + `self.invested` flag (accounts for trades straddling regimes).
- `determine_regime(price_handler, sized_order)`: build column-stacked array from
  `price_handler.adj_close_returns`, `hmm_model.predict(returns)[-1]` → current hidden state.
- `refine_orders(portfolio, sized_order)`: builds OrderEvent (but doesn't return yet):
  - **Regime 0 (desirable)**: BOT → mark invested, return order; SLD → close if invested.
  - **Regime 1 (undesirable)**: **BOT never allowed** (return []); SLD allowed **only if
    already invested** (close a straddling position), else cancelled.
- Effect: no new longs in high-vol regime, but open longs can still be closed. (Alternative —
  immediately close on entering regime 1 — left as an exercise.)

## Backtest (regime_hmm_backtest.py)
- `YahooDailyCsvBarPriceHandler(..., calc_adj_returns=True)`; strategy (short 10 / long 30 /
  qty 10,000); `RegimeHMMRiskManager` (ExampleRiskManager importable for A/B comparison);
  NaivePositionSizer; IB simulated execution; benchmark SPY; period **2005-01-01 →
  2014-12-31, out-of-sample** (no backtest returns seen in HMM training). Net of IB costs.

## Results (filtered vs unfiltered)
- **Unfiltered**: Sharpe 0.37, max daily DD ≈ benchmark, CAGR ≈ benchmark — as expected.
- **Regime-filtered**: max daily DD **cut to ≈24%** (from benchmark ≈56%) — big risk
  reduction; Sharpe 0.48 (only modest rise — still high vol exposure); CAGR 6.88% vs 6.41%.
  Trades reduced 41 → **31** (removed large downward moves, but fewer positive-expectancy
  bets → less statistical validity). **No trading at all from early 2008 → mid-2009** (sat in
  drawdown from prior high-water mark — but didn't lose money when many others did).

## Production caveats
- **Retrain periodically**: HMM transition probabilities are very unlikely to be stationary; it
  can only predict transitions from previously-seen return distributions. If the distribution
  changes (new regime/regulation) → retrain to capture new behaviour (retraining frequency =
  research question).

## Takeaways / pitfalls
- Regime filters trade off return for **tail-risk reduction** (DD 56% → 24%) — evaluate on
  max DD & drawdown duration, not just Sharpe.
- Fewer trades = less statistical validity; filters must not over-suppress positive bets.
- HMM state labels (0/1) are arbitrary — map to low/high vol via sanity plots.
- Keep HMM training strictly **out-of-sample** from the backtest window.
- RiskManager veto layer (regime-aware order filtering) is a clean way to add market
  intelligence without touching strategy code.