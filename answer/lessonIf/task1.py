"""
課題 if文
"""

def func1(value: int):
  if (1 <= value and value <= 10):
    return 'Top Ranker'
  elif (10 < value and value < 50):
    return 'Ranker'
  elif (50 < value and value <= 100):
    return 'Normal Ranker'
  else:
    return 'Unknow'

print('value 1: %s' % (func1(1)))
print('value 13: %s' % (func1(13)))
print('value 90: %s' % (func1(90)))
print('value 200: %s' % (func1(200)))