# PageRank Mini-Project

This folder contains my implementation of the PageRank assignment.

## What’s inside
- `spider.py` – crawl ~100 pages and store HTML + links in `spider.sqlite`
- `sprank.py` – compute PageRank
- `spdump.py` – show top ranks in the DB (for screenshot)
- `spjson.py` – export JSON for visualization, then open `force.html`
- Visualization assets: `force.html`, `force.js`, `force.css`, `d3.v2.js`
- Screenshots:  
  - `spdump-knownby.jpg`, `force-knownby.jpg`  
  - `spdump-quotes.jpg`, `force-quotes.jpg`

## How to run (Python 3)
1. (Optional) create venv and install deps:
python -m venv .venv && source .venv/bin/activate
pip install beautifulsoup4

markdown
Copy
Edit
2. Crawl:
python spider.py

markdown
Copy
Edit
When asked:
- **Enter web url or enter:** e.g. `https://py4e-data.dr-chuck.net/known_by_Fikret.html` *or* `https://quotes.toscrape.com/`
- **How many pages:** type `50` twice (≈100 pages total), or `100` once
3. PageRank:
python sprank.py

markdown
Copy
Edit
4. Dump (for screenshot):
python spdump.py

markdown
Copy
Edit
5. Visualization:
python spjson.py # enter 25

arduino
Copy
Edit
Then open **force.html** in your browser and take a screenshot.

