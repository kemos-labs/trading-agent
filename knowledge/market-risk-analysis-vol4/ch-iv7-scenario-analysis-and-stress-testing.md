# IV.7 Scenario Analysis and Stress Testing

Source: Carol Alexander, *Market Risk Analysis*, Vol. IV (Value at Risk
Models), ch IV.7.

## Core idea

Risk is forward-looking uncertainty — history is only one source of beliefs.
Stress testing quantifies potential losses under extreme-but-credible events.
The key message: formalize beliefs as **probability distributions**, not
vague terms like "worst case" (which is mathematically meaningless — there is
no worst case other than total loss). Scenario analysis pre-dates VaR: the
CME's SPAN margin system (1988) stresses portfolios with parallel shifts and
yield-curve tilts.

## Scenario taxonomy

Two dimensions: type of change × data source.
- **Single case scenarios**: one vector of risk-factor returns (e.g., a 100bp
  parallel yield shift) → a single "loss" via the portfolio mapping, but NO
  probability attached.
- **Distribution scenarios**: an entire multivariate distribution of
  risk-factor returns (e.g., perfectly correlated normal yield changes with
  mean 100bp, sd 50bp) → probabilities can be assigned to loss levels; a
  mathematically coherent framework.
- **Historical vs hypothetical**: historical from past data; hypothetical from
  analyst/management views (essential when little or no data — operational
  risk, unlisted stocks, junk bonds).

Crises (Russian default 1998, tech bubble 2000, credit crunch 2007) were
events with no historical precedent — reliance on history is misplaced for
tail risk; scenario analysis escapes that.

## Scenario VaR / ETL

Distribution scenarios plug into the risk model (mapping + distribution +
resolution) to derive **scenario VaR and ETL**. Distinguish scenario VaR from
Bayesian VaR: scenario VaR uses the scenario distribution directly; Bayesian
VaR updates a prior with data.

## Traditional stress testing

Worst-case loss = max loss over a set of stress scenarios applied via the
portfolio mapping. Basel Committee recommendations reviewed. Preliminary
**sensitivity analysis** (loss profile as a function of each risk factor)
identifies the main risk drivers and focuses scenarios — especially important
for option portfolios, where a *small* move in a major factor can cause the
largest loss (non-linear profiles).

## Coherent stress testing

- **Stressed covariance matrices**: replace the covariance matrix with one
  reflecting stressed conditions (higher volatilities/correlations) — apply
  in all three VaR methods (parametric, historical, Monte Carlo) to get
  stressed VaR/ETL. Hypothetical stressed matrices must be positive
  semi-definite.
- **PCA in stress tests**: reduce complexity and focus on the most likely
  market moves (shift/tilt/curvature factors).
- **Liquidity-adjusted VaR**: differentiate exogenous liquidity (market-wide)
  from endogenous (position-size-dependent).
- **Volatility clustering effects**: matter significantly for multi-day
  holdings.

## Key takeaways

- Replace verbal "worst case" language with distribution scenarios that carry
  probabilities.
- Single-case scenarios give losses without probabilities; distribution
  scenarios give coherent scenario VaR/ETL.
- Do sensitivity analysis first to identify the risk drivers and their
  non-linearities.
- Stress via stressed covariance matrices (keep them PSD), PCA-focused
  scenarios, and liquidity adjustment.

Related skills: `skills/risk-metrics`, `skills/correlated-scenario-
simulation`, `skills/parametric-var`, `skills/var-backtesting`.
