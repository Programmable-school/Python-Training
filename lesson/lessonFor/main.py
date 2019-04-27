"""
for文
  ループの回数を指定して処理を行う
  またリスト型の要素を1つづつ扱うことができる
"""

nums = [10, 20, 30, 40, 50, 60]

for value in nums:
  print(value)
# 10
# 20
# 30
# 40
# 50
# 60

for value in nums:
  # valueが30の時にループを抜ける
  if value == 30:
    print('BREAK')
    break
  print(value)
# 10
# 20
# BREAK


for value in nums:
  # valueが30の場合はそれ以降の処理をスキップする
  if value == 30:
    print('SKIP')
    continue
  print(value)  
# 10
# 20
# SKIP
# 40
# 50
# 60

# ループ正常終了後の処理（※Breakをした場合はelseは呼ばれない）
for value in nums:
  print(value)    # 10 ... 60
else:
  print('FINISH') # FINISH
# 10
# 20
# 30
# 40
# 50
# 60
# FINISH

# インデックスカウンタ range
for i in range(3):
  print(i)        # 0 ... 2
# 0
# 1
# 2

for i in range(3):
  for j in range(3):
    print(i, j)
# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2

# インデックスと要素 enumerate
for i, value in enumerate(nums):
  print(i, value) 
# 0 10
# 1 20
# 2 30
# 3 40
# 4 50
# 5 60
 
# 複数のリスト要素 zip
values1 = ['Taro', 'Hanako', 'Shun']
values2 = [40, 30, 20]
for name, age in zip(values1, values2):
  print(name, age)
# Taro 40
# Hanako 30
# Shun 20