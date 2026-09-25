# Ch15 — Minimizing Market Impact

**Source:** Irene Aldridge, *High-Frequency Trading* (2nd ed., 2013), Chapter 15.

## Purpose
Execution algorithms: parceling and routing orders to minimize cost,
impact, and footprint — the "best execution" layer beneath HFT signals.

## Why execution algos
- Large orders must be sliced (child orders) to reduce market impact
  and visibility; limit-order algos cancel/resubmit to avoid being
  picked off. Costs: fees, spread, opportunity cost of non-execution,
  and market impact.
- **Efficient trading frontier** (Almgren–Chriss 2000):
  `min Cost(α) + λ·Risk(α)` over aggressiveness α — the execution
  analogue of the CAPM frontier; λ is risk aversion (0 = cost-only,
  0.5 = fairly risk-averse). Aggressive execution (smaller α) cuts
  opportunity cost but raises impact; the frontier traces the
  trade-off.

## Order-routing objectives and tactics
- Minimize costs (choose venue/ timing for low spreads), obtain best
  price (short-term forecasting), maximize speed, maximize size,
  minimize footprint.
- **Venue selection for speed**: market orders → send to the venue
  with the *most* top-of-book liquidity (least impact per slice);
  limit orders → send to the venue with the *fewest* resting limit
  orders (fastest queue priority). Poll venues, slice accordingly.
- **Benchmarks**: daily close (hard to beat — requires forecasting),
  VWAP, algorithm benchmarks.

## Basic models and their flaws
- **TWAP**: uniform time slicing; ignores volume/momentum patterns.
- **VWAP**: trade proportional to historical volume; assumes volume is
  exogenous and stationary — but order flow is periodic (Fourier
  analysis reveals cycles in flow), so VWAP's exogeneity assumption
  breaks; it also reveals your flow pattern to observers.
- **POV**: participation-rate-based; same transparency issues.

## Advanced models
- **Resilience/shadow-book models** (Obizhaeva–Wang, Alfonsi–Schied,
  Gatheral): the book has a "shadow" form it reverts to after
  liquidity is consumed; resilience h(E) governs recovery. Optimal
  execution induces a **constant rate of book replenishment**:
  `E_t = X_t − ∫₀ᵗ h(E_s)ds`; cost `C = ∫ S_t dx_t`; optimality
  requires volume impact stays constant (`E_t = const`).
- **Under GBM** (Forsyth et al. 2011): `dS = μSdt + σSdZ`;
  cost `C = η∫v²dt + λσ∫S²x²dt`; the Euler–Lagrange closed form
  gives the optimal trading rate, and many schedules produce
  near-identical costs — robustness over elegance.
- **Under generalized MI functions** (Gatheral 2011): with
  exponential resilience `h(E) = e^{−ρt}`, costs take the
  Obizhaeva–Wang form with closed-form optimal schedules.

## Key takeaways
- Execution is a **two-objective optimization**: impact vs.
  opportunity cost, tuned by risk aversion λ — the efficient trading
  frontier is the framework for choosing an algo.
- Basic algos (TWAP/VWAP) leak your flow; advanced models exploit
  book resilience and trade at a constant replenishment rate.
- Routing heuristics: take liquidity where it's deep, post where
  queues are short.
