# Chapter 17 — Our Metrics (Algometrics)

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

The standardized metric catalogue used to describe a stock's behavior
(computed on tick data over chosen lookbacks, T = ticks, plus EOD):

1. **Range metrics**: %Range = (MAXS − MINS)/SAVG over the lookback —
   normalized by the average of MAX and MIN so stocks are comparable
   (a key personality metric; the "stripe around 0.020" in ch. 18 is a
   favorite cluster).
2. **Patterns**: global EOD / multi-session series contain useful
   pattern information; review at 100T, 150T, 200T intraday.
3. **Absolute deviation**: sums of +/− deviations from mean on LBs
   100T, 150T.
4. **Session volume as % of shares outstanding** — over long
   multi-session lookbacks, indicates whether activity is trending.
5. **Shares/transaction**: cumulative on 100T can indicate Tier-1
   involvement (ratio rises); long EOD lookbacks (20+) sometimes useful.
6. **Return RET on nT**: n = 50, 75, 100, 150, 200, 250, EOD — line
   plots and histograms. **RET histograms in basis points** (20T–200T,
   EOD lookback) guide the best *holding time* for a stock and the best
   $ stop.
7. **Sigma metrics**: SIGMARET on short lookbacks (n = 2) = comparative
   "roughness"/jitter metric; STDEV of σ on EOD and intraday
   (100T–500T); STDEV RET; SIGMA TRAVERSE (EOD, 100T, 2T, 5T).
8. **Crossing density** (mean-reversion characteristics): number of
   zero-centerline crossings per nT/nt and the amplitude of the
   reversion characteristic (average or as a series).
9. **LC Roughness Index**: absolute sum of 20T % returns, EOD lookback.

## Key takeaways

1. Metrics are standardized, tick-based, and always paired with a
   lookback; %Range and RETURN histograms directly inform parameter
   selection (holding time, stop level).
2. These "Algometrics" feed the stock-personality clustering of ch. 18.
