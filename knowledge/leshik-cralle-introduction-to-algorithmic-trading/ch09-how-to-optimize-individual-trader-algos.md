# Chapter 9 — How to Optimize Individual Trader Algos

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## Targets

- **Success metric**: 8 of 10 trades profitable; the 2 losers stopped
  out by the (adaptive) stop-loss algo, designed to cut at ≈40 bp
  (with lookback-driven adaptation). Winners average **25–40 bp net of
  commission**.
- **Optimization criterion**: basis points per trade-second = % profit
  per second (includes a risk hint: $1 on a $100 share in 30s beats 60s;
  $1 on a $50 share in 30s beats both). Money exposed longer = money at
  risk longer + unavailable for other trades.
- **Exit rule**: hold while the trade produces the predefined bps/sec;
  the moment return wanes past a set threshold, sell at market (cancel
  the protective stop first).

## Method (trial and error, not rigorous)

- **Churn** is the key optimizing parameter — capital must produce
  returns; underperforming stock/algo combinations go to the "back
  burner" for analysis.
- Test frequently (every few sessions): vary (1) moving-average
  lookbacks, (2) SMA/LMA/EMA parameters, (3) trigger parameters —
  valley levels and the **ALPHA constant** in EMAs (controls how far
  back the tick series influences the average; vary in 100-tick
  increments and observe trigger/trade effects).
- **Keep a log** of what was varied, results, and when; weekly backups.
- Workflow hygiene: be slow and methodical; paper records as desired
  (OMS keeps the rest); download session records to a log diary; keep
  pads for ideas; don't trade when unwell/sleep-deprived ("a missed
  keystroke costs").
- Philosophy: **no home runs — plenty of fast singles and doubles**;
  "There are Bears, and there are Bulls. Pigs get slaughtered."

## Key takeaways

1. Optimize on return-per-second-of-risk (bps/trade-sec), with explicit
   per-trade stop discipline (≈40 bp) — this yields a high win-rate,
   small-edge system.
2. Parameter sensitivity testing should be logged and systematic (the
   EMA alpha in 100-tick steps), done often on short lookbacks.
