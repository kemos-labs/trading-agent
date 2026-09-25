# Chapter 16 — Automated Trading

## Core idea
Putting it together: capital management (Kelly), a backtested ML strategy,
converting it to an **online algorithm**, deploying to the cloud, and
logging/monitoring — the full production loop for a single strategy.

## Capital management — the Kelly criterion
- Coin-toss setup: win `b` with probability `p`, lose with `q=1-p`; bet
  fraction `f` of capital each round.
- Expected value per round: `E[B] = (p - q)·b > 0` — risk-neutral agents
  would bet everything, but one loss then ruins them (with compounding,
  betting all = certain ruin eventually).
- Maximize the expected **average geometric growth rate**:
  `g(f) = p·log(1+f) + q·log(1-f)`.
- First-order condition gives **`f* = p - q`** (even-money case): with
  `p=0.55`, bet 10% of capital. General payoffs: `f* = (b·p - q)/b`.
- Growth-optimal, but aggressive: in practice use **fractional Kelly**
  (half/quarter) to cut variance and estimation error.
- Cross-ref: `skills/kelly-position-sizing`.

## ML-based strategy → online algorithm
- Backtest a classification strategy thoroughly (performance AND risk) in
  batch mode.
- **Online conversion**: instead of fitting once on all data, maintain a
  rolling/refit model that, at each new data point (tick/bar), computes the
  latest prediction and position — a loop driven by incoming streaming data.
- The strategy consumes the FXCM stream (ch14) and places orders via the API.

## Infrastructure & deployment
- Deploy to a **cloud instance** (ch2's droplet setup) for availability,
  performance, and security — no laptop dependencies.
- The trading process runs 24/7 with the broker's streaming feed.

## Logging & monitoring
- **Logging**: record every decision, order, fill, and error — enables
  post-mortem analysis of the deployment history.
- **Monitoring via sockets**: push status messages over TCP sockets so a
  remote client can watch the live strategy (positions, P&L) in real time.
- Together they make the black box observable.

## Pitfalls
- Kelly with estimated edge → over-betting; use fractional Kelly.
- Backtest ≠ live: slippage, latency, and data feed gaps degrade results —
  log and compare live vs backtest drift.
- Cloud deployments need process supervision (auto-restart) and security
  (keys, firewalls).

## Bottom line
The production chapter: Kelly sizing, online refit loop, cloud deployment,
logging/monitoring. Cross-refs: `skills/kelly-position-sizing`,
`knowledge/python-algorithmic-trading/ch10` (same pipeline: Kelly, online
algorithm, cloud, logging).
