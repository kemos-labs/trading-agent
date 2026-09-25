# Ch5 — Implied Volatility Dynamics

**Source:** *Volatility Trading*, 2nd ed. — Euan Sinclair (Wiley, 2013)

## What implied volatility is

IV is the volatility that, plugged into a pricing model, reproduces the
market price. It is the market's (risk-neutral) forecast of future vol over
the option's life, quoted in vol space. It is not a constant — it is a
surface across strike and maturity.

## The volatility surface

- **Term structure**: IV vs. maturity. Usually upward-sloping (longer
  options carry higher vol) in calm markets, and it can invert in crises.
  Interpreted as the market's expectation of how vol will evolve.
- **Skew (smile)**: IV vs. strike for a fixed maturity. Equity indices show
  a pronounced negative/put skew: OTM puts demand higher IV than OTM calls
  (crash insurance demand, leverage effect). FX typically shows a symmetric
  smile; commodities vary.
- **Smile dynamics**:
  - *Sticky strike*: IV stays fixed at a given strike as spot moves (each
    strike keeps its own vol). Under this regime, delta hedging is
    "correct" — the option's P&L behaves like the model says.
  - *Sticky delta*: IV stays fixed at a given delta/moneyness (S/K or
    delta), i.e. the whole surface slides with spot. Under sticky delta,
    vega and gamma behave differently — the option behaves as if the
    underlying's vol regime has changed.
  - Reality sits between; measuring which regime dominates matters for
    choosing hedging assumptions and for pricing OTM options.

## Why IV deviates from forecasts

- **Demand/supply**: hedgers systematically buy OTM puts (portfolio
  insurance) → put skew premium; short-vol sellers push index IV above
  realized (variance premium).
- **Behavioral**: overreaction to recent realized vol, crashophobia.
- **Model frictions**: discrete hedging costs, jumps, stochastic vol all
  embed premia in observed IV.

## Trading implications

- Trade IV only when you can explain *why* it is at its level — "expensive"
  or "cheap" relative to your forecast is not enough; the market may be
  right.
- Compare IV to the vol forecast over the *same horizon and at the same
  strike region* (moneyness matters: skew means ATM IV ≠ OTM IV).
- Know the surface dynamics regime (sticky strike vs. sticky delta) before
  deciding how hedges behave; this changes expected P&L of hedged trades.

## Key takeaways

- IV is a forecast with a premium, quoted as a surface, not a number.
- The skew is real and persistent on indices: price it in, don't fight it
  blindly.
- Sticky-strike vs. sticky-delta changes how hedged positions earn; measure
  which regime the market is in.
- Explain the mispricing before trading it.
