# Ch07 — Monster Key

**Source:** Scott Patterson, *Dark Pools* (2012), Chapter 7.

## Purpose
Documents the **Monster Key** — arguably the first trading algorithm —
and the escalating war between Datek's SOES bandits and Nasdaq, ending
with the Christie–Schultz odd-eighth study that exposed market-maker
collusion.

## Price beats time: the Monster Key
- Trader Joe Cammarata accidentally discovers that SOES fills orders by
  **price-time priority** and will execute at the *best* price even if
  you bid absurdly far away — up to 20% off the inside quote. Enter an
  offer 20% higher than the ask and you leap the queue but still pay the
  best price.
- Levine automates it: the **Monster Key** instantly computes the
  20%-away price (Shift-B to buy, Shift-S to sell 1,000 shares). It is
  one of the original trading algos, followed by "Bombs" and
  "SuperBombs" — ancestors of the Guerillas, Stealths, and Snipers of
  the Algo Wars.

## The regulatory war
- Nasdaq retaliates: cuts SOES sizes, limits order rates, tries to add
  a 20-second grace period for market makers — all to protect the
  dealers' ability to back away (refuse to honor quotes). On SelectNet,
  market makers routinely ignored orders: "a hunnet, sold a hunnet."
- The NASD fines Datek and Maschler repeatedly (SOES-rule violations,
  even "profane and indecorous language"); in 1993 Datek's whole Staten
  Island office is suspended 6 months for splitting orders across
  nominee accounts.
- Meanwhile the Watcher + Monster Key make Datek traders rich trading
  Microsoft/Intel-style liquid names, flat every night. Levine's Intel
  stunt — offering 1,000 shares at $1,111¼ against a $111 market — shows
  dealers who only watch the fraction get run over; "It was discipline."

## Christie–Schultz (1994)
- Finance professors Bill Christie and Paul Schultz find Nasdaq market
  makers almost never post **odd-eighth** quotes ($10⅛, $10⅜...) —
  unlike the NYSE — implying implicit collusion to keep spreads at 25¢
  or 50¢ instead of the 12.5¢ minimum. An empirical smoking gun that
  dealer spreads were rigged, costing investors billions.
- The SEC's Leo Wang and the DOJ open investigations; tape recordings
  of dealers ("Can you go one-quarter bid for me?" "I'm goosing it")
  deliver the first price-fixing evidence.

## Key takeaways
- Queue-jumping via price manipulation is the prototype of modern
  aggressive order types.
- Empirical market-structure studies (odd-eighth avoidance) can change
  markets — data exposed what phone calls hid.
- The dealer "right to back away" was the friction speed removed.
