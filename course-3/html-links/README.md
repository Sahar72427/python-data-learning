# HTML Span Sum (BeautifulSoup)

Reads an HTML page from a given URL, finds all `<span>` tags, extracts the numbers inside, and prints the **count** and **sum**.

## Files
- `sum_spans.py` — Final solution using `urllib` + `BeautifulSoup`.

## How to run
```bash
# (optional) create & activate a venv
# python -m venv .venv && source .venv/bin/activate

pip install beautifulsoup4

python sum_spans.py
Enter URL: http://py4e-data.dr-chuck.net/comments_42.html
