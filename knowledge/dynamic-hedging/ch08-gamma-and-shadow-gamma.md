# Ch08 — Gamma and Shadow Gamma

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 8.

## Purpose
Gamma (the second derivative) and its dynamic extensions — shadow gamma, skew gamma, GARCH gamma — the risk dimension that makes options hard to hedge.

## Simple gamma
- Γ = ∂²F/∂U². Time dependence: ATM gamma is *maximum near expiration*; OTM gamma is *maximum far from expiration*.
- Calendar-spread implications: a 3-month option has gamma concentrated near the money; the 6-month spread across a wider range — hedges chosen for the immediate need can be short-lived in a bursting market. **Rule**: a range must be associated with every gamma measurement.

## Gamma imperfections for a book
- For a portfolio, gamma becomes "local" — long at 100, short at 101.65, long again — depending on which structure dominates at each spot.
- Practical measure: **up-gamma** (change in delta if spot moves up by a defined increment) and **down-gamma** (down increment) — the two can differ dramatically (asymmetric, e.g., near barriers). Averaging them is deceiving; use scenario schedules.

## Shadow gamma
- The second-order effect of spot moves on the *hedging* of an option through volatility: when spot moves, volatility (and hence the option's delta/gamma) moves too.
- **Skew gamma (asymmetrical shadow gamma)**: with a volatility skew, the ATM volatility itself changes as spot moves along the skew — gamma must account for it.
- **GARCH gamma (Engle-Rosenberg 1995)**: the difference between present and future delta because future volatility responds to market moves — the first academic form of shadow gamma.
- **Advanced shadow gamma**: includes expected volatility AND carry/interest-rate moves accompanying price moves (e.g., weak currencies like the Mexican peso: selloff → defensive rate rise + vol rise; the back month moves more than the front).

## Practical implementation
- Gamma computed analytically misses the spot-volatility linkage; repricing the structure at perturbed spot and vol (scenario analysis) captures the shadow effects.
- Risk managers should demand "shadow reports," not straight reports, for barrier-heavy books.

## Key takeaways
- Gamma is a local, book-specific measure; up/down gamma differ in skewed markets.
- Shadow gamma is the practical bridge between spot risk and volatility risk — crucial for barriers and skewed assets.
- Hedging decisions must incorporate how volatility and carry respond to price moves, not just the raw second derivative.
