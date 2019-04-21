"""
課題 クラス
"""

class Util:
  def __init__(self):
    pass
  def add(self, x, y):
    return x + y
  def sub(self, x, y):
    return x - y
  def multi(self, x, y):
    return x * y
  def div(self, x, y):
    return x / y

x = 10
y = 3
util = Util()
print("%d + %d = %d" % (x, y, util.add(x, y)))
print("%d - %d = %d" % (x, y, util.sub(x, y)))
print("%d * %d = %d" % (x, y, util.multi(x, y)))
print("%d / %d = %f" % (x, y, util.div(x, y)))