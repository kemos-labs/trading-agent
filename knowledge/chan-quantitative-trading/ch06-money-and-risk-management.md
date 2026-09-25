# Ch06 — Money and Risk Management (Kelly Criterion)

**Source:** Ernest P. Chan, *Quantitative Trading* (2nd ed., 2021), Chapter 6.

## Objective & assumptions
Maximize **long-term compounded growth rate g** of equity (≡ max long-term wealth; ruin must
be impossible, else long-term wealth → 0). Assume each strategy's returns are Gaussian with
fixed mean m_i and SD s_i (**excess** returns, net of financing). Gaussianity is an
approximation — real returns have **fat tails** (huge losses far more frequent than the bell
curve allows).

## Kelly capital allocation & optimal leverage
**Multi-strategy** (Thorp, 1997 — portfolio math, here applied to strategies):
**F* = C⁻¹ M**
- C = covariance matrix of strategy returns (element C_ij = covariance of i,j); M = vector of
  mean returns. Returns are one-period, simple, **unlevered** returns (e.g. long $1/short $1
  making $0.10 → m = 0.05 regardless of equity).
- **Independent strategies** (diagonal C) → the classic **Kelly formula**:
  **f_i = m_i / s²_i** (optimal fraction of equity for strategy i = optimal leverage).

**Key identities** (Gaussian case):
- Compounded levered growth: **g(f) = r + f·m − s²·f²/2**
- **Maximum growth at Kelly leverage: g_max = r + S²/2** — growth depends on the **Sharpe
  ratio**, not raw returns! Higher Sharpe ⇒ higher max growth (with optimal leverage).

**Worked example 6.2 (SPY)**: mean annual return 11.23%, SD 16.91%, r_f = 4% → excess m =
7.231%, Sharpe = 0.4275 → Kelly f = 0.07231/0.1691² = **2.528** (f is time-scale invariant;
Sharpe is not) → g = 13.14%/yr. Unlevered growth = m − s²/2 = 9.8% (note: **risk always
lowers growth** — g = m − s²/2 < m; geometric mean < arithmetic mean).

**Worked example 6.3 (3 ETFs)**: OIH/RKH/RTH mean excess (annualized) M = (0.1396, 0.0294,
−0.0073), C given; F* = C⁻¹M = (1.29, 1.17, −1.49) — **short RTH** (negative m); portfolio
g = r + FᵀCF/2 = 15.29% and Sharpe = √(FᵀCF) = 0.475 — better than any single ETF.

## Practical implementation
- **Rebalance to Kelly continuously** (at least daily): after a 10% SPY loss on the f=2.528
  book, reduce portfolio to 2.528 × new equity.
- **Update F* periodically** from trailing mean/SD; ~6-month lookback if holding period ~1 day;
  update daily.
- **Half-Kelly** (standard practice): parameter-estimation error + non-Gaussian tails ⇒ halve
  the leverage. Also set leverage = min(half-Kelly, worst-historical-loss cap): e.g. S&P500's
  Black Monday (19 Oct 1987) one-day loss −20.47% ⇒ if you can tolerate a 20% equity drawdown,
  max leverage ≈ 1 < half-Kelly's 1.26.
- Variable #signals/day: size to the **maximum** number of positions; safer to be under Kelly.
- Retain an income source / diversification to avoid boredom-driven interference.

## Risk management
- Risk management = **reduce position size after losses** (realize them) and increase after
  profits — this forced deleveraging causes **financial contagion** (Aug 2007 quant meltdown:
  GS Global Alpha −22.5%, Renaissance −8.7% in days; Jan 2021 GameStop squeeze: Melvin −53%).
- **Stop-loss is not universally good**: in a momentum regime it prevents further losses, but
  in a mean-reverting regime it realizes losses you'd have recouped. News/fundamental-driven
  moves → momentum (don't stand in front of a freight train); unexplained/liquidity-event
  moves → likely mean-reverting.
- **Model risk** (model wrong: data-snooping, survivorship bias, competition, regime shift):
  get independent replication of backtests; **scale leverage down gradually via trailing-mean
  Kelly (→ 0 as mean return → 0)** rather than abruptly shutting down.
- **Software risk**: ATS must match backtest trades exactly (ch5).
- **Natural disaster risk**: UPS, VPS, redundancy (ch4).
- **Psychological preparedness**: despair & greed both cause overleverage (LTCM 2000, Amaranth
  2006 — one trader, one natural-gas spread, $6B loss). Author's own mistakes: adding $100M+
  to a 6-month-old strategy; stubbornly doubling a non-reverting XLE/CL spread (≈$500k, then
  −6 figures exit). Start small, gain discipline, keep portfolio size under control.
- **Loss aversion is rational** (Ole Peters & Murray Gell-Mann): the +$110/−$100 coin flip has
  positive ensemble expectation but **negative time-average (compounded) growth rate**
  g = m − s²/2 ≈ −0.0005/round. Traders live in the time series, not the ensemble — take time
  averages, not ensemble averages. Representativeness bias: don't tweak parameters after one
  big loss; backtest any modification over a long period first.

## Key takeaways
- **F* = C⁻¹M**; independent case **f = m/s²**; **g_max = r + S²/2** — Sharpe drives growth.
- Use **half-Kelly**, cap by worst historical loss, rebalance daily, update params from a
  trailing window.
- Risk management (forced deleveraging) propagates crises; keep leverage modest.
- Psychological discipline (no despair, no greed, no post-hoc parameter tweaks) is the
  ultimate risk control.
