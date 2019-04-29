"""
課題 リスト操作
"""

values = [
  {'name': 'taro',   'score': 10},
  {'name': 'ueno',   'score': 40},
  {'name': 'tanaka', 'score': 200},
  {'name': 'hanako', 'score': 90},
  {'name': 'baba',   'score': 120},
]

print('filter %s' % list(filter(lambda n: n['score'] > 100, values)))
