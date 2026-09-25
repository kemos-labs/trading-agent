# IV.8 Capital Allocation

Source: Carol Alexander, *Market Risk Analysis*, Vol. IV (Value at Risk
Models), ch IV.8.

## Core idea

Senior management must ensure capitalization covers the risks taken. Two
concepts:
- **Regulatory capital**: legal minimum set by the Basel Committee; the bank
  may use standardized rules or an internal model (validated by the
  regulator) conforming to strict quantitative criteria. With a VaR model:
  **1% 10-day VaR**; with a scenario model: aggregate maximum loss.
- **Economic capital**: internally chosen risk metric (often ETL) at high
  confidence over a long horizon; any model, metric, data. Interpreted as the
  minimum capitalization such that the probability of insolvency over horizon
  h is ≤ α. Firms often hold more than the minimum as a confidence signal.

## Basel framework

- The 1988 Basel Accord set minimum capital standards (implemented G10,
  1992); the 1996 **Market Risk Amendment** introduced market-risk capital
  charges; Basel II refined with three **pillars** (minimum capital,
  supervisory review, market discipline).
- **Banking book vs trading book**: market risks are assessed on the trading
  book; different accounting frameworks.
- **Pillar 1 market-risk charge**: general market risk + **specific risk**
  add-ons + **incremental risk charge** (for internal models with specific
  risk recognition).

## Risk aggregation paradigms

- **Bottom-up risk assessment**: instrument → portfolio → desk → business
  unit → firm-wide; market risk aggregated with credit and operational risk.
  Most common, but **aggregation risk** arises from assuming correlation-only
  linear normal dependence — the major source of model risk in firm-wide
  capital. Also assumes positions are marked to market; mark-to-model
  positions introduce pricing-model risk.
- **Top-down capital allocation**: total firm economic capital is allocated
  down to business units, desks, traders. Economic capital allocation becomes
  a management tool: more capital = more risk capacity; withdrawals control
  activities.

## RAROC

**Risk-adjusted return on capital**:

```
RAROC = expected profit / economic capital
```

Combines forecasts of expected P&L with economic capital per activity; the
firm optimizes capital allocation by maximizing firm-wide risk-adjusted
performance. One of the most common industry performance measures.

## Key takeaways

- Regulatory capital: standardized rules or internal models (1% 10-day VaR);
  economic capital: any metric (often ETL) with a solvency interpretation.
- Basel II three pillars; trading-book focus; specific-risk and incremental
  charges.
- Bottom-up aggregation introduces correlation-model risk; top-down
  allocation uses economic capital as control.
- RAROC = expected profit / economic capital — the standard for
  capital-constrained performance evaluation.

Related skills: `skills/risk-metrics`, `skills/kelly-position-sizing`
(capital allocation ideas), `skills/portfolio-optimization`,
`skills/var-backtesting`.
