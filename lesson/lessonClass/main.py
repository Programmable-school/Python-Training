"""
クラス
  オブジェクトのひとかたまりのデータ
  クラスには変数や関数を定義することができる
"""


class User1:
    # クラス変数
    name = 'user'
    age = 20


user1 = User1()
print('User1: %s %d' % (user1.name, user1.age))   # User1: user 20

user1.name = 'taro'
user1.age = 30
print('User1: %s %d' % (user1.name, user1.age))   # User1: taro 30


"""
コンストラクタ
  クラスを生成した際にはじめに呼ばれる関数
  クラス内部の初期化処理などを行う
"""


class User2:
    score = 0

    # コンストラクタ
    def __init__(self, name: str, age: int):
        # クラス変数にセットする
        self.name = name
        self.age = age
        self.score += 1


user2 = User2('hanako', 40)
print('User2: %s %d %d' % (user2.name, user2.age, user2.score))   # User2: hanako 40 1

user2.name = 'masayo'
user2.age = 100
user2.score += 1
print('User2: %s %d %d' % (user2.name, user2.age, user2.score))   # User2: masayo 100 2


"""
クラス関数
"""


class User3:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get(self):
        return {'name': self.name, 'age': self.age}

    def show_profile(self):
        print('My name is %s. I\'m %d years old.' % (self.name, self.age))


user3 = User3('ueno', 23)
print('User3: %s' % (user3.get()))  # User3: {'name': 'ueno', 'age': 23}
user3.show_profile()                # My name is ueno. I'm 23 yeras old.
