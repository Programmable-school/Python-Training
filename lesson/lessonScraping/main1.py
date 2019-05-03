"""
Webスクレイピング 1
  Webページの情報を取得する。
"""

from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html>
  <head>
    <title>Webスクレイピング</title>
  </head>
  <body>
    <div id="wrapper">
      <h1>タイトル</h1>
      <ul class="content">
        <li class="one">コンテンツ1</li>
        <li class="two">コンテンツ2</li>
        <li class="three">コンテンツ3</li>
      </ul>
    </div>
  </body>
</html>
"""

# スクレイピングする
soup = BeautifulSoup(html, 'html.parser')

# body要素を取得
body = soup.find('body')
# print(body)

# findで指定したタグの要素を取得
wrapper = soup.find('div', attrs={'id': 'wrapper'})
# print(wrapper)

# 取得した要素のタグは.指定で確認できる
print(wrapper.h1.string)        # タイトル

# find_allで指定した要素の取得
li_list = soup.find_all('li')   # [<li>コンテンツ1</li>, <li>コンテンツ2</li>, <li>コンテンツ3</li>
print(li_list)
for li in li_list:
  print(li.string)
# コンテンツ1
# コンテンツ2
# コンテンツ3

# HTML要素のvalueを取得
for li in li_list:
  try:
    # getで指定したHTML要素のvalueを取得
    value = li.get('class').pop(0)
    print(value)
    # one
    # two
    # three
    if value == 'two':
      print('This is two')  # This is two
  except:
    pass


"""
スクレイピングしたデータをCSVへ出力する
"""

import csv, os, datetime

filename = os.path.dirname(os.path.abspath(__file__)) + '/scraping_1_' + datetime.datetime.today().strftime('%Y%m%d_%H%M%S') + '.csv'

# 書き込み
f = open(filename, 'w')
for i, item in enumerate(li_list):
  writer = csv.writer(f)
  writer.writerow([i, item.string])
else:
  f.close()

# 読み込み
with open(filename) as f:
  reader = csv.reader(f)
  for item in reader:
    print(item, item[0], item[1])
# ['0', 'コンテンツ1'] 0 コンテンツ1
# ['1', 'コンテンツ2'] 1 コンテンツ2
# ['2', 'コンテンツ3'] 2 コンテンツ3
