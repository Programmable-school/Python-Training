"""
関数_スコープ
  処理を関数という単位でまとめることができる（スコープ）
  関数にすると様々な箇所から呼ぶことができる
"""

# 関数
def func1():
  print('関数です')

def func2(value: str):
  print(value)

def func3(x: float, y: float) -> float:
  return x + y

# デフォルト引数
def func4(x: float, y: float = 10) -> float:
  return x + y

# 戻り値の型を指定する
def func5(x: float, y: float) -> float:
  return x + y

# パス付き関数 中身のない関数
def func_pass():
  pass



func1()                 # 関数です
func2('Kansudesu')      # Kansudesu
print(func3(10, 2))     # 12
print(func4(10))        # 20
print(func5(10.2, 2.5)) # 12.7
print(func_pass())      # None


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