# Ch23 — NLP & Sentiment Analysis (SVM on text)

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 23.

## Full pipeline for text-driven trading strategies
Steps between raw web text and an automated strategy:
1. Automate download of continually generated articles (Scrapy/BeautifulSoup).
2. Parse documents for relevant sections.
3. Convert arbitrarily long text (many languages) into a consistent format.
4. Define class labels (e.g. bullish/bearish, topics).
5. Create a **training corpus** of manually/known-labelled documents.
6. Train classifier(s) on the corpus (scikit-learn).
7. Use classifier to auto-label new documents (ongoing).
8. Assess classification rate & metrics.
9. Integrate into an automated trading system (e.g. as a filter for other signals).
10. Continually monitor; adjust when performance degrades.

This chapter concentrates on the **classification pipeline** using the pre-labelled
**Reuters-21578** corpus (one of the most widely used text-classification test sets: news
articles tagged with topics + geographic locations).

## Supervised document classification setup
Each document → feature vector x_j, whose components = "strength" of each word; class label
y_j = topic. Classifier learns word→label representativeness from the labelled training corpus.

## Preparing the Reuters dataset
- Download `reuters21578.tar.gz`; files are `.sgm` (SGML). Python's sgmllib is deprecated/
  removed → subclass **HTMLParser** (handle_starttag/handle_endtag/handle_data), chunked
  `feed` + `parse` generator (memory-friendly), tracking in_body/in_topics/in_topic_d state.
- Output: list of (topics, body) tuples. Documents have **multiple topics** → assign a *single*
  label: strip geographic location tags (e.g. japan, thailand) then take the **first remaining
  topic**; drop articles with no topic. 135 topics total in the corpus.

## Vectorisation → Bag of Words → TF-IDF
- **Tokenisation**: split text into tokens (words, incl. numbers) on whitespace/punctuation;
  each token gets an integer index.
- **Bag of Words (BoW)**: count token frequency per document → per-document real-valued
  vector; corpus = large sparse matrix (rows=documents, cols=tokens). **Ignores word order**.
- Problem: **stop words** ("a","the","he") dominate frequency and mask informative words.
- **TF-IDF (Term-Frequency × Inverse Document-Frequency)**: token importance ↑ with frequency
  in the *document* but ↓ (normalised) by frequency across the *corpus*. "a"/"the" get low
  weight (appear everywhere); "cat" gets higher weight in documents where it's frequent but
  rare corpus-wide. Combine vectorisation + TF-IDF → normalised document-token matrix.
- scikit-learn **TfidfVectorizer** does both: input list of (label, text) tuples → output y
  (labels) + X (sparse TF-IDF matrix).

## Training the SVM
- `train_test_split(X, y, test_size=0.2, random_state=42)` — 70–80% train, rest test (k-fold
  CV would be more sophisticated). random_state ⇒ reproducible.
- **SVC(C=1e6, gamma="auto", kernel='rbf')** — radial kernel, very large C budget (params from
  ch19). Fit on train, `predict` test.
- On 1 Reuters file (reut2-000.sgm): **~66% hit rate**, confusion matrix mostly diagonal
  (correct labels). On all 21 files: full-dataset hit rate (slow to compute).

## Performance metrics
- **Hit rate / classification rate** = correct assignments / total (classifier `.score`).
- **Confusion matrix** = N×N counts: true positives/negatives, false positives/negatives
  (for binary; N×N for multi-class). `sklearn.metrics.confusion_matrix(pred, y_test)`.

## Improvements
- **GridSearch cross-validation**: sweep SVM params (C, gamma, kernel) over a grid with CV to
  pick optimal parameters → improves on the fixed C=1e6 radial default.
- Production: stream training data + partial fitting (memory), rather than load whole corpus.

## Takeaways / pitfalls
- Most quant research time = data wrangling (parsing SGML/HTML etc.) — not the ML itself.
- BoW ignores word order (limitation); TF-IDF essential to de-emphasise stop words.
- One class label per document is required — choose carefully (strip locations first).
- Huge C + rbf = high flexibility → monitor for overfitting; use grid search CV for C/gamma.
- Sentiment/classification from news is a viable alpha source only with a complete,
  monitored pipeline (steps 1–10 above).