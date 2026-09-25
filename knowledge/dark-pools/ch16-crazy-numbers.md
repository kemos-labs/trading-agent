# Ch16 — Crazy Numbers

**Source:** Scott Patterson, *Dark Pools* (2012), Chapter 16.

## Purpose
9/11 tests Island's resilience, and Nasdaq's **SuperMontage** attempt
to crush the ECNs backfires — Island escapes the "shopping mall,"
defeats Instinet's intimidation, and (with Archipelago) shows who really
sets prices during the Enron collapse.

## 9/11 resilience
- On Sept 11, 2001, ash floods Island's basement data center at 50
  Broad; Sterling pulls the plug — the first downtime in 4+ years. The
  backup data center in Secaucus, NJ (still unfinished) goes live via
  VPN within days: Island trades again Sept 13, while the NYSE reopens
  Sept 17. A distributed system that "doesn't really exist anywhere" is
  less vulnerable than a physical exchange.

## SuperMontage and the "shopping mall"
- Nasdaq builds SuperMontage: a giant super-pool aggregating best bids/
  offers across ECNs — but giving Nasdaq market makers queue preference.
  Instinet's Doug Atkin demands a united ECN front, threatening to cut
  Island off (a recorded, anticompetitive message Andresen later uses
  against him — "we're going to cut you off" = leverage in the $1.5M fee
  dispute).
- Levine's analysis: SuperMontage is anticompetitive, so no ECN will
  participate; it will die on its own. "Why don't we just leave the
  shopping mall?" Island plans to print its trades on the **Cincinnati
  Stock Exchange** (Madoff's old electronic venue) instead of Nasdaq,
  saving ~$20M/year in fees. Wick Simmons offers $7M of the $20M;
  Andresen: "I think you're thirteen million short." March 18, 2002:
  Island switches; Nasdaq's biggest user vanishes, and SuperMontage
  collapses into irrelevance.

## Enron: ECNs set the price
- Nov 28, 2001: S&P downgrades Enron to junk; the NYSE halts trading
  amid a stampede, while ECNs (Archipelago, Island) trade 10M shares
  without a hitch. When the NYSE resumes 29 minutes later, its first
  print matches the ECN price — the electronic pools are now *setting
  the prices* for the Big Board. Putnam's victory lap on CNBC enrages
  NYSE CEO Dick Grasso.

## The merger wave
- Datek Online sells to Ameritrade for $1.3B (2002); Bain, Silver Lake,
  TA (90% owners of Island) seek a buyer; Archipelago and Island — fierce
  rivals — agree to merge at a Gibsons steakhouse dinner, then
  Instinet+Island suddenly announce their own deal, blindsiding Putnam.

## Key takeaways
- Distributed, geographically redundant infrastructure wins in
  catastrophic events.
- Incumbents' anticompetitive designs fail when the ecosystem refuses
  to participate; exit can be more powerful than fighting.
- Fragmented venues + price discovery shift: the fastest, most liquid
  pool defines the price, not the listing exchange.
