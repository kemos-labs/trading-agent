# Ch10 — Exploratory Data Analysis

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 10.

## Purpose
EDA: systematically getting to know a dataset — types, shapes, summaries,
and relationships — before modeling. EDA finds problems and generates
questions; it does not test hypotheses.

## Feature types (the statistical lens)
- **Numeric**: continuous (height, price) or discrete counts.
- **Ordinal**: ordered categories (body condition score 1–5, age buckets).
- **Nominal**: unordered categories (sex, species) — one-hot encode for
  modeling.
The distinction drives summaries and plots: means only for numeric, modes
for nominal.

## Summary statistics
- Center: mean (squared-loss minimizer), median (absolute-loss), mode.
- Spread: SD/variance, IQR, range. Skew: long tails pull the mean away
  from the median — report both.
- Grouped summaries: mean/SD by category (groupby) to find structure.
- Correlation r: strength of *linear* association, unitless, −1..1. Caveat:
  identical r can hide very different relationships (Anscombe's quartet,
  ch15).

## Plots for EDA
- **Histogram / density**: shape, skew, modes, outliers.
- **Box plot**: median, IQR, whiskers, flagged outliers — great for
  comparing categories.
- **Scatter plot**: relationship between two numeric features; jitter or
  alpha to handle overplotting (ch11).
- **Bar chart / value counts**: categorical distributions.

## EDA workflow
1. Types + shape + missing counts per column.
2. Summaries per numeric column; value counts per categorical.
3. Distributions (histograms) and pairwise relationships (scatters,
   correlations).
4. Grouped comparisons for the question at hand.
5. Follow up anomalies — they are usually data errors or scope leaks, and
   occasionally the actual insight.

## Key takeaways
- EDA is iterative and cheap; modeling is expensive and assumption-heavy —
  do EDA first.
- Mean+SD is not enough for skewed data; always look at the shape.
- r only measures linearity; plot before you trust the number.

## Notes
- Chapter 11 builds the visualization vocabulary (marks, channels, grammar
  of graphics) that powers all the EDA plots.
- The donkey (ch18), air-sensor (ch12), and fake-news (ch21) case studies
  are EDA showcases.
