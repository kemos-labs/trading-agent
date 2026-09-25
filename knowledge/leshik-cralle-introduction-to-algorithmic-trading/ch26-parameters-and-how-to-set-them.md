# Chapter 26 — Parameters and How to Set Them

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## Parameter-setting philosophy

Two parameter types:
1. Internal working parameters of the algo (SMA/LMA lookbacks, EMA
   alpha).
2. Trigger-point parameters for Buy/Sell decisions (valley levels,
   zero-line crossings).

**All profitability depends on parameter setting.** Walked example:
setting the ALPHA-1 Buy parameter via a short-lookback (5-session)
method.

## Buy parameter method

- Set a horizontal line over 5 trading sessions so the green trigger
  line's valleys reach/penetrate it **≥3 times** (or more). If you
  can't achieve this → retire the stock to the "holding corral" and
  pick a more cooperative one.
- Each valley point = a Buy trigger. On trigger: OMS → buy 1,000 shares
  of MSFT at Market; immediately place the LC Adaptive Capital
  Protection Stop (stop-loss template).

## Exit / Sell

- One Buy setup, several closing options:
  - **Basis Point Stop** (the "Dollar Stop"): monitor bp gain; when the
    standard 30–35 bp target is met or exceeded, cancel the stop-loss
    and Sell at Market.
  - **Trigger-line Sell**: the green trigger line fires from a peak
    after crossing the red horizontal zero line — works optimally only
    under regime conditions the authors have not fully defined, so it
    requires empirical testing per stock.

## Key takeaways

1. Set valley-penetration count as the Buy gate (≥3 over 5 sessions),
   with a stop-loss placed immediately on fill.
2. Exit on a basis-point stop (≥30 bp) or the zero-line-crossing Sell
   trigger; the latter needs regime-specific testing.
