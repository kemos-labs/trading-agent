# Ch03 — Backtesting

**Source:** Ernest P. Chan, *Quantitative Trading* (2nd ed., 2021), Chapter 3.

## Purpose
Replicate others' results yourself (due diligence + ensure you understand the strategy),
experiment with variations, and verify performance measures. Even simple strategies must be
backtested before live trading.

## Platforms
- **Excel**: WYSIWYG, hard to introduce look-ahead bias (dates/signals visibly aligned), same
  sheet for backtest + live orders; only for simple models.
- **MATLAB**: fast, built-in toolboxes (Statistics/ML, Econometrics, Financial ~$50 ea),
  good for large-portfolio backtests, great math (e.g. PCA); author's favourite.
- **Python** (numpy/pandas): de facto standard now; huge ecosystem (scikit-learn, plotly).
  Flaws: version conflicts, slower than MATLAB, no support, weaker econometrics than R.
- **R**: best classical stats/econometrics (rugarch, copula, MASS); author recommends ML for
  *improving* (metalabeling) not *creating* strategies.
- **QuantConnect** (LEAN engine): web-based C#/Python; realistic fills/slippage/margin/costs;
  400TB data; backtest→live with no code changes. **Blueshift** (QuantInsti): research +
  visual/Python builder, turnkey backtest→live.

## Historical data issues
- **Split/dividend adjustment**: prices before ex-date T multiplied by 1/N (split) and
  (Close(T−1) − d)/Close(T−1) (dividend) — multiplier form keeps daily *returns* invariant.
  Aggregate multiplier = product of all individual multipliers (IGE worked example: 0.488386
  applied pre-6/9/2005). Unadjusted data shows spurious ex-date price drops → false signals.
- **Survivorship bias**: databases missing delisted stocks inflate results. **Worked example**:
  "buy 10 lowest-priced stocks, hold 1 year" gave **−42%** with a survivorship-bias-free
  database vs **+388%** with a biased one! Mitigate: build your own point-in-time snapshots,
  test on recent data, or pay for bias-free data (Sharadar, CRSP).
- **High/low noise**: H/L are noisier than O/C; a limit order may not fill at recorded H/L
  (small prints, wrong exchange, bad ticks) — H/L-based backtests overstate returns. Even MOO/
  MOC fills can differ from recorded primary-exchange prices.
- Data error check: flag returns >4σ from the mean; verify against news or market moves.

## Performance measurement
**Most important: Sharpe ratio, max drawdown, MAR ratio** (CAGR/maxDD — leverage-relative).
CAGR alone is ambiguous (denominator: one side or both? leveraged or not?).

**Sharpe subtleties**:
- **Dollar-neutral/self-financing portfolios: do NOT subtract the risk-free rate** (short
  proceeds fund longs; margin earns ~risk-free credit) — excess return ≈ strategy return.
  Same for long-only day-trading with no overnight exposure. Subtract risk-free only if the
  strategy incurs financing costs.
- **Annualization**: Annualized Sharpe = √N_T × (Sharpe based on period T), where N_T =
  trading periods per year. Daily: √252; hourly during NYSE hours: √(252×6.5) = √1638 (a
  common mistake is using √6048 = √(252×24)).
- Worked example: IGE buy-and-hold 2001–2007, excess daily returns (r − 0.04/252):
  Sharpe ≈ 0.789; the same position hedged with short SPY (netRet=(IGE−SPY)/2): Sharpe ≈
  0.784.

**Max drawdown & duration** (from cumulative compounded returns):
- highwatermark(t) = max(hwm(t−1), cumret(t)); drawdown(t) = (1+cumret(t))/(1+hwm(t)) − 1.
- Max DD = min(drawdown) (always ≤ 0); max DD duration = longest run of consecutive
  non-zero drawdown (reset to 0 when drawdown == 0). Worked example: max DD ≈ −10.5%,
  duration 497 days. Max DD and max duration rarely overlap in time.

## Pitfalls
1. **Look-ahead bias** — using future info at signal time ("buy within 1% of the day's low",
   or full-sample regression coefficients). Fix: **lag** all signal inputs (use data up to the
   previous close); no lag needed only if entering at the close. **Universal check**: run the
   backtest on full data → save positions file A; truncate last N days → rerun → save B; A
   and B must be identical on the shared dates, else look-ahead exists.
2. **Data-snooping bias** — overoptimizing parameters to historical noise. Finance has little
   independent data (only ~10 yrs useful; high-frequency data serially correlated). **Rule of
   thumb: ≤ 5 parameters** (entry/exit thresholds, holding period, lookbacks). Qualitative
   choices (enter at open vs close, overnight, universe) can also be snooped. Bailey/De Prado's
   **Deflated Sharpe Ratio** penalizes the number of backtest tweaks.
   - **Minimum backtest length** (Bailey et al. 2012): 95% confidence that true Sharpe ≥ 0
     requires backtest Sharpe = 1 with n = 681 points (~2.71 yrs daily); if backtest Sharpe
     ≥ 2, n = 174 suffices. True Sharpe ≥ 1 requires backtest Sharpe ≥ 1.5 with n = 2,739
     (~10.87 yrs). Applies to out-of-sample/paper-trading length too.
   - **Out-of-sample testing**: optimize on training set (older data), evaluate on test set
     (recent data). If test performance collapses → snooping; simplify model. **Moving
     optimization / "parameterless" models**: re-optimize parameters in a rolling window, or
     average decisions over many parameter sets (diversification over parameters) — reduces
     snooping. **Conditional Parameter Optimization (CPO)**: ML picks optimal params per
     trade/day (Example 7.1).
   - **Paper trading** = ultimate out-of-sample test. A published strategy's post-publication
     period is also a genuine OOS test (don't re-optimize on it).
   - **Sensitivity analysis**: vary parameters slightly; if performance collapses off the
     optimum, the model is snooped. Simplify: remove conditions one at a time; keep only those
     that matter on the *test* set (never tune to the test set — that makes it the training
     set). Consider allocating capital across multiple parameter settings.

## Transaction costs
Include commission + spread + market impact + slippage in backtests.
- **GLD/GDX pairs example (3.6)**: hedge ratio from OLS on training set (1.63); z-score
  entries at ±2σ, exits at ±1σ → training Sharpe 2.1, test Sharpe 1.5. Tuning entry to ±1σ/
  exit 0.5σ improved *both* (2.9 / 3.0). If tuning improves train but hurts test, pick a
  compromise. Passed the look-ahead truncation check.
- **Khandani-Lo mean-reversion example (3.7)**: long worst / short best prior-day returns
  (S&P500 universe), weights ∝ −(rᵢ − market). 2006 Sharpe ≈ 0.25 **without** costs (and
  most of the paper's alpha was small/microcaps), **≈ −3.2 with 5 bps one-way costs**
  (cost = Σ|Δweights| × 5bps). **Refinement (3.8)**: update at the **open** instead of close
  → strongly positive Sharpe before and after costs.

## Strategy refinement principles
Variations must improve train *and* test performance. Known refinements: exclude pharma/
M&A-pending stocks; change entry/exit timing/frequency; change universe (small-cap vs
large-cap). Prefer refinements with an economic rationale over arbitrary trial-and-error.

## Takeaways
- Data quality (split/dividend adj, survivorship bias, H/L noise) and realistic costs dominate
  backtest realism.
- Sharpe (annualized via √N_T; no risk-free subtraction for self-financing strategies) + max
  DD/duration + MAR are the core metrics.
- Guard look-ahead with lagging + the truncation check; guard data-snooping with few
  parameters, minimum sample lengths, OOS/paper testing, and sensitivity analysis.
- A high pre-cost Sharpe can flip deeply negative after costs — always model them.
