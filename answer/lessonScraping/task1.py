"""
課題 Webスクレイピング
"""

from bs4 import BeautifulSoup
import csv, os

filename = os.path.dirname(os.path.abspath(__file__)) + '/scraping_1.csv'

html = """
<!DOCTYPE html>
<html>
  <head>
    <title>Webスクレイピング</title>
  </head>
  <body>
    <div id="wrapper">
      <h1>タイトル</h1>
      <div class="content">
        <a href="https://newspicks.com/">NewsPicks</a>
        <a href="https://www.yahoo.co.jp/">Yahoo Japan</a>
        <a href="https://www.nikkei.com/">日本経済新聞</a>
      </div>
    </div>
  </body>
</html>
"""

# スクレイピングする
soup = BeautifulSoup(html, 'html.parser')

# body要素を取得
content = soup.find('content')
f = open(filename, 'w')
for i, a in enumerate(soup.find_all('a')):
  try:
    title = a.string
    href = a.attrs['href']
    writer = csv.writer(f)
    writer.writerow([i, a.string, href])
  except:
    pass
else:
  f.close()

# 読み込み
with open(filename) as f:
  reader = csv.reader(f)
  for item in reader:
    print(item)