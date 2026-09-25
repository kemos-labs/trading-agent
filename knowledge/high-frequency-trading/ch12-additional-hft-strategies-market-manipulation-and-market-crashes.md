# Ch12 — Additional HFT Strategies, Market Manipulation, and Market Crashes

**Source:** Irene Aldridge, *High-Frequency Trading* (2nd ed., 2013), Chapter 12.

## Purpose
The CFTC's list of "purported" HFT strategies, separated into three
buckets: legitimate price discovery, strategies that only work in
dark pools, and outright manipulation (pump-and-dump).

## Legitimate strategies
- **Latency arbitrage**: enforcing the law of one price across venues
  by trading same-instrument price divergences; socially beneficial
  (keeps prices consistent) and self-limiting (the speed race ends
  when an extra dollar of technology stops generating return).
- **Spread scalping** = market making; naive two-sided quoting is
  rarely profitable alone because of inventory + adverse selection
  (see ch10). The news-announcement example shows a maker getting run
  over by an informed buyer.
- **Rebate capture**: arbitraging maker/taker fee differences. The
  threshold condition:
  `p_up ≥ (transaction costs − rebate)/$0.02 + 50%`.
  With $0.0016/share costs and a $0.0020 rebate, required accuracy
  drops to 48% — rebates reduce the required forecast accuracy but
  **cannot make random trading profitable** (without rebates the same
  math requires >70%).
- **Quote matching**: copying others' limit orders; infeasible on
  anonymous exchanges (can't tag counterparties) and impact of limit
  orders is small/unreliable — a disappointment in practice.

## Dark-pool-only strategies
- **Layering**: posting and canceling orders at multiple price levels.
  Legitimate use: securing time priority (placeholders) — but the
  one-sided manipulative variant (fake supply/demand) drew SEC
  penalties (2012). Pro-rata matching (CME) removes the incentive to
  layer.
- **Ignition**: locating and triggering stop-loss orders; requires
  price manipulation in lit markets, so it's effectively a
  dark-pool/buyer-beware phenomenon.
- **Pinging/sniping/sniffing**: probing hidden liquidity and trading
  against it; screened against in some dark pools (e.g., ATD charges
  pingers).

## Manipulation and crashes
- **Quote stuffing**: flooding the network with quotes/cancellations
  to slow competitors; **spoofing**: posting non-bona-fide orders to
  fake demand; **pump-and-dump**: banned everywhere.
- **Detection**: market impact should be *symmetric* for buys and
  sells of equal size; screening for asymmetric impact in real time
  flags manipulation (an asymmetry test on Eurobund futures 2009–2010
  found no evidence of pump-and-dump).
- Empirical impact detail: FGBL futures show size-independent impact
  (α ≈ 10⁻⁵) dominating size-dependent impact (β ≈ 10⁻⁷) until ~100
  contracts — good news for institutional capacity.

## Key takeaways
- Most "predatory" HFT is either legitimate market making or
  infeasible in lit markets — the manipulative subset (spoofing,
  pump-and-dump) is already illegal and detectable via impact
  asymmetry.
- Rebate capture is a **cost-structure arbitrage**, not an alpha
  source: it lowers the accuracy bar, it doesn't remove it.
- The maximum tolerable trade size in a market is where
  size-dependent impact kicks in — 100 contracts in FGBL futures.
