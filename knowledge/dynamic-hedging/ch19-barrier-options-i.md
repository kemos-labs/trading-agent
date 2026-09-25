# Ch19 — Barrier Options (I)

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 19.

## Purpose
Regular (knock-in/knock-out) barrier options: payoff structure, the delta discontinuity, replication via risk reversal, and pricing with the reflection principle.

## Taxonomy
- **Regular barriers** die/birth out-of-the-money (KO/ KI with trigger beyond the money): down-and-out call, up-and-out put, down-and-in call, up-and-in put — low complexity.
- **Reverse barriers** die/birth in-the-money (up-and-out call, down-and-out put, reverse knock-ins) — high complexity, covered in ch20.
- Knock-outs are cheaper than vanillas (customers buy them to reduce hedging cost); path-dependence matches trend-follower psychology (place barrier at chart levels).

## Delta discontinuity
- At the barrier the delta of a KO jumps (e.g., 100 call KO 98: delta goes from ~0.66 to 0) — the hedge must be unwound at the trigger with slippage, especially on gaps. This discontinuity is why dynamic hedging is costly for barriers and why large KO positions create liquidity holes.

## Put-call symmetry and barrier replication
- For a barrier K with trigger H, the mirror put strike K' satisfies K·K' = H² (geometric symmetry), with ratio √(K/K') — e.g., 105 call KO 98 → K' = 91.47, ratio 1.0714 puts per call.
- **Replication**: KO call ≈ long call + short √(K/K') mirrored puts, constructed so the risk reversal is worth 0 at the barrier; the KI is the complement: KI(105/98) = vanilla − KO = 1.07 × puts(91.47).
- The replication holds only with constant vol; with a downside skew, the barrier call should be sold cheaper.

## Pricing via the reflection principle
- Count paths: value = Σ intrinsic × (paths reaching node)/(total paths); barrier-adjusted by reflecting paths that hit the barrier (Path 2). For no drift, a regular KO priced at spot S, strike K, barrier H equals the vanilla minus (S/S')·vanilla priced at the symmetrically reflected spot S' = H²/S — e.g., KO call (100, KO 98) = vanilla − (100/98)·vanilla at spot 96.04.
- **Girsanov**: introduce drift by shifting probabilities on the same path structure, not the paths — the basis for risk-neutral pricing of barriers with drift.

## Risk management rules
- In a mean-reverting market the barrier component of a barrier option is *overpriced*; in a trending market, *underpriced* (intraday negative autocorrelation vs. close-to-close vol).
- The expected first exit time (stopping time) is the key quantity: vega hedges must match it; hedge at shorter maturity than nominal to control rebalancing costs.

## Key takeaways
- Barriers are vanillas plus a bet on touching a level — decompose them accordingly (KO = vanilla − binary-ish spread).
- The delta discontinuity at the trigger is the defining risk; slippage and gaps dominate.
- Reflection-principle pricing is intuitive and exact under the driftless assumption; extend with Girsanov for drift.
