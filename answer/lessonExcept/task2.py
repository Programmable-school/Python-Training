"""
課題 例外処理
"""

try:
  for i in range(5):
    print(i)
    if i == 3:
      raise NameError('error by raise')
except NameError as e:
  print('except', e)
