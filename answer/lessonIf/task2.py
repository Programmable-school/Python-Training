"""
課題 if文
"""

def func1(x: float, y: float, type: int) -> float:
  if (type == 0):
    return x + y
  elif (type == 1):
    return x - y
  elif (type == 2):
    return x * y
  elif (type == 3):
    return x / y
  else:
    return 0

x = 10
y = 3
print('%d + %d: %d' % (x, y, func1(x, y, 0)))
print('%d - %d: %d' % (x, y, func1(x, y, 1)))
print('%d * %d: %d' % (x, y, func1(x, y, 2)))
print('%d / %d: %f' % (x, y, func1(x, y, 3)))