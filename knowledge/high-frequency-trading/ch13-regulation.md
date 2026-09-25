# Ch13 — Regulation

**Source:** Irene Aldridge, *High-Frequency Trading* (2nd ed., 2013), Chapter 13.

## Purpose
The regulatory landscape for HFT: jurisdiction, system stability,
investor protection, trade matching, and market structure.

## Regulatory styles
- **U.S.** (rule-based, level playing field): SEC (equities/options/
  ETFs), CFTC (futures, swaps, FX derivatives), FINRA (equity SRO),
  FIA (futures).
- **EU** (principle-based, fairness of gains); **Australia** (market
  integrity, pretrade transparency); **U.K.** (forward-looking,
  anticipating future developments); Canada/IOSCO standards.

## U.S. equities regulatory history
- **1997 Order Display Rule**: exchanges must display all customers'
  limit orders — first allowed individuals to make markets.
- **1998 Reg ATS**: mandated electronization; electronic quote
  processing/storage → tick-level transparency.
- **2005 Reg NMS**: NBBO rule (executions at national best bid/offer
  or better; routing obligations); SIP disseminates quotes (1-minute
  window). Reg NMS also enabled **flash orders** (pre-execution quote
  disclosure) — most exchanges voluntarily banned them.
- **Dodd-Frank / Volcker Rule**: banks' prop trading curtailed —
  HFT survived as client-capital "prehedging" market making. Naked
  access (DMA) restricted due to surveillance gaps.

## System stability
- The U.K. taxonomy of computer-trading instability: nonlinear
  sensitivities (small code changes, big impacts), incomplete
  information, normalization of variance (rare events seen as
  routine), and feedback loops amplified by synchronized risk
  management. The flash-crash feedback loop: index falls → synchronized
  selling → delta-hedging → volatility up → HFTs "pass the parcel" →
  NYSE quotes delayed → ETF/single-stock divergence.
- Co-location/proximity: CFTC (2010) mandated uniform fees and
  latency disclosure.

## Investor protection
- **Manipulation detection** requires two things: recurrence + intent;
  screening real-time for **asymmetric market impact** flags
  manipulation candidates.
- **Front-running**: Volcker/Dodd-Frank moved prop HFT into
  prehedging; clients mitigate by diversifying brokers to limit flow
  information.
- **Crash prediction** (post-2010) has two streams:
  1. **VPIN** (Easley–López de Prado–O'Hara): the volume-synchronized
     probability of informed trading:
     `VPIN ≈ Σ|VS_τ − VB_τ| / (n·V)` over volume-clock units
     (e.g., 50-contract E-mini buckets); extreme volume imbalance
     predicted the flash crash hours ahead.
  2. Abnormal trading patterns (long-memory analysis, etc.).

## Efficient matching & market structure
- **Legal Entity Identifiers (LEIs)**: 20-character ISO-administered
  IDs for all trading entities — restoring safe DMA by making
  attribution possible.
- Dark pool equilibrium: makers migrate between dark (better prices,
  hidden revisions) and lit venues until rents equalize.

## Key takeaways
- HFT is regulated as ordinary trading plus machine-specific concerns
  (error controls, co-location access, message traffic).
- VPIN is the leading volume-clock tool for crash prediction —
  implement it as an early-warning system.
- Attribution (LEI) and impact symmetry are the two pillars of
  post-flash-crash surveillance.
