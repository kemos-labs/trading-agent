# Ch02 — Financial Data Structures

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 2.

## Purpose
Shows how to turn raw, unstructured financial data into structured
datasets ("bars") suitable for ML, moving from time-based to
information-driven sampling, plus the "ETF trick" for multi-product
series.

## Four essential data types
- **Fundamental**: accounting data, quarterly, released with a lapse —
  always use release dates, never period-end dates; watch for
  backfilling and reinstated values.
- **Market**: exchange/trading-venue feeds (FIX messages, order books,
  BWICs). ~10 TB/day; the richest source. Every participant leaves a
  footprint (TWAP algos, GUI round lots).
- **Analytics**: derivative data processed by others (analyst ratings,
  derived sentiment) — convenient but costly, opaque, and shared.
- **Alternative**: primary info (satellites, social media, sensors)
  that hasn't reached other sources; hard to process = most promising.

## Standard bars
- **Time bars**: fixed intervals. Simple but statistically poor —
  volatility is not constant per bar (heteroscedasticity), and
  autocorrelated returns make inference invalid.
- **Volume bars**: fixed volume per bar (e.g., 10,000 contracts) —
  volatility is closer to constant; better statistical properties.
- **Dollar bars**: fixed dollar amount traded — even better; directly
  relevant to P&L and invariant across price levels.
- **Tick bars**: fixed tick count; cheapest to compute but not
  information-driven.

## Information-driven bars
- **Imbalance bars** (tick/volume/dollar): end a bar when cumulative
  signed tick counts/volume/dollars diverge from the expected value
  (E[T], estimated via EWMA of prior bars and P[b], the EWMA buy
  proportion). Sample when θ_t exceeds expectations.
- **Run bars** (tick/volume/dollar): end a bar when the number (or
  volume) of consecutive same-side ticks exceeds expectation —
  counts runs *without offsetting* (no imbalance cancellation). Run
  bars are the most information-efficient sampling.
- Rationale: sample when the market is doing something unusual, not on
  an arbitrary clock.

## The ETF trick (multi-product series)
- A futures spread has time-varying weights, can go negative, and has
  misaligned trading times. Fix: model the value of $1 invested in the
  spread — strictly positive, reflects PnL, absorbs costs.
- Futures rolls: build a *gaps* series (price change at roll) and
  subtract it from raw prices; rolled prices are for PnL simulation,
  raw prices for position sizing (rolled prices can go negative, e.g.,
  contango sell-offs). Non-negative series: compute returns from rolled
  prices divided by previous *raw* price, then `(1+r).cumprod()`.

## Sampling features
- **Downsampling** (linspace or uniform) reduces data but arbitrarily.
- **Event-based sampling**: sample around significant events. The
  **CUSUM filter** samples when cumulative deviations from the mean
  exceed a threshold — the standard event sampler used throughout.

## Key takeaways
- Bar construction choice matters more than most practitioners admit:
  information-driven bars (volume/dollar, imbalance/run) give
  homoscedastic, informative samples that standard time bars lack.
- Data that is hard to store/manipulate is usually the most valuable —
  your competitors skipped it for logistic reasons.
