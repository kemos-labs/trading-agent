# Chapter 2 — Building the Foundation: Python Basics for Finance

## Core idea
Environment setup and the Python fundamentals a financial analyst needs:
IDE choice, Anaconda/conda, version selection, and the core syntax and
libraries (pandas, NumPy, Matplotlib, datetime).

## Environment
- **IDEs**: Jupyter Notebooks (narrative + code + visuals — ideal for
  exploratory analysis), Spyder (MATLAB-like, variable explorer), PyCharm
  (professional development).
- **Anaconda**: pre-packaged scientific libraries, conda package manager,
  cross-platform. Miniconda and PyEnv as leaner alternatives.
- **Setup pattern**:
  ```bash
  conda create -n finance_project python=3.8
  conda activate finance_project
  conda install pandas numpy matplotlib
  ```
- **Python 3.8+** recommended (Python 2 EOL Jan 2020); 3.8 adds the walrus
  operator, positional-only args.

## Core libraries for finance
- **pandas**: time-series and tabular data (DataFrame/Series).
- **NumPy**: multi-dimensional arrays and numerical math.
- **Matplotlib/Seaborn**: static visualization.
- **SciPy/statsmodels**: statistical operations and tests.
- **scikit-learn/TensorFlow**: ML (ch7).
- Specialized: QuantLib (derivatives), Zipline (backtesting).

## Language basics
- Variables, types, arithmetic, strings, booleans, control flow, functions.
- Data structures: lists, tuples, dicts, sets.
- File I/O, working with dates (`datetime`, `timedelta`).

## Financial patterns shown
- Rolling averages on price series:
  ```python
  df['30_day_MA'] = df['Close'].rolling(window=30).mean()
  ```
- Date math for scheduling (payment dates, expiries):
  ```python
  from datetime import datetime, timedelta
  next_payment = datetime.now() + timedelta(days=90)
  ```

## Pitfalls
- Dependency conflicts — always isolate projects in conda environments.
- Version pinning matters: library compatibility varies by Python version.
- IDE choice affects workflow: notebooks for exploration, IDEs for
  production code.

## The analyst's daily loop
1. Activate the project environment (`conda activate finance_project`).
2. Load data with pandas (`read_csv` with `parse_dates=True`).
3. Derive features with rolling/date operations; inspect with plots.
4. Iterate in Jupyter; promote stable code into .py modules for reuse.
5. Pin versions and document the environment so the analysis reproduces.

## Bottom line
The setup + primer chapter. The environment pattern (conda env → install
stack → Jupyter) is the same four-layer idea as
`knowledge/python-for-finance/ch02`; the rolling-window idiom recurs
throughout the time-series chapters.
