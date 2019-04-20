"""
課題 イテレータ_ジェネレータ
"""

def gene():
  values = ["Hello", "world", "Good", "Morning"]
  for value in values:
    yield value

data = gene()
print(next(data))
print(next(data))
print(next(data))
print(next(data))
