# Ch20 — Panic Ticks

**Source:** Scott Patterson, *Dark Pools* (2012), Chapter 20.

## Purpose
Minute-by-minute reconstruction of the **May 6, 2010 Flash Crash** — the
day the market broke apart into fragmented, dysfunctional venues and
~$1 trillion in assets vanished in minutes — from the perspectives of
NYSE Arca (Paul Adcock), Nasdaq (Eric Noll), UBS, and Bodek's Trading
Machines.

## The sequence
- 2:35pm: Nasdaq's Noll notices Arca order executions slowing (2+
  seconds for Apple). At 2:37 Nasdaq cuts Arca off — severing the
  Archipelago–Island link built in Dec 1996.
- 2:40: a wave of sells hits P&G on the NYSE; the exchange's slowdown
  mechanism (routing to designated market makers) stalls, so orders
  slosh to other venues; P&G collapses 35%.
- Fragmentation madness: Accenture and Boston Beer trade for a penny;
  Philip Morris $49→$17; Apple ~$250→~$100,000. Reason: HFT market
  makers, required to stay in the market, used **stub quotes** — wildly
  wide prices (buy at a penny, sell at $99,999) — to comply without
  trading. When the Bots cut and run, stub quotes become the only
  quotes; market orders hit them.
- 2:43: a massive E-mini S&P sell order (several thousand contracts)
  eats through the CME book; Nanex later theorizes a "Disruptor" trade
  exploiting a 14-millisecond Chicago–New York latency gap. Citadel
  glitches and tells clients to route away; retail flow flushes into
  overwhelmed venues.
- 2:45:28: the CME's **Stop Logic** halts E-mini trading for ~5
  seconds, breaking the feedback loop; the Bots regroup and buy. The
  Dow ends −347 (from nearly −1,000).
- The cleanup: exchanges cancel trades down ≥60% from 2:40 levels —
  4,903 Arca trades canceled, none on the NYSE floor.

## Bodek's vantage
- Trading Machines sees chaos; a colleague (Eric) holding vol-down
  positions is told "If you don't flatten out, I'm going to punch you
  in the throat" — he flattens. Bodek: "There's something going on. Get
  out!" — the market's fragility is visible to microstructure-aware
  traders in real time.

## Key takeaways
- Fragmentation without coordination converts a modest imbalance into a
  crash: venues halting, cutting feeds, and glitching amplify one
  another.
- Stub quotes reveal that "always in the market" HFT obligations are
  meaningless without price discipline.
- Kill switches (Stop Logic) and trade cancellation rules are
  post-hoc circuit breakers for a system with no inherent stability.
- The crash was an emergent property of competing plumbings, not a
  single fat finger.
