# Ch28 — Bubbles, Crashes, and Circuit Breakers

**Source:** Larry Harris, *Trading and Exchanges* (2003), Chapter 28.

## Purpose
How bubbles form and crash, the microstructure of the 1929 and 1987
crashes, and what regulation (circuit breakers, margins, taxes,
collars) can and cannot do.

## Bubble mechanics
- Bubbles start with good news: prices rise on fundamental
  information, then **pseudo-informed traders overreact**, pushing
  prices above value (transitory component on top of fundamental).
- Value traders won't sell until price deviates far from value
  (uncertainty + confidence + timing problems) — so bubbles grow in
  stocks whose value is hardest to estimate.
- Crashes are triggered by bad news but caused by the prior
  overpricing: when traders refocus on value, selling cascades —
  momentum buyers leave, margin calls force sales, stop-loss orders
  fire, anticipators sell ahead of them.

## Crash mechanics (1929, 1987)
- **1929**: DJIA −13% Oct 28, −12% Oct 29; bottomed at 11% of the
  Sep 1929 peak by Jul 1932. Margin calls were the amplifier; the Fed
  later set 45% margin. The Great Depression followed from monetary
  policy and bank failures, not the crash itself.
- **1987**: DJIA −23% on Oct 19 after −9% the prior week, from a
  +44% run since January. **Portfolio insurance** (dynamic hedging:
  sell futures as prices fall) was the amplifier — it converts a
  fundamental decline into a mechanical selling cascade; program
  arbitrage transmitted futures selling to the cash market. Unlike
  1929, the market recovered within two years — a correction, not a
  new depression.

## Circuit breakers and their theory
- **Trading halts**: stop trading for a while; let liquidity
  replenish, prevent panic-driven prices, reduce margin-call
  cascades. Cost: delays price discovery.
- **Margins/transaction taxes**: higher margins shrink position
  sizes; taxes penalize high-frequency strategies. But restrictions
  hit informed traders and dealers too — the theory is
  indeterminate: halts *may* reduce transitory volatility, collars
  like **NYSE Rule 80A** (restricting index-arb program trades after
  a 2% DJIA move) probably *increase* it by letting cash and futures
  diverge.
- Empirical studies are inconclusive — extreme events are too rare to
  test.

## Key takeaways
- Crashes are **corrections to pricing errors**, not proof of market
  failure: prices generally rebound little after crashes because the
  pre-crash level was wrong.
- Amplifiers are mechanical: margin, portfolio insurance, stops, and
  anticipators convert a value change into an order-flow cascade —
  know which amplifiers your strategy is wired into.
- Circuit breakers trade price-discovery speed for orderliness; their
  net effect on volatility is theoretically indeterminate and
  empirically untested.
