# Ch18 — Buy-Side Traders (Institutional Execution)

**Source:** Larry Harris, *Trading and Exchanges* (2003), Chapter 18.

## Purpose
How institutions implement investment decisions: the execution
problem, the costs that make implementation different from theory,
and how execution is benchmarked.

## The buy-side landscape
- Institutions (mutual funds, pensions, hedge funds) trade large
  size relative to market depth, so their execution is the *hard*
  problem: they are price-makers, not price-takers.
- The portfolio manager decides *what* to hold; the **trader** decides
  *how* to acquire it — separating the alpha decision from the
  implementation decision.

## The cost taxonomy (implementation shortfall)
1. **Commissions and fees** — visible but small.
2. **Bid/ask spread** — the half-spread cost of crossing.
3. **Market impact** — price pressure from the order itself; grows
   with size and urgency, shrinks with patience.
4. **Opportunity cost / delay cost** — adverse moves while waiting;
   the flip side of impact.
5. **Timing (alpha) risk** — the cost of trading slowly when
   information is moving.

## Execution strategies
- **Market orders** (pay the spread, immediate), **limit orders**
  (save the spread, risk non-execution), **worked orders** (slice over
  time, balance impact vs. opportunity cost), **blocks/upstairs**
  (pay for search+immediacy), **crossing networks / dark pools**
  (midpoint, but uncertain fills).
- **VWAP / TWAP / POV algorithms**: benchmarked participation
  strategies that spread execution across time.
- **Implementation shortfall (Perold)**: `decision price − actual
  execution` — the full cost of implementation relative to the
  original decision; the industry-standard measure.

## Key takeaways
- The **only trade-off that matters** is impact vs. opportunity cost:
  trading faster costs more impact, trading slower risks adverse
  moves. Urgency and information decay set the optimal speed.
- Large orders should be **pre-traded**: estimate the cost curve
  (impact as a function of participation rate) and choose the schedule
  that minimizes total cost subject to urgency.
- Execution quality must be measured **relative to the decision
  price**, not to some later benchmark — shortfall is the honest
  metric, and it is why good traders look expensive in commission
  terms but cheap in shortfall terms.
