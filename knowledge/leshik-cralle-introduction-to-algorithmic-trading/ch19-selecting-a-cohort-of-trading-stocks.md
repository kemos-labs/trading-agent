# Chapter 19 — Selecting a Cohort of Trading Stocks

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

A *cohort* = symbols found to have similar trading characteristics by
the book's metrics (Appendix A–C hold the sector lists and watchlist).
The first-cut selection routine (Excel file COHORTS):

- **Price tier (first stop)**: higher-priced stocks worked better
  (speculated: different ownership profile). Start in the $75–$100
  band; trade 500-share lots as a stopgap only if you can't cover two
  1,000-share trades.
- **Volume level (liquidity proxy)**: *no* stock with a three-session
  average below 1M shares/day, or any of the three sessions below
  750,000.
- **%Range**: must be read in sector context, as a *series* — an EOD
  uptrend over ~5 days in the average daily 200T %Range can mean more
  trading opportunities. Intraday 200T %Range is a "tradability"
  indicator: ideally > 0.002 at least half the time; never trade stocks
  with EOD %Range < 0.002.
- **Traverse (roughness)**: total of squared returns EOD (classic n=2)
  or absolute price traverse over 100T/200T series and EOD.
- Favorite sectors (author preference, for context): oil & energy
  (RIG, OIH, FWLT, NOV), pharmaceuticals (PFE, AMGN, BIIB, CELG);
  global favorites CME, GOOG, SHLD. Preferences are individual and
  evolve with experience.

## Key takeaways

1. Cohort selection = priced-parameterized filters (price tier, volume
   liquidity, %Range tradability, roughness) applied per stock and re-
   evaluated as series, not snapshots.
2. Quantitative floors: ≥1M shares/day avg volume; EOD %Range ≥ 0.002.
