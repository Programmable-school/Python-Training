"""
課題 リスト操作
"""

values = [
  {'name': 'taro',   'age': 20},
  {'name': 'ueno',   'age': 32},
  {'name': 'tanaka', 'age': 10},
]
print('asc %s' % sorted(values, key=lambda x:x['age']))                
print('desc %s' % sorted(values, key=lambda x:x['age'], reverse=True))