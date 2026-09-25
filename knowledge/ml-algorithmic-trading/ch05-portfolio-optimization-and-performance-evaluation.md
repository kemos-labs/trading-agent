# Ch05 — Portfolio Optimization and Performance Evaluation

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 5.

## Purpose
Covers the classical mean-variance framework and its limitations, portfolio construction in practice, and honest performance evaluation — including why backtest metrics can mislead.

## Mean-variance optimization (Markowitz)
- Maximize expected return for a given risk (variance), or minimize variance for a return target:
  - Portfolio return: r_p = wᵀμ
  - Portfolio variance: σ²_p = wᵀΣw
- **Efficient frontier**: set of Pareto-optimal (risk, return) portfolios; **tangency portfolio** maximizes Sharpe ratio.
- **Constraints**: weights sum to 1; long-only or allow shorts; no-short-sale limits bind most retail/institutional portfolios.
- **Sensitivity problem**: optimal weights are extremely sensitive to estimated μ and Σ — estimation error dominates; small input changes produce wildly different portfolios (Markowitz's curse; cf. HRP in `advances-financial-ml` ch16).

## Estimation and shrinkage
- Use robust estimators for Σ (e.g., shrinkage toward a structured target, Ledoit–Wolf).
- Forecast μ is the hard part: historical means are noisy; factor/ML forecasts preferred.
- Resampling or bootstrap aggregation of efficient frontiers reduces instability.

## Risk measures
- **Volatility** (annualized std), **drawdown** (peak-to-trough), **VaR** (quantile of P&L), **CVaR/expected shortfall** (mean loss beyond VaR).
- **Sharpe ratio**: (r_p − r_f)/σ_p, annualized by √(periods per year).
- **Information ratio**: active return / tracking error vs. a benchmark.

## Performance evaluation pitfalls
- **Benchmarking**: judge active strategies vs. an appropriate benchmark (beta-adjust via alpha from a regression, e.g., CAPM/Fama-French).
- **Metrics**: CAGR, Sharpe, Sortino (downside deviation), max drawdown, win rate — each hides a different failure mode; report several.
- **Statistical honesty**: a Sharpe of 2 on 3 years of daily data may be noise; use standard-error estimates, multiple-testing corrections (deflated Sharpe), and out-of-sample walk-forward testing.
- **Transaction costs** (spread, market impact, borrow) must be modeled — they are decisive for high-turnover strategies.

## Practical construction
- Equal-weight / risk-parity portfolios are hard to beat once estimation error is priced in.
- Sector/industry and factor diversification reduce idiosyncratic risk.
- Combine predictions with optimization: forecasts → target weights → rebalance schedule → execution (see `market-microstructure-execution`).

## Key takeaways
- Optimization is only as good as the inputs; tame estimation error with shrinkage and robust targets.
- Evaluate performance against benchmarks with realistic costs and statistical significance, not raw CAGR/Sharpe.
- Simple, diversified, low-turnover portfolios often dominate optimized ones out of sample.
