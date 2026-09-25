# Ch30 — Sentiment Analysis Strategy with QSTrader (Sentdex)

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 30 (QSTrader application).

## Sentiment analysis for systematic trading
Goal: take large quantities of "unstructured" data (news, blogs, tweets, video, images) and use
NLP to quantify positive/negative sentiment about assets — typically by statistical ML on the
language (bullish/bearish phrasing) mapped to numeric strength (positive = bullish, negative =
bearish). Vendors: **Sentdex, PsychSignal, Accern** — proprietary entity extraction + timestamped
sentiment scores, aggregated per day → **date-entity-sentiment tuples** = trading signals.
Building a full end-to-end sentiment engine is a big software-engineering task → retail quants
typically buy vendor signals and fold them into a broader portfolio of signals.

**Sentdex API**: sentiment for many instruments, minute or daily granularity (paid; streaming).
For backtesting, use the **sample file** (~5 years of daily signals for many S&P500
constituents) — rows of `date,symbol,sentiment_signal` with integer sentiment **+6 (strongest
positive) … −3 (strongest negative)**.

## QSTrader sentiment infrastructure (new Event/Handler + Backtest changes)
- **`SentimentEvent`** (subclass of Event): stores timestamp + ticker + sentiment value
  (float/int/string), sent to the Strategy to generate SignalEvents. Generic
  "date-ticker-sentiment" shape.
- **`AbstractSentimentHandler`**: common interface for vendor sentiment handlers; subclassed
  per vendor.
- **`SentdexSentimentHandler`**:
  - `_open_sentiment_csv`: load CSV into DataFrame, filter by end_date and ticker subset.
  - `stream_next(stream_date)`: streams all SentimentEvents for the given date into the queue;
    **must pass stream_date to avoid look-ahead bias** (never peek at future sentiment). Emits
    multiple SentimentEvents (one per ticker/row that day).
- **Backtest object changes**: in the event-dispatch loop, on TICK/BAR events set `cur_time`
  and (if the strategy has a sentiment handler) call `sentiment_handler.stream_next(
  stream_date=cur_time)` so the day's sentiment events enter the queue and reach the Strategy.
  (These changes are in the current QSTrader on GitHub.)

## Strategy: SentdexSentimentStrategy (long-only, per-ticker thresholds)
- Params: tickers (SPY removed from list), events_queue, `sent_buy` (entry threshold),
  `sent_sell` (exit threshold), `qty` (base quantity).
- Fixed share quantity per ticker (no dynamic sizing/dollar-weighting — deliberately kept
  simple; noted as first thing to optimise in production).
- `self.invested` = per-ticker boolean dict.
- `calculate_signals(event)`: respond to **SentimentEvent** (not just price events — this is
  the flexibility of event-driven strategies):
  - If ticker not invested and event sentiment ≥ `sent_buy` → **BOT qty** (long entry).
  - If ticker invested and sentiment < `sent_sell` → **SLD qty** (exit).
- Backtest params: entry = 6, exit = −1; base_quantity = 2,000; equity $500k;
  YahooDailyCsvBarPriceHandler; IBSimulatedExecutionHandler; benchmark SPY. Net of IB costs.

## Results (5 stocks per sector, 2000 shares each)
- **Tech**: CAGR 21.0% vs benchmark 9.4%; gains concentrated in 3 months (May-2013,
  Oct-2013, Jul-2015); mostly flat/down otherwise; DD duration 318 days (mid-2014→mid-2015);
  max daily DD 17.23% (benchmark 13.04%); Sharpe 1.12 vs 0.75 — **not significant enough for
  production**.
- **Energy**: very volatile; max daily DD 27.49% (eliminates it); loses effectiveness after
  mid-2014 (underwater, flat through 2015); Sharpe 0.63 vs 0.75 — **not viable**.
- **Defence**: many solid gain months; long-only daily Sharpe **1.69**; max DD 9.69% (less
  than benchmark); CAGR **25.45%**; most gains in 2013 (2014–15 far smaller).

## Path to production
- Test over a far larger period (5-yr sample is short).
- Add shorts → market-neutral tilt → lower market beta.
- Optimise position sizing + risk management.
- Diversify across many more stocks/sectors.

## Takeaways / pitfalls
- Vendor sentiment data is timestamped — inject it into the event loop **by date** to avoid
  look-ahead bias.
- Per-ticker threshold entries (sent_buy=6) are naive; gains cluster in few months (regime
  dependence); Sharpe must beat benchmark by a wide margin to justify production.
- Long-only sentiment strategies carry heavy market beta and sector concentration risk
  (energy DD 27%).
- Event-driven design pays off: strategies respond to arbitrary event types (SentimentEvent),
  not just bars.