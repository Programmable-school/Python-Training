"""
課題 リスト操作
"""

values = [
  {"name": "taro",   "score": 1},
  {"name": "ueno",   "score": 4},
  {"name": "tanaka", "score": 8},
]

func1 = lambda n: {"name": n["name"], "score": n["score"]*10}
print("map %s" % list(map(func1, values)))
