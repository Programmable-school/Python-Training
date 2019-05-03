"""
課題 Webスクレイピング
"""

from urllib import request
from bs4 import BeautifulSoup, ResultSet
import csv, os, datetime

filename = os.path.dirname(os.path.abspath(__file__)) + '/scraping_2.csv'
url = 'https://www.nikkei.com'
html = request.urlopen(url)

print('url is %s %s' % (url, datetime.datetime.today().strftime('%Y/%m/%d %H:%M:%S')))
soup = BeautifulSoup(html, 'html.parser')

content = soup.find('div', attrs={'id': 'JSID_baseRefreshNxTop2'})
topics = content.find_all('div', attrs={'class': 'm-miM09'})

# CSVへ書き込む
f = open(filename, 'w')
for i, item in enumerate(topics):
  try:
    element = item.find('h3', attrs={'class': 'm-miM09_title'})
    title = element.find('span', attrs={'class': 'm-miM09_titleL'})
    href = element.find('a')['href']
    writter = csv.writer(f)
    writter.writerow([i, title.string, url + href])
  except:
    pass
else:
  f.close()

# 出力したCSVを読み込む
with open(filename) as f:
  reader = csv.reader(f)
  for item in reader:
    print(item)
