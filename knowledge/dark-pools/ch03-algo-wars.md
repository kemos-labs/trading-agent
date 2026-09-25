# Ch03 — Algo Wars

**Source:** Scott Patterson, *Dark Pools* (2012), Chapter 3.

## Purpose
The state-of-the-market survey: how high-frequency trading (HFT) firms,
maker-taker economics, dark pools, and internalizers reorganized the
U.S. stock market into a fragmented, layered, largely dark system.

## The Bots
- HFT outfits (Automated Trading Desk, Getco, Tradebot, Quantlab) rose
  in the late 1990s in isolated pockets (Chicago, Mount Pleasant SC,
  North Kansas City, Houston); by the late 2000s they executed >2/3 of
  U.S. stock volume at microsecond speeds, made money nearly every day,
  rarely held overnight, and were nearly unregulated. Leverage reached
  ~50:1.
- Exchanges courted them with **information** (expensive data feeds of
  other traders' activity) and **tiers** (e.g., 25M shares/day → Nasdaq
  top tier, higher fees; Direct Edge's top tier once 40M/day).

## Maker-taker
- Venues pay firms that **make** (post) liquidity a fraction of a cent
  per share and charge firms that **take** (cross the spread) a higher
  fee; the exchange pockets the difference. The apple analogy: whoever
  concedes the price pays.
- Rewards patience and volume, not insight. By 2008 NYSE + Nasdaq alone
  paid out ~$2B in make fees. Some firms traded at month-end losses just
  to hit volume tiers.
- Perpetuates a feedback loop: exchanges need HFT volume, so they
  design their plumbing to attract it — the core conflict that later
  breaks Bodek's firm.

## Dark pools and internalizers
- Dark pools: private venues that hide orders; by 2012 ~40% of volume
  traded in dark pools and internalizers, up from ~15% in 2008. Big ones:
  Crossfinder (Credit Suisse), Sigma X (Goldman), Liquidnet, Posit,
  Pipeline, GETMatched; 50+ in the U.S.
- Internalizers (Citadel, Knight, UBS, Citi) *buy retail order flow*
  from brokers (TD Ameritrade, Schwab, E\*Trade) and match it
  internally — retail trades never touch an exchange. The question
  Patterson poses: why would a hedge fund *pay* for those orders?

## Collapsing holding periods
Average holding period: 4 years (1945) → 8 months (2000) → 2 months
(2008) → ~22 seconds (2011, one estimate). One HFT founder's average:
11 seconds.

## Key takeaway
The market became pools within pools — lit exchanges, dark pools,
internalizers — all connected electronically but almost entirely
opaque, with the fastest, best-connected firms structurally favored.
