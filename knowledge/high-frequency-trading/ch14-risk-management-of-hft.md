# Ch14 — Risk Management of HFT

**Source:** Irene Aldridge, *High-Frequency Trading* (2nd ed., 2013), Chapter 14.

## Purpose
The real risks of HFT (not the media's manipulation narrative):
regulatory, credit/counterparty, market, liquidity, and operational —
and the ordered toolkit for managing market risk.

## Risk categories
- **Regulatory/legal**: adverse reform (e.g., co-location bans).
- **Credit/counterparty**: leverage availability and counterparty
  failure (Lehman: ~$300B frozen). Mitigation: track broker
  creditworthiness, diversify across brokers/venues. HFT leverage is
  cheap because positions are flat overnight (no unsupervised
  overnight margin risk for the lender).
- **Market risk**: the ordered management toolkit:
  1. **First order — stop losses**: linear in price. Requirements:
     limit losing trades without cutting winners; not triggered by
     natural volatility; execute immediately. Optimal stop maximizes
     `E[Profit] = E[Gain]·Pr(Gain) + E[Loss>Stop]·Pr(Loss>Stop) +
     E[Loss≤Stop]·Pr(Loss≤Stop)` — estimated by simulation.
     Volatility-scaled stops: estimate rolling volatility over a
     window matching the holding period, use its distribution to set
     a multiplier; confirm out-of-sample.
  2. **Second order — volatility cutouts**: halt strategies in
     adverse volatility regimes. Regress strategy gains on rolling
     volatility `R_t = α + β·σ̂_t + ε_t`; if β is negative and
     significant, gate the strategy when σ̂ exceeds the threshold.
     Use realized or implied (VIX) vol.
  3. **Third/fourth order — VaR**: distributional (skew/kurtosis-
     aware) value-at-risk for position sizing.
  4. **Higher order — hedging**: offset exposure with correlated
     instruments.
- **Liquidity risk**: inability to unwind without impact (see ch15).

## Portfolio construction for HFT
- Standard optimizers are too slow and ignore discrete block sizes.
  **Discrete Pairwise (DPW) optimization** (Aldridge 2010): rank
  strategies by Sharpe; pick equal numbers positively/negatively
  correlated with the market; pair them by liquidity rank (most liquid
  + with most liquid −); grid-search discrete positions (e.g., −$3M…+
  $3M) within each pair for minimum volatility; apply gross/net caps
  for market neutrality. Computes only K correlations instead of
  2K(K−1), and 7²=49 grid points per pair — fast enough for HFT.

## Key takeaways
- Risk management is an ordered ladder: stops (price-linear) → vol
  cutouts (squared) → VaR (distributional) → hedging (any shape) —
  each rung handles what the lower ones miss.
- Stop-loss and cutout parameters should be **calibrated on the
  volatility distribution**, not fixed arbitrarily — false triggers
  are the classic failure mode.
- For HFT portfolios, favor fast discrete optimization (DPW) over
  full Markowitz — the constraint is wall-clock time and clip sizes.
