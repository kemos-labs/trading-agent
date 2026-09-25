# Ch22 — A Rigged Game

**Source:** Scott Patterson, *Dark Pools* (2012), Chapter 22.

## Purpose
The post-Flash-Crash infrastructure arms race: exchange data centers
(Mahwah's Project Alpha), the Spread Networks fiber cable, global HFT
adoption, the first layering enforcement case (Trillium), and Thomas
Peterffy's scathing "complete mess" speech to the World Federation of
Exchanges.

## The physical arms race
- The NYSE's **Project Alpha** ($500M, 400,000 sq ft, Mahwah NJ, opened
  Aug 2010) sells colocation next to the matching engine (~$10k/pod/
  month); data centers rise globally (CME Aurora, London, Hong Kong,
  Mumbai, São Paulo). The real trading floor moved 30 miles from Wall
  Street.
- **Spread Networks** lays a $300M fiber cable (Carteret NJ → Chicago),
  a beeline through mountains, cutting round-trip latency 16.3ms →
  13.3ms — $100M per *millisecond*; only 20 slots; a 1ms edge worth
  >$100M. Microwaves (10ms round trip CHI–NY, vulnerable to rain and
  geese) soon beat fiber. Chips hit 740 nanoseconds (Fixnetix).
- Algorithms grow: ~25% of trading in 2005 → ~2/3 by 2010. Specialists
  touched 28% of NYSE transactions in 2000; HFT is present in ~3/4 of
  trades by 2011. Spreads are narrower but depth is thinner (100–200
  share sizes) — the spread compression is partly illusion: a 30,000-
  share order still costs 50¢+ above the offer as Bots sense a whale.

## Trillium: layering
- Sept 2010: FINRA fines **Trillium Brokerage** $2.3M for jamming
  46,000 phantom orders into the market (2006–07) to fake demand and
  bait other algos — "layering," a bait-and-switch at high velocity.
  Trillium is the direct descendant of Datek (ex-Heartland, run by
  Maschler's son Lee) — the bandits' tactics industrialized.

## Peterffy's Paris speech (Oct 11, 2010)
- The Timber Hill founder — a godfather of electronic trading — tells
  the WFE: "In the last twenty years came computers... and what we have
  today is **a complete mess**." Exchanges used to bring people together
  for price discovery; now the public "does not trust the markets, the
  exchanges, or the regulators either. To the public the financial
  markets may increasingly seem like a casino, except that the casino
  is more transparent and simpler to understand."
- The SEC's answer: the **Consolidated Audit Trail (CAT)** — a
  multi-billion-dollar machine to capture every order and cancellation,
  the ultimate attempt to see into the darkness.

## Key takeaways
- Infrastructure cost-per-microsecond is the defining investment of the
  era — the "level playing field" claim collapses when speed is
  purchasable.
- Layering/spoofing enforcement (Trillium) shows manipulation survives
  in the algos, decades after the human bandits.
- Even HFT's founders (Peterffy) concluded the complexity had become a
  systemic and reputational liability.
