# Ch08 — The Island

**Source:** Scott Patterson, *Dark Pools* (2012), Chapter 8.

## Purpose
The creation of **Island** (February 16, 1996) — the first fully lit
electronic pool — by Josh Levine, bypassing market makers entirely. The
chapter covers the Instinet dead end, the "crossed market" insight, and
the elegant ITCH/OUCH/BookViewer system.

## The Instinet dead end
- Instinet (founded 1967 as Institutional Network; bought by Reuters for
  $110M in 1987) was the largest electronic venue for Nasdaq stocks
  (~1/5 of volume by the mid-1990s): anonymous, rent-a-computer (~$1k/
  month), capital-gated, and *human*-matched. It was, to Levine, another
  insiders' club. When Instinet refuses a fee discount for Watcher flow,
  Citron vows to build their own pool.

## Jump Trades, Greenies, and the crossed market
- Watcher users often wanted to trade the same stock against each
  other — sometimes a "crossed market" (one user's offer below
  another's bid). Routing through a market maker who backs away wastes
  the match.
- Levine builds **Jump Trades** (Nov 13, 1995): any two Watcher users
  trade directly, bypassing market makers; the Watcher books the trade
  and reports to the tape. **Greenies** highlight open SelectNet orders
  from other Watcher users in green; hitting one auto-cancels the
  SelectNet order and matches internally — an internal matching engine.

## Island and its plumbing
- Island launches Feb 16, 1996: a program that simply matches buy and
  sell orders and reports to Nasdaq. Speed and simplicity were the
  design; it charged $1/trade vs. Nasdaq's $2.50.
- Feeds: **IHOST/ITCH** (market data; H=halt, W=welcome, N=night) and
  **OUCH** (order entry) — named to mock Nasdaq's four-letter acronyms.
- **BookViewer** published the *entire* order book — not just the best
  bid/offer — free, in machine-readable form: the first fully **lit
  pool**, cracking open the secret data market makers guarded. Anyone
  could see every resting order and react by computer.
- Volume explodes: by late 1996 roughly half of all SelectNet trades
  come from Island; July 1–Sept 31, 1996 saw orders for 5.6B shares
  ($22.1B). Island becomes Nasdaq's biggest customer — the bandits'
  creation now feeds the beast. ATD, Renaissance (Brown & Mercer), and
  early HFT firms (Timber Hill, Tradebot, Getco) come to trade there.

## Key takeaways
- Lit-pool transparency (full book, machine-readable) is what
  distinguishes Island from the dark pools to come — Levine believed
  information wants to be free, and speed keeps dealers honest.
- Full-book data in machine-readable form is the prerequisite for
  algorithmic trading at scale.
- A pool built for bandits (speed jockeys) hardwired speed into the
  market's future.
