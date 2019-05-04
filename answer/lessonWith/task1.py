"""
課題 with文
"""

class Model:
  def __init__(self):
    pass
  def __enter__(self):
    print('enter %s' % self)
    return self
  def __exit__(self, type, value, traceback):
    print('exit %s' % self)
    return self
  def __del__(self):
    print('del %s' % self)
    return self

with Model() as item:
  pass
