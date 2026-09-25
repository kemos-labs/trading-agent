# Chapter 1: SOFR

## Repo Market Foundations
A repo is a collateralized overnight loan: sell a bond spot, agree to repurchase at a slightly higher price tomorrow. The difference is the overnight repo rate. The repo market does $2–4T/day in the US. Lenders benefit from reduced credit risk and lower BIS capital charges (0% risk weight for US Treasuries). Borrowers benefit from lower rates vs unsecured. Repo is also essential for covering short positions in relative value trades (e.g., cheapest-to-deliver bonds).

**Special collateral:** A bond is "on special" when its repo rate is below the general collateral rate — typically cheapest-to-deliver bonds, new issues, and benchmarks. Tri-party repo (via BNY Mellon) filters out specials and failure risk, producing a narrower rate distribution than bilateral repo.

## SOFR Construction
SOFR is the **volume-weighted median** (50th percentile) of overnight repo rates from three data sources:
1. **TGCR** — tri-party repo via BNY Mellon (excluding Fed as counterparty)
2. **BGCR** — TGCR + GCF repo via FICC
3. **SOFR** — BGCR + cleared bilateral repo (FICC DVP), filtered for specials (removing below-25th-percentile trades)

Published at ~8 a.m. ET for the prior business day, revised at ~2:30 p.m. if the change ≥1bp. The 1st, 25th, 75th, and 99th volume-weighted percentiles are also published.

The bilateral repo market is the largest contributor to SOFR data; GCF repo contribution is consistently low. SOFR excludes most bond-specific disruptions (specialness) but not counterparty-specific disruptions (funding stress), creating a right-skewed distribution.

## SOFR vs Fed Funds
Counterintuitively, SOFR sometimes exceeds EFFR — an apparent arbitrage (borrow unsecured, lend secured, earn the spread with lower risk). The puzzle resolves through **balance sheet constraints**: post-GFC regulation makes expanding bank balance sheets costly. When constraints are non-binding, the arbitrage works (SOFR < EFFR). When binding, the arbitrage requires expensive equity issuance, allowing the spread to persist. This explains why SOFR spikes during stress are more pronounced than EFFR spikes.

## Standing Repo Facility (SRF)
The Fed introduced the SRF in July 2021 to cap SOFR spikes by providing an upper bound: SOFR ≤ max(SRFR, EFFR − capital cost). This created a **structural break** in the SOFR time series. Pre-SRF data contains spikes that are structurally impossible post-SRF. Analysts must treat pre- and post-SRF data as different regimes — particularly for volatility analysis.

## Key Benefits and Problems
- **Benefits:** Large, stable transaction volume; transaction-based (not survey); manipulation-resistant.
- **Problems:** The Fed does not share raw repo data — big banks with repo desks see the market in real-time while smaller participants wait until next-day publication. This asymmetry undermines the "level playing field" claim. The raw data gap also limits hedging precision: individual repo transactions have an estimated ~4bp standard deviation vs the published SOFR median.

**Formula:** Repo rate = (repurchase price − sale price) / sale price × (360/days)
