# Chapter 5 — Quantitative Trading Strategies

## Core idea
The strategy landscape: from fundamental and technical analysis to
quantitative/algorithmic approaches, and what algorithmic trading is — the
mathematical models, execution, and market impact that define it.

## Strategy families
- **Fundamental**: intrinsic value from financial statements and economic
  indicators; long-term, undervalued assets.
- **Technical**: historical price/volume patterns — moving averages, RSI,
  Fibonacci retracements.
- **Quantitative**: systematic, model-driven — high-frequency trading (HFT),
  statistical arbitrage, ML-based approaches.
- **Behavioral finance**: exploiting psychological biases and market
  inefficiencies.

## Algorithmic trading
- Models programmed into algorithms that process data at millisecond speed
  and decide buy/sell/hold across many market conditions at once.
- **Applications**: market making (liquidity, spread capture), arbitrage
  (cross-market price discrepancies), trend following, statistical
  arbitrage (converging misalignments).
- Requires rapid real-time data processing — hence HFT infrastructure.

## Quantitative vs traditional
- **Quants**: systematic, data-driven, algorithmically executed, high trade
  volume, immune to emotional bias, quantified risk thresholds.
- **Traditional**: discretionary, fundamental + intuition, fewer carefully
  selected trades, qualitative judgment.
- Quant advantage: precision of risk management, speed, absence of
  psychological distortion; risk: model errors and market anomalies.

## Market impact and ethics
- Algorithmic trading increased liquidity, narrowed spreads, improved price
  discovery — but raised concerns about flash crashes, systemic risk, and
  fairness.
- Regulatory scrutiny: market-manipulation prevention, transparency;
  ethical questions about access inequality and algorithmic errors.

## Choosing a strategy
- Driver: risk tolerance, investment horizon, capital.
  Day/HFT suits high-risk-tolerance, quick-return seekers; fundamental
  suits long-horizon investors who can weather volatility.
- Market conditions matter: volatile markets favor algorithmic
  exploitation of rapid moves; stable markets favor value strategies.
- Strategy selection is therefore a joint choice of personality, capital,
  and regime — not a single "best" strategy.

## Backtesting as the common denominator
Whatever the family, every strategy must be validated the same way:
historical data → signal → position → returns → metrics. The book points
at this pipeline implicitly; the knowledge base's `vectorized-backtesting`
and `walk-forward-validation` skills make it operational.

## Bottom line
The taxonomy chapter: it orients the reader across strategy families and
defines algorithmic trading's core applications. The knowledge base's
strategy material (`skills/vectorized-backtesting`,
`knowledge/chan-quantitative-trading/ch02-fishing-for-ideas.md`) provides
the how-to behind these families.
