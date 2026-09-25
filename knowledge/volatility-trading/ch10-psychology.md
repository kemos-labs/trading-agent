# Ch10 — Psychology

**Source:** *Volatility Trading*, 2nd ed. — Euan Sinclair (Wiley, 2013)

## The trader's mind as a risk factor

Behavioral finance identifies systematic biases that hurt traders. Knowing
them is itself an edge because the market is populated by humans with these
biases — even in an increasingly quantitative market, humans set the
marginal prices of many vol products (portfolio insurance buyers, retail
short-vol sellers).

## Key biases relevant to options/vol traders

- **Overconfidence / overprecision**: people systematically overestimate the
  accuracy of their forecasts (too-narrow confidence intervals). For vol
  traders this means overestimating forecast accuracy → over-sizing and
  over-trading. Vol forecasts should be explicitly tested and tracked.
- **Anchoring**: over-reliance on the first number seen (e.g. recent
  realized vol, the initial IV level); leads to stale forecasts — failing to
  update as conditions change.
- **Hindsight bias**: after the fact, events seem predictable; this distorts
  post-trade analysis and prevents learning from losing trades.
- **Confirmation bias**: seeking evidence that supports the position;
  dangerous when combined with the natural tendency to add to a losing
  vol position ("it must revert").
- **Loss aversion / prospect theory**: losses hurt more than equal gains;
  leads to cutting winners and holding losers, and to avoiding properly
  sized short-vol trades because of their tail.
- **Disposition effect**: selling winners too early (realizing gains) and
  holding losers — the opposite of "cut losses, let winners run."
- **Recency**: overweighting recent vol — buying vol after a spike, selling
  after a calm; the variance premium persists partly because of this.

## Why it matters more in vol trading

- Vol trades have asymmetric, lagged, path-dependent P&L: the short-vol
  trade makes money almost every day and loses rarely but big. This
  profile specifically triggers overconfidence (small daily wins), recency
  (calm markets), and loss-aversion (can't take the tail) — the exact
  biases that wreck the strategy.
- Delayed feedback makes learning hard: by the time a vol forecast is
  scored, other things changed.

## Countermeasures

- **Process over prediction**: pre-commit to sizing, hedges, and exit rules;
  follow them mechanically.
- **Keep comprehensive records** and review them with hindsight-bias
  awareness: record the reason for each trade *before* entry, then audit
  reasons vs. outcomes.
- **Track forecast accuracy** statistically (hit rate, calibration) to
  correct overprecision.
- **Pre-commit to loss rules** (vol-based stop, max vega) to defeat loss
  aversion; write them before the trade.

## Key takeaways

- Overconfidence, anchoring, hindsight, confirmation, loss aversion: each
  has a specific failure mode in vol trading.
- Short-vol's daily-win/rare-loss profile is tailor-made to breed
  overconfidence and recency bias.
- The defense is mechanical process and honest, recorded self-audit.
- Psychological discipline is a first-class risk-management tool.
