# Ch25 — Star

**Source:** Scott Patterson, *Dark Pools* (2012), Chapter 25.

## Purpose
Rebellion Research's **Star** — an AI that learned to invest long-term
on its own — and the book's closing meditation on machine learning:
Star's counterintuitive brilliance in early 2009 and Greenberg's
warning that ML is dangerous in the hands of the ignorant.

## Star
- Spencer Greenberg (pure mathematician; son of Chieftain Capital's
  Glenn Greenberg, grandson of Hammerin' Hank) builds Star with Alex
  Fleiss, Jeremy Newton, and Jonathan Sturges at Rebellion Research
  (founded 2005, ~$2M live capital in early 2007). Star monitors
  dozens of factors (earnings growth, rates, commodity prices,
  currencies, thousands of stock ticks), recalibrates signals
  continuously, holds no leverage, and never shorts.
- 2007: Star dumps real estate and financials in April, ends +17%
  (S&P +5%). 2008: an "apocalypse portfolio" (gold, utilities,
  health care, dollar stores) — down 26% vs. S&P −39%. Early 2009 it
  gets bullish on banks/insurers while Fleiss weeps daily, convinced
  the machine is suicidal; the market bottoms in March and Star finishes
  +41% (S&P +23%). 2010: +21% vs. +13%, whittling international exposure
  from ~40% to <10% before the Greek crisis. In 4+ years Star never
  trailed the S&P in any rolling 365-day period.
- The lesson of 2009: Star's training window (data back to the late
  1990s) contained no depression, yet its pattern machinery read the
  panic correctly — buying when humans were most afraid. Faith vs.
  fear: Greenberg's "perfectly rational, utterly unemotional investing
  machine."

## The Battle of the Quants (Feb 16, 2011)
- Greenberg's keynote: ML "learns to invest" rather than optimizing
  fixed parameters — leaving it up to the learning algorithm to discover
  principles humans can't see (e.g., falling rates + rising gold +
  gaining utilities ⇒ buy European airplane makers).
- His cautionary parable: the military tank-detector that "worked"
  because the no-tank photos were cloudy and the tank photos sunny —
  the model learned weather, not tanks. "Machine learning can be
  disastrous in the hands of people who don't know what they are
  doing" — confounding variables and data artifacts masquerade as
  signal.

## Key takeaways
- Autonomous ML investing works when the process is disciplined (no
  leverage, no shorting, continuous recalibration, long horizon) — but
  its edge can be invisible in real time.
- Regime-change risk: a model trained on data that lacks the current
  regime (depression) can still act correctly or catastrophically —
  never assume the training distribution covers the future.
- Always audit what the model actually learned (the tanks parable) —
  spurious correlations are the #1 ML-in-finance failure mode.
- The book's arc completes: Levine made the market free and fast;
  Star shows the endgame — a machine that invests like a digital
  Buffett, supervised (or not) by humans.
