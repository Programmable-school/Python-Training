"""
変数と定数
"""

# 変数
msg = 'Hello World'
print(msg)  # Hello World

msg = 'Hello OCA'
print(msg)  # Hello OCA

count = 1
count += 1
print(count)  # 2

# １行で複数の変数に値を設定できる
a, b = 100, 'score'
print(a, b)   # 100 score

# 定数
"""
Pythonは定数はサポートされていないが、一般的なコーディング規約として定数として扱う場合は全て大文字で表現する
"""
MSG = 'Hello World'     # 定数表現
print(MSG)
