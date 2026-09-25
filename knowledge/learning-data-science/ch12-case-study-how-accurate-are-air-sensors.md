# Ch12 — Case Study: How Accurate Are Air Sensors?

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 12.

## Purpose
Full lifecycle on a measurement/calibration problem: are cheap PurpleAir
(PA) sensors accurate enough, and can we calibrate them against government
AQS monitors? Introduces the **linear model as calibration**.

## Question & scope
- Question: how well do PA readings track AQS (reference) readings, and
  how can PA readings be corrected?
- Data: daily PM2.5 averages from co-located AQS + PA monitors across many
  locations (Georgia example in ch15), plus meteorological covariates
  (humidity). Scope/bias: sensor drift, siting differences, and — critical
  — **calibration is humidity-dependent** (sensors misread in dry, fire
  season conditions).

## EDA & measurement error
- Compare paired readings: scatter + correlation; quantify disagreement.
- Repeated measurements of the same thing (two instruments, or re-weighing
  in ch18) quantify **measurement error/repeatability**.
- Histograms of differences reveal bias (systematic offset) vs noise
  (scatter).

## Calibration as a linear model
- Fit PA ≈ θ₀ + θ₁·AQS (ordinary least squares) at co-located sites; then
  correct PA readings by inverting the model: adjusted = (PA − θ₀)/θ₁.
- Fit is done per-region/site where possible; the residual plot shows
  whether the linear correction is adequate or curvature remains.
- When the bias is driven by a covariate (humidity), the calibration must
  be conditional on it — a first taste of multiple regression (ch15).

## The lifecycle in action
- Question → scope → data (existing sensors, no new collection) → wrangle
  (align by date/location, drop bad records) → EDA (paired plots) → model
  (calibration line) → evaluate (residuals, out-of-sample checks).
- Conclusion: PA sensors are usable *after* calibration, within known
  accuracy bounds — never present raw uncorrected readings as accurate.

## Key takeaways
- Measurement error is data, not noise to ignore: quantify it and model it.
- A linear model is a calibration tool, not just a predictor.
- Check whether the correction generalizes (different seasons, sites,
  humidity) before trusting it — this is the drift concern of ch2.

## Notes
- Ch15 re-fits this example formally (simple linear model, residual SD vs
  SD of outcome); ch17 uses the humidity coefficient for bootstrap
  inference/CI.
- Teaches "fail closed": sensors give biased readings under certain
  conditions; the analysis must state where the model breaks.
