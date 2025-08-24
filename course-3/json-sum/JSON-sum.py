import ssl
import json
import urllib.request

# Import address
url = input("Enter location: ").strip()
if not url:
    url = "http://py4e-data.dr-chuck.net/comments_42.json"

print("Retrieving", url)

# SSL context 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Download and read
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, context=ctx) as resp:
    data = resp.read().decode("utf-8")

# Json
obj = json.loads(data)

# Extraction and summation
comments = obj.get("comments", [])
values = [int(item.get("count", 0)) for item in comments]

print("Count:", len(values))
print("Sum:", sum(values))
