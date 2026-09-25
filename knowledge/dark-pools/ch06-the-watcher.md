# Ch06 — The Watcher

**Source:** Scott Patterson, *Dark Pools* (2012), Chapter 6.

## Purpose
Documents Datek's SOES-bandit golden age and Josh Levine's first
masterpiece, **the Watcher** — an order-management program that gave
Datek traders a 360° view of Nasdaq's order flow and the speed to
exploit it.

## The bandit machine
- Jeff Citron, a Staten Island teenager hired as a clerk in 1988,
  becomes the archetypal SOES trader: at the open he buys from a market
  maker with a stale quote, sells seconds later $2 higher — ~90 times in
  one morning, $150,000+ profit. "A quote was a quote."
- Maschler's crew fights running battles with Nasdaq market makers
  (including a literal stabbing of a rival); Datek becomes the largest
  SOES user, and the market makers' hatred turns visceral.

## The Watcher (1990)
- Levine automates the paper-tape P&L bookkeeping first: he splices the
  printer cable of the Nasdaq Level II Workstation into a PC and writes
  a program to scrape the blotter — the trade record — and track each
  trader's profit and loss automatically.
- The Watcher evolves from passive order tracking into a full trading
  platform: keyboard shortcuts to enter orders, multiple stocks at a
  glance, reading bid/offer shifts to anticipate the next minute. It
  outpaced the market makers' Level II workstations, giving Datek
  traders speed and market view no one else had.
- Levine's bigger dream: make trading *free* and fully transparent. He
  studies market-structure literature — Robert Schwartz's *Reshaping
  the Equity Markets* — learning about early electronic markets (CATS,
  the Toronto Stock Exchange's 1977 fully automated system). He
  disagrees with Schwartz's caution about speed: to Levine, speed forces
  market makers to be honest.

## Nominee accounts and the Wire
- To hide professional SOES use, Datek signs up "nominee accounts" paid
  a fixed return (~12%); profits above that go to the house. When manual
  time-stamp backdating becomes too slow, Levine writes an automated
  trade-allocation system called **the Wire** — later the basis of the
  SEC's fraud case against Datek (ch17).

## Key takeaways
- Order-flow visibility (Level II + a fast front end) is the original
  HFT edge; the Watcher is the ancestor of every modern trading
  terminal.
- Side-channel data (printer cable) was the first "data feed."
- The fraud seeds (nominee accounts, the Wire) are planted by the very
  speed and aggressiveness the market rewarded.
