"""
辞書型
  {key: value}の形式のデータ
"""

values1 = {'id': 0, 'name': 'Taro'}
print(values1, values1['id'], values1['name']) # {'id': 0, 'name': 'Taro'} 0 Taro

# 置き換え
values1['name'] = 'Hanako'
print(values1) # {'id': 0, 'name': 'Hanako'}

# 追加
values1['age'] = 30
print(values1) # {'id': 0, 'name': 'Hanako', 'age': 30}

# 削除
del(values1['age'])
print(values1) # {'id': 0, 'name': 'Hanako'}


"""
辞書型データをforループで処理
"""
values2 = {'id': 0, 'name': 'Taro', 'age': 30}

# keyとvalue
for k, v in values2.items():
  print('key value: %s %s' % (k, v))
# key value: id 0
# key value: name Taro
# key value: age 30

# keyのみ
for k in values2.keys():
  print('key only: %s' % k)
# key only: id
# key only: name
# key only: age

# valueのみ
for v in values2.values():
  print('value only %s' % v)
# value only: 0
# value only: Taro
# value only: 30
