# Ch15 — Beware the Distribution

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 15.

## Purpose
Why the smile/tails/skew exist: volatility of volatility, leverage, and skewness — and what the shape of the implied distribution tells the trader about the market.

## Tails and the volatility of volatility
- The tails = implied vol of OTM options relative to ATM (via BSM). The main driver of tail prices: **volatility of volatility (vvol)**, related to the fourth moment (kurtosis).
- Hull-White-style demonstration: with stochastic volatility (vvol > 0), ATM options are barely affected but OTM options gain value (they are convex to vol) — the smile.
- Adding a negative correlation between spot moves (ΔS/S) and vol moves (Δσ/σ) tilts the smile: upside strikes cheapen, downside strikes richen — the **skew**. Negative spot-vol correlation is the empirical norm (leverage effect: selloffs raise vol).

## Leverage and the skew
- **Leverage**: a fall in price raises debt-to-equity → higher risk → higher vol → negative skew (downside strikes pricier). This is the classic structural explanation of the equity skew.
- Markets with different leverage structures show different skew behaviors; the "bad distribution" the market maker gets is a form of adverse selection — the anxiety of markets reflects into positions.

## Regime behavior of vol and correlation
- Crash/panic: historical vol rises markedly (often overshooting), implied rises but OTM calls usually trade *below* recent historical; skew flattens at higher vol; serial correlation often negative (whipping markets); correlations break down (low correlations increase).
- Quiet regime: low historical vol, positive autocorrelation ("quiet trend"), medium stable correlations, high skew from call selling — the lower the vol, the higher the skew.

## Value linked to price (the feedback loop)
- Rising stock prices improve financing, credit ratings, and borrowing — decreasing risk and vol (virtuous cycle); falling prices raise leverage and vol (vicious cycle). This self-referentiality is why the "constant volatility" assumption is most dangerous.

## Nonparallel accounting
- Institutions with marks-to-market vs. those without behave differently in stress (e.g., governments/issuers who benefit from their own debt rally) — a source of non-uniform behavior across market participants.

## Key takeaways
- The smile is not a pricing bug: it is the market's view of vvol and spot-vol correlation.
- Skew direction reveals leverage and funding conditions; regime tables (panic vs. quiet) guide expectations.
- Correlations and volatilities are unstable and interdependent — modeling them as constants is the classic error.
