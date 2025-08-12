import sqlite3
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# --- SSL & UA ---
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
UA = {'User-Agent': 'Mozilla/5.0'}

# --- DB setup ---
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Pages(
  id INTEGER PRIMARY KEY,
  url TEXT UNIQUE,
  html BLOB,
  error INTEGER,
  old_rank REAL,
  new_rank REAL
)''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Links(
  from_id INTEGER,
  to_id   INTEGER,
  UNIQUE(from_id, to_id)
)''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Webs(
  url TEXT UNIQUE
)''')

# --- Start URL (quotes) ---
starturl = input('Enter web url or enter: ').strip()
if len(starturl) < 1:
  starturl = 'https://quotes.toscrape.com/'

# normalize trailing slash
if not starturl.startswith('http'):
  starturl = 'https://' + starturl
if starturl.endswith('/'):
  starturl = starturl[:-1]

# base web = scheme + host (برای فیلتر داخلی)
parts = urllib.parse.urlparse(starturl)
web = f"{parts.scheme}://{parts.netloc}"

cur.execute('INSERT OR IGNORE INTO Webs(url) VALUES (?)', (web,))
cur.execute('INSERT OR IGNORE INTO Pages(url, html, new_rank) VALUES (?, NULL, 1.0)', (starturl,))
conn.commit()

def get_page(id_url):
  """fetch page bytes or (None, code)"""
  try:
    req = urllib.request.Request(id_url, headers=UA)
    doc = urllib.request.urlopen(req, context=ctx)
    if doc.getcode() != 200:
      return (None, doc.getcode())
    ctype = doc.getheader('Content-Type') or ''
    if 'text/html' not in ctype:
      return (None, 'NONHTML')
    html = doc.read()
    return (html, 200)
  except Exception as e:
    return (None, -1)

many = 0
while True:
  if many < 1:
    sval = input('How many pages:').strip()
    if len(sval) < 1: break
    many = int(sval)

  # یک صفحه‌یِ واکشی‌نشده بردار
  cur.execute('SELECT id, url FROM Pages WHERE html IS NULL AND (error IS NULL) ORDER BY RANDOM() LIMIT 1')
  row = cur.fetchone()
  if row is None:
    print('No unretrieved HTML pages found')
    many = 0
    break

  from_id, url = row
  print(from_id, url, end=' ')

  # واکشی
  html, status = get_page(url)
  if html is None:
    if status == 'NONHTML':
      print('Ignore non text/html page')
      cur.execute('DELETE FROM Pages WHERE id=?', (from_id,))
    else:
      print('Error', status)
      cur.execute('UPDATE Pages SET error=? WHERE id=?', (status, from_id))
    conn.commit()
    many -= 1
    continue

  # ذخیره‌ی HTML
  print(f'({len(html)})', end=' ')
  cur.execute('UPDATE Pages SET html=? WHERE id=?', (memoryview(html), from_id))
  conn.commit()

  # پارس و استخراج لینک‌ها
  soup = BeautifulSoup(html, 'html.parser')
  tags = soup('a')
  count = 0

  for tag in tags:
    href = tag.get('href')
    if not href: 
      continue

    up = urllib.parse.urljoin(url, href)
    up = up.split('#')[0]                 # remove fragment
    up = up.rstrip('/')                   # normalize
    # فقط لینک‌های داخلی همین وب
    if not up.startswith(web): 
      continue

    # وارد کردن مقصد
    cur.execute('INSERT OR IGNORE INTO Pages(url, html, new_rank) VALUES (?, NULL, 1.0)', (up,))
    conn.commit()

    # گرفتن to_id مطمئن (lastrowid لزوماً معتبر نیست وقتی IGNORE میشه)
    cur.execute('SELECT id FROM Pages WHERE url=?', (up,))
    to_row = cur.fetchone()
    if not to_row: 
      continue
    to_id = to_row[0]

    # ثبت یال
    cur.execute('INSERT OR IGNORE INTO Links(from_id, to_id) VALUES (?, ?)', (from_id, to_id))
    count += 1

  conn.commit()
  print(count)
  many -= 1

cur.close()
