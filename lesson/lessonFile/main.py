"""
ファイルの入出力
"""

# 書き込み 新規作成 第2引数を'w'にする
file_name1 = 'lessonFile.txt'
fw = open(file_name1, 'w')
fw.write('Hello world.\n')
fw.close()


# 書き込み 追記 第2引数を'a'にする
fa = open(file_name1, 'a')
fa.write('[ADD] Fire!\n')
fa.close()


# 読み込み 第2引数を'r'にする
fr = open(file_name1, 'r')
for row in fr:
  print(row.strip()) # 空白文字を除去して表示
fr.close()
# Hello world.
# [ADD] Fire!


"""
osパッケージを利用してファイル操作する
"""
import os

# 存在確認　ファイル
def show_exist_file(path: str):
  if (os.path.exists(path)):
    print('%s is exist' % (path))
  else:
    print('%s is not exist' % (path))

file_name2 = 'dummy.txt'
fd = open(file_name2, 'w')
fd.write('file')
fd.close()
show_exist_file(file_name2) # dummy.txt is exist

# 削除
os.remove(file_name2)
show_exist_file(file_name2) # dummy.txt is not exist


"""
ディレクトリ作成 makedirs
  exist_ok
    Flase: 既にディレクトリがある場合はエラー
    True: 既にディレクトリがあってもエラーにならない
"""
# 存在確認　ディレクトリ
def show_exist_dir(path: str):
  if (os.path.isdir(path)):
    print('%s is exist' % (path))
  else:
    print('%s is not exist' % (path))

# ディレクトリを作成する
dir1 = 'new_dir1'
os.makedirs(dir1, exist_ok=True)
show_exist_dir(dir1)          # new_dir1 is exist

# ディレクトリの中にディレクトリを作成する
dir1_child1 = 'new_dir1/child1'
os.makedirs(dir1_child1, exist_ok=True)
show_exist_dir(dir1_child1)   # new_dir1/child1 is exist


"""
ディレクトリ削除 shutil
  os系のパッケージでは空のディレクトリは削除できないためshutilを使用する
"""
import shutil
shutil.rmtree(dir1)
show_exist_dir(dir1)          # new_dir1 is not exist
show_exist_dir(dir1_child1)   # new_dir1/child1 is not exist


"""
パスを取得
  パスを指定してファイル操作する際に利用する
"""
# カレントディレクトリまでの絶対パス
print(os.getcwd())

# 該当するファイルのカレントディレクトリ（作業ディレクトリ）からの相対パス
print(__file__)

# 該当するファイルがあるディレクトリのカレントディレクトリ（作業ディレクトリ）からの絶対パス
print(os.path.dirname(os.path.abspath(__file__)))
