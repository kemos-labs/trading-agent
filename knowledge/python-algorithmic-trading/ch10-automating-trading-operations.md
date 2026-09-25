# Ch10 — Automating Trading Operations

**Source:** *Python for Algorithmic Trading: From Idea to Cloud Deployment* —
Yves Hilpisch (O'Reilly, 2021)

## Capital management: the Kelly criterion

Objective: maximize long-term wealth. In a binomial betting setting (win
prob p, lose q = 1−p, bet f fraction of capital, win/lose the bet):

```
c_n = c₀·(1+f)^h·(1−f)^t
```

Long-term wealth maximization = maximizing the average geometric growth
rate per bet, g(f) = E[log(1 + f·B)]. Maximizing over f gives the Kelly
fraction:

```
f* = p − q = 2p − 1     (for even-money bets)
```

- Betting all capital maximizes expected arithmetic value but guarantees
  ruin on the first loss — expected *log* wealth is what Kelly
  maximizes.
- Betting nothing avoids losses but forfeits the edge.
- f* is the growth-optimal fraction; the book's ML-strategy example sizes
  positions according to Kelly and sets broker leverage accordingly.
- (For general payoffs, f* = (bp − q)/b; see the kelly-position-sizing
  skill for the full treatment.)

## ML-based trading strategy (backtest)

The chapter backtests an ML classification strategy (direction prediction
from ch5) with proper train/test splits and transaction costs — the
honest evaluation loop: fit on train, predict on test, apply
position.shift(1) × returns, subtract costs, report performance and risk
characteristics (cumulative return, drawdown).

## From offline to online algorithm

An offline algorithm (backtest over the full series) must become an
**online algorithm** for live trading:
- Process bars incrementally as they arrive (ch7 sockets / broker
  streaming).
- Re-fit the model on a rolling window of recent data (or on a schedule),
  then predict the next bar — the online analog of the offline fit.
- Keep state minimal and deterministic; log every decision.

## Infrastructure and deployment (cloud)

- Cloud (e.g. DigitalOcean droplet) is the practical choice for
  availability, performance, and security — always-on execution of the
  trading script.
- Setup steps: droplet → Python env (Miniconda + packages) → upload
  scripts and the config file with credentials → run the trading script →
  monitor.
- **Logging**: record every event (orders, fills, prices, errors) to a
  log file so history can be audited after the fact.
- **Monitoring**: the trading script publishes events to a ZeroMQ PUB
  socket; a local monitoring script (SUB) displays them in real time —
  you watch the cloud instance from your laptop. (Caveat: the book's
  socket feed is plaintext — encrypt/tunnel in production.)

## Risk framing

Automated FX/CFD trading adds execution, technical, and operational risks
(logic flaws, socket issues, delayed/lost ticks). Identify and address
market, execution, operational, and technical risks before deployment;
the code is technical illustration, not advice.

## Key takeaways

- Kelly f* = p − q (even-money) sizes bets to maximize long-run growth;
  over-betting → ruin, under-betting → forfeited edge.
- Backtest honestly (train/test + costs) before automating; ML strategies
  need rolling refits to stay online.
- Deployment = cloud instance + environment + scripts + logging +
  socket-based remote monitoring.
- Log everything, monitor in real time, and treat unencrypted socket feeds
  as a security risk in production.
