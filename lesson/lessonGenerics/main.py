"""
Generics 総称型
  型をパラメータのように扱うことができる
  関数内などで束縛されず汎用的に扱うことができる
"""

from typing import TypeVar, Sequence, Generic


# Genericsで型変数Tを定義
T = TypeVar('T')

# 引数T型のListを引数でT型のデータを戻り値とする関数
def func1(l: Sequence[T]) -> T:
  return l[0]
print(func1([1, 2, 3]))   # 1


"""
int、floatに制約できる
  制約する場合、TypeVarは１つの型だけでだとエラーになるため、必ず2つ以上の型を指定する。
  int, float以外の型を入れても動作する、IDE上で合っていないことを教えてくれるのみ
"""
U = TypeVar('U', int, float)
def func2(l: Sequence[U]) -> U:
  return l[0]
print(func2([1.4, 2, 3.3])) # 1.4


"""
ClassにGenericsを用いる
  型変数をクラス定義に設定し、インスタンス生成時に型定義を明示する
"""
V = TypeVar('V')
class Model(Generic[V]):
  def __init__(self):
    pass  
  def set_value(self, value: V):
    self.value: V = value
  def get_value(self) -> V:
    return self.value


# int型のvalueを持つModelを作成
model1 = Model[int]()
model1.set_value(100)
print(model1.get_value())   # 100

class User:
  def __init__(self):
    self.name: str = 'Taro'

# User型のvalueを持つModelを作成
model2 = Model[User]()
model2.set_value(User())
print(model2.get_value().name)  # Taro

# Model型も制約できる
W = TypeVar('W', Model, Model)
def func3(l: Sequence[W]) -> W:
  return l[0].get_value()
print(func3([model1, model2]))  # 100

