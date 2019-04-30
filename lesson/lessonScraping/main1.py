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
        <li>コンテンツ1</li>
        <li>コンテンツ2</li>
        <li>コンテンツ3</li>
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
