"""
データ型
"""

dataInt = 10          # 数値（整数） int型
dataFloat = 10.1234   # 数値（浮動小数点数）float型
dataStr = "Hello"     # 文字列 str型
isTrue = True         # 真偽値 bool型

print(dataInt)        # 10
print(dataFloat)      # 10.1234
print(dataStr)        # Hello
print(isTrue)         # True

# 型変換
dataIntConv = int(dataFloat)    # float型からint型へ変換
dataFloatConv = float(dataInt)  # int型からfloat型へ変換
dataStrConv = str(dataFloat)    # float型からstr型へ変換
print(dataIntConv)         # 10
print(dataFloatConv)       # 10.0
print(dataStrConv)         # 10.1234

# 型確認
print(type(dataIntConv), type(dataIntConv) is int)            # <class 'int'>   True
print(type(dataFloatConv), type(dataFloatConv) is float)      # <class 'float'> True
print(type(dataStrConv), type(dataStrConv) is str)            # <class 'str'>   True