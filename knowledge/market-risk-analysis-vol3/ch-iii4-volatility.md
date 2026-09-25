# III.4 Volatility

Source: Carol Alexander, *Market Risk Analysis*, Vol. III (Pricing, Hedging
and Trading Financial Instruments), ch III.4.

## Core idea

A set of standard European options on one underlying has two volatility
surfaces: the **implied volatility surface** (from inverting market prices
through BSM) and the **local volatility surface** (from Dupire's equation).
Model versions come from a stochastic-volatility model. Implied vol is a
deterministic function of the option price — model it and you model prices
and hedge ratios.

## Implied volatility and the smile

- **Implied volatility** = the constant volatility that, plugged into BSM,
  reproduces the market price. If BSM's assumptions held, all options on the
  same underlying would show one flat volatility — they do not.
- **Volatility smile**: implied vol vs strike (or moneyness) is not flat.
  - Equities: pronounced **negative skew** — high vol for low strikes (crash
    insurance demand); the risk-neutral distribution of log returns is
    highly non-normal (Breeden-Litzenberger).
  - FX: fairly symmetric smile.
  - Commodities: negative or positive skews; interest rates: negative;
    volatility options: positive skew.
- **Term structure of implied volatility**: implied vol vs maturity converges
  to the long-term level.
- Key inference: smiles persist to long maturities, contradicting i.i.d.
  log-return assumptions (CLT would flatten the skew) — returns are not i.i.d.;
  volatility is not constant (and for FX, rates are stochastic too).

## Local volatility (Dupire 1994)

For every set of market option prices there is a **unique market local
volatility surface** that locks in forward volatilities — the volatility dual
of the implied surface. BSM transforms prices → implied vols; **Dupire's
equation** transforms model prices → local vols. Each surface derives from the
other via integration/differentiation. Used to price exotics consistently
with vanilla market prices.

## Stochastic volatility models

- **Heston (1993)** is the practitioner default: tractable, relatively easy
  to calibrate to the implied surface; volatility follows a mean-reverting
  square-root process correlated with the price process.
- Calibration: parameters chosen so the model implied surface matches the
  market implied surface at calibration time — but the *dynamics* of the
  model surface may differ from empirical market-surface dynamics, making
  model deltas/gammas inaccurate.
- **Scale invariance** (Alexander-Nogueira): any process appropriate for
  pricing options on tradable assets must be scale invariant; as a corollary,
  the price sensitivities of standard European, barrier, Asian, etc. options
  are **model-free** — model differences in hedge ratios are empirical (fit),
  not structural.
- Ad-hoc "Heath Robinson" multi-parameter models (vol-of-vol, jumps, mean
  reversion stacked arbitrarily) fit anything but teach nothing; generalized
  approaches (Sato/self-decomposable processes, e.g., Carr et al.) fit
  arbitrary smiles with very few parameters.

## Volatility indices and variance swaps

- A volatility index of maturity T = average implied volatility across the
  smile; under standard assumptions it equals the **variance swap rate** of
  maturity T.
- Variance swaps traded OTC; **volatility index futures** (CBOE, Eurex) since
  2003; CBOE introduced options on the VIX (30-day S&P 500 vol index) in 2006.
- Trading an index requires buying all constituent options; futures/options
  on the index are the tradable instruments.

## Key takeaways

- Implied vol surface = market's volatility view; smile shape varies by asset
  class (equity skew strongest).
- Local vol (Dupire) is the unique surface locking in forward vols — the dual
  of implied vol; both are model-free transforms of market prices.
- Heston is the default stochastic-vol model; calibrate to the surface but
  watch surface *dynamics* for hedging accuracy.
- Scale invariance ⇒ option price sensitivities are model-free for tradable
  underlyings.
- Vol indices ≈ variance swap rates; the VIX is the canonical tradeable vol.

Related skills: `skills/arma-garch-modeling` (time-varying vol in the time
series), `skills/risk-metrics`, `knowledge/market-risk-analysis-vol2/ch-ii4`
(GARCH) — the time-series half of volatility modeling.
