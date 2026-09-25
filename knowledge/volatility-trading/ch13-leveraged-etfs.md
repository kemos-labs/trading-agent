# Ch13 — Leveraged ETFs

**Source:** *Volatility Trading*, 2nd ed. — Euan Sinclair (Wiley, 2013)

## What they are

Leveraged ETFs (e.g. 2× or 3× daily long/short equity indexes, and inverse
products) promise to deliver a multiple of the **daily** return of the
underlying index. They rebalance daily to maintain constant leverage — that
daily rebalancing is the source of everything unusual about them.

## The volatility drag

A constant-leverage, daily-rebalanced position does **not** compound to the
leveraged buy-and-hold return. The long-run return of a leveraged ETF with
daily leverage L and underlying drift μ, variance σ² is approximately:

- Log-return ≈ L·μ·T − ½·L²·σ²·T (for one period, and roughly T periods).

The extra −½·L²·σ² term (vs. the un-levered −½·σ²) is the **volatility
drag**: doubling leverage quadruples the drag. In a flat but volatile
market, a 2× ETF decays even if the index ends flat; a 3× ETF decays
faster. Over time, LETF returns = leveraged index drift − leverage-squared
variance penalty.

## Consequences

- **Long-term holders lose the drag**: a 3× ETF is not "3× the index over a
  year"; it's 3× daily compounding minus the vol penalty. High vol and flat
  markets make the decay severe.
- **Inverse ETFs have the same problem** (and worse in trending markets):
  short daily leverage ≠ short buy-and-hold.
- **Rebalancing flows**: LETFs must buy on up days and sell on down days
  (to restore leverage), adding momentum-like flow to the underlying —
  especially in large, liquid leveraged products on indexes (a measurable
  feedback effect around ETF rebalance times).
- **Options on LETFs**: volatility of the LETF is roughly the leverage
  multiple of the underlying's vol (with its own dynamics from the daily
  reset); pricing/hedging LETF options needs the leverage and reset
  mechanics, not just "2× the index options."

## Trader's perspective

- LETFs are volatility-sensitive instruments: their long-run return is a
  function of the underlying's variance. This makes them (and their
  options) vehicles for expressing vol views, and a source of predictable
  flow.
- Never extrapolate the daily multiple to buy-and-hold horizons — compute
  the drag: expected LETF return ≈ L·μ − ½·L²·σ².
- The rebalancing flow is a tradable pattern (e.g. around the close on
  rebalance days) but it's crowded; treat it as microstructure alpha, not
  the main event.

## Key takeaways

- Daily rebalancing = constant leverage = volatility drag: return ≈ L·μ −
  ½·L²·σ².
- Leveraged and inverse ETFs decay in volatile/flat markets; they are not
  simple multiples of buy-and-hold.
- LETF rebalancing creates predictable flows into the underlying.
- LETF options price off leveraged, resetting volatility — model the
  mechanics.
