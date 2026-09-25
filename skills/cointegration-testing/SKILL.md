# Cointegration Testing and Pairs Trading

## name
Cointegration testing and mean-reverting pairs trading

## description
Test whether two (or more) non-stationary price series share a stable linear
relationship (cointegration), estimate a static hedge ratio, and trade the
z-scored spread with threshold (Bollinger-band) entries/exits.

## when to use it
- Finding pairs of stocks/ETFs whose price ratio mean-reverts (stat-arb
  pairs trading).
- Before trusting any pair, you must test for cointegration — correlation
  alone is not enough.
- Choosing between alternative hedge-ratio candidates or extending to
  multi-asset portfolios (Johansen).

## method / formula / code

**Tests:**
- **CADF** (Cointegrated ADF / Engle-Granger style): regress y on x
  (y = α + βx + ε); run the **ADF unit-root test on the residuals** ε.
  Rejecting the null of a unit root ⇒ cointegrated.
- **Phillips-Perron** & **Phillips-Ouliaris**: robust variants of the
  residual-based test.
- **Johansen test**: rank r of the cointegrating space via VAR/VECM —
  handles >2 assets and multiple cointegrating vectors.
- Hedge ratio = regression slope β (e.g. y = α + βx); if two candidate
  directions, pick the one with the **more negative ADF statistic** on
  residuals.

**Trading rules (Bollinger bands on the spread):**
```
spread_t = price(y)_t − β · price(x)_t
z_t      = (spread_t − rolling_mean) / rolling_std      # lookback L
Entry:   z_t ≤ −z_entry  → long the spread  (long y, short β·x)
         z_t ≥ +z_entry  → short the spread (short y, long β·x)
Exit:    revert through ∓z_exit (e.g. z_entry=1.5, z_exit=0.5, L=15)
```
Fractional hedge quantities (β·N) are floored to integer share counts.

```python
# CADF sketch (R, tseries)
comb  <- lm(aAdj ~ bAdj)          # slope = hedge ratio
adf.test(comb$residuals)          # p<0.05 ⇒ cointegrated
```

## known pitfalls
- **ADF rejection of cointegration ⇒ don't trade the pair** — Halls-Moore's
  ARNC/UNG example failed the test and only "worked" due to a lucky month
  plus look-ahead bias.
- **Implicit look-ahead bias**: the hedge ratio must be estimated on a
  sample *separate* from the backtest window, not the same data.
- Residual tests assume iid residuals; low SNR in financial data makes
  cointegration hard to detect reliably.
- Single-pair results are fragile — a structural change (e.g. the company
  hedging its own input costs) can kill the relationship.

## source book
Halls-Moore, *Advanced Algorithmic Trading*, ch12 (cointegrated time series)
and ch27 (ARNC/UNG cointegration + Bollinger strategy).
