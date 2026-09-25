# Ch13 — Working with Text

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 13.

## Purpose
Turning unstructured text into usable data: string canonicalization,
extraction, and numeric features — via Python string methods, **regular
expressions**, and tf-idf.

## Text tasks
1. **Canonicalize** (standard format): lowercase, fix spellings/abbreviations/punctuation so joins and matches work (the county-name join example).
2. **Extract**: pull structured pieces (dates, IPs) out of strings (web log example).
3. **Transform to features**: 0-1 indicators for the presence of words/phrases.
4. **Analyze**: compare whole documents via word-count vectors (tf-idf).

## String methods
- `str.lower()`, `str.replace(a,b)`, `str.strip()`, `str.split(a)`,
  slicing `str[x:y]` — composable primitives for canonicalization.
- In pandas, the `.str` accessor applies these per-element without loops:
  `df['col'].str.lower().str.replace('&', 'and')`.
- `re.split` with a pattern beats chained splits for extracting many pieces
  (e.g. log timestamps).

## Regular expressions
- **Literals & concatenation**: `cat` matches the substring "cat".
- **Character classes** `[0-9]`, `[a-z]`; negated `[^0-9]`; shorthand
  `\d` (digit), `\w`, `\s`.
- **Wildcard** `.` (any char but newline); **anchors/boundaries** `^` `$`
  `\b` (word boundary) to prevent partial matches.
- **Quantifiers**: `{m,n}`, `*` (0+), `+` (1+), `?` (0-1) — greedy by
  default; lazy variants exist. Greediness causes overmatching
  (`[0-9].+[0-9]` grabs across two numbers — use `\b` and specific classes).
- **Alternation** `|` ("hand|nail|hair|glove") and **groups** `(...)` to
  extract sub-parts (`re.findall` returns groups).
- `re.findall(pattern, s)` returns all matches; use raw strings `r'...'`;
  escape metacharacters with `\`.

## From text to features: tf-idf
- **Term frequency**: normalized word counts per document.
- **Inverse document frequency**: weight words by rarity — rare words are
  more informative. tf-idf = tf × log(N/df).
- `sklearn.feature_extraction.text.TfidfVectorizer`: tokenize, remove
  stopwords, optionally stem; output is a sparse feature matrix for
  modeling (used end-to-end in ch21's fake-news case study).

## Key takeaways
- Regex is the general tool; string methods are the simple tool — start
  simple, escalate deliberately.
- Greedy matching is the classic regex bug: prefer specific classes +
  boundaries over `.` + `*`.
- tf-idf turns documents into model-ready vectors while down-weighting
  ubiquitous words.

## Notes
- Ch21 runs tf-idf + logistic regression to detect fake news; ch9's
  restaurant-violation word features are the chapter's motivating example.
- Always test regexes on the actual messy data — patterns that pass on
  clean examples fail on real strings.
