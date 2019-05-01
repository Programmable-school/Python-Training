"""
with文
  終了処理を自動的に行ない、安全に処理できる。
  クラス内に定義されている。
  __enter__, __exit__, __del__　の処理が自動的に実行される。
"""


import os

filename = os.path.dirname(os.path.abspath(__file__)) + '/output.txt'
print(filename)

"""
open
  with文を使うことでclose処理は自動的に行われる
"""

# write
with open(filename, 'w') as text:
  text.write('Hello world')

# read 
with open(filename) as text:
  print(text.read())  # Hello world

"""
Userクラスにwith文で実行される処理を実装する
  1. __enter__が呼ばれる
  2. with内の処理が実行
  3. with内の処理が終了後、__exist__が呼ばれる
  4. __del__が呼ばれる
"""
class User:
  def __init__(self, name: str):
    self.name: str = name
  def __enter__(self):
    print('enter')
    return self
  def __exit__(self, type, value, traceback):
    print('exit', type, value, traceback)
    return self
  def __del__(self):
    print('del')
    return self
  def show_name(self):
    print(self.name)

with User('taro') as u:
  u.show_name()
# enter
# taro
# exit None None None
# del