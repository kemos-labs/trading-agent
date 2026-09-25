# Ch10 — Automated Market Making I: Naïve Inventory Models

**Source:** Irene Aldridge, *High-Frequency Trading* (2nd ed., 2013), Chapter 10.

## Purpose
The fundamentals of automated market making: the two risks (inventory,
adverse selection), simulation of limit orders, and naïve offset
strategies.

## Market-making principles
- Market makers post limit orders on both sides of the market; bids
  are "hit" by market sells, asks are "lifted" by market buys. When
  buy/sell inventory neutralizes, the spread is the compensation for
  providing liquidity to takers.
- Two core risks:
  1. **Inventory risk**: the value of accumulated inventory moves
     against you; includes liquidation difficulty and opportunity cost.
  2. **Adverse selection** (per Copeland & Galai 1983): limit orders
     are systematically picked off by better-informed traders — the
     fill itself is bad news.
- Automation advantages: stays on script (no discretionary blow-ups),
  cost-efficient, and **portable** across any CLOB venue/asset class.

## Simulating limit orders
- Market orders simulate as executing at the latest trade price; limit
  orders require care: a limit buy is executed only when the last
  trade price or best ask **falls to or crosses** the limit price
  (and vice versa for sells). This yields nonlinear, path-dependent
  payoffs.

## Naïve strategies
1. **Fixed offset**: quote N ticks away from the market on both sides.
   Execution probability rises as the offset shrinks; **turnover
   (flip frequency) drives profitability**, not time spent quoting
   (Sandas 2001) — modern market makers cancel and resubmit
   constantly, unlike the static-equilibrium models of Rock/Glosten/
   Seppi. Quotes must stay within ~10% of market price (stub-quote
   limits). Slow technology → use larger offsets.
2. **Volatility-dependent offset**:
   `offset_t = round( (1/T)·Σ_{τ=t−T}^{t−1} (P_τ − P_{τ−1})² )` —
   widen the offset when volatility is high.
3. **Order-arrival-rate-dependent offset**: adjust offset to the
   arrival frequency of market orders (Parlour & Seppi 2008).

## Liquidity measurement toolkit
- **Kyle's lambda** (1985): `ΔP_t = α + λ·NVOL_t + ε_t` — the price
   sensitivity to net volume imbalance; lower λ = more liquid.
- **Amihud illiquidity**: `γ = (1/D)·Σ |r|/volume` — absolute price
   change per unit volume.
- **Support/resistance projection** (Kavajecz & Odders-White 2004):
   extrapolate recent minima/maxima to estimate the book's shape when
   Level II data is unavailable.

## Key takeaways
- Market making is a **risk business in disguise**: the naive spread
  capture is eaten by inventory swings and adverse selection.
- Turnover beats patience: profitability tracks execution frequency,
  which is why HFT market makers churn quotes.
- Offset selection is the dial that trades execution probability
  against spread capture; volatility- and arrival-aware offsets
  outperform fixed ones.
