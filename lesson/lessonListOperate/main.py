"""
リスト操作
"""

"""
sort
  値を昇順・降順で並べ換える（ソート）
"""
# sort
values1 = [20, 41, 2, 30, 4, 50]
values1.sort()
print('sort %s' % (values1))          # sort [2, 4, 20, 30, 41, 50]
values1.sort(reverse=True)
print('sort %s' % (values1))          # sort [50, 41, 30, 20, 4, 2]

# sorted
values2 = [20, 41, 2, 30, 4, 50]
print('sorted %s' % sorted(values2))  # sorted [2, 4, 20, 30, 41, 50]

# 辞書型をソート
values3 = [
  {'name': 'taro',   'age': 20},
  {'name': 'hanako', 'age': 64},
  {'name': 'ueno',   'age': 32}
]
print('sorted %s' % sorted(values3, key=lambda x:x['age']))                # sorted [{'name': 'taro', 'age': 20}, {'name': 'ueno', 'age': 32}, {'name': 'hanako', 'age': 64}]
print('sorted %s' % sorted(values3, key=lambda x:x['age'], reverse=True))  # sorted [{'name': 'hanako', 'age': 64}, {'name': 'ueno', 'age': 32}, {'name': 'taro', 'age': 20}]

"""
map
  リストの要素を加工する
"""
values4 = [1, 2, 3, 4, 5]
r1 = list(map(lambda n:n*3, values4)) # 全ての要素を3倍にする
print('map %s' % r1)    # map [3, 6, 9, 12, 15]

"""
filter
  リストから特定の要素を取り出す（フィルタリング）
"""
values5 = [1, 2, 3, 4, 5]
r2 = list(filter(lambda n: n % 2 == 0, values5))  # 2の倍数の要素だけにフィルタリングする
print('filter %s' % r2)  # filter [2, 4]
