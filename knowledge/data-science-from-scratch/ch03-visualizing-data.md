# Ch03 — Visualizing Data

**Source:** Grus, *Data Science from Scratch*, Chapter 3.

## Purpose
How to explore data visually with `matplotlib`. The running theme: **"for
the most part, 'visualization' is just 'making plots'"** — the goal is to see
your data before you model it.

## matplotlib basics
- `from matplotlib import pyplot as plt` — the standard import.
- **Line chart**: `plt.plot(xs, ys, marker='.', linestyle='none')` (points
  without connecting lines), `plt.title(...)`, `plt.xlabel(...)`,
  `plt.ylabel(...)`, `plt.show()`.
- **Bar chart**: `plt.bar([i for i, _ in xs], [y for _, y in xs])` — good for
  comparing counts across categories (e.g. friends per user).
- **Scatter plot**: `plt.scatter(xs, ys)` — the workhorse for exploring the
  relationship between two numeric variables.
- **Histogram**: `plt.hist(xs, bins=...)` — shows the distribution of one
  variable.
- **`plt.axis([xmin, xmax, ymin, ymax])`** — control plot extent.
- **Multiple series**: call `plt.plot`/`scatter` repeatedly before
  `plt.show()`, optionally with `label=` + `plt.legend()`.

## Good chart practices (implicit rules in the chapter)
- **Label axes and titles** on every chart — otherwise it's not an analysis,
  it's decoration.
- **Prefer scatter plots over line plots** when points are not a sequence
  (line charts imply ordering/time).
- **Use bar charts for categorical counts** and histograms for numeric
  distributions — don't force the wrong glyph onto the data.
- Choose ranges/axes so the data fills the frame; prune misleading
  defaults.
- Visualize *before* modelling: the eye spots outliers, clusters, and
  nonlinearity that summary stats hide.

## Key takeaways
- matplotlib's core model: build the plot imperatively (`plt.*` calls), then
  `plt.show()` once. `plt.clf()` clears the figure between plots.
- The book's data is tiny and toy-like, but the *habit* of always plotting
  first carries over to real work: **plot, then summarise, then model**.
- `plt.annotate(...)` places text labels at specific (x, y) positions —
  used later for word-vector and cluster plots (ch21).
- Layouts can be organized with `fig, ax = plt.subplots(rows, cols)` and
  plotting into each `ax[row][col]` — shown in ch12's Iris scatter matrix.

## Notes
- No formulas; pure plotting practice.
- Later chapters lean on this foundation: histograms of distances (ch12),
  scatterplots of clusters (ch20), embedding projections (ch21).
