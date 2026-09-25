# Ch05 — Market Structures

**Source:** Larry Harris, *Trading and Exchanges* (2003), Chapter 5.

## Purpose
Classifies markets along two dimensions — **order-driven vs.
quote-driven** and **call vs. continuous** — and explains how each
design allocates liquidity provision.

## The four-way taxonomy
1. **Order-driven, continuous** (electronic limit order books, e.g.
   Island, ECNs): traders post limit orders; marketable orders match
   against the book; liquidity comes from other traders.
2. **Order-driven, call** (auction markets, e.g. opening auctions,
   crosses): orders accumulate and clear at a single price at a fixed
   time — maximizes liquidity per cross, no continuous price.
3. **Quote-driven, continuous** (dealer markets, e.g. Nasdaq
   historically, OTC bonds): dealers post quotes; public traders trade
   with dealers, not each other.
4. **Quote-driven, call** (rare): dealers quote at a call time.

## Key design choices
- **Who supplies liquidity?** In order-driven markets, public limit
  order traders do; in quote-driven markets, dealers do (and are
  obligated to quote).
- **Who sets prices?** Order-driven: the book; quote-driven: dealers'
  quotes. Dealers shade quotes to manage inventory and adverse
  selection.
- **Precedence rules** (price priority, then time priority; size
  pro-rata in some markets) govern how orders in a book match.
- **Transparency**: how much order/quote information is displayed
  affects whether traders can find liquidity and whether dealers can
  hide.

## Hybrids
Most real markets are hybrids: the NYSE is an order-driven public
auction with a specialist providing continuity; Nasdaq moved from a
pure dealer market to include an order book; modern equities are
electronically integrated.

## Key takeaways
- There is **no single best market structure** — the right design
  depends on who trades: patient traders prefer order-driven (low cost,
  price priority), impatient traders prefer quote-driven (execution
  certainty).
- The core question for any market: *who is obligated to provide
  liquidity, and how are they compensated?*
- Continuity vs. certainty: call markets sacrifice continuous trading
  for deeper single-cross liquidity; continuous markets sacrifice depth
  for immediacy.
