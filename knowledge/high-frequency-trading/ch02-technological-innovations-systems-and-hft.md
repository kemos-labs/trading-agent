# Ch02 — Technological Innovations, Systems, and HFT

**Source:** Irene Aldridge, *High-Frequency Trading* (2nd ed., 2013), Chapter 2.

## Purpose
The hardware, messaging, and networking stack that enables HFT — and
why each layer's latency budget matters.

## Hardware
- **Multicore CPUs**: shared memory, thread-based parallelism; cheap
  ($100+).
- **GPUs**: most chip area is arithmetic logic units; threads execute
  in parallel batches ("warps"); speed requires code with uniform loop
  counts (no branching divergence).
- **FPGAs**: no fixed instruction set — the circuit is programmed
  directly (Verilog/VHDL), bypassing the compile step; best for
  processing a limited number of time series (<2,000 inputs), where
  they beat GPUs/CPUs; ~$4–5,000 per chip. Programming is
  inexpensive; latency is saved by avoiding run-time compilation.

## Messaging
- Standard message architecture: session start, **heartbeat** (liveness
  signal — its absence closes the channel), quote, order, cancellation,
  order/cancel acknowledgments, execution acknowledgment, session end.
- Protocols: **FIX** (XML-like, human-readable, dominant for order
  flow; 75%+ of buy-side firms, 80% of sell-side), **ITCH/OUCH**
  (Nasdaq binary), FAST. FIX is slow; proprietary APIs trade speed for
  vendor lock-in.
- **Security**: TCP/IP and UDP carry no encryption — trading messages
  travel in plain text over the Internet; co-location's private lines
  are the security fix, not just a speed fix.

## Network models
- **Client-server** (via ISP): moderately secure, slow.
- **Peer-to-peer**: faster, but traffic can be observed/read by peers.
- **Co-location**: trader servers inside the exchange facility with
  dedicated lines — fast and secure. Latency is physical: Newark→
  Chicago ≈ 15ms round trip; the co-located Chicago trader shaves
  17–22ms vs. a New York connection to Nasdaq.

## Key takeaways
- Every layer — chip, message format, network path — contributes to
  latency; HFT latency budgets are microseconds to milliseconds.
- Hardware choice is workload-dependent: FPGA for few-stream, low-
  latency signal processing; GPU for massively parallel computation;
  CPU for general logic.
- The same infrastructure that provides speed also provides **security
  of communications** — a co-location ban would expose order flow.
