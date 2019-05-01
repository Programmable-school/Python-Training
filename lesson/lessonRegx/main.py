"""
文字列操作_正規表現
"""

# 正規表現を利用する場合は re をimportする
import re

content1: str = 'abcdefg,-,12345678,ABCD,abc,efg,?,123efg456' 

"""
文字列操作
  置換、分割
"""
# replace 文字列を指定して置換する
print(content1.replace('abc', 'ABC'))   # ABCdefg,-,12345678,ABCD,ABC,efg,?,123efg456

# translate 複数の文字を指定して置換する。変換テーブルはstr.maketransを使用する、但し指定する文字は1文字でなけれえばならない。
print(content1.translate(str.maketrans({'a': 'A', 'b': 'B', 'c': 'C'})))    # ABCdefg,-,12345678,ABCD,ABC,efg,?,123efg456

# split　文字列を分割して配列で返す
print(content1.split(','))    # ['abcdefg', '-', '12345678', 'ABCD', 'abc', 'efg', '?', '123efg456']

"""
正規表現
  様々な文字列を一つの文字列で表現する。文字列の検索、置換、分割する際に利用される

  基本的な正規表現一覧
    https://murashun.jp/blog/20190215-01.html
"""

# 正規表現 小文字のaからzで1回以上繰り返す場合にマッチする
pattern1: str = 'abcd'
pattern2: str = 'efg'
pattern3: str = r'[a-z]+'

# match 先頭から文字列からパターンに一致する場合、結果を返す
r_match1 = re.match(pattern1, content1)
r_match2 = re.match(pattern3, content1)
print(r_match1)           # <_sre.SRE_Match object; span=(0, 4), match='abcd'>
print(r_match1.span())    # (0, 4)
print(r_match1.group())   # abcd
print(r_match2)           # <_sre.SRE_Match object; span=(0, 7), match='abcdefg'>
print(r_match2.span())    # (0, 7)
print(r_match2.group())   # abcdefg


# search 存在する文字列（先頭から一致していなくてもよい）からパターンに一致する場合、結果を返す
r_search1 = re.search(pattern2, content1)
r_search2 = re.search(pattern3, content1)
print(r_search1)          # <_sre.SRE_Match object; span=(4, 7), match='efg'>
print(r_search1.span())   # (4, 7)
print(r_search1.group())  # efg
print(r_search2)          # <_sre.SRE_Match object; span=(0, 7), match='abcdefg'>
print(r_search2.span())   # (0, 7)
print(r_search2.group())  # abcdefg

# findall 一致した文字列を全て返す
print(re.findall(pattern2, content1))   # ['efg', 'efg', 'efg']
print(re.findall(pattern3, content1))   # ['abcdefg', 'abc', 'efg', 'efg']

# sub 正規表現で置換する、第4引数で最大置換回数を指定できる
print(re.sub(pattern3, 'ABC', content1))      # ABC,-,12345678,ABCD,ABC,ABC,?,123ABC456
print(re.sub(pattern3, 'ABC', content1, 1))   # ABC,-,12345678,ABCD,abc,efg,?,123efg456

# subn 置換回数を取得
r_subn = re.subn(pattern3, 'ABC', content1)
print(r_subn)       # ('ABC,-,12345678,ABCD,ABC,ABC,?,123ABC456', 4)
print(r_subn[0])    # ABC,-,12345678,ABCD,ABC,ABC,?,123ABC456
print(r_subn[1])    # 4


"""
処理の高速化
  compileをすると処理が速くなる
"""

re_pattern = re.compile(pattern3)
re_match = re_pattern.match(content1)
re_search = re.search(re_pattern, content1)
print(re_match.group())   # abcdefg
print(re_search.group())  # abcdefg
print(re.findall(re_pattern, content1))     # ['abcdefg', 'abc', 'efg', 'efg']
print(re.sub(re_pattern, 'ABC', content1))  # ABC,-,12345678,ABCD,ABC,ABC,?,123ABC456
