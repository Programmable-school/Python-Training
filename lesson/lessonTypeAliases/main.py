"""
TypeAliases
  型を別名で定義できる
"""
from typing import List

# intをIntに定義
Int = int

# List[int]をIntsに定義
Ints = List[int]

def show_value(a: Int):
  print('show_value: %d' % (a))

def show_values(a: Ints):
  print('show_values: %s' % (a))

show_value(0)           # show_value: 0
show_values([1, 2, 3])  # show_values: [1, 2, 3]
