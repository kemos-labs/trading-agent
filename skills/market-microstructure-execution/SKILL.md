# Market-Microstructure Execution (Not Being the Dumb Money)

## name
Execution-layer market microstructure for electronic markets: maker-taker
fee math, order types, queue position, latency/SIP effects, tick-size
economics, and a fragility checklist — the playbook for placing orders
that don't get run over.

## description
The modern electronic market is a fragmented set of pools (lit
exchanges, dark pools, internalizers) where the edge lives in the
plumbing: fees, queue position, order types, and speed. This skill
distills how that plumbing works and how to design execution so you
aren't structurally disadvantaged. Distilled from the history of
Island/Archipelago and the 2010 Flash Crash: maker-taker incentives,
Reg NMS best-price routing, the slow SIP feed, colocation, stub quotes,
and toxic order types.

## when to use it
- Before placing any order into a modern fragmented market: choose the
  right order type and venue, and understand the fee/rebate economics.
- Designing an execution algo or a trading agent that sends orders
  (smart order routing, icebergs, pegging).
- Backtesting execution assumptions: does the backtest assume fills
  that the microstructure would never give you?
- Estimating true costs: spread + fees + market impact + latency vs.
  the quoted spread.
- Auditing a strategy for exposure to HFT predators (front-running of
  large orders, latency arbitrage).

## method / formula / code

**1. Maker-taker fee math.**
- Venues pay firms that *make* (post) liquidity a rebate; firms that
  *take* (cross the spread) pay a fee; the exchange keeps the
  difference. Example (Island, June 1998): make rebate 1¢ per 100
  shares, take fee 2½¢ per 100, venue keeps 1½¢.
- Net P&L of a round trip: `profit = spread_captured - take_fee +
  make_rebate` (or reverse). When spreads compress below the fee
  differential, spread scalping is only viable via rebates — the
  zero-sum rebate economy. Always compute
  `expected_pnl = size * (spread - take_fee + make_rebate) - impact - latency_cost`
  before assuming a scalp is profitable.
- Volume tiers: exchanges pay higher fees/rebates to firms hitting
  volume thresholds — retail-sized flow never sees these terms.

**2. Order types: know the language.**
- Market orders: guaranteed fill, terrible price control. Limit orders:
  price control, but in a Reg NMS best-price-routing world they can be
  "run over" by exotic order types that interact with the book in
  undocumented ways (priority, protection, display flags).
- Before trading size on any venue, read its order-type spec: hidden/
  iceberg, post-only, pegged, IOC, and the venue's queue-priority rules
  (price-time vs. size/time). Plain default limit orders are the prey
  of sophisticated order types.
- 90%-cancelation "phantom liquidity": most displayed size may vanish
  before you can trade against it — never size against the full visible
  book.

**3. Latency and the SIP.**
- The SIP (Securities Information Processor) consolidates prices
  across venues and is slow relative to direct HFT feeds; dark pools
  often price off the SIP. Gap between direct-feed price and SIP price
  = latency arbitrage window (Tradebot bought in dark pools before the
  new price arrived). If you trade against a slow feed, you can be
  arbitraged; if you run a venue, your feed latency is your product.
- Colocation: distance converts directly into money; a 16.3ms→13.3ms
  fiber cut cost $300M and was worth >$100M/ms. Latency budgets matter
  at every level: data path, order path, cancel path.

**4. Tick-size economics.**
- Quote granularity is a structural rent to intermediaries: 1/16
  fractions (~6.25¢) made wide spreads profitable; decimalization
  compressed spreads to pennies and pushed human market makers out.
- With penny ticks, displayed spread is no longer a cost estimate —
  real cost is queue position + impact + fees. Depth thinned (100–200
  share quotes), so a 30,000-share order pays 50¢+ above the offer
  while Bots detect the whale.

**5. Fragility checklist (the Flash Crash pattern).**
- Signs a venue/market is fragile: mandatory presence rules without
  price discipline (stub quotes — buy at a penny, sell at $99,999 —
  become the only quotes when HFT exits), venues cutting each other's
  feeds mid-crash, exchange halts that slosh orders to other venues,
  feedback loops (selling begets selling) with no kill switch.
- Mitigations: pre-defined kill switches and halts (CME Stop Logic
  broke the May 6, 2010 loop in 5 seconds), trade-break rules (trades
  ≥60% off reference canceled), and never assume "always in the
  market" means "always priced fairly."

## known pitfalls
- **Assuming displayed liquidity is real**: cancellation rates of 90%+
  mean the book can evaporate exactly when you need it.
- **Ignoring fee/rebate asymmetry**: what looks like a scalp profit can
  be net-negative after take fees; what looks like a loss can be a
  rebate play.
- **Retail flow being harvested**: internalizers pay brokers for
  uninformed flow and match it internally — your retail-sized order
  may never reach a lit exchange. Execution quality claims are
  entangled with payment for order flow.
- **Backtesting with perfect fills**: real fills face queue position,
  impact, and latency; a backtest that fills every limit order
  immediately will be fiction.
- **Chasing latency you don't need**: latency edges are zero-sum and
  cap-ex heavy; the right response is usually avoiding markets where
  speed is the only edge, or using order types that don't advertise
  your size.
- **Trusting venue self-interest**: exchanges profit from volume and
  data sales; order types designed "to attract predatory traders"
  (Kane's 2011 testimony) serve the venue's economics, not yours.

## source book
Patterson, *Dark Pools* (2012): ch3 (maker-taker, dark pools,
internalizers, holding periods), ch4 (Reg NMS, order types, SIP), ch8
(Island's ITCH/OUCH, lit pool), ch11 (maker-taker invented), ch13
(decimalization, tick size), ch14 (cost of ignorance, payment for order
flow), ch15 (colocation, latency arb, spoofing), ch20–21 (Flash Crash
mechanics, circuit breakers), ch22 (Trillium layering, CAT, data
centers), ch24 (toxic order types). Complements the `market-structure-
risk` skill (where risk sits) — this is *how* to execute.
