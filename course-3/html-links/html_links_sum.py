import ssl
import urllib.request
from bs4 import BeautifulSoup

# ask URL from user
url = input("Enter URL: ").strip()

# SSL context Error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# HTML with User-Agent 
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, context=ctx) as resp:
    html = resp.read()  # bytes

# HTML Parser with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# span finder
spans = soup.find_all("span")

# int extraction
values = []
for tag in spans:
    txt = tag.get_text(strip=True)  
    
    try:
        values.append(int(txt))
    except ValueError:
        
        pass

# report
print("Count", len(values))
print("Sum", sum(values))
