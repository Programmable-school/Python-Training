"""
Lambda
  無名関数
  lambda 引数:返り値 で実装する
"""

func1 = lambda x: x*3
func2 = lambda x, y: x + y
func3 = lambda x: 'Good' if x == 1 else 'Unknow'
print(func1(10))      # 30
print(func2(10, 2))   # 12
print(func3(1))       # Good
print(func3(2))       # Unknow
