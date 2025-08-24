import ssl
import urllib.request
import xml.etree.ElementTree as ET

#Input URL
url = input("Enter URL: ").strip()

# 2) SSL context 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# XML download with User-Agent
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, context=ctx) as resp:
    data = resp.read()  # bytes

# XML parser
tree = ET.fromstring(data)

# find all count parts
counts = tree.findall(".//count")

# int and summation
values = [int(c.text) for c in counts if c.text and c.text.strip().isdigit()]

print("Count", len(values))
print("Sum", sum(values))



   

