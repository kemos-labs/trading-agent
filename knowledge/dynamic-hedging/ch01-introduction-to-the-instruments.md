# Ch01 — Introduction to the Instruments

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 1.

## Purpose
Defines the analytical framework of the book: derivatives, linearity vs. nonlinearity, and the vocabulary of hedging — from the viewpoint of a *manufacturer* (book runner) rather than a *user*.

## Derivatives and nonlinearity
- A **derivative** is a security whose price depends on another asset (the underlying). Two broad families:
  - **Linear derivatives** (forwards, futures): easy to hedge and lock in completely.
  - **Nonlinear derivatives** (options): have a nonzero second derivative (convexity) with respect to a parameter — they require *dynamic hedging*.
- **Risk Management Rule**: all nonlinear derivatives are time-dependent in their price (the *contamination principle*: if a spot in time/space can bring a profit, the areas surrounding it must account for that effect).
- Linearity/convexity/concavity test on a function of the underlying y(S) between S₁ and S₂; most instruments are only "quasi-linear."

## The Greeks (sensitivities)
- **Delta**: sensitivity of option price to underlying price.
- **Gamma**: sensitivity of delta to underlying price (second derivative; convexity).
- **Vega**: sensitivity to implied volatility.
- **Theta**: expected change in price with the passage of time (risk-neutral growth).
- **Rho**: sensitivity to interest rates/dividend payout.
- Long gamma/vega = positive sensitivity to the parameter.

## User vs. manufacturer
- The **user** cares about terminal value; the **manufacturer** (dynamic hedger) cares about the replication process — for a hedger, a put and a call of the same strike/expiration are first-order identical; what matters is strike, expiration, and gamma (convexity) paid for with theta (the "rent").
- Dynamic hedging makes every option **path dependent** — a key warning: returns of a sum of positions under dynamic hedging differ from the sum of independent returns.

## Synthetics
- A **synthetic security** is a linear combination of primary instruments; a basket's price is a weighted combination of components.
- Geometric averaging introduces convexity (e.g., a geometric-weighted dollar index trades at a premium), so convexity commands a price — Wall Street rarely grants free lunches.

## Key takeaways
- Nonlinearity (gamma) is the essence of option trading and the reason for dynamic hedging.
- The Greeks are derivatives of the option price with respect to market parameters; the framework extends beyond the underlying to volatility and rates.
- The book's stance: option theory is a young, misspecified craft; hedging is learned through practice ("it ain't physics").
