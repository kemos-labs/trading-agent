# Chapter 4 — Who Uses and Provides Algos

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## Ecosystem (circa 2009–2011)

- **Sell side / Tier 1** (Goldman Sachs, Morgan Stanley, Citi, Credit
  Suisse, UBS) and the **buy side** (Fidelity etc.) all run algo
  strategies. Appendix A surveys Tier-1 product lists.
- **Hedge funds** are the largest users; little regulation ⇒ little
  disclosure. Renaissance (J. Simons) and D.E. Shaw are the archetypes —
  rumored 50+ PhD mathematicians/statisticians/physicists each, and the
  most powerful hardware; one brilliant individual driving the firm.
- Proprietary source code is guarded "like diamonds"; even mainstream
  algos have company-specific implementations and tweaks (cyber vaults).
  Sell side must disclose a bit more to buy-side clients, but full
  disclosure is unlikely — it would erode the competitive edge.
- **Market evolution**: post-1987 "program trading" was blamed (the
  authors call it unjust). Later, deregulation → off-exchange trading →
  fragmented markets, **dark pools / MTFs** (anonymous liquidity pools;
  trade without revealing to the "lit" market). **Smart Order Routing
  (SOR)** algorithms choose venues by liquidity, fee reduction, and
  anonymity. Authors note dark venues are poorly policed and
  participants can be "gamed" (e.g., front-running large orders).
- **Individual traders**: ~8M+ direct-trading individuals in the US;
  algo adoption likely very small — the book's target audience and
  mission ("levelling the playing field", full computer automation for
  individuals next).

## Key takeaways

1. Algo trading's competitive core is proprietary parameterization and
   execution engineering, not the algos themselves.
2. Fragmentation (dark pools, SOR) is both opportunity and risk for
   individual algo traders — order routing decisions matter.
3. The authors' thesis: individual traders can adopt scaled-down
   versions of Tier-1 machinery.
