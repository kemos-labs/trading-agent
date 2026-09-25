# Ch28 — Kalman-Filter Pairs Trading Strategy (TLT/IEI)

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 28 (QSTrader application).

## Strategy origin & setup
Pairs-trading on two US Treasury-bond ETFs — **TLT** (long-duration) and **IEI** (short-
duration) — originally due to Ernie Chan, tested on Quantopian by Aidan O'Mahony. The
**synthetic spread** is the tradeable series; the **Kalman filter dynamically tracks the hedge
ratio** (one component of the hidden state θ_t, the regression "beta" slope θ0, with an
intercept).

Why Kalman instead of fixed ratios: no need to empirically fix absolute spread bounds
(which would add a free overfitting-prone parameter). Instead use the filter's own
uncertainty:
- Let **e_t = forecast/residual error** (actual TLT price minus Kalman estimate of TLT today)
  and **Q_t** = variance of the predictions (√Q_t = SD of prediction).
- **Rules**:
  1. e_t < −√Q_t → **long the spread**: buy N TLT, short ⌊θ0·N⌋ IEI.
  2. e_t > +√Q_t → **short the spread**: short N TLT, buy ⌊θ0·N⌋ IEI.
  3. Exit when spread reverts (opposite of entry rules).
- floor ⌊x⌋ because only whole units are tradeable; N = base quantity.

## QSTrader implementation
`KalmanPairsTradingStrategy(AbstractStrategy)`:
- Fixed Kalman params (hardcoded for clarity; could be keyword args for optimisation):
  - **δ = 1e-4** (system-noise scaling): **W_t = δ/(1−δ) · I₂** (2×2 state transition noise).
  - **V_t = 1e-3** (measurement noise variance).
  - State θ (intercept, slope); covariance P; Q (observation variance) starts None.
- `qty = 2000` units on **100,000 USD** account equity; tracks `cur_hedge_qty` (recomputed
  when slope changes).
- `_set_correct_time_and_price`: waits until **both tickers have same-day prices** before
  updating the filter (handles out-of-order arrival in the event-driven backtest loop; live,
  prices arrive near-instantaneously).
- `calculate_signals`:
  - y = latest IEI price; **F = observation matrix** = [latest TLT price, 1] (intercept).
  - R = measurement noise variance (or zeros if uninitialised).
  - Compute predicted value ŷ = F·θ, forecast error e_t, variance Q_t, √Q_t; apply the
    standard Kalman update rules (from the state-space chapter) to update θ (posterior).
  - Generate BOT/SLD SignalEvents on TLT/IEI per the entry/exit rules, with
    `cur_hedge_qty = floor(qty × θ[0])` updated on entry (slope changes → re-hedge).
- `PriceParser`: prices multiplied by a large constant and stored as **integers** internally to
  avoid floating-point rounding accumulation over long backtests (divide by
  `PriceParser.PRICE_MULTIPLIER` when reading).
- Backtest file: equity 100,000 USD; **NaivePositionSizer** (accepts the strategy's absolute
  quantities), ExampleRiskManager, YahooDailyCsvBarPriceHandler, IBSimulatedExecutionHandler,
  TearsheetStatistics.

## Results & critique
- Equity: flat first year; rapid gains late 2010–2011; 2012 onward much more volatile,
  "underwater" until 2015, max daily drawdown **17.46%**; gradual recovery to max.
- **CAGR 7.66%, Sharpe 0.65**; max drawdown duration **817 days (over 2 years!)**. Net of
  transaction costs (IB fixed pricing) → reasonably realistic.
- Required research to make it robust: parameter validation/grid search or ML optimisation;
  asset selection (more/alternative pairs adds diversification but complexity); (book also
  mentions walk-forward etc. implicitly via "validation grid search").

## Takeaways / pitfalls
- Kalman filter removes the free "spread deviation threshold" parameter: thresholds emerge
  from the filter's own prediction uncertainty (√Q_t).
- Dynamic hedge ratio (θ0) updates online; re-hedge quantities must be recomputed (floor to
  whole shares).
- Event-driven backtest: wait for all constituents' same-day prices before filtering.
- Long drawdown durations (817 days) make such strategies hard to hold psychologically and
  in a capital-constrained setting — risk-manage accordingly.