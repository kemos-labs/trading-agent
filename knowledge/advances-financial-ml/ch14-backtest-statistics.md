# Ch14 — Backtest Statistics

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 14.

## Purpose
The metrics investors use to judge a backtest: general characteristics,
performance, runs, implementation shortfall, efficiency — with the
Sharpe-ratio family (PSR, DSR) as the centerpiece.

## General characteristics
Time range (long enough to span regimes), average AUM, **capacity**
(highest AUM delivering target risk-adjusted performance; decays with
size), leverage (avg position / avg AUM), max dollar position (prefer
close to avg AUM — not outlier-dependent), ratio of longs (~0.5 for
market-neutral), **frequency of bets** (runs of same-side positions =
one bet; count bets, not trades), average holding period, annualized
turnover, and correlation to the underlying (high |corr| = no added
value).

## Performance and runs
- **Performance**: PnL, PnL from longs (bias check), annualized
  time-weighted rate of return (TWRR — GIPS: geometrically link
  sub-period returns, adjust daily-weighted external cash flows), hit
  ratio, average return from hits/misses.
- **Runs/drawdowns**: HHI concentration on positive/negative returns
  and time between bets; 95-percentile drawdown; 95-percentile time
  under water (TuW).

## Implementation shortfall
Broker fees per turnover; average slippage per turnover (fill vs. mid);
**dollar performance per turnover** (how much worse execution can get
before breakeven); return on execution costs (should be a large
multiple — survive worse-than-expected execution).

## Efficiency — the Sharpe family
- **Sharpe ratio** SR = μ/σ of excess returns (IID Gaussian assumed —
  rarely true).
- **Probabilistic Sharpe Ratio (PSR)**: probability that the true SR
  exceeds a benchmark SR* given observed returns, correcting for
  non-normality:
  PSR = Z[(SR̂ − SR*)√(T−1) / √(1 − γ₃·SR̂ + (γ₄−1)/4·SR̂²)]
  where γ₃ skewness, γ₄ kurtosis. Increases with SR̂, T, positive
  skew; decreases with fat tails.
- **Deflated Sharpe Ratio (DSR)**: PSR with SR* endogenized to account
  for the number of trials N and their variance:
  SR* = √(V[SR̂])·[(1−γ)·Z⁻¹(1−1/N) + γ·Z⁻¹(1−1/(N·e))]
  (γ = Euler–Mascheroni). The more trials, the higher the benchmark —
  a lucky backtest from many trials needs a much higher Sharpe to be
  significant.

## Classification scores
Precision/recall/F1 for ML strategies (ch3); accuracy is misleading
with imbalanced classes.

## Key takeaways
- Report a battery, not one number: general characteristics expose
  capacity/leverage/regime issues; shortfall metrics expose execution
  fragility.
- Always report PSR (corrected for skew/kurtosis) and, when many
  trials were run, the **DSR** — it is the honest significance test for
  any backtested Sharpe.
- Preference for strategies whose max position ≈ average AUM: they
  don't depend on extreme events.
