# Chapter 2 — All About Trading Algorithms You Ever Wanted to Know (FAQ)

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## FAQ distillation

- **What is an algo?** A list of steps/instructions: inputs → processing
  → desired output. No heavy math or stats required to *use* the book's
  algos (a high-school level suffices; Part II provides the toolkit).
- **Excel**: the book's vehicle — templates ship on the CD; Excel is the
  de facto standard workhorse spreadsheet.
- **Do algos vary by stock?** *Yes* — a given algo's efficiency differs
  across stocks and decays over time (a recurring theme: stock-specific
  parameterization and periodic meta-analysis).
- **Capital requirements (US, circa book's writing)**: $25,000 minimum
  for a margin/PDT account; 4:1 intraday leverage (must be flat by
  4:00pm close); authors recommend ≥$50,000 in practice. Never risk
  money whose loss would alter your lifestyle.
- **Time commitment**: ~2 months of concentrated effort to basic
  proficiency; paper trade on a simulator before risking real money.
- **Asset classes**: the authors argue markets differ in basic
  principles; this book targets **US equities** (NASDAQ/NYSE), though
  much machinery adapts elsewhere (futures, FX, commodities).

## Key takeaways

1. Algo usage is accessible to non-programmers through spreadsheet
   templates, but capital, risk appetite, and stock-specific behavior
   constrain results.
2. Paper trade first; treat drawdowns as a risk-management problem, not
   an algorithm failure per se.
