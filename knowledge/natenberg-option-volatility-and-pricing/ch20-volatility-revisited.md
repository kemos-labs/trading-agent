# Chapter 20 — Volatility Revisited

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## The central principle

> **The longer an option position is held, the more important realized
> volatility is and the less important implied volatility. Held to
> expiration, realized volatility is the *only* thing that matters.**

Example: buy 100 straddle at IV 20% (6.25). IV → 22%: *immediately*
+0.62; *over 3 weeks with a flat market* −0.82 (theta overwhelms the
vega move). IV → 18%: immediately −0.63, but with a spot move to 105 →
+0.84, to 95 → +0.62 (gamma pays). Prices (IV) drive interim cash flow
and funding; value is determined by realized vol.

## Calculating historical volatility

- Population σ (÷n) vs. sample σ (÷n−1) — use **sample** when
  forecasting (the sample understates extremes).
- Returns: percent or ln(S_t/S_{t−1}) (settlement-to-settlement,
  business days); **zero-mean assumption** (μ = 0): a contract rising
  1%/day for 10 days has 0 vol by the usual formula — wrong for trading.
- Annualize: σ_ann = σ_period × √(periods per year). Trading days
  (~250–260) vs. 365-day (0-change days) barely differ. Daily vs. weekly
  returns look similar; daily chosen for more data points (smoother).
- Alternative estimators: **Parkinson** (high-low):
  `σ = √(1/(4n)) · Σ [ln(h_i/l_i)]² / √t`... (annualized from intraday
  extremes); **Garman-Klass** adds open/close terms. Both run *below*
  close-to-close for partial-day markets (overnight vol unobservable) —
  weight the estimates accordingly.

## Volatility characteristics

- **Serial correlation**: tomorrow's vol ≈ today's (weather analogy).
- **Mean reversion**: vol always returns to a mean (S&P ~15–20%, Bund
  ~5%, gold ~10–20% over 2001–2010) — price does NOT revert, vol does.
- **Term structure / volatility cones**: short-horizon realized vol
  ranges wildly (S&P 2-wk: 5–100%), long-horizon converges (300-wk:
  14–24%) → **long-term vol is easier to predict** — but long-term
  options have more vega, so a given vol error hurts more there.
- Trending segments exist; technical analysis partially applies to vol
  charts (modified).

## Forecasting

- Weighted averages of trailing realized vols: weight the horizon that
  *matches the option's time to expiration* most heavily (serial
  correlation argument).
- **EWMA**: σ²_next = Σ α_i·r_i² with geometrically decaying weights
  (α_n > α_{n−1}); common λ ≈ 0.94 (RiskMetrics). Uses the non-overlapping
  return series (true time series).
- **ARCH (Engle, 1982) / GARCH**: EWMA + *volatility clustering*
  (large returns follow large returns) + a *mean-reversion* term.
- **Implied volatility as a predictor**: imperfect at best — it *lags*
  realized vol (reacts to it) and, in the S&P sample, tended to be too
  high ("options are overpriced" — sellers' edge, like insurance
  premium), while occasionally being catastrophically too low (2008).
  Rational: buyers pay the insurance-type premium for tail protection.

## Term structure of implied volatility & calendar trades

- Short-dated IV moves more than long-dated (mean reversion): if the
  Mar IV rises 3 pts, June/Sept rise less. A portfolio with **zero vega
  summed across months is NOT vega-neutral** — scale each month's vega
  by its expected IV response (for 1 pt in Apr: Jun ×0.67, Aug ×0.50,
  Oct ×0.37) to get true IV risk (example: "neutral" position is really
  −4.08 per Apr point).
- Term-structure model inputs: primary month (often not the front —
  front-month IV trades erratically), mean vol, whippiness factor.
  Seasonality: ag summer months; natural-gas October (hurricane season).
- **Calendar-spread implied volatility**: the single vol that reprices
  the spread at market (Feb/Mar spread: 29.61 vs 28.06 individual IVs →
  spread IV 25.94). Quick estimate:
  `IV_spread ≈ (price of spread) / (vega of spread)`.
  Downward-sloping term structure → spread IVs sit *below* the curve;
  deviations flag mispriced months (June 2010 cheap, Sept/Dec rich —
  trade via a time butterfly). The graph acts as a magnifying glass for
  relative month mispricing.
- **Forward volatility** (variance is linear in time, unlike rates):
  `σ_f²·(t2−t1) = σ2²·t2 − σ1²·t1` — implies the vol between two
  expiries; chains across periods like forward rates.

## Key takeaways

1. Trade on *expected realized vs. implied vol*; hold time decides which
   dominates.
2. Use sample σ, log returns, zero mean; Parkinson/GK estimators when
   available; expect mean reversion toward a per-market mean.
3. IV term structure: short end moves most; measure true vega risk with
   month-scaled vegas; mine calendar-spread IVs for relative mispricing.
