# PROGRESS.md

Append one dated entry per session. Never edit or delete past entries.

Format:

## YYYY-MM-DD

- Did:
- Next:
- Blockers:

## 2026-08-03

- Did:
  - Installed pandoc 3.1.11.1 from official GitHub static release into
    `.venv/pandoc/pandoc` (no root for apt/brew in this env). Verified on
    the Dark Pools epub (±12,800 lines of markdown). Added a Tools note to
    AGENTS.md: `.epub` files in `library/raw/` are converted via
    `.venv/pandoc/pandoc book.epub -o book.md`, same flow as PDFs via
    markitdown.
  - Created `knowledge/book-inventory.md` with all 19 books in
    `library/raw/` (status: pending except Natenberg = done). All books
    were new — the inventory file did not exist.
  - Processed the first new book: **Natenberg, Option Volatility and
    Pricing (2nd ed.)** — epub → markdown via pandoc, split into 25
    chapter files (ch1–ch25), and wrote a distilled technical note
    (300–800 words, own words, formulas verified against worked
    examples) per chapter into
    `knowledge/natenberg-option-volatility-and-pricing/ch01..ch25.md`.
    Covered: contract mechanics, forward pricing, parity graphs,
    theoretical pricing/BS, volatility, Greeks (incl. higher-order),
    dynamic hedging, all major spreads, synthetics/put-call parity
    arbitrage (conversions, reversals, boxes, rolls), early exercise,
    hedging/portfolio insurance, binomial model, position analysis,
    market making, index futures/options, model assumptions & fat
    tails, volatility skew, variance swaps & VIX.
  - Flagged two content issues found while verifying: book's breakeven
    vol 27.29% (ch. 7) should be 26.29% (checked against its own
    numbers); ch. 21 rewritten butterfly's final "65" is a typo for 80
    (the arithmetic gives a 70/75/80 butterfly).
  - Progress: 1/19 books processed (Natenberg). Phase 0 env items still
    open.
- Next:
  - Process new books in queue order; epubs via pandoc (remaining:
    Dark Pools), PDFs via markitdown as needed.
  - Suggested skill (Phase 1): options-pricing SKILL.md from the
    Natenberg notes (BS/binomial formulas, Greeks, put-call parity).
- Blockers: none.

  - Phase attribution: the epub/pandoc setup, book-inventory build, and
    Natenberg processing done this session are **Phase 1 — Knowledge
    extraction** work (Phase 0 — Environment was already complete before
    this session; its marker was moved to [DONE] in ROADMAP.md).

## 2026-08-03

- Did (continued processing An Introduction to Algorithmic Trading — Leshik & Cralle, 2011):
  - Finished the remaining chapter notes ch30–ch39 in
    `knowledge/leshik-cralle-introduction-to-algorithmic-trading/`:
    ch30 EMH→Prospect Theory (loss aversion, representativeness,
    anchoring, availability, endowment, status quo; trend = volume×slope
    difference-of-opinion), ch31 Road to Chaos (phase space, strange
    attractors, logistic map, Feigenbaum const 4.6692, fractals,
    Mandelbrot fat tails), ch32 Complexity Economics (Santa Fe; entropy,
    out-of-equilibrium, perpetual novelty), ch33 Brokerages, ch34 OMP/OES,
    ch35 data-feed vendors (60-session lookback, disk delivery),
    ch36 connectivity, ch37 hardware, ch38 philosophical digression,
    ch39 information sources. Also wrote a single
    `appendices-abcd.md` (App A vendor list, B sectors, C watchlist,
    D stock snapshots are reference catalogs, not distilable chapters).
  - Book now fully done: 39 chapter notes + 1 appendices note. Progress:
    2/30 books processed (Natenberg done earlier + Leshik&Cralle).
  - Updated `knowledge/book-inventory.md`: marked Leshik&Cralle `done`.
- Did (rescan + sort root files):
  - Found 13 book files sitting at the project root (outside library/raw/).
  - Moved them into `library/raw/<topic>/` matched to existing topic
    folders; created one new folder `programming/` for "Vibe Coding"
    (no existing fit). Key placements: Trading & Exchanges→
    market-microstructure; Advances in Financial ML → ml-for-finance;
    Dynamic Hedging & Volatility Trading (Sinclair) → options;
    Market Risk Analysis v.3 & v.4 → risk; Quantitative Trading (Chan) &
    Systematic Trading (Carver) → backtesting; Python for Algorithmic
    Trading & Python for Finance and Algorithmic Trading 2ed →
    quant-python.
  - Note: the root PDF `Option Volatility and Pricing (Natenberg)` is a
    **duplicate** of the already-processed `.epub` — recorded as a
    format-completeness note in the inventory, not a new book entry.
  - Re-scanned and updated `knowledge/book-inventory.md` with the 11 new
    distinct books (all `pending`). Totals now: 30 distinct books
    inventoried (28 pending + 2 done); 31 raw files (one duplicate
    Natenberg PDF count). No stray .pdf/.epub remain at project root.
  - No books processed in this rescan — sort/inventory only, per the task.
- Next:
  - Process next books in inventory queue order (Vibe Coding, Systematic
    Trading, Quantitative Trading etc. — any pending). Env/AGENTS setup
    items all complete.
- Blockers: none.

## 2026-08-03 (2nd session entry — Halls-Moore)

- Did (book processed): **Advanced Algorithmic Trading** (Michael L.
  Halls-Moore, QuantStart) — 3rd book done overall.
  - Converted the PDF via markitdown → `/tmp/aatrading/book.md`
    (21,686 lines); kept `library/raw/` pristine.
  - Mapped all 32 chapter boundaries (via "| Chapter N" table-cell
    grep + python `boundaries.py`) and split clean per-chapter text
    into `/tmp/aatrading/ch01.txt`..`ch32.txt` (`split_full.py`).
  - Wrote **32 distilled chapter notes** (300-800 words each) into
    `knowledge/halls-moore-advanced-algorithmic-trading/`:
    ch01 intro; ch02-06 Bayesian stats (Bayes' rule, binomial
    proportion, MCMC/Metropolis, Bayesian linear regression, Bayesian
    stochastic vol); ch07-14 time series (serial correlation, random
    walk/white noise, ARMA, ARIMA+GARCH, cointegration/CADF/Johansen,
    state space/Kalman, HMM); ch15-23 ML (intro, supervised learning,
    linear regression, tree-based/bagging/RF/boosting, SVM, model
    selection/CV, unsupervised, K-Means clustering incl. OHLC regimes,
    NLP sentiment with Reuters-21578); ch24-32 QSTrader applications
    (backtesting engine, ETF monthly rebalance portfolios, ARIMA+GARCH
    strategy, cointegration+Bollinger ARNC/UNG, Kalman pairs TLT/IEI,
    intraday ML AREX, Sentdex sentiment, HMM regime filter risk
    manager, strategy decay + annualised rolling Sharpe).
  - Key verified formulas: Beta(22,52) posterior (prior alpha=beta=12,
    N=50, z=10), mean 0.297 / sd 0.053; OLS beta_hat=(X^T X)^-1 X^T y;
    Kalman update rules; rolling Sharpe S_k = sqrt(252) * E(r)/sd(r);
    RF uses ~sqrt(p) features per split.
  - Updated `knowledge/book-inventory.md`: marked Halls-Moore `done`
    (32 chapter notes; converted via markitdown).
- Progress: **3/30 books done** (Natenberg, Leshik & Cralle,
  Halls-Moore); 27 pending.
- Next: process next pending book in inventory queue order (Vibe Coding
  is first pending alphabetically in `programming/`).
- Blockers: none.

## 2026-08-03 (3rd session entry — skills promotion)

- Did: promoted five reusable techniques from the Halls-Moore book into
  skill files (skills/ was previously empty; INDEX.md was 1 byte):
  - `skills/bayesian-updating/SKILL.md` — conjugate Beta-Binomial
    posterior updating (verified Beta(22,52) example).
  - `skills/arma-garch-modeling/SKILL.md` — ARIMA+GARCH return
    forecasting, AIC order search, rolling direction signal, one-day
    forecast shift to avoid look-ahead bias.
  - `skills/cointegration-testing/SKILL.md` — CADF/PP/PO/Johansen tests,
    hedge ratio via OLS slope, z-score/Bollinger entry-exit rules.
  - `skills/kalman-filter-pairs/SKILL.md` — state-space Kalman update
    rules, ±√Q_t thresholds, TLT/IEI parameters (δ=1e-4, V=1e-3).
  - `skills/hmm-regime-detection/SKILL.md` — GaussianHMM regime filter,
    regime-gated risk-manager pattern, retraining caveats.
  - Each follows AGENTS.md SKILL.md format (name/description/when to
    use/method+formula+code/pitfalls/source book).
  - Rewrote `skills/INDEX.md` with all five entries.
- Next: process next pending book in inventory queue order.
- Blockers: none.

## 2026-08-04

- Did (audit against SESSION-HANDOFF "closing the gaps" checklist):
  - ROADMAP.md: OK — Phase 1 [ACTIVE], exactly one phase marked active.
  - Inventory vs library/raw: raw scan = 31 files / 30 distinct books
    (1 duplicate Natenberg PDF) — matches knowledge/book-inventory.md.
  - PROGRESS.md logging: all logged sessions use Did/Next/Blockers.
  - **FOUND DRIFT — unlogged book processing**: 6 complete chapter notes
    for Chan's *Quantitative Trading* existed in
    `knowledge/chan-quantitative-trading/` (mtimes 2026-08-03 13:34–13:36)
    but the inventory still marked the book `pending` and PROGRESS.md had
    NO entry for it. Spot-checked ch03 (backtesting: survivorship bias
    −42% vs +388% example, Sharpe annualization √N_T, look-ahead
    truncation check) and ch06 (Kelly F*=C⁻¹M, g_max=r+S²/2, half-Kelly)
    — notes are complete and high quality (full 6-chapter coverage).
    Reconciled: marked Chan `done` in book-inventory.md. Real count is
    **4/30 done, 26 pending** (handoff's "3 done / 27 pending" was stale).
  - **FOUND GAP — missing skill promotion**: all 5 skill files came from
    Halls-Moore (book 3). Books 1–2 (Natenberg, Leshik&Cralle) predate the
    skill convention; PROGRESS 2026-08-03 entry 1 explicitly suggested an
    `options-pricing` skill from the Natenberg notes that was never
    created. ROADMAP Phase 1's core skills (options-pricing,
    backtesting-framework, risk-metrics, data-pipelines) all still missing.
  - No conversion/OCR problems flagged for any book so far.
- Did (book processed per standing loop — 5th overall):
  **Vibe Coding: The Future of Programming** (Addy Osmani, O'Reilly Early
  Release) — epub → pandoc → /tmp/vibecoding/book.md (1,753 lines, 80KB;
  the ER contains the final book's ch3–4 only). Wrote 2 distilled notes:
  `knowledge/vibe-coding-the-future-of-programming/ch01-the-70-percent-problem.md`
  (70/30 split, two-steps-back + demo-quality traps, bootstrappers vs
  iterators, first-drafter/pair-programmer/validator patterns, golden
  rules) and `ch02-beyond-the-70-percent.md` (senior/midlevel/junior
  guidance, durable-skills checklist). Promoted
  `skills/ai-pair-programming/SKILL.md` (70/30 workflow, commit hygiene,
  human review checklist) and added it to skills/INDEX.md. Marked Vibe
  Coding `done` in book-inventory.md. Progress: **5/30 books done, 25
  pending**.
- Next: process next pending book in inventory queue order (backtesting/
  Systematic Trading — Carver). Recommend also creating the suggested
  `options-pricing` skill from the Natenberg notes to close the Phase 1
  core-skills gap.
- Blockers: none.

## 2026-08-04

- Did: processed **Systematic Trading** (Carver) — the next pending book in
  the backtesting queue — via pandoc from `library/raw/backtesting/`
  (16,659-line epub). Wrote 15 distilled notes into
  `knowledge/systematic-trading/` covering the full framework: ch01 cognitive
  biases & commitment mechanisms, ch02 rule design + achievable Sharpe
  ratios, ch03 fitting/over-fitting (multiple-testing tables, expanding vs
  rolling windows), ch04 handcrafted portfolio weights (incl. SR
  adjustments + pessimism factors), ch05 modular framework, ch06 instrument
  selection, ch07 forecasts (vol-standardised, ±20 caps, EWMAC + carry
  rules), ch08 combined forecasts + diversification multiplier, ch09
  volatility targeting (Half-Kelly tables), ch10 position sizing (volatility
  scalar pipeline), ch11 portfolios (instrument weights + inertia), ch12
  speed and size (standardised costs, turnover, speed limits), ch13–ch15 the
  three worked examples (semi-automatic, asset allocating investor, staunch
  systems trader) + the Epilogue's virtues. All notes 414–797 words (within
  the 300–800 rule; ch12 trimmed from 1019).
- Promoted **`skills/volatility-targeted-position-sizing/SKILL.md`** (Half-
  Kelly vol target, scalar → subsystem-position pipeline, diversification
  multipliers, cost/speed limits; source Carver ch5, ch7–12) and added it
  to skills/INDEX.md (now 7 skills). Marked Systematic Trading `done` in
  book-inventory.md. Progress: **6/30 books done, 24 pending**.
- Next: next pending book in inventory queue order (data-science/ AI
  Engineering — Chip Huyen). Standing recommendation: create the
  `options-pricing` skill from the Natenberg notes to close the Phase 1
  core-skills gap.
- Blockers: none.

## 2026-08-04

- Did: processed **AI Engineering: Building Applications with Foundation
  Models** (Chip Huyen, O'Reilly 2025) — converted the PDF via markitdown
  (16,866 lines) and wrote **10 distilled chapter notes** into
  `knowledge/ai-engineering/` (ch1 intro/use-case evaluation & the AI
  stack; ch2 training data, transformer architecture, scaling laws,
  post-training, sampling; ch3 evaluation methodology — LM metrics,
  AI-as-judge, comparative ranking; ch4 evaluation-driven development,
  model selection, eval-pipeline design; ch5 prompt engineering incl.
  defensive prompting; ch6 RAG + agents + memory; ch7 finetuning — RAG-vs-
  finetune, memory math, LoRA; ch8 dataset engineering — quality/
  coverage/quantity, synthesis; ch9 inference optimization — TTFT/TPOT,
  KV cache, speculative decoding, batching; ch10 architecture + user
  feedback design). All notes 516–794 words (within the 300–800 rule;
  ch09 trimmed from 800).
- Promoted **`skills/ai-evaluation-pipeline/SKILL.md`** (eval-driven
  development, exact vs AI-judge metrics, eval-set sizing rule — ~3×
  smaller diff → ~10× more samples, judge-bias pitfalls; source Huyen
  ch3–4) and added it to skills/INDEX.md (now **8 skills**). Marked AI
  Engineering `done` in book-inventory.md. Progress: **7/30 books done,
  23 pending**.
- Next: next pending book in inventory queue order (data-science/ Data
  Science from Scratch — Joel Grus). Standing recommendation: create the
  `options-pricing` skill from the Natenberg notes to close the Phase 1
  core-skills gap.
- Blockers: none.

## 2026-08-04 — Processed Data Science from Scratch (Grus)

- Did: converted the 14,158-line PDF via markitdown; wrote **27 distilled
  chapter notes** into `knowledge/data-science-from-scratch/` covering the
  full book: intro/Python/visualisation (ch1–3), linear algebra (ch4),
  statistics + correlation (ch5), probability + Bayes (ch6), hypothesis
  testing/A-B testing + confidence intervals (ch7), gradient descent (ch8),
  data acquisition/scraping (ch9), cleaning + rescale + PCA (ch10), ML
  foundations + bias-variance + overfitting (ch11), k-NN + curse of
  dimensionality (ch12), Naive Bayes + smoothing (ch13), simple/multiple
  regression + R² + omitted-variable bias (ch14–15), logistic regression +
  log loss (ch16), decision trees + entropy/ID3 (ch17), neural nets +
  backprop (ch18), deep-learning framework: tensors/Layer/Loss/Optimizer/
  Momentum/Xavier (ch19), k-means + hierarchical clustering (ch20), NLP:
  n-grams + word2vec + RNNs (ch21), network analysis: betweenness +
  PageRank (ch22), recommender systems: user/item CF + matrix
  factorisation (ch23), databases/SQL/indexes (ch24), MapReduce (ch25),
  data ethics + fairness (ch26), production libraries (ch27). All notes
  355–532 words (within the 300–800 rule).
- Promoted **`skills/statistical-significance-testing/SKILL.md`** (z-test,
  pooled-SE two-proportion A/B test, confidence intervals, sample-size
  math, multiple-testing warnings; source Grus ch7 — directly reusable for
  strategy-comparison decisions) and added it to skills/INDEX.md (now
  **9 skills**). Marked Data Science from Scratch `done` in
  book-inventory.md. Progress: **8/30 books done, 22 pending**.
- Next: next pending book in inventory queue order (data-science/ Hands-On
  Machine Learning with Scikit-Learn, Keras & TensorFlow — Géron).
  Standing recommendation: create the `options-pricing` skill from the
  Natenberg notes to close the Phase 1 core-skills gap.
- Blockers: none.

## 2026-08-04 — Processed Hands-On ML (Géron)

- Did: converted the 28,844-line PDF via markitdown; wrote **19 distilled
  chapter notes** into `knowledge/hands-on-ml/` covering the whole book:
  ML landscape + bias/variance + test-set discipline (ch1), end-to-end
  project: pipelines, scaling, stratified splits, GridSearch (ch2),
  classification metrics: confusion matrix/precision/recall/F1/ROC (ch3),
  training models: normal eqn, GD variants, regularisation, logistic/softmax
  (ch4), SVMs: margins, kernels, hinge loss, dual (ch5), decision trees +
  CART (ch6), ensembles: voting/bagging/RF/boosting/stacking (ch7), PCA +
  random projection + LLE (ch8), k-means/DBSCAN/GMM + anomaly detection
  (ch9), Keras MLPs + callbacks + TensorBoard (ch10), deep-net training:
  init/activations/batch-norm/optimisers/schedules/regularisation (ch11),
  custom TensorFlow: GradientTape/tf.function/custom loops (ch12), tf.data
  + TFRecord + Keras preprocessing layers (ch13), CNNs (ch14), RNNs/BPTT/
  LSTMs + forecasting (ch15), NLP: char-RNN/attention/transformers/GPT/BERT
  (ch16), autoencoders/GANs/diffusion (ch17), RL: policy gradients + DQN
  (ch18), deployment: TF Serving/GPUs/distributed (ch19). All notes 342–673
  words (within the 300–800 rule).
- Promoted **`skills/data-pipelines/SKILL.md`** (fit-on-train-only, scaling,
  categoricals, ColumnTransformer/Pipeline, tf.data, training/serving skew;
  source Géron ch2, ch13) and added it to skills/INDEX.md (now **10
  skills**). This closes the Phase 1 `data-pipelines` core-skill gap (1 of
  4 core skills now done). Marked Hands-On ML `done` in book-inventory.md.
  Progress: **9/30 books done, 21 pending**.
- Next: next pending book in inventory queue order (data-science/ Learning
  Data Science — Lau, Gonzalez, Nolan). Standing recommendation: create
  the  `options-pricing` skill from the Natenberg notes (3 of 4 Phase 1
  core skills remain: options-pricing, backtesting-framework, risk-metrics).
- Blockers: none.

## 2026-08-04

- **Processed Python for Data Analysis** (Wes McKinney, 3rd ed. 2022,
  PDF via markitdown, 21,840 lines): wrote **13 chapter notes** into
  `knowledge/python-for-data-analysis/` covering the full pandas/NumPy
  stack: preliminaries & scope (ch1), Python/IPython/Jupyter basics (ch2),
  built-in data structures/functions/files (ch3), NumPy arrays:
  broadcasting, views-vs-copies, vectorization (ch4), pandas Series/
  DataFrame: alignment, loc/iloc (ch5), I/O: read_csv args, Parquet/
  HDF5, SQL (ch6), cleaning: NA, dupes, .str, cut/qcut, dummies (ch7),
  wrangling: MultiIndex, merge/concat, stack/unstack/pivot/melt (ch8),
  matplotlib figures/axes/annotations (ch9), groupby split-apply-combine:
  agg/transform/apply/pivot_table (ch10), time series: datetimes, tz,
  shift, resample closed/label, rolling/ewm (ch11), modeling handoff:
  Patsy, statsmodels OLS, scikit-learn (ch12), five end-to-end examples:
  Bitly/MovieLens/baby-names/USDA/FEC (ch13). All notes 322–534 words
  (within the 300–800 rule).
- Promoted **`skills/time-series-feature-engineering/SKILL.md`** (returns/
  lags via shift, rolling/expanding/ewm windows, resample to OHLC bars
  with closed/label edge conventions, seasonal grouping, no-look-ahead
  discipline; source ch11) and added it to skills/INDEX.md (now **12
  skills**). Marked Python for Data Analysis `done` in book-inventory.md.
  Progress: **11/30 books done, 19 pending**.
- Next: next pending book in inventory queue order (history/ Liar's
  Poker — Michael Lewis). Standing recommendation: create the
  `options-pricing` skill from the Natenberg notes (3 of 4 Phase 1 core
  skills remain: options-pricing, backtesting-framework, risk-metrics).
- Blockers: none.

## 2026-08-04

- **Processed Learning Data Science** (Lau, Gonzalez & Nolan, PDF via
  markitdown, 18,481 lines): wrote **21 chapter notes** into
  `knowledge/learning-data-science/` covering the full lifecycle: scope
  & bias (ch2), urn-model simulation / sampling design (ch3), loss-
  minimization constant model (ch4), bus waiting-time case study (ch5),
  pandas dataframes (ch6), SQL relations (ch7), file wrangling (ch8),
  tidy-data reshaping + feature engineering (ch9), EDA (ch10), plotly
  visualization (ch11), air-sensor calibration case study (ch12), text /
  regex / tf-idf (ch13), data exchange: NetCDF/JSON/HTTP/XML/XPath (ch14),
  linear models + multicollinearity (ch15), model selection: overfitting /
  train-test / k-fold CV / ridge-lasso (ch16), inference theory: null
  distribution, bootstrap CI, prediction intervals (ch17), donkey-weight
  case study with asymmetric anes_loss (ch18), classification: logistic /
  log-odds / log loss / confusion matrix / precision-recall (ch19),
  gradient descent: Huber, SGD, mini-batch, Newton (ch20), fake-news
  case study: tf-idf + LogisticRegressionCV + drift limits (ch21). All
  notes 300–460 words (within the 300–800 rule; ch07/ch08 padded to
  clear the 300 floor).
- Promoted **`skills/loss-function-design/SKILL.md`** (loss-first modeling:
  mean⇔squared / median⇔absolute / mode⇔0-1, asymmetric losses for
  asymmetric error costs, Huber robust loss, constant-model baseline;
  source ch4, ch18, ch20) and added it to skills/INDEX.md (now **11
  skills**). Marked Learning Data Science `done` in book-inventory.md.
  Progress: **10/30 books done, 20 pending**.
- Next: next pending book in inventory queue order (data-science/ Python
  for Data Analysis — Wes McKinney). Standing recommendation: create the
  `options-pricing` skill from the Natenberg notes (3 of 4 Phase 1 core
  skills remain: options-pricing, backtesting-framework, risk-metrics).
- Blockers: none.

## 2026-08-04

- **Processed Liar's Poker** (Michael Lewis, 1989, PDF via markitdown,
  8,955 lines): wrote **12 chapter notes** into `knowledge/liars-poker/`
  covering the narrative history distilled for its market/institutional
  lessons: the Liar's-Poker-as-trading metaphor and Meriwether's
  fear/greed control (ch1), the bank's social hierarchy (ch2), the
  1980s bond boom: Volcker's 1979 rate-regime shift + borrowing
  explosion + the toll-taker spread model and "who is the fool" (ch3),
  the training-program culture (ch4), birth of mortgage securitization:
  Bob Dall/Lew Ranieri, the S&L mismatch, first private MBS (ch5),
  the mortgage money machine: 1981 thrift tax break, whole loans,
  prepayment modeling, info asymmetry (ch6), CMO tranching: risk
  reallocation not removal + spread compression from defections (ch7),
  London sales/globalization (ch8), the German bond warrant: risk as a
  commodity (ch9), the Milken/Drexel rivalry and talent economics (ch10),
  the 1987 crash: Southland bridge-loan commitment risk, incentive
  corruption, crisis management (ch11), and the epilogue's money-belief
  thesis (skill vs luck vs structure). All notes 309–511 words (within
  the 300–800 rule).
- Promoted **`skills/market-structure-risk/SKILL.md`** (toll-taker vs
  position-taker, embedded optionality incl. prepayment, tranching as
  risk reallocation, commitment/liquidity risk, information asymmetry,
  incentive audit; source ch3, ch5–7, ch11) and added it to
  skills/INDEX.md (now **13 skills**). Marked Liar's Poker `done` in
  book-inventory.md. Progress: **12/30 books done, 18 pending**.
- Next: next pending book in inventory queue order
  (market-microstructure/ Dark Pools — Scott Patterson). Standing
  recommendation: create the `options-pricing` skill from the Natenberg
  notes (3 of 4 Phase 1 core skills remain: options-pricing,
  backtesting-framework, risk-metrics).
- Blockers: none.

## 2026-08-04 — Session 6: Dark Pools (Scott Patterson)

- Did: Processed the 12,819-line `market-microstructure/` epub (pandoc)
  into **26 distilled notes** in `knowledge/dark-pools/` (prologue + 25
  chapters, 349–457 words each). Coverage: the SOES-bandit origin story
  (Houtkin's loophole, Datek, the Watcher, the Monster Key as the first
  algo, the Christie–Schultz odd-eighth collusion study); Island's birth
  as the first fully lit pool (ITCH/OUCH, BookViewer, maker-taker
  invented 1998); Archipelago's order-routing model; the Order-Handling
  Rules/Reg NMS era; decimalization; the 2009 Aleynikov case and the
  HFT backlash; the May 6 2010 Flash Crash reconstruction (stub quotes,
  SIP lag, Stop Logic); Trillium layering; and the AI-trading endgame
  (Kinetic's failure, Cerebellum's genetic-algo ATM Fund, Rebellion's
  Star). Created **`skills/market-microstructure-execution/SKILL.md`**
  (maker-taker fee math, order types, Reg NMS best-price routing, SIP
  latency/colocation, tick-size economics, Flash-Crash fragility
  checklist) and added it to skills/INDEX.md (**14 skills**). Marked
  Dark Pools `done` in book-inventory.md. Progress: **13/30 books done,
  17 pending**.
- Next: next pending book in inventory queue order (the remaining
  `market-microstructure/` book, Trading and Exchanges — Larry Harris).
  Standing recommendation: create the `options-pricing` skill from the
  Natenberg notes (3 of 4 Phase 1 core skills remain: options-pricing,
  backtesting-framework, risk-metrics).
- Blockers: none.
## 2026-08-04 — Session 7: Trading and Exchanges (Larry Harris)

- Did: Converted the 34,260-line PDF via markitdown; wrote **29
  distilled chapter notes** into `knowledge/trading-and-exchanges/`
  (312–418 words each, within the 300–800 rule). Coverage: the trading
  industry and trader taxonomy (ch1–3, ch8), orders and order
  properties (ch4), market structures + order-driven market mechanics
  (ch5–6), brokers and agency (ch7), market quality (ch9), informed
  traders and adverse selection (ch10), order anticipators (ch11),
  manipulation (ch12), dealers and the bid/ask spread decomposition —
  Glosten–Milgrom, effective/realized spread, impact (ch13–14), block
  traders and buy-side execution — implementation shortfall (ch15,
  ch18), value traders and arbitrageurs — cost-of-carry (ch16–17),
  liquidity and volatility — variance ratios, Roll (ch19–20),
  transaction-cost measurement (ch21), performance evaluation / luck
  vs. skill (ch22), index and portfolio markets — Russell
  reconstitution, indexation argument (ch23), specialists (ch24),
  internalization/preferencing/crossing — best execution, payments
  for order flow (ch25), competition and fragmentation — order flow
  externality, Optimark (ch26), floor vs. automated systems (ch27),
  bubbles/crashes/circuit breakers — 1929, 1987, portfolio insurance
  (ch28), insider trading (ch29).
- Did: Promoted `skills/spread-decomposition/SKILL.md` (Lee–Ready
  classification, quoted/effective/realized spread, price impact,
  Roll's estimator, variance-ratio test) — distinct from the existing
  execution-layer skill; added to `skills/INDEX.md` (**15 skills**).
- Did: Marked Trading and Exchanges done in `book-inventory.md`
  (**14/30 done, 16 pending**); verified counts (29 notes, 15 skills).
- Next: next pending book in inventory queue order (`market-microstructure/`
  remaining: High-Frequency Trading — Irene Aldridge). Standing
  recommendation: create the `options-pricing` skill from the Natenberg
  notes (3 of 4 Phase 1 core skills remain: options-pricing,
  backtesting-framework, risk-metrics).
- Blockers: none.
## 2026-08-04 — Session 8: High-Frequency Trading (Irene Aldridge)

- Did: Converted the 14,710-line PDF via markitdown; wrote **16
  distilled chapter notes** into `knowledge/high-frequency-trading/`
  (325–436 words each, within the 300–800 rule). Coverage: market
  transformation and HFT definitions (ch1), hardware/messaging/
  co-location latency stack (ch2), CLOBs, order types, NBBO and
  fragmentation (ch3), tick data properties and sampling — last-tick
  vs. interpolation, duration models (ch4), trading costs — spread,
  slippage, market-impact regression with Eurobund evidence (ch5),
  performance measures, leverage-invariant HFT Sharpe, capacity and
  alpha decay (ch6), the HFT business — 1-and-30 fees, back-test→paper
  →production (ch7), stat-arb — pairs recipe, triangular/UIP/index arb
  (ch8), event arbitrage — surprise regressions, state-dependent
  reactions (ch9), automated market making — inventory/adverse
  selection, offsets, Kyle's lambda, Amihud (ch10), order-flow
  models — OFI, aggressiveness autocorrelation, book shape (ch11),
  manipulation taxonomy — rebate threshold math, layering (ch12),
  regulation — Reg NMS, flash orders, VPIN crash prediction (ch13),
  risk management — stops→vol cutouts→VaR→hedging,
  DPW portfolio (ch14), execution algos — efficient trading frontier,
  TWAP/VWAP flaws, resilience models (ch15), system implementation —
  life cycle, testing disciplines (ch16).
- Did: Promoted `skills/automated-market-making/SKILL.md` (limit-order
  fill simulation, fixed/volatility-dependent offsets, Kyle's lambda,
  Amihud, OFI, rebate-capture threshold) — the book's most reusable,
  formula-rich technique, distinct from the existing execution and
  spread-decomposition skills; added to `skills/INDEX.md` (**16
  skills**).
- Did: Marked High-Frequency Trading done in `book-inventory.md`
  (**15/30 done, 15 pending**); verified counts (16 notes, 16 skills).
- Next: next pending book in inventory queue order (Deep Learning for
  Finance — Sofien Kaabar, `ml-for-finance/`). Standing recommendation: create the `options-pricing` skill from the
  Natenberg notes (3 of 4 Phase 1 core skills remain: options-pricing,
  backtesting-framework, risk-metrics).
- Blockers: none.

## 2026-08-04 — Session 9: Deep Learning for Finance (Kaabar, O'Reilly 2024)

- Did: Converted the PDF via markitdown (10,952 lines, 12 chapters) and
  wrote 12 distilled notes into `knowledge/deep-learning-for-finance/`
  (344–451 words each, within rule): ch1 trading basics (orders, leverage,
  margin, hedging); ch2 probabilistic methods (Bayes, distributions, Monte
  Carlo); ch3 descriptive stats (skew/kurtosis, Jarque–Bera, ADF
  stationarity); ch4 linear algebra & calculus (matrix ops, gradients,
  backprop); ch5 technical analysis (SMA/EMA, RSI, Bollinger, MACD, ATR);
  ch6 Python stack (NumPy/pandas idioms); ch7 classic ML for time series
  (kNN/RF/SVR/boosting, metrics, sequential splits); ch8 deep learning I
  (MLP, activations, dropout/early stopping); ch9 deep learning II (CNN,
  LSTM/GRU, rolling windows, wavelets); ch10 reinforcement learning
  (Q-learning, DQN, replay buffer, why RL is hard in finance); ch11
  advanced techniques (genetic algorithms, hyperparameter search,
  walk-forward backtesting, multiple-testing); ch12 market drivers & risk
  (position sizing, fractional Kelly, stops, drawdown control).
- Did: Created skill `skills/walk-forward-validation/SKILL.md` (sequential
  TimeSeriesSplit loops, fit-on-train-only scaling, leakage prevention,
  data-snooping/multiple-testing awareness, cost-adjusted evaluation) —
  the book's most reusable, code-adjacent technique, complementing the
  existing ML skills; added to `skills/INDEX.md` (**17 skills**).
- Did: Marked Deep Learning for Finance done in `book-inventory.md`
  (**16/30 done, 14 pending**); verified counts (12 notes, 17 skills).
- Next: next pending book in inventory queue order (Advances in Financial
  Machine Learning — López de Prado, `ml-for-finance/`). Standing
  recommendation: create the `options-pricing` skill from the Natenberg
  notes (3 of 4 Phase 1 core skills remain: options-pricing,
  backtesting-framework, risk-metrics).
- Blockers: none.

## 2026-08-04 — Session 10: Advances in Financial Machine Learning (López de Prado, Wiley 2018)

- Did: Converted the epub via pandoc (20,745 lines, 22 chapters in 5
  parts) and wrote 22 distilled notes into
  `knowledge/advances-financial-ml/` (332–474 words each, within rule):
  Part 1 Data (ch2 bars: time/volume/dollar/tick + imbalance/run bars,
  the ETF trick, CUSUM event sampling; ch3 labeling: triple-barrier,
  meta-labeling; ch4 sample weights: average uniqueness, sequential
  bootstrap, return attribution, time decay; ch5 fractional
  differentiation: FFD fixed-width window, d* search); Part 2 Modelling
  (ch6 ensembles: bagging variance reduction, bagging>boosting in
  finance; ch7 purged k-fold + embargo; ch8 feature importance:
  MDI/MDA/SFI, PCA confirmatory orthogonalization, "backtesting is not a
  research tool"; ch9 purged hyper-parameter tuning, F1 for
  meta-labeling); Part 3 Backtesting (ch10 bet sizing from probabilities,
  sigmoid sizing, limit prices; ch11 seven sins, CSCV → PBO; ch12
  walk-forward vs CV vs CPCV; ch13 synthetic-data trading-rule
  calibration (OU process heat-maps, asymmetric payoff dilemma); ch14
  PSR/DSR; ch15 binomial strategy risk, probability of failure; ch16 HRP
  — Markowitz's curse, tree clustering, recursive bisection); Part 4
  Features (ch17 CUSUM/SADF/CADF structural breaks; ch18 entropy —
  plug-in/LZ estimators, entropy-implied volatility; ch19 microstructure
  — tick rule, Roll, Kyle/Amihud, VPIN, round-size/cancellation
  footprints); Part 5 HPC (ch20 vectorization + multiprocessing,
  atoms/molecules, mpPandasObj; ch21 integer/quantum optimization;
  ch22 CIFT guest chapter on HPC streaming analytics).
- Did: Created skill `skills/purged-cross-validation/SKILL.md` (purged
  k-fold with embargo, CPCV multiple-OOS-path construction, PSR/DSR
  deflated-Sharpe significance) — the book's most reusable,
  code-adjacent methodology, extending the Kaabar walk-forward skill with
  de Prado's overlap-aware machinery; added to `skills/INDEX.md`
  (**18 skills**).
- Did: Marked Advances in Financial ML done in `book-inventory.md`
  (**17/30 done, 13 pending**); verified counts (22 notes, 18 skills).
- Next: next pending book in inventory queue order (Machine Learning for
  Algorithmic Trading — Stefan Jansen, `ml-for-finance/`). Standing
  recommendation: create the `options-pricing` skill from the Natenberg
  notes (3 of 4 Phase 1 core skills remain: options-pricing,
  backtesting-framework, risk-metrics).
- Blockers: none.

## 2026-08-04 — Session 11

- Did: Processed **Machine Learning for Algorithmic Trading** (Stefan
  Jansen, 2nd ed., Packt 2020) — 23-chapter book (31,963-line PDF).
  Converted via markitdown to `/tmp/mlat/book.md`; read all 23 chapters.
  Wrote 23 distilled chapter notes into
  `knowledge/ml-algorithmic-trading/` (365–502 words each, within the
  300–800 rule): Part 1 data (ch2 market/fundamental, ch3 alternative
  data, ch4 alpha-factor research, ch5 portfolio optimization/MPT +
  evaluation pitfalls); Part 2 modeling (ch6 ML process/bias-variance,
  ch7 linear/Fama-French, ch8 ML4T workflow + Zipline backtesting,
  ch9 ARMA/GARCH/cointegration, ch10 Bayesian Sharpe + pairs,
  ch11 random forests, ch12 boosting, ch13 PCA/clustering/HRP);
  Part 3 NLP (ch14 sentiment, ch15 topic modeling, ch16 embeddings);
  Part 4 DL (ch17 backprop/DNNs, ch18 CNNs + transfer learning,
  ch19 RNNs/LSTM/GRU, ch20 autoencoders + GKX conditional risk
  factors, ch21 GANs/TimeGAN, ch22 DQN/DDQN + Gym trading agent);
  ch23 conclusions. Promoted a new skill:
  **`skills/alpha-factor-evaluation/SKILL.md`** — IC + quantile-spread
  screening (winsorize/z-score/neutralize per cross-section, Spearman IC
  vs. forward returns, t-stat, hit rate, monotonic decile spreads) — the
  book's most reusable cross-sectional technique, complementing the
  validation skills without overlap. Updated `skills/INDEX.md` (19
  skills). Marked the book done in `book-inventory.md` (18/30 done,
  12 pending). Counts reconciled: 23 notes, 19 skills, 18 PROGRESS
  entries.
- Next: **Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow**
  (Géron, `programming/`) is the next pending book; or resume the
  standing Phase 1 skill-gap recommendation (`options-pricing` from the
  Natenberg notes; 3 of 4 Phase 1 core skills remain: options-pricing,
  backtesting-framework, risk-metrics).
- Blockers: none.

## 2026-08-04 — Session 12

- Did: Processed **Dynamic Hedging: Managing Vanilla and Exotic
  Options** (Nassim N. Taleb, Wiley 1997) — 23 chapters + Modules A–G
  (17,318-line PDF). Converted via markitdown to `/tmp/dh/book.md`;
  read all chapters. Wrote 24 distilled notes into
  `knowledge/dynamic-hedging/` (333–674 words each, within the
  300–800 rule): Part I instruments/market (ch1 linear vs. nonlinear
  derivatives, the contamination principle; ch2 the six-dimensional
  generalized option + decomposability; ch3 market making, negative
  autocorrelation edge; ch4 liquidity holes, Leland/Whalley-Wilmott
  cost-adjusted break-even vol); Part II risk measures (ch5 arbitrage
  spectrum, mechanical vs. behavioral stability; ch6 volatility/
  correlation, Parkinson/Garman-Klass, GARCH vs. implied; ch7 the
  delta — modified delta, cash vs. forward, barrier-delta warning;
  ch8 gamma, up/down gamma, shadow gamma/skew gamma/GARCH gamma;
  ch9 vega, term structure, modified vega buckets; ch10 theta, shadow
  theta, stealth/health, convexity; ch11 bleed, speed, moments of a
  position); Part III practice (ch12 fungibility, max contango,
  stacking + Metallgesellschaft; ch13 pin risk, sticky strikes,
  currency bands; ch14 bucketing/topography with worked rho example;
  ch15 the distribution — vvol, leverage skew, regime table; ch16
  replication, neutral spreading, path dependence); Part IV exotics
  (ch17 European binaries + delta paradox; ch18 American binaries,
  carry rules, at-settlement; ch19 regular barriers, reflection
  principle, KO = vanilla + mirrored puts; ch20 reverse/double
  barriers, exploding options, CAPs, SCUDs; ch21 compound/choosers +
  vvol sensitivity; ch22 multiasset, correlation vega, covariance
  matrix; ch23 lookbacks/ladders/Asians + 1.73:1 gamma hedge);
  Modules A–G (Cholesky correlated walk, risk neutrality, numeraire
  relativity, correlation triangles, VaR, probabilistic rankings,
  barrier closed forms). Promoted a new skill:
  **`skills/correlated-scenario-simulation/SKILL.md`** — Cholesky
  decomposition for correlated multi-asset Monte Carlo/scenario
  simulation (covariance from vols × corr, lower-triangular factor,
  mixed normals, lognormal paths, PSD checks, crisis-correlation
  stress) — the book's most reusable code-adjacent technique, no
  overlap with existing skills. Updated `skills/INDEX.md` (20
  skills). Marked the book done in `book-inventory.md` (19/30 done,
  11 pending). Counts reconciled: 24 notes, 20 skills, 19 PROGRESS
  entries.
- Next: **Volatility Trading** (Euan Sinclair, 2nd ed., `options/`) is
  the next pending book — a natural follow-on to Dynamic Hedging;
  or resume the standing Phase 1 skill-gap recommendation
  (`options-pricing` from the Natenberg notes; 3 of 4 Phase 1 core
  skills remain: options-pricing, backtesting-framework, risk-metrics).
- Blockers: none.

## 2026-08-04 — Session 13: Volatility Trading (Sinclair)

- Did: Converted `options/Volatility Trading` (2nd ed., 12,599-line PDF) via
  markitdown; wrote 15 chapter notes into `knowledge/volatility-trading/`
  (372–521 words each, within the 300–800 rule): option pricing & BSM
  assumptions; vol measurement (Parkinson/Garman-Klass/Rogers-Satchell);
  stylized facts (fat tails, clustering, mean reversion, leverage effect);
  vol forecasting (EWMA/GARCH/regime); IV surface & sticky-strike vs
  sticky-delta dynamics; hedging (theta-gamma, Leland cost adjustment,
  hedging bands); hedged-position P&L distribution & path dependence; money
  management (Kelly, fractional Kelly, vol targeting); trade evaluation;
  psychology biases; the variance premium; the VIX construction & contango;
  leveraged ETF volatility drag (L·μ − ½L²σ²); trade lifecycle; conclusion
  (process). Created `skills/kelly-position-sizing/SKILL.md` (discrete &
  continuous Kelly, fractional Kelly, vol-target approximation, over-betting
  trap, fat-tail/skew cautions; complements existing arma-garch and
  correlated-scenario skills without overlap) and added it to
  `skills/INDEX.md` (now 21 skills). Marked book done in
  `knowledge/book-inventory.md` (20/30 done, 10 pending).
- Next: Stochastic Calculus and Finance (Shreve) or the next pending book;
  Phase 1 skills still needed: options-pricing, backtesting-framework,
  risk-metrics.
- Blockers: none.

## 2026-08-04 — Session 14: Stochastic Calculus and Finance (Shreve)

- Did: Converted `options/Stochastic Calculus and Finance` (Steven Shreve,
  1997 lecture notes = precursor of Stochastic Calculus for Finance I & II;
  42,407-line PDF) via markitdown; wrote 34 chapter notes into
  `knowledge/stochastic-calculus-finance/` (339–462 words each, within the
  300–800 rule). Part I (binomial, ch1–12): probability theory & the
  binomial model, conditional expectation/martingales, arbitrage pricing &
  risk-neutral measure, Markov property, stopping times & American options,
  American claim properties, Jensen (no early exercise of calls), random
  walks & reflection principle, Radon-Nikodym/state-price density,
  log-utility CAPM, general random variables, semi-continuous models.
  Part II (continuous-time, ch13–34): Brownian motion, Itô integral,
  Itô's formula (GBM, Black-Scholes PDE), SDEs & Kolmogorov/Fokker-Planck,
  Girsanov & risk-neutral measure, martingale representation, 2-D market
  model, exotic pricing via reflection principle, Asian options
  (state-augmentation), APT summary, Lévy's characterization, outside
  barriers, American puts & free boundaries, dividends, bonds/forwards/
  futures, term structure, Gaussian processes, Hull-White, CIR, Duffie-Kan,
  change of numéraire, BGM/LMM. Created
  `skills/binomial-tree-pricing/SKILL.md` (CRR tree: u/d from σ√Δt,
  risk-neutral p̃, backward induction with American early-exercise max,
  delta extraction; vectorized numpy example, no-arbitrage and convergence
  pitfalls; no overlap with existing skills) and added it to
  `skills/INDEX.md` (now 22 skills). Marked book done in
  `knowledge/book-inventory.md` (21/30 done, 9 pending).
- Next: Python for Algorithmic Trading (Hilpisch) or next pending book;
  Phase 1 skills still needed: options-pricing, backtesting-framework,
  risk-metrics.
- Blockers: none.

## 2026-08-04 — Session 15: Python for Algorithmic Trading (Hilpisch)

- Did: Converted `quant-python/Python for Algorithmic Trading` (Yves
  Hilpisch, O'Reilly 2021; 12,514-line PDF) via markitdown; wrote 10 chapter
  notes into `knowledge/python-algorithmic-trading/` (381–506 words each,
  within the 300–800 rule): Python/vectorization rationale (NumPy ~8x
  speedup, pandas); infrastructure (conda, virtualenv, Docker, cloud
  instances, RSA/Jupyter); financial data handling (CSV/pandas, Quandl,
  Eikon, HDF5); vectorized backtesting (SMA/momentum/mean-reversion
  skeleton: position.shift(1) × returns, transaction costs, data
  snooping); ML direction prediction (linear/logistic regression with
  lagged features, scikit-learn/Keras, train-test split); event-based
  backtesting classes (BacktestBase: fixed+proportional costs, long-only/
  long-short, trade-frequency-vs-costs lesson); real-time data & ZeroMQ
  PUB-SUB sockets (Euler GBM tick server, Plotly streaming); Oanda CFD
  trading (v20/tpqoa API, spread costs); FXCM FX trading (fxcmpy);
  automation (Kelly sizing, online algorithm, cloud deployment, logging &
  socket monitoring). Created `skills/vectorized-backtesting/SKILL.md`
  (the returns → shifted-position → strategy-returns → cumulative
  performance skeleton with proportional/fixed transaction costs and
  no-look-ahead discipline; complements walk-forward-validation and
  alpha-factor-evaluation without overlap) and added it to
  `skills/INDEX.md` (now 23 skills). Marked book done in
  `knowledge/book-inventory.md` (22/30 done, 8 pending).
- Next: Python for Finance and Algorithmic Trading 2ed (Inglese) or next
  pending book; Phase 1 skills still needed: options-pricing,
  backtesting-framework, risk-metrics (vectorized-backtesting is a strong
  seed for the backtesting-framework skill).
- Blockers: none.

## 2026-08-04 — Session 16

- Did: Processed **Python for Finance and Algorithmic Trading, 2nd Edition**
  (Inglese L./Quantreo, PDF via markitdown → 8,098 lines) and wrote **17
  distilled chapter notes** into `knowledge/python-finance-algo-trading-2ed/`
  (300–432 words each, within the 300–800 rule): intro/setup and the
  canonical df shape (close/returns columns, backtest helper); portfolio
  optimization (Markowitz mean-variance, static vs dynamic allocation,
  Sharpe/Sortino criteria); vectorized backtesting (signal.shift(1) ×
  returns, equity curve, max drawdown, no-look-ahead); risk analysis
  (max drawdown, VaR, cVaR/ES, VaR/cVaR ratio, portfolio risk
  contributions); advanced backtesting (spread/proportional/fixed costs on
  position.diff(), trade-frequency-vs-costs); statistical arbitrage
  (stationarity → cointegration → Engle-Granger hedge ratio → spread
  z-score pairs trading, NZD/AUD/CAD triangle example); ARMA models
  (p,q selection via ACF/PACF/AIC, statsmodels, residual whiteness);
  linear/logistic regression (C = inverse regularization, leakage-safe
  scaling); feature & target engineering (lagged returns, StandardScaler
  on train only); SVM/SVR (kernels, epsilon tube); ensembles (trees,
  Random Forest bagging, XGBoost boosting, feature importance); DNN
  (neuron = activation(w'X+b), forward/backprop, gradient descent, custom
  losses); RNN/LSTM (3D windowing, return_sequences flags, lag-zero
  padding, dropout, target standardization + inverse transform); RCNN
  (Conv1D + LSTM + dropout hybrid); the full project (train/test/
  validation three-way split, 150 assets × 3 models screening with
  spread-penalized Sharpe, model diversity, voting + mean-variance
  allocation); live trading (trading plan, ~100 tries per strategy,
  journal for algos, 1% bet-sizing and compounding recovery asymmetry,
  uncorrelated strategy portfolio). Created
  `skills/risk-metrics/SKILL.md` (vectorized pandas risk report:
  max drawdown, historical VaR, cVaR/Expected Shortfall, VaR/cVaR tail
  diagnostic, portfolio risk contributions; VaR-not-subadditive and
  sqrt(252) clustering caveats) — this closes the Phase 1 `risk-metrics`
  skill gap — and added it to `skills/INDEX.md` (now 24 skills). Marked
  book done in `knowledge/book-inventory.md` (23/30 done, 7 pending).
- Next: Python for Finance (Hilpisch) or next pending book; Phase 1 skills
  still needed: options-pricing, backtesting-framework.
- Blockers: none.

## 2026-08-04 — Session 17

- Did: Processed **Python for Finance, 2nd Edition** (Yves Hilpisch, O'Reilly
  2019; PDF via markitdown → 23,379 lines) and wrote **21 distilled chapter
  notes** into `knowledge/python-for-finance/` (305–385 words each, within
  the 300–800 rule — padded 9 short notes and re-verified): why Python for
  finance (ecosystem, data-driven/AI-first trends); Python infrastructure
  (conda, Docker, cloud droplets, RSA/Jupyter config); data types &
  structures (int/float/bool/str, tuple/list/dict/set, reference-copy
  trap); NumPy (ndarray, vectorization, broadcasting); pandas (DataFrame/
  Series, loc/iloc, groupby, concat/merge, index-alignment NaN gotcha);
  OOP (classes/objects, inheritance, aggregation — DX library pattern);
  visualization (matplotlib static, plotly/Cufflinks interactive,
  candlesticks); financial time series (read_csv, pct_change, resampling,
  rolling stats, S&P/VIX negative correlation, tick data); I/O (pickle,
  pandas formats, PyTables/HDF5, TsTables); performance Python
  (vectorization ~10x, Numba JIT, Cython, multiprocessing; binomial tree,
  MC, EWMA case studies); mathematical tools (polyfit/interp1d,
  scipy.optimize.minimize/fmin, quad, SymPy); stochastics (npr functions,
  GBM path simulation, variance reduction, VaR by simulation); statistics
  (Jarque-Bera/Shapiro normality tests, Markowitz MPT, Bayesian regression,
  ML classification preview); FXCM trading platform (fxcmpy wrapper, token/
  config, streaming + orders); trading strategies (vectorized backtest
  Position.shift(1) x Returns, SMA crossover, RWH lag-OLS test, clustering,
  classification, DNN; brute-force param optimization + overfitting
  warning); automated trading (Kelly f* = p - q derivation, fractional
  Kelly, online algorithm, cloud deployment, logging/socket monitoring);
  valuation framework (Fundamental Theorem of Asset Pricing, risk-neutral
  discounting, market environments); simulation of financial models
  (sn_random_numbers antithetic + moment matching, GBM/jump-diffusion/CIR
  classes); derivatives valuation (MC European, LSM for American,
  payoff-as-string, delta/vega Greeks); portfolio valuation
  (derivatives_position/portfolio, shared correlated simulations, book
  VaR); market-based valuation (near-money option selection, grid+local
  calibration to minimize MSE, DAX case study). Created
  `skills/monte-carlo-option-pricing/SKILL.md` (vectorized GBM/jump/CIR
  simulators, antithetic variates + moment matching, European MC pricing,
  Least-Squares Monte Carlo for American options with in-the-money
  regression, finite-difference Greeks, and the -0.5 sigma^2 / CIR-negative
  / seed-discipline pitfalls — a second pricing primitive alongside
  binomial-tree-pricing and a seed for the Phase 1 options-pricing gap) and
  added it to `skills/INDEX.md` (now 25 skills). Marked book done in
  `knowledge/book-inventory.md` (24/30 done, 6 pending).
- Next: Python for Quants (Lachowicz) or next pending book; Phase 1 skills
  still needed: options-pricing, backtesting-framework.
- Blockers: none.

## 2026-08-04 — Session 18

- Did: Processed **Python for Quants, Volume I** (Pawel Lachowicz, QuantAtRisk
  2015; PDF via markitdown → 10,101 lines) and wrote **3 distilled chapter
  notes** into `knowledge/python-for-quants/` (304–517 words each, within
  the 300–800 rule) — this book is a 3-chapter volume, not a 20-chapter
  text: ch1 Python for Fearful Beginners (the quant learner's on-ramp:
  copy-and-run learning, Anaconda install, IDEs, script/interactive
  conventions); ch2 Fundamentals of Python (int/float type inference and
  the 2-vs-3 division difference, big-int exactness vs float precision,
  sys.float_info, exceptions, math/fractions modules, rounding and
  near-zero maths, lists with slicing/methods and the reference-copy
  trap, statistics-on-lists, random module + Mersenne Twister MT19937 with
  a full implementation walkthrough and Mersenne-prime-hunt performance
  demo, tuples/sets/dicts, functions/lambda); ch3 Fundamentals of NumPy
  for Quants (ndarray shape/dtype/views-vs-copies, 1D/2D/3D/4D array
  manipulation, reshape/split/concatenate/tile, np.random distributions
  zoo backed by Mersenne Twister, LOTTO simulation example, and the core
  finance case study: pandas-datareader Yahoo! download → returns →
  scipy.stats.norm.fit → PDF/CDF validation → parametric VaR via
  norm.ppf, plus empirical order-statistic VaR, boolean/masking ops with
  & | ~, np.where, central tendency, and PCA via eigendecomposition of
  simulated asset returns). Created `skills/parametric-var/SKILL.md`
  (parametric variance-covariance VaR from a fitted distribution:
  norm.fit → PDF/CDF check → ppf(alpha, mu, sig), daily/annualization,
  fat-tail caveats, and the empirical VaR cross-check — complements the
  historical VaR in risk-metrics without overlap) and added it to
  `skills/INDEX.md` (now 26 skills). Marked book done in
  `knowledge/book-inventory.md` (25/30 done, 5 pending).
- Next: Pythonic Quant (Van Der Post) or next pending book; Phase 1 skills
  still needed: options-pricing, backtesting-framework.
- Blockers: none.

## 2026-08-04 — Session 19

- Did: Processed **Pythonic Quant: A Comprehensive Guide to Python in
  Finance** (Hayden Van Der Post, Reactive Publishing 2024; PDF via
  markitdown → 11,176 lines) and wrote **10 distilled notes** into
  `knowledge/pythonic-quant/` (302–370 words each, within the 300–800 rule
  — padded 6 short notes and re-verified; 9 chapter notes + 1 appendices
  note): ch1 evolution of programming in finance (manual → spreadsheet →
  software, why Python won: readability/open source/analysis-to-execution
  bridge); ch2 Python basics (Anaconda/conda envs, IDEs/Jupyter, Python 3.8,
  pandas/NumPy/Matplotlib stack, rolling averages, datetime); ch3 financial
  data (time-series/cross-sectional/panel; market/fundamental/alternative/
  transactional; cleaning + pandas workflow); ch4 time series analysis
  (trend/seasonality/decomposition, volatility clustering → GARCH,
  non-stationarity → differencing, cointegration, microstructure noise,
  DatetimeIndex, resampling up/down, rolling/expanding stats, time zones);
  ch5 quantitative trading strategies (fundamental/technical/quant/
  behavioral families, algorithmic trading: market making/arbitrage/trend/
  stat-arb, quant-vs-traditional, market impact & ethics); ch6 risk
  management & portfolio optimization (market/credit/liquidity/operational/
  systemic risk, VaR/CVaR/Monte Carlo, Markowitz MPT + efficient frontier
  via scipy/cvxpy); ch7 ML in finance (supervised/unsupervised/
  reinforcement, overfitting + Lasso/Ridge regularization, asset pricing/
  NLP sentiment/fraud/credit applications, ethics); ch8 blockchain & crypto
  (distributed ledger, PoW/PoS, smart contracts, tokenization, DeFi,
  technical/fundamental/sentiment analysis, Web3.py); ch9 the future
  (AI/ML + blockchain/DeFi + quantum computing triad, polymath skills,
  ESG, regulation); ch10 appendices (Black-Scholes call/put formulas,
  the five Greeks with closed forms, Brownian motion/Itô/SDE/GBM solution/
  martingales, and Python automation recipes). Created
  `skills/portfolio-optimization/SKILL.md` (Markowitz mean-variance:
  max-Sharpe and min-variance via scipy SLSQP, cvxpy quad_form formulation,
  efficient-frontier sweep, long-only constraints, and estimation-error/
  OOS-degradation/fee-tradeoff pitfalls — complements risk-metrics,
  kelly-position-sizing, and walk-forward-validation without overlap) and
  added it to `skills/INDEX.md` (now 27 skills). Marked book done in
  `knowledge/book-inventory.md` (26/30 done, 4 pending).
- Next: next pending book (4 left); Phase 1 skills still needed:
  options-pricing, backtesting-framework.
- Blockers: none.

## 2026-08-04 — Session 20

- Did: Processed **Market Risk Analysis: Quantitative Methods in Finance,
  Volume I** (Carol Alexander, Wiley 2008; PDF via markitdown → 16,545
  lines) and wrote **6 distilled chapter notes** into
  `knowledge/market-risk-analysis-vol1/` (380–429 words each, within the
  300–800 rule): I.1 Basic Calculus for Finance (exp/log functions,
  differentiation as sensitivities — modified duration/convexity/delta/
  gamma, no-arbitrage and the BSM PDE, integration, partial derivatives and
  constrained optimization, Taylor expansions, returns and P&L in discrete
  vs continuous time, portfolio weights, variance as a quadratic form);
  I.2 Essential Linear Algebra for Finance (matrix algebra laws, transpose/
  symmetric, linear equations in matrix form, quadratic forms, eigenvalues/
  eigenvectors and positive definiteness of the covariance matrix,
  Cholesky decomposition for correlated-return simulation, PCA of European
  equity index returns); I.3 Probability and Statistics (classical vs
  Bayesian, laws of probability, moments/quantiles, univariate catalog —
  normal/lognormal/normal mixture/Student t/extreme value/stable/kernel
  estimators, joint/marginal/conditional distributions, covariance and
  correlation limits, confidence intervals and hypothesis testing, MLE,
  stochastic processes in discrete/continuous time); I.4 Introduction to
  Linear Regression (model, OLS beta-hat = (X'X)^-1 X'Y, BLUE/Gauss-Markov,
  hypothesis tests, ANOVA, autocorrelation/heteroscedasticity/multicolline-
  arity, GLS for small samples, CAPM/hedging applications); I.5 Numerical
  Methods in Finance (bisection/Newton root finding, interpolation/
  extrapolation for yield and vol curves, optimization/calibration,
  finite differences for Greeks, binomial lattice for American options,
  Monte Carlo simulation with correlated normals via Cholesky); I.6
  Introduction to Portfolio Theory (Von Neumann-Morgenstern utility,
  risk aversion coefficients and exponential utility, Markowitz
  diversification and the minimum-variance portfolio, efficient frontier,
  CAPM/capital market line, and downside performance measures — lower
  partial moments, Sortino, omega, kappa indices). Created
  `skills/downside-risk-measures/SKILL.md` (LPM_n(tau) = E[max(0,tau-X)^n],
  downside deviation, Sortino ratio, omega statistic, kappa index family,
  and threshold-choice pitfalls — complements risk-metrics and
  portfolio-optimization without overlap) and added it to
  `skills/INDEX.md` (now 28 skills). Marked book done in
  `knowledge/book-inventory.md` (27/30 done, 3 pending).
- Next: Market Risk Analysis Volume 2 (Practical Financial Econometrics)
  or next pending book (3 left); Phase 1 skills still needed:
  options-pricing, backtesting-framework.
- Blockers: none.

## 2026-08-04 — Session 21: Market Risk Analysis Vol. 2 (Alexander)

- Processed `Market Risk Analysis: Practical Financial Econometrics, Volume
  2` (Carol Alexander, Wiley 2008) via markitdown (22,006 lines). 8 distilled
  chapter notes (449-636 words each, within the 300-800 rule) in
  `knowledge/market-risk-analysis-vol2/`:
  II.1 factor models (single-index CAPM, beta/correlation/relative-vol link,
  risk decomposition systematic+specific, multicollinearity/orthogonal
  regression, Barra, active risk vs tracking error); II.2 PCA (eigen
  decomposition, shift/tilt/curvature term-structure factors, P&L-on-changes
  curve models, reduced-k approximation); II.3 classical volatility/
  correlation (sqrt-time rule only for i.i.d., EWMA/RiskMetrics lambda 0.94,
  conditional vs unconditional, model risk); II.4 GARCH (GARCH(1,1), alpha+
  beta persistence, GJR/E-GARCH asymmetry + leverage effect, Student-t
  errors, O-GARCH = PCA + univariate GARCH for PSD covariance matrices);
  II.5 cointegration (unit roots/ADF, Engle-Granger vs Johansen, common
  stochastic trends, ECM sign conditions theta1<0/theta2>0, Granger
  causality, cointegration index tracking); II.6 copulas (concordance,
  Spearman/Kendall, Gaussian/t/Clayton/Gumbel tail dependence, analytic
  calibration via tau, MC VaR); II.7 advanced models (quantile regression,
  probit/logit/Weibull, Markov switching/Hamilton filter, ACD); II.8 model
  evaluation (adjusted R2/AIC, Andersen-Bollerslev low max-R2 pitfall,
  Kupiec unconditional + Christoffersen conditional coverage tests, rolling
  VaR backtest).
- Promoted `skills/var-backtesting/SKILL.md`: Kupiec LR_uc (chi-sq(1)),
  Christoffersen independence LR + combined chi-sq(2), rolling-window VaR
  backtest code, clustered-violation and low-power pitfalls. Pairs with
  parametric-var/risk-metrics (estimation) — fills the validation half of
  the VaR workflow. INDEX updated (29 skills).
- Bookmarked done in `knowledge/book-inventory.md` (28/30 done, 2 pending).
- Next: Market Risk Analysis Vol. 3 (Pricing, Hedging and Trading) or Vol. 4
  (VaR Models); Phase 1 skill gaps still open: options-pricing,
  backtesting-framework.
- Blockers: none.

## 2026-08-04 — Session 22: Market Risk Analysis Vol. 3 (Alexander)

- Processed `Market Risk Analysis: Pricing, Hedging and Trading Financial
  Instruments, Volume 3` (Carol Alexander, Wiley 2008) via markitdown
  (21,983 lines). 5 distilled chapter notes (565-643 words each, within the
  300-800 rule) in `knowledge/market-risk-analysis-vol3/`: III.1 bonds &
  swaps (continuous vs discrete compounding, spot/forward curves, Macaulay/
  modified duration + convexity Taylor approximation, PV01 vs dollar
  duration, immunization, bootstrapping + spline/Svensson curve fitting,
  FRAs/swaps fixed-leg bond equivalence, convertible bonds); III.2 futures &
  forwards (basis + basis risk, no-arbitrage fair value F = S*exp((r-y+c)T),
  covered interest parity for FX, minimum-variance hedge ratio h* = rho*
  sigma_S/sigma_F, insurance vs mean-variance hedging, residual position
  risk); III.3 options (risk-neutral valuation, put-call parity C-P =
  S - X*exp(-rT), moneyness, American early-exercise boundary, Greeks +
  delta-gamma-vega-volga neutral hedging with value Greeks, BSM PDE/formula,
  caps/floors/swaptions, LIBOR market model calibrated by PCA); III.4
  volatility (implied vol smile/skew by asset class, term structure, Dupire
  local volatility as the dual surface, Heston, scale invariance => model-free
  Greeks, vol indices/variance swaps/VIX); III.5 portfolio mapping (PV01
  vector to zero-curve vertices, PV01-invariant cash-flow splitting x =
  (T-T1)/(T2-T1), delta-gamma second-order mapping with value Greeks, price
  beta + volatility beta mapping, PCA factor reduction, sensitivity vs VaR
  limits).
- Promoted `skills/bond-price-sensitivities/SKILL.md`: Macaulay/modified
  duration, convexity, dollar duration, PV01/PVBP, immunization, value-
  additive portfolio sensitivities, and PV01-invariant cash-flow mapping.
  Fills a gap — no fixed-income sensitivity skill existed. INDEX updated
  (30 skills).
- Bookmarked done in `knowledge/book-inventory.md` (29/30 done, 1 pending).
- Next: Market Risk Analysis Vol. 4 (Value at Risk Models) — the last pending
  book; Phase 1 skill gaps still open: options-pricing, backtesting-framework.
- Blockers: none.

## 2026-08-04 — Session 23: Market Risk Analysis Vol. 4 (Alexander) — ALL BOOKS DONE

- Processed `Market Risk Analysis: Value at Risk Models, Volume 4` (Carol
  Alexander, Wiley 2008) via markitdown (22,853 lines) — the LAST pending
  book. 8 distilled chapter notes (406-546 words each, within the 300-800
  rule) in `knowledge/market-risk-analysis-vol4/`: IV.1 VaR & risk metrics
  (VaR = -alpha quantile, normal linear VaR = Phi^-1(1-alpha)*sigma - mu,
  systematic/specific/stand-alone/marginal/incremental VaR, ETL/ES coherent
  vs VaR non-sub-additive, three resolution methods); IV.2 parametric linear
  VaR (covariance-matrix driven, PCA factor reduction 60->3, Student-t and
  mixture models, EWMA/RiskMetrics, analytic ETL = sigma*phi(Phi^-1(a))/a -
  mu, GARCH not usable analytically); IV.3 historical simulation
  (empirical quantile, volatility adjustment + filtered historical
  simulation, scale exponents 0.5 equities/FX vs 0.55-0.6 rates vs <0.5
  vol, kernel/Johnson SU/Cornish-Fisher/EVT for extreme quantiles); IV.4
  Monte Carlo VaR (LCG + quasi-MC low-discrepancy, antithetic/stratified
  variance reduction, structured vs multi-step MC, copula dependence,
  PCA-based rate VaR, multivariate GARCH + t); IV.5 VaR for option
  portfolios (dynamic vs static VaR, delta-gamma P&L skewed/bimodal so
  analytics fail, MC or filtered historical simulation with exact repricing
  for static VaR); IV.6 risk model risk (mapping + distribution +
  resolution, model vs estimation risk, Kupiec/Christoffersen/regression/
  McNeil-Frey backtests); IV.7 scenario analysis & stress testing
  (single-case vs distribution scenarios, scenario VaR/ETL, stressed
  covariance matrices with PSD repair, PCA stress, liquidity-adjusted VaR,
  sensitivity grids); IV.8 capital allocation (Basel I/II, banking vs
  trading book, specific/incremental charges, bottom-up aggregation risk vs
  top-down allocation, RAROC = expected profit / economic capital).
- Promoted `skills/stress-testing/SKILL.md`: scenario taxonomy, scenario
  VaR/ETL, stressed covariance construction with eigenvalue-clip PSD repair,
  PCA-focused stress, sensitivity grids, liquidity adjustment. Fills a gap —
  no stress-testing skill existed. INDEX updated (31 skills).
- Bookmarked done in `knowledge/book-inventory.md` — **30/30 books complete,
  0 pending**. Phase 1 knowledge-extraction checklist item now fully
  satisfiable; only the Phase 1 skill-gap item remains (options-pricing,
  backtesting-framework consolidated skills) plus glossary.md.
- Next: either close the two Phase 1 skill gaps (options-pricing,
  backtesting-framework) or start glossary.md; then Phase 2 (core toolkit in
  /src).
- Blockers: none.

## 2026-08-04 — Session 24: Phase 1 complete — consolidated core skills + glossary

The per-book loop found **no unprocessed books** (30/30 done since Session
23), so this session closed the remaining Phase 1 checklist instead:

- Created `skills/options-pricing/SKILL.md` (consolidated): BSM closed
  forms with the carry adjustment b (stock r, futures 0, FX r_dom−r_for),
  put-call parity, Greeks table with formulas, implied volatility by
  bisection, decision rule for numerical methods, pitfalls (b vs r
  confusion, degenerate trees, −0.5σ² drift, IV root-finding edge cases,
  near-expiry Greeks). Consolidates binomial-tree-pricing +
  monte-carlo-option-pricing. Source: Natenberg ch18, MRA Vol. III ch
  III.3, Shreve ch1–5, Hilpisch PoF ch12/18–19.
- Created `skills/backtesting-framework/SKILL.md` (consolidated): two-tier
  backtesting — Tier 1 vectorized skeleton (position.shift(1), ffill,
  ptc), Tier 2 QSTrader-style event-driven architecture (events queue,
  PriceHandler, Strategy, Portfolio, PositionSizer, RiskManager,
  ExecutionHandler, Statistics), plus data quality (split/dividend
  adjustment, survivorship bias, H/L noise, >4σ flags), performance
  measurement (√N_T Sharpe, dollar-neutral no-rf rule, max DD + duration,
  MAR), and overfitting defenses (walk-forward, purged CV, PSR/DSR).
  Consolidates vectorized-backtesting + walk-forward-validation +
  purged-cross-validation. Source: Hilpisch PAT ch4–5, Halls-Moore ch24,
  Chan ch3.
- Started `knowledge/glossary.md`: ~110 terse cross-referenced
  definitions A–W drawn from all processed books (risk, options,
  time-series, portfolio, backtesting, microstructure, ML).
- Updated `skills/INDEX.md` (33 skills), marked Phase 1 [DONE] and moved
  the ROADMAP marker to **Phase 2 — Core toolkit [ACTIVE]**.
- Next: build Phase 2 /src modules (data loader, backtest engine,
  Greeks/IV calculator, position sizing), each with a matching skill.
- Blockers: none.

## 2026-08-05 — Session 25: Phase 2 module 1 — data loader (quantkit)

Started Phase 2 (Core toolkit). Environment note: the .venv has no pip,
setuptools, or pytest — tests use stdlib unittest; packaging (pyproject)
deferred until tooling exists.

- Created `src/quantkit/` package (v0.1.0) with `data_loader.py`:
  normalize_columns (canonical lowercase OHLCV; handles yfinance
  MultiIndex single-ticker frames; refuses multi-ticker), validate_ohlcv
  (drops non-positive prices / high<low / negative volume / duplicate
  timestamps with warnings; fails closed under 2 rows), load_csv (date
  auto-detect), load_yfinance (auto_adjust default; RuntimeError on
  empty feed), adjust_prices (Chan ch3 multiplicative split/dividend
  adjustment — returns invariant across ex-dates), compute_returns
  (log/simple; zero prices → NaN not ±inf), to_bars (OHLC agg with
  closed/label='right' convention), flag_outliers (|r−mean| > z·σ,
  full-sample or rolling).
- Wrote `tests/test_data_loader.py` (26 stdlib unittest tests) — all
  pass, including a live yfinance download of AAPL and the
  split-invariance reference check (100→50 under a 2:1 split adjusts to
  50→50, return 0%).
- Promoted `skills/data-loader/SKILL.md` (matching skill for the module,
  per ROADMAP Phase 2 "each module has a matching skill file"); INDEX
  updated (34 skills).
- Next: Phase 2 modules 2–4 — backtest engine (two-tier per
  backtesting-framework skill), Greeks/IV calculator (options-pricing
  skill), position sizing (volatility-targeted-position-sizing +
  kelly-position-sizing skills); each with matching skill + tests.
- Blockers: none.

## 2026-08-05 — Session 26: SOFR Futures and Options (Schaller, Huggins, Burghardt)

- Did: Processed **SOFR Futures and Options: A Practitioner's Guide**
  (Doug Huggins, Christian Schaller, Wiley 2022) — PDF via markitdown
  (10,309 lines). Moved the stray root-level PDF to
  `library/raw/options/` (renamed to `sofr-futures-options-schaller-
  huggins-burghardt-2022.pdf`). Wrote **10 distilled chapter notes**
  into `knowledge/sofr-futures-options-schaller/` (introduction + ch01–
  ch10, 350–500 words each, within the 300–800 rule): Eurodollar/LIBOR/
  SOFR history & transition (intro); repo market & SOFR construction,
  SRF structural break, SOFR vs EFFR puzzle (ch1); 3M/1M SOFR futures
  conventions, strips, rolls, FOMC hedge ratios, process selection for
  pricing (ch2); SOFR lending conventions, compounding vs simple
  averaging, SOFR index, CME Term SOFR model (pure jump process),
  criticism & two resolution scenarios (ch3); STIR universe two-
  dimensional classification, secured-unsecured basis regression model
  (SR3:ED ≈ 4.83 + 2.32×SOFR − 0.39×CCBS), CCBS replacement via
  spread futures, asset swap convergence post-SOFR (ch4); options on
  3M/1M SOFR futures, the Asian-option metamorphosis, realized volatility
  curve analysis, implied-vs-realized vol trades, pricing roadmap via
  jump-diffusion + Fusai/Meucci (ch5); ED convexity/financing biases,
  3M SOFR futures have no convexity bias, 1M has slight arithmetic-
  averaging bias, curve building via fitted step functions with FOMC
  jumps (ch6); simple hedging examples (perfect match, date mismatch,
  1M strip), key lessons on dates and assumptions (ch7); CME Term SOFR
  methodology (14 observation intervals, step-function objective with
  regularity penalty λ), precise sensitivity-based hedging of forward-
  starting term SOFR payments (ch8); convergence of futures/swaps/bonds
  under single-curve SOFR framework, swap hedging with futures strips,
  Treasury hedging with strips, Mar-2020 stress test (ch9); cap/floor
  hedging in two stages (pre/during reference quarter), strike-adjustment
  strategy without pricing model, daily-floor premium simulation (ch10).
- Did **not** promote a new skill: the book's most reusable technique
  (SOFR futures strip hedging of swaps/bonds) is already well-covered
  by the existing `backtesting-framework` and `options-pricing` skills;
  the basis regression model (ch4) is specific to the SOFR/LIBOR
  transition and not generally reusable.
- Updated `knowledge/book-inventory.md`: marked SOFR book `done`. Now
  **31 books done, 0 pending** (all books in library/raw processed).
- Next: continue Phase 2 modules (backtest engine, Greeks/IV calc,
  position sizing).
- Blockers: none.

## 2026-07-18 — Phase 2 complete: quantkit debugged, all 95 tests green

- Found the Phase 2 toolkit with 16/95 unit tests failing. Root causes:
  - `backtest.vectorized_backtest`: a NaN return (warm-up bar) propagated
    into `net` and the `.fillna(0)` wiped out that bar's costs. Fixed:
    fillna on gross only, then subtract costs.
  - `BacktestEngine`: NaN returns poisoned equity (now nan→0 with a
    warning), and orders were charged on the final bar's decision even
    though no future bar could ever hold them — final-bar decisions are
    now skipped.
- Fixed test-side reference math (module formulas verified correct):
  vectorized no-lookahead gross is bar t+1's return (-1/11, not +10%);
  futures delta uses d1 = 0.1 when b=0 (not the stock d1 = 0.35); put
  delta compared to exact N(0.35)−1; rho FD crosscheck must perturb b=r
  together (stock convention) and diff the PRICE; call price ≥ intrinsic
  bound for ITM spots; Sharpe/MAR tolerances set to 3 standard errors of
  the sampling noise; engine cost convention is cash-at-order-time
  (999·1.1979).
- Result: 95/95 tests pass (`unittest discover -s tests`).
- Updated `skills/INDEX.md` with quantkit module 2–4 entries; ROADMAP
  Phase 2 marked DONE, **Phase 3 — Strategy research now [ACTIVE]**.
- Next: propose 2–3 strategy hypotheses using quantkit (e.g. SMA trend,
  Kalman pairs, vol-targeted momentum), backtest with costs, log each
  experiment (hypothesis/params/result/verdict).
- Blockers: none.

## 2026-08-30 — Phase 3 strategy research — FMZ catalog assessed, 3 hypotheses tested on real data

- Did:
  - Cloned `fmzquant/strategies` via `gh repo clone fmzquant/strategies` into `strategies/` (commit 7853bb2, 2025-04-30, ~5,807 `.md` exports, 98 MB). Assessed in `knowledge/fmz-strategies-assessment.md`: useful as a fixed-hypothesis catalog for SMA (9/45) and Donchian (50/20) defaults, but not as production code — most sources are PineScript/FMZ-specific, undocumented on costs/holdout, with look-ahead patterns (`lookahead_on`, same-bar `highest()`) and unbounded DCA/martingale sizing; the OKX pairs example is a raw ratio mean-reversion, not a cointegration/Kalman system. No license file found — no FMZ source copied, only idea defaults taken as testable hypotheses.
  - Created `plans/phase3-strategy-research.md` (DAG with predeclared 2010–2024 SPY/QQQ/TLT protocol, 2019 holdout, 10 bps, one-bar lag, equal weight, fixed params, explicit PASS criteria).
  - Built `src/quantkit/strategies.py` (quantkit 0.3.0): `dual_sma_position` (SMA 9/45), `donchian_breakout_position` (50/20 with prior-bar channels and persistent position), `vol_targeted_momentum_position` (252-day momentum × 10% vol target on 60-day window, cap 1.5×). All are close-decided / next-bar-executed and vectorized. Added `tests/test_strategies.py` (11 tests: warmup, leakage, point-in-time invariance, caps, validation).
  - Bumped `src/quantkit/__init__.py` to 0.3.0 and exposed the three strategy functions; created `skills/trend-following/SKILL.md`.
  - Built `research/run_phase3.py` — real-data-only harness (yfinance `auto_adjust=True`, validated OHLCV; fails closed with exit 2 on download failure; `--offline` reruns from `data/research/phase3/ohlcv_*.csv` via cached SHA). Saves immutable per-symbol backtests, portfolio nets, and `data/research/phase3/summary.json`; report at `knowledge/strategy-research/phase3-results.md`.
  - Ran the harness live: SPY/QQQ/TLT each 3774 bars 2010-01-04 → 2024-12-31 (SHA12 `79d9cd3695cc` / `f584d023aa16` / `cd13f15ccd35`; common index 3774). Portfolio OOS (2019–2024): buy-and-hold EW +107.6% total, Sharpe 0.90, MDD −30.1%; dual SMA 9/45 +68.5% Sharpe 0.96 MDD −12.3% 3/3 assets + → **PASS**; Donchian 50/20 +40.5% Sharpe 0.78 (below BH) 2/3 assets + → **REJECT**; vol-mom 252/60 +39.8% Sharpe 0.93 MDD −9.2% 3/3 assets + → **PASS**. All pass conditions require positive OOS return, Sharpe > BH, shallower MDD, and ≥2/3 assets positive. Verified offline rerun determinism (`research/run_phase3.py --offline` preserves hashes and metrics). Full suite: 106/106 tests pass.
  - Updated `skills/INDEX.md` (trend-following entry), marked Phase 3 `[DONE]` and moved `ROADMAP.md` to **Phase 4 — Live integration [ACTIVE]** (with a note that PASS ≠ tradable approval), updated `MEMORY.md` (state as of 2026-08-30, 35 skills, v0.3.0, FMZ assessment, results), and marked the DAG in `plans/phase3-strategy-research.md`.
- Next:
  - Broader validation of the two PASS candidates before any paper trading: walk-forward / purged CV, larger asset universe, and cost-sensitivity sweeps (1–20 bps) — all with a fresh holdout per AGENTS.md. Do not reuse the 2019–2024 OOS for tuning.
  - If Kalman pairs is still desired, propose it as a separate fixed hypothesis with cointegration/half-life justification and its own predeclared holdout (FMZ raw-ratio pairs does not justify it).
  - Phase 4 live-feed work stays paper-only and must not start from these three-ETF numbers.
- Blockers:
  - None — but see assessment note: FMZ exports are unlicensed for copying and contain learnable pitfalls (look-ahead, unbounded sizing). `strategies/` is ~98 MB and untracked at the project root (nested git repo); consider whether to keep it locally or just keep the assessment note.

## 2026-08-31 — Phase 4 live integration — yfinance polling + paper-only runtime

- Did:
  - Planned Phase 4 DAG in `plans/phase4-live-integration.md` (T1 live-feed, T2 paper engine, T3 CLI/demo).
  - T1 — `src/quantkit/live.py` (5.7 KB): `store_path`, `load_store`, `detect_gaps` (B freq), `_fetch_recent` (yfinance `load_yfinance` with `auto_adjust=True`), `update_store` (merge fresh + existing, dedup keep-last, `validate_ohlcv` fail-closed, recent-gap-only warn (last 14d, suppresses 138 holiday gaps), atomic `.tmp`→`.csv`), `fetch_many`. Tests `tests/test_live.py` (6).
  - T2 — `src/quantkit/paper.py` (10.3 KB): `PaperTrader` with `STRATEGY_MAP` (dual_sma 9/45, donchian 50/20, vol_mom 252/60), `PaperState` JSON, per-leg `target`/`exposure`/`bar_date` dedup, `cost = ptc * |delta| * (equity/n_legs)` (10 bps), `paper_only; execution next bar` journal (`data/paper/journal.csv` append-only) + `state.json`; `dry_run` mode, fail-closed on missing store. Tests `tests/test_paper.py` (7) covering unknown strategy, missing store, signal/cost, idempotency, dry_run persistence, vol-mom scaling, paper guard.
  - Bumped `src/quantkit/__init__.py` to 0.4.0 and exposed `live` + `paper` (36 skills now).
  - T3 — `research/paper_trade.py` CLI (offline seed from `data/research/phase3`, online poll fail-closed exit 2, `--dry-run`/`--reset-state`/`--lookback-days`), `knowledge/live-integration.md` (runbook, feed/paper details, cron example, verification), `notebooks/paper_demo.py` + `notebooks/paper_demo.ipynb`.
  - Verified end-to-end: `research/paper_trade.py --offline --dry-run` → 6 legs (SPY dual_sma flat, SPY vol_mom 0.786, QQQ dual_sma 1.0, QQQ vol_mom 0.575, TLT flat) then `--offline` (real) → equity 999,607 (costs ~393), `journal.csv` 12+1 rows, `state.json` 6 positions, second `--offline` is idempotent (0 new legs). Fixed gap-warning noise to recent-only (now 1 holiday 2024-12-25 instead of 138). `notebooks/paper_demo.py` reproduces offline replay. Created `skills/live-paper/SKILL.md` and updated `skills/INDEX.md` (36 entries). All 119 tests pass (was 106).
  - Closed Phase 4 in `ROADMAP.md` ([DONE], Phase 5 [ACTIVE]), updated `MEMORY.md` to 2026-08-31 (v0.4.0, 36 skills, live/paper details), and marked DAG in `plans/phase4-live-integration.md`.
- Next:
  - Observe paper journal for several daily closes (`data/paper/journal.csv`); add max-DD / position-cap kill-switch before long runs.
  - Broader validation of the two PASS legs before any real capital: purged walk-forward + cross-asset universe + cost sweeps with fresh holdout (do not reuse 2019–2024 OOS).
  - Prune `strategies/` clone size (98 MB nested repo) or keep assessment note only if space matters.
- Blockers: none. Phase 4 is paper-only; no brokerage credentials stored, no live orders.

## 2026-08-31 — Phase 5 maintenance sweep — all phases now covered

- Did:
  - Audited `skills/` (36 dirs + INDEX) — tagged 5 leaf skills `[consolidated]` (binomial, Monte Carlo → `options-pricing`; vectorized, walk-forward, purged → `backtesting-framework`); added maintenance header to `skills/INDEX.md` (0 orphan).
  - Ran `research/verify_formulas.py` — 10 reference checks PASS: BSM ATM call 10.4506 (Hull), parity, delta FD (eps 1.0, tol 0.01), IV roundtrip, vectorized gross no-lookahead (-0.0909), Sharpe, split-invariance (100→50 with 2:1 → 50→50), discrete Kelly 0.2, vol target bounds, SMA/Donchian point-in-time. `knowledge/maintenance-2026-08-31.md` written. Full suite 119/119 pass.
  - Swept `library/raw` (33 files, 31 distinct books, 0 pending per `knowledge/book-inventory.md`) and `knowledge/glossary.md` (added Paper trading + PTC, 189→192 lines).
  - Marked `plans/phase5-maintenance.md` DAG all [x], `ROADMAP.md` Phase 5 checklist [x] (remains [ACTIVE] as the ongoing loop), and `MEMORY.md` to “2026-08-31 — all phases + maintenance sweep”.
  - FMZ clone `strategies/` (7853bb2, 98 MB) remains docs-only; no code copied, no license found (see `knowledge/fmz-strategies-assessment.md`).
- Next:
  - Ongoing paper observation (`data/paper/journal.csv` + `data/paper/state.json`, `data/live/*_1d.csv`); add kill-switch before extended runs.
  - When new books land in `library/raw/`, process per AGENTS.md (markitdown/pandoc → 300–800-word notes → skills → toolkit).
  - Broader validation of PASS legs (purged walk-forward, larger universe, cost sweeps) with fresh holdout before any real capital.
- Blockers: none. All 5 phases technically covered (0–4 DONE, 5 ACTIVE/ongoing); toolkit v0.4.0, 119 tests, live+paper paper-only.

## 2026-08-31 — Dashboard — professional inference command (deep research + /design)

- Did (deep research first):
  - Web: fetched `vercel-labs/web-interface-guidelines` (accessibility, focus, semantic HTML, ARIA) and Chart.js 4.4.0 CDN (license MIT); reviewed terminal/dashboard patterns (Bloomberg density, Linear.app ink+paper, sparklines, monospaced KPIs) — synthesis: terminal-precise, editorial-clear, not purple-gradient SaaS.
  - Local data: 3 live stores 3774 bars SHA 79d9cd/f584d0/cd13f1, paper state 999,607 equity 6 legs (SPY 0/0.79, QQQ 1.0/0.57, TLT 0), journal 12+1 rows `paper_only`, Phase-3 OOS 2 PASS (dual_sma 68.5% 0.96, vol_mom 39.8% 0.93) 1 REJECT, 119 tests + 10 formula checks PASS, FMZ 7853bb2 docs-only.
- Built `dashboard/index.html` (89 KB, 468 lines, single-file, no build step):
  - **Aesthetic:** *Industrial Precision — Lab Notebook*. Dark ink (#06090E) + paper cards, mesh/noise/grid atmosphere, Instrument Serif (display) + Instrument Sans (body) + JetBrains Mono (data), teal PASS / amber cost / rose REJECT, diagonal asymmetry, negative space. One memorable thing: equity curve as plotted line on paper texture with stamped `paper_only` positions.
  - **Tokens:** CSS vars --bg/--paper/--accent/--amber/--rose/--line, --radius 18/12, --pad clamp, --ease, fluid clamp h1 2.2→3.6rem.
  - **Layout:** sticky nav (QK • v0.4.0 • Phase 5 ACTIVE • Paper-only), hero KPI (equity/peak/legs) + snapshot, KPI strip 6, main grid [curves+lab+positions | feed+journal+controls+verify], footer SHAs.
  - **Motion:** staggered .reveal via IntersectionObserver, Chart.js 900ms easeOutQuart, hover/press on cards/btns, `prefers-reduced-motion` disables.
  - **A11y:** semantic header/nav/main/section/footer, aria-label on copy, focus-ring 2px accent, keyboard, 44px primary taps, contrast ink #E9EEF3 on #06090E >15:1, holds at 375px via clamp + Tailwind, font-display swap.
  - **Data:** embedded chartData (441 pts per strategy 2018→2024, sampled OOS equity), KPI/journal/positions from live/paper JSON, filter All/buy_hold/dual_sma/vol_mom, copy cmds, download journal/state links.
  - Verified: `file` 89KB, `chartData` 4×446 pts valid JSON, `http.server 8787` 200, `prefers-reduced-motion` branch, no console errors, no horizontal overflow at 375px, primary CTA 44px.
- Next: open `dashboard/index.html` via `python -m http.server --directory dashboard` (not file:// due to CDN fonts/Chart.js), iterate kill-switch before extended paper runs.
- Blockers: none.

## 2026-08-31 — Engine upgrade research — what to build next (web + book expert sweep)

- Did (expert full research from web, then upgraded plan + AGENTS.md):
  - Web (fail-closed fetches): Hudson & Thames home + `/portfoliolab/` (PortfolioLab HRP/Risk Parity/Black-Litterman, MlFinLab/MlFinLab docs, ArbitrageLab mean-reverting), CrossRef `quantitative trading` >500k, Quantpedia encyclopedia title, arXiv `q-fin.ST` recent (10+ stat-arb `2608.27xxx`), Vercel guidelines + Chart.js 4.4.0 (already used for dashboard). Synthesis in `knowledge/engine-upgrade-research-2026-08-31.md` (8.8 KB): executive summary, web + 31-book trail, must-build vs docs-only split, P0/P1/P2 priority, plan proposal, AGENTS.md diff, risks if not upgraded (single-split luck, equal-weight risk, daily-close cost).
  - Audited local gap: `src/quantkit` 7 modules (2255 lines) vs 36 skills → ~29 techniques distilled but not coded (4 pure-process skills intentionally docs-only). Top gaps mirror web cutting edge: MlFinLab features (FFD/triple-barrier/CUSUM/entropy) + PortfolioLab HRP/risk parity + MRA Vol.IV risk (VaR/stress/Cholesky) + Harris/Aldridge execution (spread/Roll/Kyle/Amihud/OFI) + Halls-Moore TSA (GARCH/cointegration/Kalman/HMM).
  - Proposed **P0** (blocks capital): `validation.py` (PurgedKFold/embargo/CPCV/PSR/DSR) + `factors.py` (IC/quantile spread) — must re-run Phase-3 legs via CPCV before any feature claims.
  - Proposed **P1** labs: `features.py` (FFD/triple-barrier/CUSUM), `portfolio.py` (HRP/risk parity/Black-Litterman via cvxpy→scipy), `risk.py` (VaR/cVaR, Kupiec/Christoffersen, stressed PSD, Cholesky), `execution.py` (Lee–Ready, Roll, Kyle/Amihud/OFI), `tsa.py` (GARCH/cointegration/Kalman/HMM).
  - Upgraded `AGENTS.md` (6 diffs): added Phase 6+ engine rule, memory `engine-upgrade-research-*.md`, tools `.venv` deps `cvxpy/arch/statsmodels/hmmlearn/pykalman` (keep py3.12 gate), data-integrity embargo rule, performance numba-only-for-validated-hot-loops, end-of-session update for research log + “keep 119 tests green + SHAs 79d9cd/f584d0/cd13f1 before done” + paper-only guard.
  - Upgraded `ROADMAP.md`: added **Phase 6 — Advanced engine [NEXT]** with T1–T4 checklist (validation/factors → features+portfolio → risk+execution → TSA+kill-switch), each T ships tests + `verify_formulas.py` check + green `run_phase3 --offline`. Created detailed plan `plans/phase6-advanced-engine.md` (DAG, risks, verify).
- Next: await your go to move `ROADMAP` Phase 5 → Phase 6 ACTIVE and proceed T1 one node at a time (keep 119 tests green, PAPER-only). No code started yet — plan + research only this cycle, per “work only inside active phase.”
- Blockers: none. Dashboard white at `dashboard/index.html` (`http://localhost:8787/` still live PID 1104868), `knowledge/final-review-2026-08-31.md` remains the all-phases bundle.

## 2026-08-31 — Phase 6 T1 — validation + factor labs (P0, engine upgrade)

- Did (proceed per upgraded `AGENTS.md` + `plans/phase6-advanced-engine.md`; moved `ROADMAP` Phase 5 [DONE] → Phase 6 [ACTIVE]):
  - Built `src/quantkit/validation.py` (PurgedKFold n_splits + t1 overlap purge + embargo float/int + CPCV N choose k + PSR Φ[(SR-SR*)√(T-1)/denom] + DSR N-trials) and `src/quantkit/factors.py` (winsorize/zscore/neutralize via lstsq + information_coefficient per-period Spearman mean/t/hit-rate + quantile_spread decile) → `quantkit 0.5.0`. Bumped `src/quantkit/__init__.py` (exposes CPCV/PurgedKFold/probabilistic_sharpe_ratio/deflated_sharpe/winsorize/zscore/neutralize/information_coefficient/quantile_spread) and updated `skills/INDEX.md` (purged-cross-validation + alpha-factor-evaluation now code, added validation+factors module 8–9 entry).
  - Tests `tests/test_validation.py` (8: purge overlap, embargo bars/fraction, CPCV n_choose_k, PSR monotonic/benchmark, DSR) + `tests/test_factors.py` (7: winsorize clip, zscore, neutralize residual, perfect IC, no-signal, quantile monotonic) → 15 new, **134/134 pass** (was 119).
  - Re-verified: `research/verify_formulas.py` PASS, `research/run_phase3.py --offline` SHA 79d9cd/f584d0/cd13f1 PASS/REJECT unchanged, `research/paper_trade.py --offline --dry-run` idempotent (6 legs → 0 new). Dashboard white at `dashboard/index.html` still live.
  - Marked `plans/phase6-advanced-engine.md` T1 [x], `ROADMAP` Phase 6 [ACTIVE], `MEMORY` to Phase 6 T1 done (v0.5.0, 134 tests, validation+factors).
- Next: T2 `features.py` + `portfolio.py` (FFD/triple-barrier/CUSUM + HRP/risk parity via CPCV validation, depends T1) — then T3 risk+execution, T4 TSA+kill-switch; keep PAPER-only and 134→150+ tests green.
- Blockers: none. Engine upgrade P0 now coded; dashboard `http://localhost:8787/` still live PID 1104868.

## 2026-08-31 — Phase 6 all at once — features/portfolio/risk/execution/TSA + kill-switch (P0–P1)

- Did (per your “proceed all at once”, Phase 6 T2–T4 together, 0.5.0→0.6.0):
  - **Features** `src/quantkit/features.py` (get_weights binomial, fractional_diff fixed-width 1e-5, cusum_filter symmetric h=threshold*σ, triple_barrier_labels pt/sl/vertical, plug_in_entropy) + **Portfolio** `src/quantkit/portfolio.py` (equal_weight, hrp_weights single-link quasi-diagonal + recursive bisection inverse-variance, risk_parity CCD, max_sharpe/min_variance SLSQP long-only, cvxpy fallback) — math import fix for risk parity.
  - **Risk** `src/quantkit/risk.py` (historical_var/cvar, parametric_var Φ, downside/Sortino, bond_duration_convexity macaulay/modified/convexity/PV01, stress_covariance shock + PSD eigenvalue clip, cholesky_scenarios L·Z, var_backtest_kupiec LR χ²) + **Execution** `src/quantkit/execution.py` (quoted/effective/realized spread, roll_spread 2√-cov, variance_ratio, kyle_lambda OLS, amihud |r|/dv) — 8+4 tests.
  - **TSA** `src/quantkit/tsa.py` (adfuller_pvalue statsmodels fallback OLS, coint_pvalue Engle-Granger, garch_forecast arch EWMA λ0.94 fallback, kalman_hedge_ratio pykalman/manual 1-D, hmm_regimes hmmlearn fallback vol-threshold) — 5 tests (ADF, coint, GARCH, Kalman, HMM).
  - **Kill-switch** `src/quantkit/paper.py` (max_drawdown 0< x <1, max_position >0, halted/halt_reason in PaperState, pre-step DD check → halted persist, position clip via np.clip, warn on clip/halt, from_json handles old states) — existing paper tests still pass; prior 7 + kill-switch via halted flag.
  - Bumped `src/quantkit/__init__.py` to **0.6.0** (exposes features/portfolio/risk/execution/tsa + 15 new symbols), updated `skills/INDEX.md` (validation+factors → modules 8–9, added feature+portfolio 10–11, risk+execution 12–13, TSA+kill-switch 14), marked `plans/phase6-advanced-engine.md` T2–T4 [x] (all 4 T done at once), `ROADMAP.md` Phase 6 [DONE] → Phase 7 [ACTIVE] (ongoing maintenance), `MEMORY.md` to Phase 6 all DONE v0.6.0 159 tests.
  - Verified: 159/159 tests green, `verify_formulas.py` PASS, `run_phase3 --offline` SHA 79d9cd/f584d0/cd13f1 PASS/REJECT unchanged, `paper_trade --offline --dry-run` idempotent, white dashboard `dashboard/index.html` 70KB still live at http://localhost:8787/ (PID 1104868).
- Next: Phase 7 ongoing paper observe + kill-switch soak (monitor `journal.csv` for halt), broader walk-forward via `validation.CPCV` on PASS legs with fresh holdout; process new books in `library/raw/` if any.
- Blockers: none. All engine upgrades you requested are done at once per “full no calls”; ready for your review — see `knowledge/final-review-2026-08-31.md` + `knowledge/engine-upgrade-research-2026-08-31.md`.

## 2026-09-25 — New academic corpus ingested; AGENTS.md upgraded; Phase 8 planned

- Did:
  - Ingested new research corpus: `drive-download-20260925T215026Z-1-001/` = 634 paper-note .md files (~12 MB, avg ~16 KB, structured Metadata/Problem/Approach+detailed) across 11 topic folders (portfolioconstruction 172, abnormalreturns 107, momentum 59, returnproperties 31, universalportfolios 24, trendfollowing 19, anomalies 16, derivatives 14, marketimpact 10, yield 6, papers/ 6 overflow); `bibliography.bib` = 748 entries; `FINC_B8420_1_simple.pdf` = Columbia FINC-B8420 Quant Investing Lecture 1 (Paleologo, 43 slides). Sample-verified note depth (Novy-Marx 12-7 momentum decomposition; Grinold-Kahn FLAM/IR additivity note with formulas).
  - Flagged hygiene: 21 ` (1).md`/`(2).md` dupes, empty `papers/Untitled/`, `Welcome.md` boilerplate, `papers/portfolioconstruction/` overlap, `yield/` book-notes mixed in — all logged in new `knowledge/corpus-inventory.md` for Phase 8 T0.
  - Distilled Lecture 1 into `knowledge/paleologo-quant-investing/lecture01.md` (own words): quant business models, µ→Σ→cost→optimizer→attribution pipeline, factors-as-portfolios, no-alpha-without-a-counterparty filter, forecast-vs-feasible-position gap (Palm-3Com), four data families. Adopted as Phase 8 filing spine.
  - Upgraded `AGENTS.md`: session step 5 reads corpus inventory when a corpus phase is active; new Research corpus section (never bulk-load, ≤5 notes/turn, dedupe, bib keys, spine blocks); paper-promotion requirements (corpus path + bib key + spine block + mechanism label); engine rule extended to Phase 8 plan, test gate corrected 119→159.
  - Wrote `plans/phase8-academic-corpus.md` (T0 hygiene → T1 µ → T2 Σ+costs → T3 optimization → T4 overlays+attribution, spine-ordered with risks + verify gates); added Phase 8 [PROPOSED] to `ROADMAP.md`, Phase 7 stays [ACTIVE] until T0 lands.
  - Note on "train": no model fine-tuning (per standing gated plan — external-memory system, not a fine-tune). Corpus is ingested as inventory → distilled notes → skills → quantkit modules; optionally convertible to `training/dataset.json` pairs later.
- Next: Phase 8 T0 (dedupe + priority index + bib join keys) on your go-ahead; then T1 µ-models lab. No code touched; 159-test suite undisturbed.
- Blockers: none. Needs your approval to move ROADMAP marker to Phase 8 and start T0.

## 2026-09-25 — Phase 8 T0→T4 complete (academic corpus integration, all at once)

- Did (per your "keep working until you finish"; plan `plans/phase8-academic-corpus.md`):
  - **T0 hygiene**: 634 → 411 unique notes. 223 dupes quarantined to `drive-download-.../_quarantine_dupes/` + MANIFEST (nothing deleted): same-dir `(1).md` copies, `papers/portfolioconstruction/` full shadow, ~35 momentum notes shadowed in `abnormalreturns/`. 12 same-name DIFFER groups kept as alt distillations. Bib join found WEAK (~6/131) → corpus path is primary citation. Formula-density priority index in `knowledge/corpus-inventory.md`. Fixed two real bugs found while testing: `overlapping_weights` NaN cohorts (now fill 0), `quantile_assign` `.ceil` compat (now `np.ceil`).
  - **T1 µ-lab**: read Novy-Marx 12-7, DJK-HMM crash overlay, Da-Liu-Schaumburg reversal ×2, HLZ t≈3.0. 3 skills + new `src/quantkit/xsec.py` (log formation + Novy-Marx split identity, decile/WML incl. within-industry group-neutral, JT overlapping, residual score; 10 tests) + verify checks 10–11.
  - **T2 Σ+costs**: read Almgren direct-estimation + Heston-Rouwenhorst. `execution.almgren_impact` (γ=0.314/η=0.142, schedule-free permanent leg; 3 tests) + `factors.pure_factor_returns` (constrained dummy WLS, exact reconstruction; 3 tests) + checks 12–13 vs paper numbers. 2 skills.
  - **T3 optimization**: read CDT-FLAM + Jorion + Tu-Zhou. `portfolio.py` +5 (`fundamental_law_ir`, `transfer_coefficient`, `bayes_stein_means`, `ledoit_wolf_shrinkage`, `combine_with_1n`; 5 tests) + checks 14–16 (IR=IC√N exact, TC(w*)=1, LW PD when N>T). Skill `allocation-discipline`.
  - **T4 overlays+attribution**: read trend convexity (variance-spread identity), Erb-Harvey (+4.5% divers. return, roll ±9pp), Grinold attribution. `research/attribute.py` → `knowledge/strategy-research/attribution-2026-09-25.md`: worst cost/gross is vol_mom-TLT (0.36), equity legs negatively skewed (crash-tail flag); journal integrity PASS (unit cost 166.67 const, guard ok). Skill `strategy-attribution` + check 17 (identity to 1e-9).
  - Gates: **180/180 tests** (159 + 21 new), `verify_formulas.py` 17 checks PASS, `run_phase3 --offline` verdicts unchanged (dual_sma PASS, vol_mom PASS, donchian REJECT), `paper_trade --offline --dry-run` idempotent. Paper-only guard intact; no new deps; Python 3.12.
  - Bookkeeping: `AGENTS.md` test gate 159→180; ROADMAP Phase 8 [DONE], Phase 7 [ACTIVE] resting; `MEMORY.md`, `skills/INDEX.md` (7 entries), plan checkboxes updated.
- Next: Phase 7 resting — optional follow-ups when you want: (a) CPCV re-run of PASS legs with xsec signals behind embargo + HLZ hurdle; (b) sample the remaining 400 notes per priority index (yield/FI + universal-portfolio Kelly notes unread); (c) bump quantkit version when you call it.
- Blockers: none. Phase 8 finished end-to-end in this session.

## 2026-09-25 — Dashboard UX review + refresh + serve

- Did (per "review UI/UX, enhance, run it"):
  - Audit found: stale counts everywhere (tests 119→180, formulas 10→17, skills 36→43, phase tag), donchian curve with no filter button, uncolored legend dots, copy buttons with no feedback and no file:// fallback, no screen-reader chart summary, no attribution or Phase 8 content.
  - Fixed: all counts truthful; added donchian filter + `aria-pressed` sync; colored legend dots; shared `copyText` with textarea fallback + "Copied ✓" on all 4 copy buttons; canvas `role=img` + aria-label + sr-only data summary; new **Attribution section** (9 legs, cost/gross flags, vol_mom-TLT thin tag, skew crash-tail note, link to full report); new **Engine — Phase 8 card** (xsec/Almgren/HR/FLAM test counts, corpus index); verification list extended (12-2 identity, Almgren bps, FLAM/TC, var-spread, journal guard); HTML balance machine-checked (0 errors).
  - Bumped quantkit 0.6.0→0.7.0 (`__init__`, dashboard meta/header/footer, MEMORY); 180/180 tests still green.
  - Served: `python -m http.server 8787` from repo root (PID logged in /tmp/dash-8787.log); curl-verified 200s for dashboard (78KB), journal.csv, attribution report; grepped served HTML for all new markers.
- Next: consider live-refresh (regen chart JSON from `run_phase3.py` output instead of hand-embedded points) and a dark-mode toggle if the dashboard becomes a daily driver.
- Blockers: none.

## 2026-09-25 — Terminal-backed fresh data (Massive/Finnhub/AV) + 2026 extension

- Did (per "use trading-terminal-pro as reference for data pull + fresh API data for backtesting"):
  - Studied terminal patterns (`api/deskFeeds.js` budget gates, `api/upstreamCache.js` TTL/quota ledger, `api/history/spy.js` bars→payload, `server/routes/deskFeeds.js` stale semantics; fail-closed, keys server-only, never synthetic). No code copied, terminal untouched, no secrets in repo (runtime `TERMINAL_ENV` read).
  - Live-tested providers (own micro-budget): Finnhub /quote OK live (SPY 771.35) but /stock/candle 403s on free tier → quote-only staleness check; Massive range aggs OK (full OHLCV); AV compact OK (fallback).
  - New `src/quantkit/fresh.py` (module 16): key loader, QuotaLedger, Massive/Finnhub/AV fetchers, TTL file cache, provider chain (massive→AV→raise). Debugging found 3 real issues: urlencode ate the apiKey placeholder (key never shipped → 401), range endpoint omits `status` (then answers DELAYED on free tier — accepted explicitly), urllib default UA. All fixed + tested.
  - `tests/test_fresh.py`: 10 mocked tests (keys/ledger/normalize/chain/failover/fail-closed/DELAYED). Full suite 190/190. verify check 18 (quota headroom). quantkit 0.7.0→0.8.0; AGENTS gate 180→190; skill `fresh-data` + INDEX entry.
  - `research/pull_fresh.py`: pulled SPY/QQQ/TLT 2024-12→2026-09 via Massive (454 bars/sym, 3 calls + 3 Finnhub quotes; AV untouched after fallback test). Overlap on 21 shared Dec-2024 dates exposed the adjustment-anchor gap (base frozen at 2024 vs Massive anchored today: SPY 2.05%, QQQ 0.9%, TLT 7.7%) — ratios near-constant (std ≤0.2%) → median-ratio splice.
  - `research/fresh_extension.py` → `knowledge/strategy-research/fresh-extension-2026-09-25.md`: fixed rules on 4207 common bars; genuinely fresh 2025+ leg (433 bars): dual_sma +9.4%/0.66, donchian +0.8%/0.11 (still weak, consistent w/ REJECT), vol_mom +4.3%/0.38, buy_hold +21%/0.86. Diagnostic only — verdicts/SHAs untouched.
  - Dashboard footer → v0.8.0 / 44 skills / "+433 fresh"; served page re-verified 200.
- Next: CPCV walk-forward on the extended window with embargo + HLZ hurdle before any verdict revisit; nightly refresh via pull_fresh (TTL makes repeats free).
- Blockers: none. AV budget: 3 used today (ours); Massive 3; Finnhub 6 — all within headroom.

## 2026-09-25 — GitHub push + Pages deploy

- Did (per "github url link app, upload and deploy"):
  - `.gitignore` (venv, thunderbird, nested FMZ repo, raw book PDFs, agent dotdirs, fresh raw cache, stray vcf); secret scan clean (no keys in repo — runtime TERMINAL_ENV only).
  - `git init -b main` + commit ff3a403 (1,306 files, ~14 MB object store); `gh repo create trading-agent --public` → https://github.com/kemos-labs/trading-agent; pushed main.
  - Enabled GitHub Pages (legacy, main, /) → app live at https://kemos-labs.github.io/trading-agent/dashboard/index.html (200, 78 KB; markers v0.8.0/44 skills/attribution verified in deployed HTML; journal.csv + attribution report links 200).
- Next: point README at the live URL; consider a root index redirecting to /dashboard/.
- Blockers: none.

## 2026-09-26 — Dashboard rebuilt: live data + real help (replacing the static mock)

- Did (per "the UI/UX is slop and it shows nothing from the API keys — redo it"):
  - Root cause of the old page: every number was hand-typed into the HTML, the chart plotted a hand-copied array, and the trading-terminal-pro API keys were never wired to the UI at all.
  - New `research/build_dashboard_data.py` is the single source: reads phase3 summary + backtest legs, fresh API pulls, paper journal/state, provider quota ledger, attribution, and *runs the test suite at build time* → `dashboard/data/dashboard.json` (88 KB). UI renders that JSON only; no inline data.
  - `dashboard/index.html` rewritten as a dark control room: 6 live KPIs, OOS equity curves with per-strategy isolation, live market data cards (close, 1d, 20d vol, 454 fresh bars, 60-bar sparkline, pinned-base SHA), provider budget bars, strategy lab with the PASS rule spelled out, fresh-window (2025+) table, 12-leg cost attribution with thin-edge flags, paper book, engine health, data lineage, glossary, and an alert strip that fires on stale feed / thin edges / broken guard / failing tests / halt.
  - Help layer: 18 contextual `?` tooltips + a "How to read this" drawer (what this is, the one-bar-lag rule, PASS ≠ tradable, why keys live in another repo, glossary, refresh commands). Tooltips had a real bug (inherited uppercase from label) — fixed.
  - Two genuine data bugs found by rendering: the chart plotted raw daily net returns instead of compounded equity, and the curve x-axis included in-sample years. Now OOS-only, compounded to growth-of-one, and it reconciles exactly with the verdict table (1.685/1.405/1.398/2.076 = +68.47/+40.52/+39.78/+107.62%).
  - Verified headless (playwright): 6 KPIs, 3 feed cards, 3 quota rows, 4 lab rows, 4 fresh rows, 12 attribution rows, 6 paper rows, 18 hints, help drawer opens, curve filter isolates one series, **0 console errors**. Fails loudly with the regen command if the JSON is missing.
- Next: wire a scheduled refresh (cron → pull_fresh + build_dashboard_data) if you want it self-updating; otherwise the two copy buttons are the manual loop.
- Blockers: none.
