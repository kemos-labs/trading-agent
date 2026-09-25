# Spread Decomposition and Transaction-Cost Measurement

## name
Spread decomposition and transaction-cost measurement: estimating the
quoted/effective/realized spread, price impact, and the fundamental vs.
transitory volatility split from trade and quote data.

## description
The bid/ask spread is an information tax, not just a fee. This skill
distills the standard quantitative toolkit for measuring what trading
actually costs — and *who pays whom* — from tick data: Lee–Ready trade
classification, quoted vs. effective vs. realized spreads, the
adverse-selection (price-impact) component, Roll's covariance-based
spread estimator, and variance-ratio tests that separate fundamental
volatility (information) from transitory volatility (liquidity
friction). Distilled from Larry Harris, *Trading and Exchanges*
(2003), chapters 14, 20, and 21.

## when to use it
- Measuring the true cost of an execution or a strategy: is your edge
  bigger than the spread + impact you pay?
- Estimating the adverse-selection risk of a liquidity-supplying
  strategy (limit-order or market-making): how much of the spread do
  you actually keep after informed traders pick you off?
- Auditing venues/brokers: effective spread vs. NBBO, realized
  spread vs. quoted spread.
- Deciding whether a mean-reversion signal is real: variance-ratio
  tests tell you how much short-horizon price noise (transitory
  volatility) is available to harvest.

## method / formula / code

**1. Classify trades (Lee–Ready).** A trade is buyer-initiated if its
price is above the prevailing midpoint (and by tick test when at the
midpoint):

```python
mid = (bid + ask) / 2
buy = price > mid  # price < mid -> sell; at mid, use tick rule (uptick -> buy)
```

**2. Spread measures** (per trade, then averaged; the *full* spread is
2× the half-spread measures below — keep the convention consistent):
- Quoted spread: `ask - bid` (the visible cost of immediacy).
- Effective half-spread: `|price - mid|` — what a marketable order
  actually pays, including price improvement.
- Realized half-spread: `sign * (price - mid_after)` where
  `mid_after` is the midpoint ~5 minutes (or N trades) later — the
  component the liquidity provider *keeps* after the price moves.
- Price impact = effective − realized: the adverse-selection cost
  (informed traders' profits plus order-flow persistence).

**3. Roll's estimator** (spread without quote data, from the serial
covariance of price changes):

```python
d = price.diff()
cov01 = np.cov(d.dropna(), d.shift(1).dropna())[0, 1]  # lag-1 autocov
spread = 2 * np.sqrt(-cov01) if cov01 < 0 else 0.0
# valid when cov01 < 0 (bid/ask bounce); if cov01 >= 0 (trending),
# the estimator is undefined — report 0/NaN rather than forcing it
```

**4. Variance ratio** (fundamental vs. transitory volatility):
`VR(k) = Var(k-period returns) / (k * Var(1-period returns))`.
A pure random walk gives VR = 1; transitory (bounce) noise makes
`VR(k) < 1` because short-horizon variance is inflated relative to
long-horizon. The gap `1 - VR(k)` is a proxy for the tradeable
transitory component.

## known pitfalls
- **Misclassification bias**: tick rules and quote rules misclassify
  trades around the midpoint; this inflates effective spread estimates
  and distorts impact. Cross-check with actual trade direction when
  available (e.g., exchange flags).
- **Impact vs. drift**: observed post-trade moves mix the order's own
  impact with market drift; a short (5-min) horizon mitigates but
  does not remove this. Control for market returns where possible.
- **Roll estimator sign**: the covariance must be negative; if
  positive (trending markets), the estimator is undefined — do not
  force it.
- **Benchmark choice defines the answer**: arrival price vs. VWAP vs.
  close yield wildly different "costs." Always state the benchmark
  (prefer arrival for shortfall).
- **Timestamp alignment**: quote and trade timestamps must be
  synchronized; using stale midpoints biases realized-spread
  estimates toward zero.

## source
Harris, *Trading and Exchanges* (2003), ch14 (spread decomposition,
Glosten–Milgrom logic), ch20 (fundamental vs. transitory volatility,
variance ratio, Roll), ch21 (transaction-cost measurement, benchmarks).
