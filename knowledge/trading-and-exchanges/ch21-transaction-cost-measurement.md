# Ch21 — Transaction Cost Measurement

**Source:** Larry Harris, *Trading and Exchanges* (2003), Chapter 21.

## Purpose
How to measure the true cost of trading: the components, the
benchmarks, and the measurement problems that make execution quality
hard to audit.

## Cost components
1. **Commissions/fees** — visible, easy.
2. **Half-spread** — for a marketable order: |execution price −
   prevailing mid| (the effective half-spread).
3. **Market impact** — the portion of the price move *caused by the
   order itself*: estimated as the difference between the effective
   spread and the *realized* spread (impact = effective − realized).
4. **Opportunity/delay cost** — adverse moves between decision and
   execution; measured against the decision price.
5. **Timing cost** — the component due to trading over a window vs.
   instantaneously.

## Benchmarks
- **Arrival price** (decision price at order submission): the
   standard for measuring shortfall.
- **VWAP** (volume-weighted average price over the trading day):
   popular but gameable; only meaningful for orders that should
   participate evenly.
- **TWAP**, **POV** (participation rate), **implementation
   shortfall** (Perold): `shortfall = (arrival − execution)/shares`
   expressed in bps of the decision value.
- **Pre-trade cost models** (impact curves) predict cost as a
   function of size, volatility, and participation rate.

## The measurement problems
- **Trade classification**: whether a trade was buyer- or seller-
  initiated (needed for signed analysis) requires tick rules
  (Lee–Ready) or quote matching — errors bias spread estimates.
- **Impact vs. drift**: the observed price move mixes the order's own
  impact with market drift; separating them needs matched control
  periods or models.
- **Timing benchmarks**: choosing the benchmark defines the answer —
  arrival vs. VWAP vs. close yield very different "costs."
- Retail traders can rarely measure these at all (no data, no norms),
  which is why execution-quality regulation exists.

## Key takeaways
- **Transaction costs are the strategy**: for high-frequency or
  low-edge strategies, the difference between quoted and effective
  costs can exceed the entire expected edge.
- Measure costs **against arrival price**, in bps, per order and per
  strategy; report spread, impact, and opportunity cost separately.
- Validate brokers/venues by realized execution quality (effective
  spread + impact), not by commission schedules.
