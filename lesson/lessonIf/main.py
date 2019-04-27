"""
if文
  条件判断 データの値が任意の条件を満たすと任意の処理を行う
"""

# if文
def func1(value: int):
  if value == 1:
    print('value is 1')
  elif value == 3:
    print('value is 3')
  else:
    print('value is not 1')

def func2(score: int):
  if (80 <= score and score <= 100):
    print('Good')
  elif (60 <= score and score < 80):
    print('Normal')
  elif (20 <= score and score < 60):
    print('Bad')
  else:
    print('ahahaha..')

# 条件演算子
def func3(score: int):
  print('Good' if 100 >= score and score >= 80 else 'ahahaha')


func1(1)    # value is 1
func1(2)    # value is not 1
func1(3)    # value is 3

func2(96)   # Good
func2(72)   # Normal
func2(27)   # Bad
func2(0)    # ahahaha..

func3(100)  # Good
func3(79)   # ahahaha
