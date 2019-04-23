"""
型判定
  データの型判定を行う
  型判定はtype()とisinstance()の2種類ある
"""

class User:
  def __init__(self):
    pass

class ManUser(User):
  def __init__(self):
    super().__init__()

str_value = "string"
int_value = 100
float_value = 1.23
is_value = True
list_value = [0, 1, 2, 3]
user = User()
man_user = ManUser()

print(type(str_value))        # <class 'str'>
print(type(int_value))        # <class 'int'>
print(type(float_value))      # <class 'float'>
print(type(is_value))         # <class 'bool'>
print(type(list_value))       # <class 'list'>
print(type(user))             # <class '__main__.User'>

# typeでの型判定
print(type(str_value) is str)       # True
print(type(int_value) is int)       # True
print(type(float_value) is float)   # True
print(type(is_value) is bool)       # True
print(type(list_value) is list)     # True
print(type(user) is User)           # True


# isinstance 第1引数が確認するデータ 第2引数が確認したい型
print(isinstance(str_value, str))   # True
print(isinstance(int_value, str))   # True
print(isinstance(user, User))       # True


"""
type()とisinstance()との違い
  type():       子クラスに対して親クラスの型判定した場合はFalseになる
  isinstance(): 子クラスに対して親クラスの型判定した場合はTrueになる
"""
print(type(user))                   # True
print(type(man_user))               # True

print(type(user) is User)           # True
print(type(man_user) is User)       # False

print(isinstance(user, User))       # True
print(isinstance(man_user, User))   # True
print(isinstance(int_value, bool))  # False
print(isinstance(int_value, int))   # True

# boolはintの子クラスのため bool型は全てint型と見なされてしまう
print(isinstance(is_value, bool))   # True
print(isinstance(is_value, int))    # True


