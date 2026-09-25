# Automated Market Making (Quote Offsets, Inventory Risk, and Order-Flow Metrics)

## name
Automated market making: limit-order quote-offset models, inventory/
adverse-selection risk control, liquidity metrics (Kyle's lambda,
Amihud), order-flow imbalance (OFI) prediction, and the rebate-capture
profitability threshold.

## description
Market making is the HFT activity of posting two-sided limit orders
and earning the spread — but naive spread capture is eaten by
inventory risk and adverse selection. This skill distills the
quantitative toolkit for designing, simulating, and sizing a market-
making operation: how to set quote offsets (fixed, volatility-
dependent), how to simulate limit-order fills correctly, how to
measure the liquidity you trade against, how to predict short-term
moves from order-flow imbalance, and the cost/rebate math that decides
whether posting is profitable. Distilled from Irene Aldridge,
*High-Frequency Trading* (2013), chapters 10–12.

## when to use it
- Designing a market-making or liquidity-provision bot on a CLOB
  venue.
- Simulating limit-order strategies in a backtest (fills are
  conditional, not automatic).
- Choosing quote offsets given volatility and order-arrival rates.
- Measuring market liquidity (depth/impact) with Kyle's lambda or
  Amihud when building execution or alpha models.
- Building a short-horizon predictor from Level I data (OFI).
- Deciding whether maker rebates make a strategy viable.

## method / formula / code

**1. Limit-order fill simulation.** A limit buy executes only when the
last trade price or best ask **falls to or crosses** the limit price;
a limit sell when the trade price or best bid **rises to or crosses**
it. Simulate per tick:

```python
for t in ticks:
    if side == 'buy' and (last_price[t] <= limit or best_ask[t] <= limit):
        fill(limit)   # path-dependent: check every tick, not just bars
```

**2. Quote offsets.**
- Fixed offset: quote N ticks away; execution probability rises as N
  shrinks; turnover (flip frequency) drives profit, not time quoted.
- Volatility-dependent offset:
  `offset_t = round(mean((P_τ − P_{τ−1})²) over last T ticks)`
  i.e., scale the offset to recent realized variance.
- Order-arrival-dependent: shrink offset when market orders arrive
  slowly, widen when they flood in (avoid being picked off).

**3. Liquidity metrics.**
- Kyle's lambda: `ΔP_t = α + λ·NVOL_t + ε_t` where NVOL is the
  difference between best-bid and best-ask sizes at the touch (net
  order-flow imbalance); low λ = deep liquidity.
- Amihud illiquidity: `γ = (1/D)·Σ|r|/V` (avg absolute price change
  per unit volume).
- Support/resistance projection (when Level II unavailable):
  `SL_{t+1} = min(P_t) + (min(P_t) − min(P_{t−1}))`, analog for
  resistance with maxima.

**4. Order flow imbalance (OFI)** — Cont–Kukanov–Stoikov (2011):
sum signed changes in top-of-book size, signed by whether the best
bid/ask moved up or down:

```python
# e_n: +size if bid improves (new higher bid), -size if bid drops,
#      -size if ask improves (new lower ask), +size if ask rises
OFI_t = sum(e_n over ticks in bucket t)
# positive OFI predicts upward price drift in the next bucket
```

**5. Maker profitability / rebate threshold.** Posting a limit buy is
rational when expected value beats costs:

```python
# p_up = probability price rises one tick
p_up >= (txn_costs - rebate) / (2 * tick_value) + 0.5
```

Example: $0.0016/share costs with a $0.0020/share rebate →
`p_up ≥ 48%` (rebates lower the bar but never to 50%− for free
money; without the rebate the same costs need >70%).

## known pitfalls
- **Adverse selection**: your limit order fills preferentially when
  you are wrong (picked off by informed flow). Always quote wide
  enough to survive the informational fill rate; volatility-scaled
  offsets are the minimum defense.
- **Inventory drift**: buy-side fills and sell-side fills are rarely
  balanced — an unbalanced book is a directional position you didn't
  intend. Rebalance or cancel before the position grows.
- **Stub quotes**: quotes far from the market can execute during
  volatility spikes; most venues enforce ~10% distance limits — stay
  inside them.
- **Fill simulation naïveté**: simulating limit fills at bar close or
  at market price overstates fill probability; tick-level crossing
  logic is required.
- **OFI needs clean quote changes**: treat only top-of-book price/size
  changes; ignoring cancellations that don't move the touch biases the
  imbalance.

## source
Aldridge, *High-Frequency Trading* (2nd ed., 2013), ch10 (offset
models, Kyle, Amihud, support/resistance), ch11 (OFI, flow
autocorrelation, aggressiveness), ch12 (rebate-capture threshold).
