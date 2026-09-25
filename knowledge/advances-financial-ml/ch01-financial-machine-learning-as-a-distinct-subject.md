# Ch01 — Financial Machine Learning as a Distinct Subject

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 1.

## Purpose
Argues that financial ML is a discipline in its own right — related to,
but separate from, standard ML — and diagnoses why most financial ML
projects fail, proposing a factory-style research organization
(the meta-strategy paradigm) as the cure.

## Why financial ML projects fail
- **The Sisyphus paradigm**: firms hire many PhDs in silos and demand a
  strategy from each within months. Each researcher either settles for
  a false positive (overfit backtest) or a crowded standard factor
  strategy — both disappoint, and true discoveries can't cover the
  headcount. The structure guarantees failure.
- **The meta-strategy paradigm**: successful quant firms mass-produce
  strategies like a factory. Each researcher specializes in one station
  (data, features, strategies, backtesting, deployment, oversight)
  while keeping a holistic view. The money is in making a car factory,
  not a car.
- **The seven sins of quant investing** (Luo et al. 2014): survivorship
  bias, look-ahead bias, storytelling (ex-post rationalization), data
  mining/snooping, unrealistic transaction costs, outlier dependence,
  and ignoring shorting frictions (borrow cost/availability).

## The six research stations
1. **Data curators** — raw data, correctly timestamped (release dates
   matter: fundamental data is backfilled/reinstated).
2. **Feature analysts** — turn data into informative signals; collect
   *libraries of findings*, not strategies.
3. **Strategists** — build theories (white-box) that explain the
   features; a strategy is an experiment testing a theory.
4. **Backtesters** — evaluate under scenarios, quantify probability of
   backtest overfitting from the number of trials; results go to
   management only.
5. **Deployment team** — production integration, latency optimization.
6. **Portfolio oversight** — the strategy lifecycle: embargo → paper
   trading → graduation → re-allocation (concave allocation over time)
   → decommission.

## Key pitfalls table (ch1's map of the book)
Chronological sampling → use the volume clock; integer differentiation
→ fractional differentiation; fixed-time-horizon labeling →
triple-barrier; learning side+size together → meta-labeling; IID
weighting → uniqueness weighting/sequential bootstrap; CV leakage →
purging+embargoing; walk-forward backtesting → combinatorial purged CV;
backtest overfitting → synthetic data + deflated Sharpe ratio.

## Key takeaways
- Most "discoveries" in finance are false positives from multiple
  testing; ~20 iterations on the same data at a 5% significance level
  suffice to find a false strategy.
- Overfitting is not just a technical mistake — it's ethically dubious
  (promising returns that can't be delivered) and commercially futile
  (industry pays only for out-of-sample returns).
- Financial ML fails when imported off-the-shelf from academia/Silicon
  Valley; the data structure (non-IID, low signal-to-noise, overlap)
  demands bespoke methods that the rest of the book develops.
