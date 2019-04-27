"""
イテレータ_ジェネレータ
"""

"""
イテレータ
  要素を反復して取り出せる手段
"""

values = [0, 1, 2, 3, 4, 5]
it = iter(values) # イテレータ化

print('iter %d' % (next(it))) # iter 0
print('iter %d' % (next(it))) # iter 1
print('iter %d' % (next(it))) # iter 2

# for文で残りの要素を取り出す
for i in it:
  print('iter %d' % (i))
# iter 3
# iter 4
# iter 5

# itの取り出せる要素がないためエラーとなる
# next(it) # error

"""
ジェネレータ
  値を返しつつ内部の処理は継続して実施する、返す値はyieldで指定する

yield
  関数の処理を一旦停止し、値を返す
  returnの場合は関数の処理を終了して値を返すが、yieldは処理を続行する

用途
  メモリの使用量を節約できるため。容量が大きいデータを扱う場合に有効
"""

def gen1() -> int:
  i = 0
  # 例えば2000行のデータがあると仮定した場合、whileループないでyieldを使うことで1行毎に処理を返す
  while i < 2000: 
    yield i       
    i += 1

data = gen1()
for i in data:
  print('gene %d' % (i))
  if i == 5:
    break
# gene 0
# gene 1
# gene 2
# gene 3
# gene 4
# gene 5

for i in data:
  # 前のfor文で返した値を記憶しているため、次のデータから取得することができる
  print('gene %d' % (i))
  if i == 10:
    break
# gene 6
# gene 7
# gene 8
# gene 9
# gene 10


def gen2():
  a = 10
  yield a
  b = 20
  yield b
  c = 30
  yield c

# __next__でyieldで指定された値を順次取り出す
gen = gen2()
print(gen.__next__())   # 10
print(gen.__next__())   # 20
print(gen.__next__())   # 30
