# Ch16 — Implementation of HFT Systems

**Source:** Irene Aldridge, *High-Frequency Trading* (2nd ed., 2013), Chapter 16.

## Purpose
Building "mission-critical" HFT systems: the software life cycle,
system architecture, and the testing discipline that separates
profitable operations from Knight Capital-style disasters.

## Model development life cycle
- Five phases: planning (goals, feasibility, budget) → analysis
  (requirements, scope — the most critical phase) → design
  (specifications, component interfaces, test cases) → implementation
  (coding + unit tests) → maintenance. The cycle is continuous.

## System architecture
- **Core engine** (run-time processor): receives/archives quotes,
  performs run-time econometrics, portfolio management, signal
  generation, order transmission, execution confirmation, real-time
  P&L and risk management.
- Languages: C++ preferred (light, fast, no garbage collection);
  Java used but with GC disabled (Nasdaq OMX matching engine); Q
  (Kx) for time-series-heavy shops.
- Connectivity via **FIX** (emerged 1992 Fidelity–Salomon;
  75%+ buy-side, 80% sell-side, 75%+ exchanges by 2006); FAST, ITCH/
  OUCH also used. FIX message = header (BeginString #8, BodyLength
  #9, MsgType #35) + body + trailer.

## Testing trading systems (the key discipline)
- **Data-set testing**: out-of-sample/clean data; repeat at multiple
  sampling frequencies.
- **Unit testing**: each function/component in isolation — catch
  errors early.
- **Integration testing**: module interoperability as the system
  grows.
- **System testing**:
  - **GUI** testing (interfaces work as specified);
  - **Usability/performance** (e.g., shutdown latency);
  - **Stress testing**: extreme scenarios (10% price drop, exchange
    outage) and their P&L impact;
  - **Security testing**: external (Internet hijacking) and internal
    (disgruntled employees) threats;
  - **Scalability**: max securities processed without performance
    degradation;
  - **Reliability**: failure rate ≤ 0.01% (99.99% uptime);
  - **Recovery**: restart/network-unplug integrity.
- **Regression testing**: retest after every code change; **automation
  testing**: scripted, repeatable test runs.
- Separating coders from testers (testers paid ~1/3 of coders)
  prevents self-serving validation.

## Key takeaways
- HFT systems are software businesses: the engineering discipline
  (life cycle, modular design, rigorous testing) IS the competitive
  edge.
- Stress, reliability, and recovery testing are not optional — the
  failure modes they catch (Knight 2012: a mis-deployed code block
  losing $10M/minute) are tail events with unbounded downside.
- Reconciliation between back-test, paper trading, and production at
  every stage is the safety net that catches both coding bugs and
  assumption drift.
