"""
Webスクレイピング 2
  Webページの情報を取得する。
  URLから取得したHTML要素をスクレイピングする
"""


from urllib import request
from bs4 import BeautifulSoup
import csv, os, datetime

filename = os.path.dirname(os.path.abspath(__file__)) + '/scraping_2_' + datetime.datetime.today().strftime('%Y%m%d_%H%M%S') + '.csv'

url = 'https://newspicks.com/'
html = request.urlopen(url)

# newsのtopicをスクレイピングする
soup = BeautifulSoup(html, 'html.parser')
news_cards = soup.find_all('div', attrs={'class': 'news-card vertical'})

f = open(filename, 'w')
for i, news in enumerate(news_cards):
  try:
    # topicのtitleとhrefを取得
    a = news.find('a')
    href = a.attrs['href']
    title = a.find('div', attrs={'class': 'title'}) 

    # 出力
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
# ['0', 'GoogleがChromeとアプリの履歴、位置情報履歴の自動削除機能を発表', 'https://newspicks.com//news/3865077?ref=index&block=top']
# ['1', '【山崎元】新入社員がGWに考えたい「初任給からのマネー習慣」', 'https://newspicks.com//news/3857889?ref=index&block=top']
# ['2', 'NASA下請けが約20年間アルミ素材の品質認証を偽造。衛星の軌道投入失敗で7億ドルの損失', 'https://newspicks.com//news/3865040?ref=index&block=top']
# ['3', 'アマゾン、倉庫の完全自動化の可能性排除\u3000「あと10年かかる」', 'https://newspicks.com//news/3864754?ref=index&block=top']
# ['4', '改元特番でＮＨＫだけが伝えた”不都合な真実”', 'https://newspicks.com//news/3864189?ref=index&block=top']
# ['5', 'ＦＲＢ金利据え置き、経済・労働情勢は「堅調」\u3000当面現状維持へ', 'https://newspicks.com//news/3864735?ref=index&block=top']
