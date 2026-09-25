# Backtesting Framework (Consolidated)

## name
Two-tier strategy backtesting: fast vectorized first pass, then an
event-driven engine for realism — plus the data-quality and
performance-measurement discipline that keeps backtests honest.

## description
The complete backtesting playbook. Tier 1 is the vectorized skeleton
(returns → position.shift(1) → strategy returns → cumulative P&L with
transaction costs) for instant signal screening. Tier 2 is the
event-driven architecture (event queue + data/price handler + strategy +
portfolio + position sizer + risk manager + execution handler +
statistics) that mirrors live deployment — realistic fees, partial
fills, path-dependent state. Wraps both tiers in the measurement
discipline: correct Sharpe annualization, max drawdown + duration, MAR,
and the data-quality checks (split/dividend adjustment, survivorship
bias, H/L noise) and overfitting defenses (walk-forward, purged CV)
that separate honest numbers from self-deception. Consolidates
`skills/vectorized-backtesting`, `skills/walk-forward-validation`, and
`skills/purged-cross-validation`.

## when to use it
- You have a signal (indicator, ML prediction, factor) and need P&L
  quickly → Tier 1 vectorized first.
- You need realism the vectors can't give: stops, position sizing,
  risk overrides, execution details, fixed costs, path-dependent state
  → Tier 2 event-driven.
- Before trusting any result: check data quality, use yesterday's
  signals, model costs, and quote out-of-sample numbers only.
- Auditing whether a strategy has edge before investing in live
  infrastructure (most strategies should die in Tier 1).

## the method

### Tier 1 — Vectorized backtest (the fast first pass)
```python
import numpy as np
import pandas as pd

data = pd.read_csv('prices.csv', index_col=0, parse_dates=True)
data['returns'] = np.log(data['price'] / data['price'].shift(1))

# signal → position (-1/0/+1), ffill to hold between signals
sma_s, sma_l = data['price'].rolling(42).mean(), data['price'].rolling(252).mean()
data['position'] = 0.0                                   # warm-up flat (rolling NaN)
valid = sma_s.notna() & sma_l.notna()
data.loc[valid, 'position'] = np.where(sma_s[valid] > sma_l[valid], 1, -1)
data['position'] = data['position'].ffill()              # hold between signals

# THE no-look-ahead step: yesterday's position × today's return
data['strategy'] = data['position'].shift(1) * data['returns']

# transaction costs (proportional per position change)
ptc = 0.001
data['strategy_net'] = np.where(data['position'].diff() != 0,
                                data['strategy'] - ptc, data['strategy'])

perf = data['strategy_net'].cumsum().apply(np.exp)       # log-return compounding
bench = data['returns'].cumsum().apply(np.exp)
```

### Tier 2 — Event-driven engine (realism)
Architecture that mirrors a small quant fund's bespoke stack (QSTrader
is the canonical open-source implementation):

- **Event** — all messages as subclassed objects (BarEvent, SignalEvent,
  OrderEvent, FillEvent…), exchanged through a queue.
- **DataHandler / PriceHandler** — ingests bars/ticks (backtest replay or
  live feed) and produces MarketEvents.
- **Strategy** — the alpha-generation code; consumes market data, emits
  SignalEvents. Keep this isolated from everything else (swap strategies
  freely).
- **Portfolio** — positions + cash; computes equity, realized/unrealized
  PnL, handles averaging across lots.
- **PositionSizer** — turns signals into order size (vol targeting,
  Kelly — see `skills/volatility-targeted-position-sizing`).
- **RiskManager** — can veto or modify orders (position limits,
  correlation checks, drawdown cutoffs).
- **ExecutionHandler** — sends orders, receives fills; in backtests this
  is *simulated with realistic fees, slippage, and impact* (turn fees ON
  by default).
- **Statistics** — equity curve, Sharpe, drawdowns, tearsheets.

Loop: for each bar → PriceHandler emits → Strategy reacts → Signal →
PositionSizer → RiskManager → ExecutionHandler → Fill → Portfolio
updates → Statistics. Loose coupling via the event queue lets you swap
any component for live equivalents without touching the rest.

### Data quality (do this before believing any result)
- **Splits/dividends**: apply multiplicative adjustment factors so daily
  returns are invariant; unadjusted data shows spurious ex-date drops →
  false signals.
- **Survivorship bias**: databases missing delisted stocks inflate
  results massively (Chan: "buy 10 lowest-priced stocks, hold 1y" gave
  +388% on biased data vs −42% on bias-free data). Use point-in-time
  snapshots.
- **High/low noise**: H/L are noisier than O/C; a limit order may not
  fill at recorded H/L — H/L-based backtests overstate returns.
- **Return sanity**: flag returns > 4σ from the mean and check them
  against news before treating them as real.

### Performance measurement
- **Sharpe**: annualized = √N_T × period-Sharpe (N_T = periods/year;
  daily √252; NYSE-hourly √1638, not √6048). For dollar-neutral /
  self-financing portfolios do NOT subtract the risk-free rate (short
  proceeds fund longs) — excess return ≈ strategy return.
- **Max drawdown & duration**: hwm(t) = max(hwm(t−1), cumret(t));
  DD(t) = (1+cumret(t))/(1+hwm(t)) − 1; max DD = min(DD); duration =
  longest run of non-zero DD. Max DD and max duration rarely overlap.
- **MAR ratio** = CAGR / max drawdown — leverage-relative, better than
  raw CAGR.
- **Net numbers only**: gross P&L is the sales pitch; proportional +
  fixed costs + slippage + impact are the reality (see Tier 1 ptc).

### Overfitting defenses (never skip)
- Train/test split or walk-forward (`skills/walk-forward-validation`) —
  report only out-of-sample numbers.
- For overlapping/path-dependent labels: purged k-fold with embargo and
  Combinatorial Purged CV (`skills/purged-cross-validation`); judge
  significance with PSR/DSR (deflated Sharpe) to correct for the number
  of trials.

## known pitfalls
- **Missing shift(1)**: the classic look-ahead bug — verify
  `position.shift(1)` before believing anything.
- **Signal churn**: re-signaling every bar without ffill creates phantom
  turnover; real costs then expose it and can reverse strategy rankings.
- **Costs omitted**: a strategy that looks great gross can be net-
  negative; model all costs before conclusions.
- **Survivorship + split bias**: both silently inflate returns — the two
  most common data-quality killers.
- **Vectorization limits**: fixed costs, non-divisible units, stops, and
  running-P&L-dependent logic need Tier 2 — know when to graduate.
- **Warm-up NaNs**: rolling windows leave NaNs; `np.where` on NaN
  comparisons yields −1 (False), so set positions to 0 explicitly for
  the warm-up region (see Tier 1 code) rather than relying on fillna.
- **Sharpe annualization mistakes** and subtracting risk-free where the
  strategy never borrows — both distort ranking across strategies.

## source
Hilpisch, *Python for Algorithmic Trading*, ch4–5 (vectorized
backtesting, transaction costs, data snooping); Halls-Moore, *Advanced
Algorithmic Trading*, ch24 (QSTrader event-driven architecture);
Chan, *Quantitative Trading*, 2nd ed., ch3 (data issues, performance
measurement, pitfalls). Consolidates `skills/vectorized-backtesting`,
`skills/walk-forward-validation`, `skills/purged-cross-validation`;
knowledge notes in `knowledge/chan-quantitative-trading/ch03-backtesting`
and `knowledge/halls-moore-advanced-algorithmic-trading/ch24-qstrader-
backtesting-engine`.
