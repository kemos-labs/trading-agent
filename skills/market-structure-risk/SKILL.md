# Market-Structure Risk Audit (Who Actually Holds the Risk?)

## name
A checklist for locating where risk, edge, and fragility actually sit in a
market or trade structure — toll-taker vs position-taker, embedded
optionality, tranching as risk reallocation, commitment/liquidity risk,
and information asymmetry.

## description
Before sizing a position or trusting an edge, map the *structure*: who is
the counterparty, what do they know, what options are embedded in the
instrument, and what happens if the market stops cooperating. Distilled
from the institutional mechanics of the 1980s bond markets — the
toll-taker spread model, mortgage prepayment optionality, CMO
tranching, and bridge-loan commitment risk — these patterns transfer to
any market (MBS/ABS, credit, equities, crypto, FX) and any strategy.

## when to use it
- Before trading any instrument with embedded optionality (MBS
  prepayment, convertible bonds, early-exercise options, structured
  products).
- Evaluating a market-making / spread-capture strategy: is the edge a
  structural toll (flow) or a directional bet (position)?
- Auditing a portfolio or deal for hidden commitments: bridge loans,
  underwritten offerings, inventory that can't be liquidated.
- Building or buying structured products: understanding what tranching
  does (reallocates risk, doesn't remove it).
- Post-mortems: asking "who was the fool on the other side?" and "whose
  bonus depended on the deal being good?"

## method / formula / code

**1. Classify the business: toll-taker vs position-taker.**
- Toll-taker: profit = spread × flow (market making, underwriting,
  brokerage). Risk is inventory, not direction. Example: the 1980s bond
  trader's eighth-of-a-point on every bond that passed through —
  $62,500 on a $50M trade, repeatable.
- Position-taker: profit = direction × size (directional bets, vol
  books). Risk is being wrong.
- Ask: if flow stopped, does the P&L stop (toll) or turn against you
  (position)?

**2. Find the embedded optionality.**
- Every instrument can contain an option the holder didn't price:
  - Mortgage prepayment: the homeowner holds a call — refinance when
    rates fall. Bondholder is effectively short that call. Buy at 60,
    paid at 100 when prepayment fires = windfall; but your yield math
    must model WHEN.
  - Callable/convertible bonds, early-exercise rights, covenant
    triggers, regulatory options (the 1981 tax break that created the
    mortgage supply shock was a policy option that fired).
- Method: enumerate "who can act, when, and what does it cost them?"
  Price the option explicitly (see options-pricing skill) before
  trusting static yield.

**3. Tranching = risk reallocation, not risk removal.**
- A CMO pooled mortgages and split cash flows into sequential tranches:
  T1 gets all principal prepayments first (short life ~≤5y), T2 next
  (7–15y), T3 last (15–30y).
- Effect: the SAME total risk, sliced by maturity/priority so each
  investor buys the piece matching their horizon. Total risk unchanged.
- Method: when evaluating any structured product, sum the tranches back
  — verify no risk was "lost" in the packaging, only moved.

**4. Audit commitment / liquidity risk.**
- Bridge loans and underwritten deals are commitments: if you can't
  syndicate (Southland 1987: $4.9B bridge, junk unsold), the commitment
  becomes a huge long position at the worst moment.
- Method: before any underwriting/commitment, compute the stress case —
  if distribution fails, what is the inventory, the funding cost, and
  the exit? Treat committed capital as a position with a worst-case
  holding period.

**5. Map the information asymmetry (who is the fool?).**
- Buffett's rule: any player unaware of the fool in the market probably
  is the fool. The edge is knowing value better than the counterparty
  (the thrifts that sold loans at 65¢ without knowing their terms).
- Method: for each trade, write down (a) what you know about the value,
  (b) what the counterparty knows, (c) which one is more likely wrong.
  If (c) is you, don't trade.

**6. Incentive audit.**
- People whose bonus depends on a deal can't be trusted to price it
  (Southland's junk specialists: $30M department profit riding on it).
- Method: before trusting a valuation or recommendation, ask whose
  compensation is correlated with the deal going through.

## known pitfalls
- **Confusing toll with edge**: spread-capture looks like alpha until
  competition compresses the spread (the Salomon mortgage monopoly
  decayed to 94.5/94.55 within two years of traders defecting). Monopoly
  edges are temporary.
- **Ignoring embedded options**: treating a callable/prepayable asset as
  bullet paper inflates yield and hides tail risk.
- **Believing tranching removed risk**: senior tranches can still default
  in systemic stress; structure ≠ safety.
- **Commitments as free optionality**: an underwriting commitment is
  short a put on your own distribution ability.
- **Trusting insider-optimistic information**: incentive-corrupted
  valuations fail exactly when you most need them.
- **Forgetting counterparty knowledge**: the 1980s thrifts sold
  identical loans at 75 and bought at 85 — the "fee" was asymmetric
  information. Never assume the other side is equally informed; verify
  what they'd need to know to price it right.

## source book
Lewis, *Liar's Poker* (1989): ch3 (toll-taker model, the fool), ch5–6
(mortgage securitization birth, prepayment modeling), ch7 (CMO
tranching, spread compression), ch11 (Southland bridge-loan commitment
risk, incentive corruption). Related: Chan & Halls-Moore risk-management
notes; our `options-pricing` and `risk-metrics` skill gaps in Phase 1.
