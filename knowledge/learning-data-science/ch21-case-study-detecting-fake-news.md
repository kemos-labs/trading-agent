# Ch21 — Case Study: Detecting Fake News

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 21.

## Purpose
Capstone lifecycle run: predict whether a news article is fake or real
using **logistic regression + tf-idf** on text, pulling together scope
(ch2), wrangling (ch8/9), text (ch13), model selection (ch16), and
classification evaluation (ch19).

## Question & scope
- Question: can we automatically detect fake news from article content?
- Data: FakeNewsNet political subset, labeled by **PolitiFact** fact-checks.
- Bias checklist: coverage (only monitored outlets), selection (only
  "most newsworthy" claims — skews toward shared/controversial), measurement
  (single organization's judgment), **drift** (2007–2020 content; models
  trained on 2016 candidates won't know 2020/2024 names).

## Wrangling
- FakeNewsNet's repo *scrapes* articles (doesn't store them) — reproducible
  but fragile: dead links become missing data; document fetch date, respect
  ToS.
- Load each article's `news content.json`, extract url/text/title/date,
  drop missing text, convert Unix timestamps, extract base URLs (strip
  `web.archive.org` prefixes), concatenate title+text into one `content`
  column.
- Granularity: one row per article; label = fake/real.

## Modeling (3 models, escalating features)
1. **One-word model**: single binary feature (contains "vote") — logistic
   fit; odds multiplier e^θ₁ ≈ 0.37 per word. Weak.
2. **15 handpicked words**: better accuracy (~74.8%); precision improves
   (0.57 → 0.70); coefficients interpretable (trump, investig ⇒ fake;
   congress, vote ⇒ real). But handpicking is biased and incomplete.
3. **tf-idf (23,800 tokens)**: TfidfVectorizer (stem, remove stopwords) +
   `LogisticRegressionCV` (regularization via CV, solver='saga'). 100%
   train accuracy; **0.88 test accuracy** — the gap is the overfitting
   signature (ch16). 100× slower at prediction, uninterpretable weights,
   quirky features (punctuation).

## Evaluation & the real lesson
- Test-set errors: 0.61 → 0.70 → 0.88. More features ⇒ better test
  accuracy here (the simple models were underfit — too much bias), but at
  the cost of interpretability and speed.
- Precision matters most in this domain: mislabeling a real article as
  fake (FP) is the costly error — precision improved from 0.57 to 0.70.
- **The model's limits**: tied to vocabulary seen in training; won't
  generalize to new names/topics (drift). A good test score ≠ production
  readiness.

## Key takeaways
- The lifecycle is messy and iterative: cleaning questions surfaced at the
  very end would loop you back to earlier stages.
- Feature engineering is a trade: handpicked (interpretable, weak) vs
  full-text tf-idf (strong, opaque, slow) vs everything between.
- Logistic + tf-idf is a shockingly strong baseline for text
  classification.
- Always state what the model can't do (drift, scope) alongside what it
  does.

## Notes
- Brings ch13's regex/tf-idf and ch19's precision/recall together; the
  book's closing argument for "keep the whole lifecycle in mind."
- Directly applicable to financial news/sentiment pipelines.
