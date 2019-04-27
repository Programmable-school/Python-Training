"""
データ型
  数値（整数）、数値（浮動小数点）、文字列、真偽値を扱える
"""

data_int = 10          # 数値（整数） int型
data_float = 10.1234   # 数値（浮動小数点数）float型
data_str = 'Hello'     # 文字列 str型
is_true = True         # 真偽値 bool型

print(data_int)        # 10
print(data_float)      # 10.1234
print(data_str)        # Hello
print(is_true)         # True

# 型変換
data_int_conv = int(data_float)    # float型からint型へ変換
data_float_conv = float(data_int)  # int型からfloat型へ変換
data_str_conv = str(data_float)    # float型からstr型へ変換
print(data_int_conv)         # 10
print(data_float_conv)       # 10.0
print(data_str_conv)         # 10.1234

# 型確認
print(type(data_int_conv), type(data_int_conv) is int)            # <class 'int'>   True
print(type(data_float_conv), type(data_float_conv) is float)      # <class 'float'> True
print(type(data_str_conv), type(data_str_conv) is str)            # <class 'str'>   True