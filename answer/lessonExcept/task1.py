"""
課題 例外処理
"""

try:
  value = 30 / 0
except ZeroDivisionError as e:
  print('except', e)
