# Ch23 — Conclusions and Next Steps

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 23.

## Purpose
Synthesis of the ML4T thesis: the ML workflow adds value across the whole investment process, but only with disciplined data handling, honest evaluation, and continuous monitoring — plus a roadmap of what's next.

## Key takeaways
1. **Data is the most important ingredient** — sourcing, cleaning, and integration dominate outcomes; model choice is secondary.
2. **Domain expertise is essential** — to define objectives, select data, engineer features, and interpret results; ML doesn't replace it.
3. **ML is a toolkit to adapt and combine** — linear, trees, deep nets, NLP, RL each suit different problems; the workflow unifies them.
4. **Objectives and performance diagnostics drive iteration** — choose the right loss and metrics (IC, spreads, costed returns), not just accuracy.
5. **Backtest overfitting is the huge challenge** — multiple testing, leakage, and estimation error inflate results; significance-aware validation is mandatory (skills `purged-cross-validation`, `walk-forward-validation`).
6. **Transparency helps adoption** — feature importance, residual diagnostics, and explainable models build confidence in black boxes.

## Data lessons repeated
- Match model complexity to data noise (bias-variance); deep models only pay off with large, rich datasets.
- **Data integration** beats single sources: combining prices, fundamentals, and alternative data exploits interaction effects.
- **Point-in-time integrity**: labels and features must respect publication timestamps — third-party timestamps often need adjustment to avoid lookahead bias.
- Data quality has no universal standard — quality means *signal content for your objective*, evaluated cost-effectively.

## Where to go next (the book's suggestions)
- **Production infrastructure**: scalable data pipelines, feature stores, model registry, and monitoring — the engineering layer under the workflow.
- **Advanced models**: transformer architectures for text, graph neural networks, and more sophisticated generative/RL setups as data and compute allow.
- **Strategy operations**: execution quality, transaction-cost modeling, and capacity analysis (see `market-microstructure-execution`).
- **Robustness**: stress testing with synthetic data (ch21), regime-awareness (see `hmm-regime-detection`), and decay monitoring — signals fade as markets adapt; retrain and redeploy on schedule.

## The recurring discipline (worth re-reading ch6, ch8)
- Honest splits → leakage-free features → costed backtests → significance tests → monitoring. Every chapter's "trading application" is only as good as this pipeline.

## Key takeaways
- ML for trading is a *process*, not a model: data → features → model → strategy → evaluation → monitoring, iterated.
- The biggest risks are silent: lookahead bias, survivorship bias, overfitting, and signal decay — each needs an explicit control.
- Start simple (linear/factors), benchmark honestly, and add complexity only where it demonstrably improves out-of-sample economics.
