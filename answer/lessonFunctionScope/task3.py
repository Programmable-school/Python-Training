"""
課題 関数・スコープ
"""
def add(x: float, y: float):
  print("%d + %d = %d" % (x, y, x + y))

def sub(x: float, y: float):
  print("%d - %d = %d" % (x, y, x - y))

def multi(x: float, y: float):
  print("%d * %d = %d" % (x, y, x * y))

def div(x: float, y: float):
  print("%d / %d = %d" % (x, y, x / y))

add(10, 2)
sub(10, 2)
multi(10, 2)
div(10, 2)
