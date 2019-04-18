"""
関数・スコープ
"""

# 関数
def func1():
  print("関数です")

def func2(value):
  print(value)

def func3(x, y):
  return x + y

# デフォルト引数
def func4(x, y = 10):
  return x + y

# パス付き関数 中身のない関数
def funcPass():
  pass

func1()               # 関数です
func2("Kansudesu")    # Kansudesu
print(func3(10, 2))   # 12
print(func4(10))      # 20
print(funcPass())     # None


# スコープ
const1 = 0
const2 = 10
def scopeFunc():
    # グローバル変数の参照はできるが書き換えができない
    print(const1)   # 0   

    # global をつけることで書き換えができる
    global const2      
    const2 += 20
    print(const2)   # 30
    
scopeFunc()