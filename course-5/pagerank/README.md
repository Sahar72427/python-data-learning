# PageRank mini-project (Coursera, Course 5)

This folder contains my implementation of the PageRank assignment:
- Crawl ~100 pages
- Compute PageRank
- Dump top ranks
- Visualize 25 nodes with D3 force layout

## How to run (macOS / Python 3)
1) Create venv and install deps (optional):
   python3 -m venv .venv && source .venv/bin/activate
   pip install beautifulsoup4 html5lib lxml

2) Crawl:
   python spider.py
   # enter start URL when prompted (e.g., known_by_* or https://quotes.toscrape.com/)
   # enter 50 twice to crawl ~100 pages

3) PageRank:
   python sprank.py

4) Dump:
   python spdump.py

5) Visualization:
   python spjson.py  # enter 25
   open force.html

Screenshots: 
- Known_by set: `spdump_knownby.png`, `force_knownby.png`
- Quotes set:   `spdump_quotes.png`, `force_quotes.png`
