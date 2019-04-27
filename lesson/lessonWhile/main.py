"""
while文
  for文と同様にループの回数を指定して処理を行う
"""

# whileループ elseを用いることでループ終了後の処理を実行できる
i = 0
while i < 3:
  print('loop i: %d' % (i))
  i += 1
else:
  print('FINISH')
# loop i: 0
# loop i: 1
# loop i: 2
# FINISH


# 途中でループを抜ける（Break）
j = 0
while j < 10:
  if j == 3:
    break
  print('loop j: %d' % (j))
  j += 1
# loop j: 0
# loop j: 1
# loop j: 2


# 処理をスキップする（continute）
k = 0
while k < 3:
  if  k == 1:
    print('CONTINUE')
    k += 1
    continue
  print('loop k: %d' % (k))
  k += 1
# loop k: 0
# CONTINUE
# loop k: 2
