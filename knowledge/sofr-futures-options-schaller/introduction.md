# SOFR Futures and Options — Introduction

## Context and Purpose
The book covers the CME SOFR futures and options complex, framing SOFR as the successor to LIBOR. Two fundamental changes underpin the transition: (1) from a term rate (LIBOR) to an overnight rate (SOFR), requiring new methods for term-rate construction; (2) from an unsecured to a secured reference rate, introducing a new basis dimension to the STIR (short-term interest rate) universe.

## Historical Arc
- **Eurodollars** originated from offshore USD deposits (e.g., Chinese government moving funds to Paris in 1950). CME launched the first cash-settled futures contract on Eurodollar rates in 1981 — initially illiquid, then explosive once Continental Illinois failed and swaps markets grew.
- **Eurodollar futures** enabled zero-coupon-style decomposition of the yield curve into 3M forward segments. Key discoveries: the convexity bias (Hoskins & Burghardt) — futures rates systematically overstate forward rates due to daily margining; and the carry trade analysis showing the most profitable part of the curve carry was the first 2–3 years.
- **LIBOR** was standardized by the BBA in 1986 as a panel survey of 16 banks. The 1998 question change to "At what rate *could you* borrow" (hypothetical) was critical — after the GFC, unsecured interbank lending collapsed and LIBOR became fiction ("the rate at which banks don't lend to one another").
- **The rigging scandal** (2008 onwards): banks submitted artificially low rates; $9B+ in fines. Regulators concluded LIBOR was unfit for purpose.
- **SOFR** (Secured Overnight Financing Rate) was selected by ARRC in 2017 as the USD LIBOR replacement. It is the volume-weighted median of overnight repo transactions, published by the NY Fed at ~8 a.m. ET.

## Book Structure
- **Section 1 (Concepts):** Ch1 SOFR mechanics → Ch2 SOFR futures → Ch3 lending markets & term rate → Ch4 spread futures & basis → Ch5 options → Ch6 biases & curve building.
- **Section 2 (Use Cases):** Ch7 simple hedging examples → Ch8 hedging CME Term SOFR → Ch9 hedging swaps & bonds → Ch10 hedging caps & floors.

## Key Thesis
The transition from LIBOR to SOFR is easy for futures (back-months are essentially a "renaming exercise"), but fundamentally harder for options (the shift from forward-looking term rates to backward-looking averages turns standard options into path-dependent Asian options during the reference period). This asymmetry explains why SOFR futures liquidity surged ahead of SOFR options liquidity.
