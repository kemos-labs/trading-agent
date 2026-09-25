# Ch03 — Market Making and Market Using

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 3.

## Purpose
Describes market participants, the book-runner vs. price-taker distinction, and the microstructure evidence (negative short-term autocorrelation) behind the market maker's edge.

## Participants (pit-trader taxonomy)
- **Locals**: floor market makers, liquidity-driven, benefit from the time-and-space advantage; they capture the bid/offer spread.
- **Paper**: end customers; the locals' natural counterparties.
- **Arbs**: arbitrageurs, mixture of market maker and user; transfer liquidity between markets (cash-future program trading).
- **Book runners (market makers)** are *defensive* (price-sensitive, willing to trade more at better prices); **market users (price takers)** may be aggressive.
- Commoditized vs. nonstandardized products: liquid phase (narrow spread, high volume, small edge — "a fast nickel beats a slow dollar") vs. tailor-made structures (wide margin, low volume); all successful exotics eventually commoditize.

## The market maker's edge: negative autocorrelation
- Empirical studies (e.g., Guillaume et al. 1995, dollar/DM): **first-order negative autocorrelation** of price changes at very high frequency — significant up to ~4 minutes, vanishing beyond.
- Interpretation: the bid/ask bounce gives the market maker a short-term "edge"; only someone who can transact at both sides (a market maker) captures it — for the rest, it translates into transaction costs.
- The negative autocorrelation (a submartingale for the market maker) does not violate a fair-dice (martingale) world once transaction costs are priced in.

## The illusion of profitability
- Mark-to-model at mid-market books an immediate profit on the spread; but the future dynamic-hedging costs (slippage, rolling, cross-currency adjustments) are concealed — complex products' true cost only appears over time.
- Market makers are crippled by position size vs. appetite for risk; ideas that sell get imitated, drying up hedge liquidity (e.g., Mexican peso range notes).

## Adverse selection and signaling
- Adverse selection: the market maker tends to get the worse side of the trade (like insurance getting the sick customers).
- Traders' edge depends on interpreting who is on the other side (informed vs. liquidity) — signaling and disguising orders.

## Key takeaways
- Market making is a positive-expectancy *liquidity* business, not a forecasting business; the edge lives in the microstructure (short-horizon autocorrelation) and in managing inventory.
- Booked profits on complex products are not realized until all future hedging costs are paid.
- Exchange locals control their inventory and can widen markets in stress; institutional book runners cannot easily refuse a customer.

## Source note
This chapter is microstructure-heavy; see the `market-microstructure-execution` and `automated-market-making` skills for the modern framing of the same edge.
