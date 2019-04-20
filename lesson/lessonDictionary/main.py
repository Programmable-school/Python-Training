"""
辞書型
  {key: value}の形式のデータ。
"""

values = {"id": 0, "name": "Taro"}
print(values, values["id"], values["name"]) # {'id': 0, 'name': 'Taro'} 0 Taro

# 置き換え
values["name"] = "Hanako"
print(values) # {'id': 0, 'name': 'Hanako'}

# 追加
values["age"] = 30
print(values) # {'id': 0, 'name': 'Hanako', 'age': 30}

# 削除
del(values["age"])
print(values) # {'id': 0, 'name': 'Hanako'}

