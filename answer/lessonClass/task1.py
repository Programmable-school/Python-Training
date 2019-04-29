"""
課題 クラス
"""

class User:
  name = ''
  score = 0
  def __init__(self):
    pass
  
  def show(self):
    print('My name is %s. My score is %d.' % (self.name, self.score))

user = User()
user.name = 'Taro'
user.score = 100
user.show()
