"""
リスト型_タプル型
"""

"""
リスト型
  データの配列。同型のデータを複数扱える
"""
nums1 = [0, 1, 2, 3]
print(nums1)                # [0, 1, 2, 3]
print(nums1[0], nums1[3])   # 0 3

# 最後に新しい要素を追加
nums1.append(4)
print(nums1)               # [0, 1, 2, 3, 4]

# 先頭に新しい要素を追加
nums1.insert(0, 5)
print(nums1)               # [5, 0, 1, 2, 3, 4]

# 最後の要素を取得
last = nums1[-1]
print(last)                # 4

# 値の書き換え
nums1[0] = 1000
print(nums1)               # [1000, 0, 1, 2, 3, 4]

# 結合
nums2 = [200, 300, 400]
nums3 = nums1 + nums2
print(nums3)              # [1000, 0, 1, 2, 3, 4, 200, 300, 400]

# 要素数
length = len(nums3)
print(length)             # 9

# 存在する要素数を取得
num4 = [3, 3, 20, 30, 1, 2]
print(num4.count(3))      # 2

# 検索（要素の位置を取得）
print(nums3.index(1000))  # 0
print(nums3.index(200))   # 6

# 削除（要素を指定）
nums3.remove(1000)        # [0, 1, 2, 3, 4, 200, 300, 400]
print(nums3)

# 削除（末端）
lastPop = nums3.pop()
print(lastPop, nums3)     # 400 [0, 1, 2, 3, 4, 200, 300]

# 参照渡し
list1 = [0, 1, 2, 3]
print('list1', list1)     # list1 [0, 1, 2, 3]
list2 = list1
list2[2] = 100
print('list1', list1)     # list1 [0, 1, 100, 3]
print('list2', list2)     # list2 [0, 1, 100, 3]

"""
タプル型
  違う型のデータを複数扱える
"""
values = (0, 10.123, 'Hello')
print(values)                 # (0, 10.123, 'Hello')
print(values[0], values[2])   # 0 Hello

print(values.index('Hello'))  # 2
print(values.count('Hello'))  # 1

# スライス
slice_values = [10, 20, 30, 40]

# 要素の位置の1〜3番目を表示
print(slice_values[1:4]) # [20, 30, 40]

# 要素の位置の0〜1番目を表示
print(slice_values[:2])  # [10, 20]

# 要素の位置の2番目以降
print(slice_values[2:])  # [30, 40]

