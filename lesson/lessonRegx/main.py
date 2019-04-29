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
print('')

# search 存在する文字列（先頭から一致していなくてもよい）からパターンに一致する場合、結果を返す
print('---- search ----')
r_search = re.search(pattern2, content1)
print(r_search)
print(r_search.span())
print(r_search.group())
print('')

# findall 一致した文字列を全て返す
print('---- findall ----')
r_findall= re.findall(pattern2, content1)
print(r_findall)
print('')

# split　文字列を分割して配列で返す
print('---- split ----')
content1_list = content1.split(',')
print(content1_list)
print('')
