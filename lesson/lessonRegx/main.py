"""
正規表現
"""

import re

content1: str = 'abcdefg,-,12345678,ABCD,abc,efg,?,123efg456' 
pattern1: str = 'abcd'
pattern2: str = 'efg'
pattern3: str = r'[a-z]+'

# match 先頭から文字列からパターンに一致する場合、結果を返す
r_match = re.match(pattern1, content1)
print('---- match ----')
print(r_match)
print(r_match.span())
print(r_match.group())

# search 存在する文字列（先頭から一致していなくてもよい）からパターンに一致する場合、結果を返す
print('---- search ----')
r_search = re.search(pattern2, content1)
print(r_search)
print(r_search.span())
print(r_search.group())

# findall 一致した文字列を全て返す
print('---- findall ----')
print(re.findall(pattern2, content1))

# split　文字列を分割して配列で返す
print('---- split ----')
print(content1.split(','))

# replace 文字列を指定して置換する
print('---- replace ----')
print(content1.replace('abc', 'ABC'))

# translate 複数の文字を指定して置換する。変換テーブルはstr.maketransを使用する、但し指定する文字は1文字でなけれえばならない。
print('---- translate ----')
print(content1.translate(str.maketrans({'a': 'A', 'b': 'B', 'c': 'C'})))

# sub 正規表現で置換する
print('---- sub, subn ----')
print(re.sub(pattern3, 'ABC', content1))

# 第4引数で最大置換回数を指定できる
print(re.sub(pattern3, 'ABC', content1, 1)) 

# subn 置換回数を取得
r_subn = re.subn(pattern3, 'ABC', content1)
print(r_subn)
print(r_subn[0])
print(r_subn[1])
