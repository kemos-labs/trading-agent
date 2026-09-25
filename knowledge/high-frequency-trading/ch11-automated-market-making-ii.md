# Ch11 — Automated Market Making II

**Source:** Irene Aldridge, *High-Frequency Trading* (2nd ed., 2013), Chapter 11.

## Purpose
Information-based market making: reading the order flow and book to
infer what other participants know, then optimizing quotes
accordingly.

## Reading the tape (four canonical cases)
1. **No move**: small trades at bid then ask; quotes static — order
   flow carries no information, no action.
2. **Move and rebound**: a large sell sweeps the bid; quotes drop then
   recover — transitory impact, no information. The maker may then
   lower the ask to disgorge inventory quickly.
3. **Permanent move**: a sell shifts both bid and ask down with no
   recovery — the trade carried information; the maker who detects it
   adjusts quotes (or prehedges via the broker who sees the flow).
4. **Quotes widen**: spreads widen without price movement — rising
   uncertainty (e.g., pre-announcement); makers pull near-the-money
   quotes ("quoting wide").

## Modeling information in order flow
- **Order flow**: `x_t = v^a_t − v^b_t` (volume executed at ask minus
  volume at bid). Order flow is responsible for ≥50% of information
  impounded into prices (Lyons 2001); after news, flow becomes highly
  directional. It is informative because (1) market orders are
  irrevocable commitments reflecting honest beliefs; (2) flow data is
  decentralized and partly invisible (internalization hides it); (3)
  large positions move prices regardless of information.
- **Flow autocorrelation** (Biais et al. 1995 "diagonal effect"):
  order aggressiveness persists — large institutional orders arrive
  in similarly aggressive slices; momentum amplifies this. Informed
  traders trade more aggressively (Vega 2007) — mimicking aggressive
  flow can be profitable.
- **Book shape**: liquidity peaks near the market *push* price away;
  peaks far away *pull* price toward them (the "gravitational pull",
  CMSW 1981). Depth predicts volatility (Foucault et al. 2005);
  limit orders far from market around announcements carry private
  information (Berber & Caglio 2004).
- **Order flow imbalance (OFI)** — Cont, Kukanov & Stoikov (2011):
  track tick-to-tick changes in top-of-book liquidity, signed by
  whether the best bid/ask moved up or down. OFI computed from Level I
  data alone predicts short-term price moves.
- **Anand et al. (2005)**: institutional limit orders outperform
  individual ones; aggressive orders outperform passive; bigger orders
  outperform smaller — size, aggressiveness, and institutionality
  each add predictive value (5- and 60-minute horizons).

## Key takeaways
- Level I data suffices for predictive order-flow models: bid/ask
  moves + sizes encode OFI.
- Quote dynamics reveal maker behavior (rebound vs. permanent move vs.
  widening) — each signals a different market state to react to.
- Aggressiveness is information: the most informative traders are the
  most impatient; flow autocorrelation lets you trade with, not
  against, the institutional wave.
