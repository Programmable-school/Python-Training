"""
Callable
  defやlambdaで作った関数の引数と戻り値を型定義する
  主に関数の引数にCallable型として明示的に定義することで引数がdefやlambdaであることがわかるようにする
"""
from typing import Callable


# 引数の型をCallableで指定
def show_func(item: Callable[[int, int], str]) -> None:
  pass

