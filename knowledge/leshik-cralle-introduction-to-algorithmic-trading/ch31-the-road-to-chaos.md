# Chapter 31 — The Road to Chaos (Nonlinear Science)

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## Concepts

- **Phase space**: mathematical construct where coordinates = variables
  specifying a system's state (phase) at any time. **Dynamical systems**
  = anything that evolves with time (each successive state is a
  function of the previous one).
- **Attractors / basins of attraction**: chaotic systems have
  attractors in phase space that draw in orbits from given starting
  conditions over many iterations; the long-run trajectory settles to
  the attractor. Lorenz's weather equations produced the owl-shaped
  "**strange attractor**" (the name's origin).
- **Embedding / lagging**: lagging phase space reconstructs a system's
  trajectory from time series (Floris Takens; embedding dimension) —
  the basis of nonlinear time-series prediction (use lagged values to
  predict future).
- **Chaos is deterministic, not random** (Poincaré foresaw it; Yorke &
  Li coined "chaos" in 1975). Turbulence (Ruelle & Takens, 1971) was
  controversial at first.
- **Period doubling & universality** (Mitchell Feigenbaum, Los Alamos,
  mid-1970s): changing forces on a dynamical system can double its
  period; the **logistic map** `X_{n+1} = α·X_n·(1 − X_n)` (0≤X≤1,
  0≤α≤4) goes irregular then chaotic beyond a critical α. All systems
  undergoing period doubling share the behavior qualitatively and
  quantitatively → the **Feigenbaum constant = 4.6692…** (transcendental
  like π and e). Feigenbaum's papers were rejected for 2+ years.
- **Sensitive dependence on initial conditions**: the slightest
  difference at the start magnifies to a completely different,
  unpredictable trajectory that revisits a basin of attraction without
  repeating.
- **Fractals** (Mandelbrot, 1975): a new geometry quantifying
  "roughness"; his cotton-price study showed non-Gaussian, fat-tailed
  distributions — a backlash resonating today.

## Markets as chaotic/complex systems

- Markets are chaotic and complex: time-evolution with sensitive
  dependence on initial conditions + "intelligent" participants +
  regime/regulatory/structural shifts + behavioral overlays. Far fewer
  participants than physical systems but more "intelligent."
- Mandelbrot: price variation is *not* the same across all markets; a
  single statistical model can't describe all. Schwager (minority
  view): markets share characteristics. The authors' take: shared
  properties + stock-specific variables (a law unto themselves).
- Chaos is here as a *conceptual* tool, not directly an algo source —
  to weave complexity/unpredictability-from-simple-constructs into
  thinking and design.

## Key takeaways

1. Markets are chaotic (deterministic but sensitive to initial
   conditions) — use this as a conceptual frame, not a trading signal.
2. Mandelbrot's fat-tail cotton study refutes universal Gaussian
   assumptions; per-market and per-stock differences matter.
3. Logistic-map period doubling and the Feigenbaum constant reveal
   universal structure in the onset of chaos.
