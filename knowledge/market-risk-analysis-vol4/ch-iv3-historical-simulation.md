# IV.3 Historical Simulation

Source: Carol Alexander, *Market Risk Analysis*, Vol. IV (Value at Risk
Models), ch IV.3.

## Core idea

Historical VaR estimates the empirical quantile of historical (adjusted)
portfolio returns — no parametric assumption about the distribution, and the
dynamics and dependencies of risk factors are inferred directly from history.
~75% of banks prefer it (Perignon-Smith survey). It is not limited to linear
portfolios and naturally captures path dependence (volatility clustering)
without fitting a model.

## Why it wins / where it loses

**Advantages** over parametric linear VaR: no parametric form, no i.i.d.
assumption, no correlation-only dependence, works for non-linear portfolios.
**Advantages** over Monte Carlo: no dependence on a possibly-misspecified
behavioral model.

**Limitations**:
- **Data requirements**: ~4 years of daily data is insufficient for accurate
  tail estimates; long horizons hard (overlapping h-day returns distort the
  tail).
- **Scaling problem**: usually estimate 1-day VaR and scale. Square-root-of-
  time assumes stable/self-similar distributions; estimated **scale
  exponents** (log-log slope of quantile ratio vs horizon) are ≈ 0.5 for
  equities and $/£ FX, but ≈ 0.55–0.6 for US interest rates (trending), and
  < 0.5 for volatility indices (fast mean reversion) — scaling volatility
  with √t is definitely wrong.
- **Static portfolio assumption**: holding the *current* portfolio
  throughout history is unrealistic when market conditions differed.
- **Regime mixing**: a long history spans calm and crisis regimes with very
  different volatilities/correlations; equal weighting misrepresents current
  conditions.

## The implementation recipe

1. Obtain a sufficiently long history of risk-factor data.
2. **Adjust returns to current market conditions** — the choice of data, not
   the model, usually determines accuracy. Recommend a **volatility
   adjustment**: scale historical returns so current volatility is embedded.
3. Fit the empirical distribution of adjusted returns.
4. Derive VaR/ETL at the required significance and horizon.

**Filtered historical simulation** (Barone-Adesi et al. 1998/99): combine a
GARCH volatility model with the empirical (bootstrap) distribution of
residuals — Monte-Carlo-like scenarios from realistic conditional
distributions. It fixes the regime-mixing and scaling problems and is the
recommended historical approach.

## Tail precision (99%+)

With only a few years of data, extreme-quantile estimates are noisy:
- **Non-parametric smoothing**: kernel density (Epanechnikov, Gaussian).
- **Parametric fitting**: Johnson SU (fit first four moments), Cornish-Fisher
  expansion, generalized Pareto / extreme value distributions (EVT).

## Systematic historical VaR

For linear portfolios: simulate historical returns on the risk-factor mapping
(current weights/betas/PV01s held constant), compute the empirical quantile;
disaggregate into stand-alone and marginal VaR components like the parametric
model. ETL is computed as the average of losses beyond the VaR quantile;
parametric fitting (e.g., Johnson) gives analytic historical ETL.

## Key takeaways

- Historical VaR = empirical quantile of adjusted historical returns; no
  parametric assumption.
- Volatility-adjust the data and use filtered historical simulation for
  regime-aware, tail-accurate estimates.
- Scale exponents: use ≈0.5 for equities/FX, >0.5 for rates, <0.5 for vol.
- For extreme quantiles with short histories, smooth (kernel) or fit
  parametric tails (Johnson SU, Cornish-Fisher, EVT).
- Explicitly hold the current portfolio (weights/sensitivities) constant.

Related skills: `skills/risk-metrics`, `skills/parametric-var`,
`skills/var-backtesting`; `knowledge/market-risk-analysis-vol2/ch-ii4`
(GARCH for filtered historical simulation).
