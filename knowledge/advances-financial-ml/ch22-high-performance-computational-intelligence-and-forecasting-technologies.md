# Ch22 — High-Performance Computational Intelligence and Forecasting Technologies

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 22 (contributed by Kesheng Wu and
Horst D. Simon, LBNL).

## Purpose
A guest chapter on the CIFT project at Lawrence Berkeley National
Laboratory: applying high-performance computing (HPC) to streaming
financial data analysis — motivated by the five-month delay in the
SEC/CFTC report on the 2010 Flash Crash (data volume cited as the
cause).

## Motivation
- On May 6, 2010 the DJIA dropped ~10% in minutes and recovered; the
  investigation took ~5 months, with ~20 TB of data given as the
  reason. HPC systems (e.g., NERSC) routinely process hundreds of TB in
  minutes — the delay was a tooling problem, not a data problem.
- HPC vs. cloud: cloud is built for high-throughput parallel tasks
  over independent objects; streaming analysis needs *real-time*
  responses on a single evolving object, dividing work across cores
  within one time-step — the HPC ecosystem has the better tooling.

## HPC hardware & software
- Hardware: clusters (the CIFT machine, "dirac1"), many cores per
  node, high-speed interconnect, GPUs; MPI for inter-node
  communication, shared memory within a node.
- Software: workflow/in-transit processing (ADIOS + ICEE transport
  engine) to analyze data before it reaches slow disk; streaming
  toolkits; results: 21× data-handling speedup, 720× speedup computing
  an early-warning indicator.

## Use cases (transferred techniques)
- **Supernova hunting (Palomar Transient Factory)**: automated
  image-difference workflow classifies transient objects in near-real
  time; SN 2011fe identified 11 hours after explosion; 3.8% overall
  mislabeling rate. Pattern: stream → detect change → classify with
  confidence → alert.
- **Fusion plasma (KSTAR)**: distributed workflow collects ECEI + XGC
  data, detects "blobs," tracks and predicts their movement between
  runs (10–30 min windows) — in-transit analysis with parallel
  connected-component labeling; blobs detected in milliseconds per
  time step.
- **Intraday peak electricity usage**: AMI smart-meter streams —
  detecting impending grid failure, analogous to detecting emerging
  illiquidity in markets.

## Financial takeaway
- The same pattern applies to markets: detect signs of emerging
  illiquidity during trading hours, fast enough to act — the tooling
  for real-time streaming analytics exists in HPC and should be applied
  to market data (order books, tape) rather than waiting months for
  post-hoc analysis.

## Key takeaways
- Financial big data is mostly time series; streaming analysis
  requires HPC-style parallelism (divide a single time-step across
  cores), not cloud-style batch parallelism.
- In-transit processing (analyze before storing) is the key technique
  for real-time decisions on fast streams.
- CIFT demonstrates the transferable recipe: stream → feature
  extraction → classification with confidence → alert — shared across
  astronomy, plasma physics, the power grid, and markets.
