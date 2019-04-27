"""
課題 TypeAliases
"""
from typing import List

Str = str
Strs = List[str]

def show_value(a: Str):
  print("show_value: %s" % (a))

def show_values(a: Strs):
  print("show_values: %s" % (a))

show_value("a")
show_values(["a", "b", "c"])
