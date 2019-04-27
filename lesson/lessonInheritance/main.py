"""
継承
  クラスを継承することで継承先の資産を利用することができる
"""

# 親クラス（スーパークラス）
class BaseUser:
  def __init__(self, name: str):
    self.name = name
  def show_profile(self):
    print('My name is %s.' % self.name)
  def show_base_user(self):
    print('My class is BaseUser.')

# 子クラス（サブクラス） BaseUserを継承する
class ManUser(BaseUser):
  """
    オーバーライド
      親クラスの関数を上書きする
      この場合は__init__、show_profileの関数を子クラスが上書きして利用している
  """
  def __init__(self, name: str, age: int):
    """
      親クラスの資産を利用する場合は super() で指定する
      親クラスのコンストラクタを呼ぶ
    """
    super().__init__(name)

    # 子クラスの変数を設定
    self.age = age

    # 親クラスの変数を上書きする
    self.name = name

  def show_profile(self):
    print('My name is %s. I\'m %d yeras old.' % (self.name, self.age))
  
  """
    勿論、子クラスだけの関数を定義できる
  """
  def show_man_user(self):
    print('My class is ManUser.')
    

user1 = ManUser('Taro', 20)

# 親クラスの関数を呼ぶ
user1.show_base_user()    # My class is BaseUser.

# 子クラスの関数を呼ぶ
user1.show_man_user()     # My class is ManUser.

# 親クラスの関数をオーバーライドした子クラスの関数を呼ぶ
user1.show_profile()      # My name is Taro. I'm 20 years old.
