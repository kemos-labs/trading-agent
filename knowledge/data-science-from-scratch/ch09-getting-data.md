# Ch09 — Getting Data

**Source:** Grus, *Data Science from Scratch*, Chapter 9.

## Purpose
How to acquire data in Python: **HTML scraping** and **APIs** (with a brief
look at regex). Data usually arrives messy and must be pulled from the web.

## Getting data with `requests` + scraping
- **`requests` library**: `requests.get(url)` → `response.text`; check
  `response.status_code == 200`, `response.ok`; set headers like
  `User-Agent` so servers respond well; handle errors with try/except.
- **Parsing HTML**: the book uses `BeautifulSoup` (from `bs4`):
  ```python
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html, "html5lib")
  ```
  - `soup.find("table", {"class": "dataframe"})` → find a tag by name/attrs.
  - `table.find_all("tr")` → rows; `row.find_all("td")` → cells of a row.
  - `row.get_text()` / cell `.get_text()` → extract text content.
  - `soup.select(selector)` supports CSS selectors.
- **Rule of thumb**: prefer the structured page (Wikipedia's data tables)
  and targeted `.find_all` over brittle string slicing.

## Regex for extracting patterns
- `re.findall(r"pattern", text)` returns all matches; raw strings avoid
  escape noise.
- Used to pull dates/IDs/numbers out of text, e.g.
  `re.findall(r"\d{4}", text)` for 4-digit years.
- Regex is the right tool for well-defined patterns; for real-world HTML,
  BeautifulSoup is usually better.

## APIs (the clean way)
- **JSON**: `requests.get(url).json()` decodes an API response into Python
  dicts/lists. The chapter's example: the book's own GitHub issue list
  `https://api.github.com/repos/joelgrus/data-science-from-scratch/issues`.
- **GitHub API practice**: unauth'd requests are rate-limited; the book
  reduces load by fetching only issues that haven't been updated recently
  (conditional requests, `?since=` param) — be a good API citizen.
- Inspect JSON structure (dict keys) before coding around it.

## Ethics / etiquette (the chapter's real lesson)
- **Don't hammer servers**: batch requests, add delays, respect
  `robots.txt` and API rate limits.
- Check the site's terms of service before scraping at scale; prefer
  official APIs when they exist.
- Cache what you download so you don't re-fetch.

## Key takeaways
- The standard pipeline: `requests.get` → parse (BeautifulSoup for HTML,
  `.json()` for APIs) → extract into Python structures.
- Test with a single page/sample before writing the loop over everything.
- Save fetched data locally (the book saves HTML to disk) so later steps
  don't depend on the network.

## Notes
- No formulas; it's tooling. The `parse_iris_row`-style CSV handling in
  ch12 and `csv.reader` in ch23 follow the same "acquire → structure" theme.
- Later chapters use these patterns: downloading Iris (ch12) and MovieLens
  (ch23) datasets.
