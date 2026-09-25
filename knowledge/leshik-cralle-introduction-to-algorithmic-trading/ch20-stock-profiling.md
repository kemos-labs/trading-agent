# Chapter 20 — Stock Profiling

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## The profiling discipline

- **Dedicated Excel file per traded stock** (STOCK PROFILING template)
  archiving all activity, results, and trade data — becomes a valuable
  database over time. Note which algos perform best on the main
  optimizing criterion, **bp/sec** (trade return over trade duration).
- Copy the transaction log from the OMS to disk at each session's end.
- **Profit target**: minimum net basis-point return of **25 bp** —
  compute wins minus losses *minus brokerage commissions* (true net).
  Commission structure: flat round-trip break up to ~2500 shares,
  fractional per-share beyond; verify the broker's tariff.
- **Session volume smile**: most volume at the open (price discovery,
  overnight-news assimilation) and close (position completion/closing).
  The ALPHA ALGOS are time-agnostic (small time slices), but many
  practitioners wait 15 minutes to ~11:30am for price discovery to
  stabilize; large swings at the open are profitable if you're on the
  right side — the algos are designed to take on that turbulence (watch
  the stop-loss reaction speed).

## Key takeaways

1. Per-stock archives + bp/sec focus + 25 bp net floor define the
   performance-management loop.
2. Know your broker's commission breakpoints — they change optimal
   sizing and targets.
3. The open is where the biggest moves happen; either exploit the
   turbulence with tested algos or wait for stabilization.
