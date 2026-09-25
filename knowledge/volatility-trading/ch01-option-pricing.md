# Ch1 — Option Pricing

**Source:** *Volatility Trading*, 2nd ed. — Euan Sinclair (Wiley, 2013)

## The core idea

Options can be traded without a valuation model (e.g. converting/boxing for
theoretical value), but to trade **volatility** we need a pricing framework
that translates between price space and volatility space. The
Black-Scholes-Merton (BSM) framework is the workhorse: it is wrong in its
details but robust enough to be modified for real markets.

## BSM assumptions (all violated in practice)

- Underlying follows geometric Brownian motion: dS = μS dt + σS dZ (constant
  drift μ and constant volatility σ)
- No transaction costs, no taxes, no dividends
- Continuous, costless hedging
- Constant risk-free rate; can borrow/lend freely at it
- No arbitrage

Each violation maps to a real-world fudge factor: jumps → fat tails in the
skew; stochastic vol → vega risk and the vol surface; discrete hedging →
gamma/theta trade-off and hedging costs.

## Key results

- **Option price** is the discounted expected payoff under the risk-neutral
  measure: C = e^(-rT) E*[max(S_T − K, 0)]. Pricing requires no view on μ —
  the drift disappears because the option is hedged (delta hedge).
- **Hedge ratio (delta)**: Δ = ∂C/∂S = N(d₁). Holding Δ shares per short
  option (or the reverse) removes first-order price risk; the remaining
  exposure is volatility.
- **Greeks**: delta (price), gamma (delta's sensitivity), vega (vol),
  theta (time). BSM pins the relationships: |theta| ≈ ½·Γ·σ²·S² (the gamma
  bleed offsets theta decay when the hedge is fair).

## Trading implications

- The largest source of edge in option trading is trading our **estimate of
  future volatility against implied volatility**: buy options when forecast
  vol > implied, sell when forecast < implied, then hedge to convert the
  price view into a vol trade.
- A model is not a strategy, and a strategy is not a business. The model
  only tells you what the option is worth given its inputs; the edge comes
  from having better inputs (especially the vol forecast).
- Modified pricing models exist (transaction-cost-adjusted break-even vol via
  Leland-style scaling; stochastic-vol and jump models), but the BSM
  framework's value is a consistent language for thinking about risk
  (Greeks, vol space) rather than absolute accuracy.

## Key takeaways

- Options are instruments for trading volatility, not just direction.
- Understand every assumption behind the pricing model and how well it
  applies to real markets; don't memorize derivations.
- The pricing model converts a volatility forecast into a tradable quantity
  (option price); hedging converts the option price into a pure volatility
  position.
- Know exactly what your edge is before trading; the model is the measuring
  stick, not the source of edge.
