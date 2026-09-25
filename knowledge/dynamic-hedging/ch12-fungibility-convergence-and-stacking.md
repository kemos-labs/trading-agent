# Ch12 — Fungibility, Convergence, and Stacking

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 12.

## Purpose
Delivery mechanics and their risk consequences: fungibility, the cash-and-carry line (maximum contango), convergence of cash and forward, and the hedging practice of stacking.

## Fungibility
- **Fungibility** = degree of specificity required to satisfy the deliverability obligation; reflects the feasibility of risk-neutral replication.
- Totally fungible: currencies (created electronically, wired anywhere) — two-way arbitrage on the time line.
- Delivery-specific: physical commodities (location, grade, storage, perishability) — one-way or no arbitrage on the time line.
- Nonfungibility means the same commodity can trade at different prices in different places (shipping costs) and permits squeezes: open interest exceeding deliverable supply lets the physical holders force delivery and profit.

## The cash-and-carry line (maximum contango)
- Forward ≤ spot + financing + storage costs: if a commodity one year hence is too expensive relative to spot, arbitrageurs buy cash, carry it, and sell the future — capping the forward. **Rule**: calendar spreads in less-fungible commodities must be decomposed into components and analyzed separately.
- Forward prices can also trade far below cash (backwardation) with no force to correct, since no one can arbitrage a *lack* of supply.

## Convergence and the futures basis
- Convergence: cash and futures must converge at delivery; mapping convergence across expirations is a hedge-ratio problem.
- The term-structure shape (contango/backwardation) embeds storage, financing, and convenience-yield information.

## Stacking
- **Stacking** = hedging a multi-expiration exposure with contracts concentrated in a single (usually nearby) expiration — a transitory hedge when speed matters more than precision.
- **Market-neutral stack**: sell total exposure in one expiration (e.g., sell 760 contracts of Euro4 to hedge a strip of -95 per expiration).
- **Butterflying stack**: adds protection against yield-curve shape shifts.
- Risks grow with time (relationships and hedge ratios change); stacking permanently is dangerous — the Metallgesellschaft case (a "market neutral" oil hedge stacked in the front future) produced a ten-digit loss.

## Key takeaways
- Fungibility determines whether arbitrage can enforce relationships — and where squeezes live.
- The maximum-contango boundary bounds forward prices from above (for storable goods); backwardation can persist unarrested.
- Stacking is a temporary liquidity maneuver, never a permanent hedge — concentration in one expiration is tail risk.
