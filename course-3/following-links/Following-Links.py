import ssl
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def pick_kth_link(url, k, ctx):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, context=ctx) as resp:
        html = resp.read()

    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a")
    if len(links) < k:
        raise IndexError(f"Not enough links on page: need {k}, found {len(links)}")

    tag = links[k - 1]  # 1-based → 0-based
    href = tag.get("href", None)
    text = tag.get_text(strip=True)
    if not href:
        raise ValueError("Selected link has no href")

    href = urljoin(url, href)
    return href, text

# ---- Inputs ----
start_url = input("Enter URL: ").strip()
count = int(input("Enter count: ").strip())
position = int(input("Enter position: ").strip())

# ---- SSL context (for the exercise) ----
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

current = start_url
for i in range(count):
    next_url, link_text = pick_kth_link(current, position, ctx)
    print(f"Step {i+1}: {link_text} -> {next_url}")
    current = next_url

print("Final URL:", current)


