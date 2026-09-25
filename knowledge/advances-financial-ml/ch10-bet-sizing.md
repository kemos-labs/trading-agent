# Ch10 — Bet Sizing

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 10.

## Purpose
Turns ML predictions into position sizes. High accuracy without proper
bet sizing loses money — poker, not chess, is the right analogy.

## Strategy-independent sizing
- Bet size m_{i,t} ∈ [−1, 1] (−1 = full short, 1 = full long).
- Example: two strategies both forecast a +25% move; one sizes
  [0.5, 1, 0] (profit), the other is forced [1, 0.5, 0] after adverse
  movement (loss). Reserve cash so a signal can strengthen before it
  weakens.
- **Concurrency-based sizing**: with concurrent long count c_tl and
  short count c_ts (from the `t1` objects), either (a) fit a mixture of
  two Gaussians on concurrency and size via the CDF — the stronger the
  signal, the larger the bet; or (b) budget: cap at max concurrent
  counts so the maximum position isn't reached before the last signal.

## Meta-labeling sizing
- Fit a secondary classifier (SVC/RF) on {0,1} meta-labels (ch3) to
  predict the probability of a false positive; size from that
  probability. Decouples size from side, enables sizing features that
  predict false positives, and directly maps probability → size.

## Sizing from predicted probabilities
- For binary labels {−1, 1} with predicted probability p[x], test
  H0: E[p[x]] = 1/2 with the z-statistic
  z = (p − 1/2)/√(p(1−p)) — the bet's "confidence."
- **Sigmoid mapping**: size m = f_i − p_t · m₁ (monotonic — losses
  can't be realized as p_t → f_i); calibrate the sigmoid so a chosen
  divergence x yields a chosen m* (e.g., m* = 0.95 at x = 10).
- **Dynamic limit prices**: given current price p_t, forecast f_i, and
  target size, compute the limit price between p_t and f_i so orders
  rest closer to the market when confidence is high.
- **Power-function alternative**: m = |2x − 1|^ω sign(x) — curvature
  directly controlled by ω; concave for ω < 1, convex for ω > 1.

## Averaging and discretization
- **Averaging active bets**: when multiple concurrent bets exist,
  average their sizes (long/short separately) to define the net
  position — avoids the concurrency trap of overcommitting.
- **Size discretization**: round sizes to allowed increments;
  `np.floor(x/k)*k` — keep discretization monotonic so it never
  flips a bet's sign.

## Key takeaways
- The side decision and the size decision are separate problems; size
  from meta-labeling probabilities to avoid ruin from "high accuracy on
  small bets, low accuracy on large bets."
- Always reserve capacity for signals to strengthen; size against
  concurrency, not in isolation.
- A monotonic probability→size mapping guarantees you can't lose more
  as your confidence grows.
