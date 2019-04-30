"""
Webスクレイピング 2
  Webページの情報を取得する。
  URLから取得したHTML要素をスクレイピングする
"""


from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.yahoo.co.jp/'
html = request.urlopen(url)

# スクレイピングする
soup = BeautifulSoup(html, 'html.parser')

# body要素を取得
body = soup.find('body')
print(body)