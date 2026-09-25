# Ch9 — Trade Evaluation

**Source:** *Volatility Trading*, 2nd ed. — Euan Sinclair (Wiley, 2013)

## Evaluating a volatility trade

A potential trade must be evaluated on its **expected value** given your
forecast, costs, and the distribution of outcomes — not on whether it
"feels" cheap. "In theory there is no difference between theory and
practice" — the gap is costs and path.

## Framework

- **Inputs**: your volatility forecast over the trade's life, implied vol at
  the strikes/maturities traded, expected hedging costs, and the
  distribution of realized vol (vol-of-vol).
- **Expected P&L of a delta-hedged option** ≈ ½·Γ·(σ_r² − σ_i²)·S² over the
  position's life — but this is the *mean*; evaluate the full distribution
  (skew, kurtosis, worst-case quantiles) because vol trades are
  path-dependent.
- **Breakeven analysis**: what realized vol (or what move) makes the trade
  break even net of costs? Long options: need realized > implied + cost
  uplift. Short options: need realized < implied − cost allowance.
- **Edge check**: state precisely what you expect to capture (e.g. "implied
  at 30, forecast 22, trade the difference, hedging costs ~2 vol points").
  If you can't write the edge down, don't trade.

## Costs & frictions

- Transaction costs (spread + commission) on both entry and every hedge
  rebalance; model them as an effective vol penalty (Leland-style).
- Slippage on the underlying hedge is often larger than the option spread
  itself — include it.
- Financing/carry (rates, dividends) shift put-call parity and hence
  which side is "cheap."

## Comparing trades

- Rank by **expected value per unit risk** (e.g. expected P&L per vega or
  per dollar of risk capital), not by headline premium.
- Account for the opportunity cost: capital used in one trade can't be in
  another; sizing and selection are joint decisions (see money management).
- Stress the evaluation: re-run with vol-of-vol ±, skew changes, and gap
  scenarios; the trade should survive the stress or be rejected.

## Key takeaways

- Evaluate the distribution of outcomes, not just expected value.
- Always net of costs: costs are part of the edge, not a footnote.
- Write down the edge in one sentence before trading.
- Rank candidates on expected value per unit risk and stress the
  assumptions (vol-of-vol, skew, gaps).
