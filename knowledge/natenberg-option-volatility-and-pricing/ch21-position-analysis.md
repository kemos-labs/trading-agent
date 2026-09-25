# Chapter 21 — Position Analysis

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## Simplify first: synthetics

Rewrite mixed call/put positions as all calls (or all puts) via
synthetics; underlying legs often cancel, revealing a known structure.
Example position (29 underlying, mixes of 65/70/75/80 calls & puts)
collapses to +42 (70) −84 (75) +42 (80) calls = a **long 70/75/80
butterfly** (42×84×42) — delta positive below the inside strike of 75,
wanting the market at 75. (The book's printed "65" in the final line is
a typo; the arithmetic gives 80.) Real positions rarely simplify so
neatly — then use a model.

## Greeks under *changing* conditions

A position can show **zero delta, gamma, theta, vega** today (long 10
Sep 95 puts Δ−25, short 10 Sep 105 calls Δ+25, +5 underlying) yet be
fully exposed tomorrow:

- **Market falls** → 95 put gamma ↑ (moving toward ATM), 105 call gamma
  ↓ → total gamma becomes positive → delta turns *negative* as it
  falls. **Market rises** → gamma becomes negative → delta also turns
  negative. (Delta-negative both ways — the "safe" position is a hidden
  short-volatility structure between the strikes.)
- **Vol up** → deltas converge to ±50 → position −100 (wants market
  down); **vol down** → deltas diverge → +100 (wants market up).
- **Time passes** → deltas move away from 50 → calls/puts go OTM → the
  5 underlying dominate → +delta.
- Θ and vega follow the sign of gamma (long gamma ⇒ −θ, +vega).

Graphical reading: negative delta = downward-sloping line; positive =
upward; negative gamma = frown; positive gamma = smile; the inflection
point (gamma changing sign) = where the value curve is straightest.

## Net contract position (tail risk)

Compute the position after an extreme move (all options deep ITM/OTM):
- Example 1 (10 long 95 puts + 5 underlying / 10 short 105 calls + 5
  underlying): **net short 5 both directions** — the delta approaches
  −500 on either side.
- Example 2 (Figure 21-9): Δ −297, Γ ≈ −24, edge 6.00. Wants a *slow*
  decline; delta-neutral around 101.25 − 297/24 ≈ **89** (graph shows
  max profit ≈ 95 because gamma grows on the way down). Upside contract
  position: net short 7 calls + 13 underlying = **+6 long** (unlimited
  profit on a huge rally). Downside: net long 5 puts + 13 underlying =
  **+8 long** (disaster on a crash). Breakeven vol = 27 + 6.00/0.759 ≈
  **34.9%** (7.9 vol points of margin); improve it by raising edge or
  cutting vega. Extreme vol/time analysis: all deltas → 50 gives +700
  (bullish at high vol); ITM legs acting as underlying gives −900
  (bearish at low vol/time).
- Always compute the *contract* position — big moves happen (tail
  events); far-OTM shorts can still go ITM, and clearinghouses still
  margin them (cabinet bids exist to clean up worthless options).

## Market making

- Obligations: continuous two-sided quotes within a max spread width
  (e.g., 2.00), minimum size (e.g., 100), size quotes (200×200; 500×200
  skew); wider quotes permitted for large "size" orders. Perks: fee
  breaks, allocation priority (50/25/25).
- Three questions: (1) what does the market think it's worth
  (equilibrium price → scalp the spread), (2) what do I think
  (theoretical model → buy cheap/sell rich and dynamic-hedge), (3) what
  am I carrying (risk limits on Δ/Γ/Θ/vega/rho).
- Quotes are a risk-management tool: to reduce a too-negative gamma,
  raise *both* bid and offer (63.50–65.50 vs. fair 63–65) so you're
  more likely to buy.
- Diversify: a zero total gamma with −1,000 concentrated at one strike
  (95) is a trap as expiry approaches — spread risk across strikes,
  dates, and sensitivities.
- Scenario planning: what if conditions move against me? in my favor?
  what can I do now? Respect clearing-firm stress limits (e.g., survive
  a 20% underlying move or a doubling of IV).

## Key takeaways

1. Zero Greeks ≠ zero risk — always re-analyze the position under
   changed price, vol, and time, plus the net *contract* position for
   tails.
2. Position breakeven vol = model vol + edge/vega (with volga
   corrections); it quantifies the margin for error in vol terms.
3. Market makers manage inventory by skewing quotes, not by avoiding
   positions; concentration is the real risk.
