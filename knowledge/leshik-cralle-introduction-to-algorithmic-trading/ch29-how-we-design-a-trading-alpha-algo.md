# Chapter 29 — How We Design a Trading Alpha Algo

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## The authors' design workflow

1. **Assumption/conjecture**: about the price behavior of a target
   ticker — from a coffee thought, a spec requirement, a wishful
   "wouldn't it be wonderful", or live tick-chart observation. Or start
   from a desired spec ("what would we like the algo to do?").
2. **Brainstorm** from many perspectives; pull tick charts (10+ recent,
   yesterday's on top) — let the data "whisper its secrets"; look for
   what moves with what, patterns, structural similarities between
   sessions.
3. **Metrics scan**: time-series of volatility, %Range, basis-point
   returns — note anything unusual/surprising.
4. **Simmer** (coffee → overnight); the mind integrates at night.
5. **Formalize** the conjecture in *pseudocode* (natural-language
   English logic, free of syntax constraints) — the first step in
   mathematizing.
6. **Translate to Excel function language** (rarely Visual Basic/Java)
   — microcode-optimized functions = fast; staged, transparent
   approach preferred.

## Pseudocode constructs used

- SEQUENCE (one statement after another)
- DO WHILE / REPEAT UNTIL (loop with test at start/end)
- IF…THEN / IF…THEN…ELSE / CASE (branching)
- FOR…NEXT (counter loop)
- Boolean: AND, OR, NOT, XOR; comparison: EQUAL, GREATER THAN,
  SMALLER THAN

## Design maxims

- Complex designs have a *shorter working life* than simple ones.
  **"Less is more"** (Occam's razor) — fewer dimensions generalize
  better.
- Boolean/comparison operators expand designs indefinitely, but the
  palette is bounded only by imagination; use restraint.
- Staged implementation: build band-aids first while deeper problems
  are resolved; refine iteratively.

## Key takeaways

1. Algo design = conjecture → brainstorm → metrics → simmer →
   pseudocode → Excel function code; pseudocode is the bridge between
   idea and executable logic.
2. Keep designs simple and low-dimensional (Occam); complexity shortens
   shelf life and worsens generalization.
