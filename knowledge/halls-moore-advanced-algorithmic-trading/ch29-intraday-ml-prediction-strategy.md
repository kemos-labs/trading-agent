# Ch29 — Intraday ML Prediction Strategy (AREX, Random Forest/LDA)

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 29 (QSTrader intraday).

## Prediction goals & the class-imbalance trap
Possible targets: (1) **Direction** — sign of next-bar returns; (2) **Short-term trend** —
predict several periods ahead; (3) **"Up/down factor"** — bars where the stock rises ≥ a
factor and doesn't drop below another (e.g. up ≥2% and not down >1% within lookforward
minutes). Ch29 uses (1) and (3).

**Class imbalance** is common in quant returns prediction: "up/down factor" bars are rare vs
normal bars. Naive classifiers just predict the majority class → **Hit Rate merely reflects the
class ratio** (a 58% hit-rate can be an artifact of choosing one class almost always). Detect
via **confusion matrix** (TP/TN/FP=Type I/FN=Type II errors) — lopsided cells reveal it.
Mitigations: sample more data (hard — only one history), reduce majority-class samples, etc.
**Serial correlation** compounds it: bars aren't iid → can't randomly subsample the majority
class without care. **Always inspect a confusion matrix before deploying** any ML-driven
trading engine.

## Model training (intraday_ml_model_fit.py)
- Equity: **AREX**, late 2007 → 2012 for training; out-of-sample 2013/14.
- Features: **lagged minutely returns** (pth bar's close return behind current). Response:
  directional change (+1/−1) or up/down factor (+1/−1). Commented-up/down = fewer positive
  samples → more imbalance.
- `create_up_down_dataframe(csv, lookback_minutes=30, lookforward_minutes=5,
  up_down_factor=2.0, percent_factor=0.01)`: reads intraday OHLCV CSV; builds lag features;
  computes up/down label via bitwise ops: **down_tot = AND of all lookforward returns >
  −down** (never dropped below), **up_tot = OR of any lookforward return > up** (rose ≥ 2×
  percent_factor at least once); label = up & down.
- Model: **RandomForestClassifier(n_estimators=400, max_depth=10, random_state=42,
  n_jobs=1)** (LDA, Bagging, GradientBoosting also imported). **max_depth controls
  bias–variance**: small → faster + smaller file; large → overfit risk, and the *default
  (unconstrained) RF pickles to a 4.1 GB model* — infeasible.
- Serialise with **joblib.dump → ml_model_rf.pkl** (Scikit-Learn "model persistence").

## Strategy (intraday_ml_strategy.py)
`IntradayMachineLearningPredictionStrategy` — **long-only** (go long & exit; shorting = simple
modification).
- Init: `lags=5`; `cur_prices` (len lags+1), `cur_returns` (len lags); `qty=10000` on
  $500k equity; unpickle model in `__init__` (`joblib.load`).
- `_update_current_returns`: shift price array back by one, add new bar close
  (÷ PriceParser.PRICE_MULTIPLIER); after lags+1 minutes compute returns
  ((p_i/p_{i+1})−1)×100 (deque-like rolling window using NumPy).
- `calculate_signals`: after lags+2 minutes, `model.predict(cur_returns.reshape((1,-1)))[0]`
  (reshape avoids sklearn deprecation; [0] extracts scalar). If not invested & pred=+1 → BOT
  10,000 units; if invested & pred=−1 → EXIT.

**Prediction-speed caveat**: complex models (deep RF) predict slowly — up to 3 orders of
magnitude slower than linear models; a 4.1 GB pickle can exceed RAM → disk swapping kills
performance. Final RF (max_depth=10) ran ~60 predictions/second — a trade-off between
accuracy and backtest speed.

## Backtest (intraday_ml_backtest.py)
- **IQFeedIntradayCsvBarPriceHandler** (intraday bars) instead of Yahoo daily; `periods`
  set so **Sharpe annualisation is correct** for the bar frequency. NaivePositionSizer,
  ExampleRiskManager, IBSimulatedExecutionHandler, TearsheetStatistics; $500k equity.
- Period: 2013-01-01 → 2014-03-11 (just over a year), **out-of-sample**, **net of IB
  commissions** (no slippage/impact/spread — would all hurt CAGR).

## Results
- **LDA**: OOS **Sharpe 2.02**, CAGR 5.35%, max daily DD 1.71% (tiny DDs from minute-scale
  holding periods). Broadly rising equity.
- **Random Forest (max_depth=10)**: OOS **Sharpe 3.02**, CAGR 10.63% (misleading on ~1yr —
  ≈ total return); higher returns with similar drawdowns; underwater late 2013 then recovers.

## Road to production
- Replicate across many (tens–hundreds) equities to build uncorrelated return streams.
- Hyperparameter study (esp. RF max_depth) to manage bias–variance.
- Account for **slippage, market impact, average daily volume, realistic commissions**.
- Minutely frequency is far harder operationally than daily — "the price to pay" for higher
  Sharpe.

## Takeaways / pitfalls
- Check class imbalance via confusion matrix before trusting hit-rate/Sharpe.
- Split train/test by time (train ≤2012, test 2013–14), not random (serial correlation).
- Keep deployed models small/fast (max_depth limit) — pickle size & predict speed matter
  in event-driven intraday backtests.
- Intraday Sharpe ~2–3 is achievable out-of-sample on a single equity but costs real
  implementation friction (slippage etc.).