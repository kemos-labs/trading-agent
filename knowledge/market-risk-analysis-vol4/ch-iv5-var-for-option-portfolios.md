# IV.5 Value at Risk for Option Portfolios

Source: Carol Alexander, *Market Risk Analysis*, Vol. IV (Value at Risk
Models), ch IV.5.

## Core idea

Option prices are **non-linear** in their risk factors (underlying price and
implied volatility; also the squared price change — gamma), so VaR for option
portfolios needs different treatment than linear portfolios. Two distinct
estimates:
- **Dynamic VaR**: scale 1-day VaR to h days (√h), implicitly assuming the
  portfolio is rebalanced daily to constant sensitivities. Suitable for
  actively traded, delta-gamma-vega-neutral books; admissible under banking
  regulation (though Basel expects full 10-day shocks eventually). For normal
  i.i.d. returns dynamic and static VaR coincide for linear portfolios —
  NOT for options.
- **Static VaR**: measured directly from the h-day P&L with no rebalancing.
  Suitable for a single structured product held static. Gamma, vega, and
  theta effects are much more pronounced (gamma greatest).

## Why analytics fail

Delta-gamma mapping `P&L ≈ delta*R + 0.5*gamma*R^2` produces a P&L that is
highly **skewed and bimodal** — very hard to capture parametrically, and VaR
needs a precise fit in the tails where small discrepancies cause large errors.
Also, the Greeks are a local (small-move) approximation while VaR concerns
large moves; they are especially unreliable for stress testing.

## Historical simulation

Standard historical simulation works for **dynamic** VaR (large number of
daily returns, scaled). For **static** VaR it fails: overlapping h-day returns
distort the tail, and the only viable route is a parametric model of
conditional returns (GARCH) — filtered historical simulation (Barone-Adesi et
al.). A delta-gamma-hedged option portfolio has minimal price risk only if
continually rebalanced to neutrality.

## Monte Carlo VaR

The recommended approach, with exact revaluation at the risk horizon:
simulate the underlying and implied volatility as (typically negatively
correlated) factors, reprice options, take the quantile of the h-day P&L.
Key demonstration: measuring h-day VaR directly (static, correct for a single
option) vs scaling simulated daily P&L by √h (dynamic) — scaling ignores
gamma, vega, theta.

For large portfolios, use delta-gamma-vega mapping with a multivariate Taylor
expansion to revalue at the horizon, then MC on the mapped P&L (real-time VaR
under trader limits at 95% daily). A case study builds the risk-factor
returns model for a large energy options book.

## Strong conclusions

- The only viable method for **static** option VaR is parametric simulation —
  Monte Carlo or filtered historical simulation — based on a suitable model
  of risk-factor returns (non-normal + volatility clustering; mean reversion
  in vol factors matters except over very short horizons).
- Greeks-based approximations are crude for VaR (local approximation vs tail
  concern) but enable real-time VaR.
- Risk-factor mapping itself is a source of error for options (Taylor
  expansion is local).

## Key takeaways

- Dynamic VaR = scaled 1-day VaR (rebalanced portfolio); static VaR = h-day
  P&L quantile (no trading). Static has bigger gamma/vega/theta effects.
- Delta-gamma P&L is skewed/bimodal — parametric analytic VaR is unreliable.
- Use MC or filtered historical simulation with exact repricing for accurate
  option VaR; Greeks mapping only for fast real-time approximations.

Related skills: `skills/monte-carlo-option-pricing`, `skills/parametric-var`,
`knowledge/market-risk-analysis-vol3/ch-iii3` (option theory) and
`ch-iii5` (delta-gamma mapping).
