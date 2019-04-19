"""
集合型
"""

# 順序なし、重複を許されないデータ型
values1 = set([0, 1, 2, 3, 4])
values2 = {0, 1, 2, 3, 4}
print(values1)  # {0, 1, 2, 3, 4}
print(values2)  # {0, 1, 2, 3, 4}

values3 = {0, 0, 1, 1, 2, 3, 4, 0, 5, 6}
print(values3)  # {0, 1, 2, 3, 4, 5, 6}

# 要素の確認
print(4 in values1)   # True
print(10 in values1)  # False

# 値を追加
values1.add(10)
print(values1)        # {0, 1, 2, 3, 4, 10}
print(10 in values1)  # True

# 値を削除
values1.remove(0)
print(values1)        # {1, 2, 3, 4, 10}
print(0 in values1)   # False


values4 = {1, 3, 5, 8}
values5 = {3, 5, 6, 10}

# 和集合
print(values4 | values5)  # {1, 3, 5, 6, 8, 10}

# 積集合
print(values4 & values5)  # {3, 5}

# 差集合
print(values4 - values5)  # {8, 1}
