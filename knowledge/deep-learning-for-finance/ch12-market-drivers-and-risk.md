# Ch12 — Market Drivers and Risk

**Source:** Sofien Kaabar, *Deep Learning for Finance* (O'Reilly, 2024), Chapter 12.

## Purpose
The closing chapter ties the ML toolkit to the real world: the macro
and sentiment drivers that move markets, and the risk management —
position sizing, stop-losses, risk-reward — that determines whether a
good signal becomes a profitable account.

## What drives markets
- **Macro factors**: interest rates, inflation, GDP, central-bank
  policy. Rates up → growth and bond prices down; inflation surprises
  move currencies, bonds, and equities in correlated ways.
- **Sentiment and flows**: news, earnings, and investor psychology
  drive short-term price moves that fundamentals can't explain — the
  reason technical features and news-derived signals can add value.
- **Correlation regimes**: assets that are uncorrelated in calm
  markets can correlate near 1 in crises (the "correlation goes to 1
  in a crash" effect) — diversification assumptions fail exactly when
  needed most.
- Implication for ML: models trained on one regime (e.g., low rates,
  low volatility) silently decay when the regime shifts — regime
  detection and retraining are ongoing requirements, not one-time
  steps.

## Position sizing
- **Fixed fractional**: risk a fixed fraction f of capital per trade
  (e.g., 1–2%). Position size = (capital × f) / (per-unit risk).
- **Kelly criterion**: f* = p − (1−p)/b (with win probability p and
  payoff ratio b) maximizes long-run growth but is notoriously
  aggressive — fractional Kelly (half or quarter Kelly) is the
  practical compromise.
- Position size should be driven by **volatility and per-trade risk**,
  not by "feeling good" about a signal.

## Stop-losses and risk-reward
- **Stop-loss**: a precommitted exit price that caps loss per trade;
  the price must be outside normal noise (e.g., a multiple of ATR) or
  you get stopped out by noise, not by being wrong.
- **Take-profit and risk-reward ratio**: if risk is R (stop distance)
  and expected reward is ≥ 2R, the strategy can win less than half the
  time and still profit: breakeven win rate = 1/(1 + reward/risk).
- **Drawdown control**: a 50% drawdown needs +100% to recover —
  compounding asymmetry means capital preservation dominates return
  maximization. Set portfolio-level drawdown limits and cut
  size/leverage after large losses.

## Key takeaways
- A model is only one component of a trading system; sizing, stops,
  and costs decide survival. Risk management turns model signals into
  an equity curve that survives drawdowns.
- Fit model outputs into a risk framework (volatility-scaled sizing,
  ATR-based stops, fractional Kelly) rather than trading raw
  predictions.
- Expect regime shifts: monitor performance vs. the drivers above,
  and rebuild models when the macro/sentiment backdrop changes.
