# Ch3 — Stylized Facts about Returns and Volatility

**Source:** *Volatility Trading*, 2nd ed. — Euan Sinclair (Wiley, 2013)

## The empirical regularities

Any volatility model must reproduce these facts or it is not fit for
purpose:

1. **Fat tails / leptokurtosis**: return distributions have excess kurtosis
   vs. the normal; extreme moves happen far more often than a Gaussian
   predicts. Log returns are closer to normal than prices, but still
   heavy-tailed.
2. **Volatility clustering**: large moves tend to follow large moves, small
   moves follow small moves; vol is positively autocorrelated (persistent)
   at daily/weekly horizons.
3. **Mean reversion of volatility**: while clustered, vol is stationary —
   it reverts to a long-run level; low-vol periods follow high-vol periods.
   This mean reversion + clustering pair is the most predictable feature of
   markets and the basis of vol forecasting.
4. **Leverage/volatility feedback effect**: volatility tends to rise when
   prices fall (negative correlation between return and subsequent vol).
   Two explanations: (a) leverage — falling equity raises debt/equity ratio
   and hence equity vol; (b) risk premium/feedback — anticipated higher
   risk demands higher expected return, forcing prices down.
5. **Non-Gaussianity of returns**: skewness, particularly negative skew for
   indices; extreme downside more likely than extreme upside.

## Distributional modeling

- Mixtures of normals or t-distributions capture fat tails better than a
  single Gaussian.
- For option pricing, the relevant question is the distribution of the
  underlying over the option's life, which is the **risk-neutral**
  distribution — recoverable from option prices (via the vol surface)
  rather than history.
- Vol is itself a random variable (vol-of-vol), making the unconditional
  return distribution a mixture that is naturally fat-tailed.

## Consequences for traders

- Fat tails mean short-vol positions have severe negative skew: small
  frequent gains, rare large losses. Sizing must account for this
  asymmetry (Kelly-style sizing on vol trades needs the full distribution,
  not just mean/var).
- Vol clustering justifies GARCH-style/EWMA forecasts: today's vol predicts
  tomorrow's.
- Vol mean reversion is what makes "sell high implied, buy low implied"
  viable and why vol gets rich after crashes (skew steepens, IV spikes).
- The leverage effect explains the skew: OTM puts are systematically more
  expensive than OTM calls.

## Key takeaways

- Clustering + mean reversion are the twin engines of volatility
  predictability; most of vol's forecastability comes from these two.
- Fat tails + negative skew are the danger of short-vol and the edge of
  long-vol: know which side of the distribution you're harvesting.
- Any vol model (GARCH, EWMA, regime-switching) should be validated against
  these stylized facts before use.
