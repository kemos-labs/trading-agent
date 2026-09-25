"""quantkit — Phase 2 core toolkit.

Reusable Python modules built from the Phase 1 knowledge base and skills.
Each module pairs with a matching skill file in ``skills/``.

Modules
-------
data_loader : market-data loading, split/dividend adjustment, returns,
    bar resampling, outlier flags (skill: ``skills/data-loader``).
backtest : two-tier backtesting — vectorized first pass, bar-by-bar
    engine, performance metrics (skill: ``skills/backtesting-framework``).
options : BSM prices, Greeks, put-call parity, implied volatility
    (skill: ``skills/options-pricing``).
sizing : Kelly + Carver volatility-targeted position sizing
    (skills: ``skills/kelly-position-sizing``,
    ``skills/volatility-targeted-position-sizing``).
strategies : leakage-safe trend targets — dual SMA, Donchian, vol-targeted
    momentum (skill: ``skills/trend-following``).
live : yfinance polling adapter — validated stores, gap detection, fail-closed
    (skill: ``skills/live-paper``).
paper : paper-trading runtime — close-decided/next-bar-executed, cost-aware,
    journaled, no real orders (skill: ``skills/live-paper``).
validation : purged K-Fold / CPCV + PSR/DSR — leakage-free CV for
    overlapping labels (skill: ``skills/purged-cross-validation``).
factors : IC / quantile-spread factor screening — winsorize/z-score/
    neutralize + Spearman IC + decile spreads (skill: ``skills/alpha-factor-evaluation``).
features : FFD, CUSUM, triple-barrier, entropy — AFML feature lab
    (skill: ``skills/alpha-factor-evaluation`` / ``purged-cross-validation``).
portfolio : HRP, risk parity, mean-variance — PortfolioLab
    (skill: ``skills/portfolio-optimization``).
risk : VaR/cVaR, stress, scenarios, downside — MRA risk lab
    (skill: ``skills/risk-metrics`` / ``stress-testing``).
execution : spread / impact / illiquidity — execution lab
    (skill: ``skills/spread-decomposition`` / ``automated-market-making``).
tsa : ARMA/GARCH, cointegration, Kalman, HMM — time-series lab
    (skill: ``skills/arma-garch-modeling`` / ``cointegration-testing`` / ``kalman-filter-pairs`` / ``hmm-regime-detection``).
xsec : cross-sectional formation/decile/WML/overlapping sorts + residual
    score — Phase 8 T1 µ-models lab (skills: ``skills/intermediate-momentum``
    / ``skills/residual-reversal`` / ``skills/factor-zoo-hurdle``).
"""

__version__ = "0.8.0"

from quantkit import backtest, data_loader, execution, factors, features, fresh, live, options, paper, portfolio, risk, sizing, strategies, tsa, validation, xsec
from quantkit.backtest import (  # noqa: F401
    BacktestEngine,
    annualized_return,
    annualized_sharpe,
    drawdown_duration,
    mar_ratio,
    max_drawdown,
    performance_summary,
    vectorized_backtest,
)
from quantkit.data_loader import (  # noqa: F401
    OHLCV,
    adjust_prices,
    compute_returns,
    flag_outliers,
    load_csv,
    load_yfinance,
    normalize_columns,
    to_bars,
)
from quantkit.options import (  # noqa: F401
    bs_greeks,
    bs_price,
    call_from_put,
    implied_vol,
    put_call_parity,
    put_from_call,
)
from quantkit.sizing import (  # noqa: F401
    carver_position,
    cash_vol_target,
    discrete_kelly,
    instrument_value_volatility,
    kelly_fraction,
    subsystem_position,
    vol_target_weight,
    volatility_scalar,
)
from quantkit.strategies import (  # noqa: F401
    donchian_breakout_position,
    dual_sma_position,
    vol_targeted_momentum_position,
)
from quantkit.fresh import (  # noqa: F401
    ALPHAVANTAGE_FREE_DAILY,
    FINNHUB_SOFT_DAILY,
    MASSIVE_FREE_DAILY,
    QuotaLedger,
    fetch_alphavantage_daily,
    fetch_finnhub_quote,
    fetch_massive_aggs,
    load_terminal_keys,
    normalize_massive,
    pull_symbol,
)
from quantkit.factors import (  # noqa: F401
    information_coefficient,
    neutralize,
    pure_factor_returns,
    quantile_spread,
    winsorize,
    zscore,
)
from quantkit.validation import (  # noqa: F401
    CPCV,
    PurgedKFold,
    deflated_sharpe,
    probabilistic_sharpe_ratio,
)
from quantkit.features import (  # noqa: F401
    cusum_filter,
    fractional_diff,
    get_weights,
    plug_in_entropy,
    triple_barrier_labels,
)
from quantkit.portfolio import (  # noqa: F401
    bayes_stein_means,
    combine_with_1n,
    equal_weight,
    fundamental_law_ir,
    hrp_weights,
    ledoit_wolf_shrinkage,
    max_sharpe_weights,
    min_variance_weights,
    risk_parity_weights,
    transfer_coefficient,
)
from quantkit.risk import (  # noqa: F401
    bond_duration_convexity,
    cholesky_scenarios,
    downside_deviation,
    historical_cvar,
    historical_var,
    parametric_var,
    sortino_ratio,
    stress_covariance,
    var_backtest_kupiec,
)
from quantkit.execution import (  # noqa: F401
    almgren_impact,
    amihud_illiquidity,
    effective_spread,
    kyle_lambda,
    quoted_spread,
    realized_spread,
    roll_spread,
    variance_ratio,
)
from quantkit.tsa import (  # noqa: F401
    adfuller_pvalue,
    coint_pvalue,
    garch_forecast,
    hmm_regimes,
    kalman_hedge_ratio,
)
from quantkit.xsec import (  # noqa: F401
    formation_returns,
    overlapping_weights,
    quantile_assign,
    residual_score,
    wml_weights,
)

__all__ = [
    "ALPHAVANTAGE_FREE_DAILY",
    "BacktestEngine",
    "CPCV",
    "FINNHUB_SOFT_DAILY",
    "MASSIVE_FREE_DAILY",
    "OHLCV",
    "PurgedKFold",
    "QuotaLedger",
    "adfuller_pvalue",
    "adjust_prices",
    "almgren_impact",
    "amihud_illiquidity",
    "annualized_return",
    "annualized_sharpe",
    "backtest",
    "bayes_stein_means",
    "bond_duration_convexity",
    "bs_greeks",
    "bs_price",
    "call_from_put",
    "carver_position",
    "cash_vol_target",
    "cholesky_scenarios",
    "coint_pvalue",
    "combine_with_1n",
    "compute_returns",
    "cusum_filter",
    "data_loader",
    "deflated_sharpe",
    "discrete_kelly",
    "donchian_breakout_position",
    "downside_deviation",
    "drawdown_duration",
    "dual_sma_position",
    "effective_spread",
    "equal_weight",
    "execution",
    "factors",
    "features",
    "fetch_alphavantage_daily",
    "fetch_finnhub_quote",
    "fetch_massive_aggs",
    "flag_outliers",
    "formation_returns",
    "fractional_diff",
    "fresh",
    "fundamental_law_ir",
    "garch_forecast",
    "get_weights",
    "historical_cvar",
    "historical_var",
    "hmm_regimes",
    "hrp_weights",
    "implied_vol",
    "information_coefficient",
    "instrument_value_volatility",
    "kalman_hedge_ratio",
    "kelly_fraction",
    "kyle_lambda",
    "ledoit_wolf_shrinkage",
    "live",
    "load_csv",
    "load_terminal_keys",
    "load_yfinance",
    "mar_ratio",
    "max_drawdown",
    "max_sharpe_weights",
    "min_variance_weights",
    "neutralize",
    "normalize_columns",
    "normalize_massive",
    "options",
    "overlapping_weights",
    "paper",
    "parametric_var",
    "performance_summary",
    "plug_in_entropy",
    "portfolio",
    "probabilistic_sharpe_ratio",
    "put_call_parity",
    "put_from_call",
    "pull_symbol",
    "pure_factor_returns",
    "quantile_assign",
    "quantile_spread",
    "quoted_spread",
    "realized_spread",
    "residual_score",
    "risk",
    "risk_parity_weights",
    "roll_spread",
    "sizing",
    "sortino_ratio",
    "strategies",
    "stress_covariance",
    "subsystem_position",
    "to_bars",
    "transfer_coefficient",
    "triple_barrier_labels",
    "tsa",
    "validation",
    "var_backtest_kupiec",
    "variance_ratio",
    "vectorized_backtest",
    "vol_target_weight",
    "vol_targeted_momentum_position",
    "volatility_scalar",
    "winsorize",
    "wml_weights",
    "xsec",
    "zscore",
]
