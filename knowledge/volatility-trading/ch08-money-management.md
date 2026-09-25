# Ch8 — Money Management

**Source:** *Volatility Trading*, 2nd ed. — Euan Sinclair (Wiley, 2013)

## Why sizing matters more than edge

Two traders with identical edge can have wildly different outcomes purely
from position sizing. Sinclair's example: two coin-flip traders with a 55%
win rate; one sizes fixed fraction, one over-bets → one ends with ~$5,200,
the other ~$620. Sizing is a first-order determinant of long-run wealth.

## The Kelly criterion

For a bet with win probability p, loss probability q = 1−p, and payoff odds
b (net gain per unit staked):

- **Discrete Kelly**: f* = (bp − q) / b = p − q/b. This is the fraction of
  capital that maximizes the expected *growth rate* of wealth.
- **Continuous/Gaussian Kelly** (for normally distributed returns with mean
  m and variance σ²): f* = m / σ² (betting fraction proportional to Sharpe
  per unit variance).
- Kelly maximizes expected log-wealth growth; over-betting beyond 2× Kelly
  destroys growth (expected growth goes negative past ~2f*).

## Practical Kelly for volatility trading

- **Vol trades are not single Bernoulli bets**: they have continuous,
  fat-tailed, skewed P&L. Use the continuous version with the full
  distribution (mean and variance, but know kurtosis/skew: short-vol has
  negative skew, so full Kelly is aggressive — the tail is worse than the
  Gaussian assumes).
- **Fractional Kelly**: trade a fraction (e.g. ½ or ¼ Kelly) to reduce
  variance and drawdowns; growth is only slightly reduced while tail risk
  drops a lot.
- **Estimation error is huge**: Kelly is very sensitive to errors in p/odds;
  a slightly overestimated edge → over-betting. Hence fractional Kelly is
  the professional default.
- **Volatility targeting**: size positions so portfolio vol (or vega) is a
  constant fraction of capital; this is a practical approximation to Kelly
  for normally-sized books and is robust to estimation error.

## Framework

- Each trade is sized according to its projected return and risk **in the
  context of your overall goal** — the same trade is sized differently by a
  profit-maximizer, a target-return trader, or a hedger.
- Aggregate risk across the book (net vega/gamma/delta exposure), not per
  trade.
- Keep comprehensive records: you must know your P/L profile to know your
  true edge and to size correctly. Without records there is no way to
  improve.

## Key takeaways

- Sizing scheme is as important as the edge itself.
- Kelly maximizes growth but is fragile to estimation error; use fractional
  Kelly or vol targeting.
- Continuous, fat-tailed distributions (options P&L) → be conservative with
  Kelly; short-vol's negative skew argues for smaller size.
- Records → edge estimation → correct sizing: the loop that makes a string
  of uncertain trades a profitable business.
