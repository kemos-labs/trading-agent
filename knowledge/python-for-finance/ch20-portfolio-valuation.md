# Chapter 20 — Portfolio Valuation

## Core idea
Extending the DX library from single instruments to **portfolios of
derivatives**: a `derivatives_position` class (instrument + quantity) and a
`derivatives_portfolio` class (many positions + aggregation + risk).

## Design requirements
- **Nonredundancy**: each risk factor (underlying) is modeled once and
  shared by multiple valuation objects — one simulation per underlying, not
  per option.
- **Correlations**: multiple underlyings must be correlated (via Cholesky on
  correlated normal draws — see `skills/correlated-scenario-simulation`).
- **Positions**: a position = valuation object + quantity (number of
  contracts).
- Single-currency assumption simplifies aggregation (no FX).

## Derivatives positions
```python
class derivatives_position(object):
    def __init__(self, name, quantity, underlying, mar_env, otype, payoff_func):
        ...
    def get_info(self): ...   # prints name/quantity/otype/payoff
```
A lightweight container: which valuation class (`otype`), what underlying,
what payoff string, how many contracts.

## Derivatives portfolios
- Holds a list of positions.
- Valuation: **run each position's simulation once** (sharing the underlying
  simulation object), aggregate values weighted by quantity.
- Risk reporting: portfolio-level delta/vega by summing position Greeks;
  VaR via re-simulation of the joint paths (correlated).
- `get_info()` and summary methods for reporting.

## Why this matters
- A derivatives book is a portfolio; consistent valuation requires common
  market environments and shared, correlated simulations — exactly what
  these classes enforce.
- Portfolio-level risk (aggregated Greeks, VaR) is what institutions manage,
  not single-option risk.

## Pitfalls
- Double-simulating the same underlying per option wastes compute and breaks
  consistency — share simulation objects.
- Ignoring correlations understates portfolio risk (fat-tailed joint moves).
- Currency mismatches require FX modeling — the book sidesteps by assuming
  single currency.

## How the pieces fit (DX recap)
- `market_environment` holds constants/curves for each instrument.
- One simulation object per underlying (GBM/jump/CIR) is shared across all
  positions on that underlying — correlated underlyings via Cholesky.
- `valuation_mcs_european/american` price each instrument; positions add
  quantity; the portfolio sums to a book value and aggregates Greeks.
- Risk: re-simulation of the joint paths gives the portfolio value
  distribution → VaR/cVaR at the book level.

## Bottom line
The aggregation layer: position → portfolio → portfolio Greeks and VaR,
with shared correlated simulations. Cross-refs:
`skills/correlated-scenario-simulation` (correlated draws),
`skills/risk-metrics` (VaR/cVaR on portfolio returns), and
`knowledge/python-for-finance/ch21` (the full market-based case study).
