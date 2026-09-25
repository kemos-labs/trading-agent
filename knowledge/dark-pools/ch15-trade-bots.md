# Ch15 — Trade Bots

**Source:** Scott Patterson, *Dark Pools* (2012), Chapter 15.

## Purpose
Dave Cummings and Tradebot push speed to its limit: **colocation**,
maker-taker arbitrage on WorldCom, and **latency arbitrage** against
dark pools via the slow SIP feed — while Getco builds the 
machine-learning empire. The chapter closes with the rise of spoofing
and the dark-pool boom.

## Tradebot and colocation
- Cummings (ex-Getco) founds Tradebot in Kansas City. Speed is
  existential: he must react to stale feeds instantly. ATD has its
  computers beside Island's racks at 50 Broad; distance = money.
- **Colocation** ("colo"): Tradebot pays Island a few thousand $/month
  to place its computers beside the matching engine. Result: 20 orders
  executed in the 1/50-second an order takes to travel KC→NY. Colo
  becomes the backbone of HFT and eventually the standard exchange
  business model.
- Tradebot also exploits cross-venue price differences (buy Intel $20 on
  Island, sell $20.02 on Archipelago) — instant arb that dies if
  execution lags even seconds.

## Latency arbitrage (dark pools)
- Dark pools price stocks off the **SIP**, which lags HFT feeds. If
  Intel ticks to $20.02 on Island, dark pools still show $20 until the
  slow SIP catches up. A colocated ITCH feed lets Tradebot buy in the
  dark pools milliseconds before the new price arrives — pennies per
  share, thousands of times a day. "Like watching the Kentucky Derby on
  a delayed feed while others bet live."
- Maker-taker also pays: with WorldCom <10¢ after its 2002 bankruptcy,
  Tradebot buys 1,000 shares ($100 cost) and *makes* a dime per 100 —
  profit on the rebate with minimal risk, massively scalable. Fees, not
  spreads, became the strategy.

## Getco and the Bots' scale
- Getco (Schuler, Tierney) hires AI/ML programmers, absorbs Hull
  diaspora talent (Blink Trading), becomes one of the most active firms
  globally (up to 20% of daily GE/Google volume). By the mid-2000s just
  four firms — ATD, Renaissance, Tradebot, Getco — did 25–30% of U.S.
  stock trading.
- Exchanges catered to HFT: exotic **custom order types** built per
  client (post-then-cancel, never-rout-to-NYSE orders). "They trained us
  to be fast... guaranteed economics."

## Phantom liquidity and spoofing
- A 2001 study: >25% of Island orders canceled within 2 seconds
  ("fleeting orders") — a figure that later exceeds 90% for HFT
  generally. Real liquidity, or phantom?
- **Spoofing/layering**: fake orders create the illusion of demand to
  bait other algos, canceled before execution.

## Key takeaways
- Latency is a first-class edge; colocation and fast feeds convert
  distance into money.
- When spreads compress to zero, rebates and microstructure quirks
  become the profit — the market's center of gravity shifts to plumbing.
- Cancellation rates undermine the "liquidity provision" defense of HFT.
