"""
モジュール分割_パッケージ分割
"""
"""
モジュール
  関数やクラスなどをまとめて書いたファイルをモジュール
"""
# モジュールをインポート この場合はmathモジュールをインポート
import math

# モジュールをインポートして別名で使用できるようにする この場合はmathモジュールのpiをインポート
import math as mt

# モジュール内の関数をインポート この場合はmathモジュールのpiとradiansをインポート
from math import pi, radians
# モジュールの全てのオブジェクトを使用
# from math import *

print(math.pi)            # 3.141592653589793
print(mt.pi)              # 3.141592653589793
print(pi, radians(180))   # 3.141592653589793 3.141592653589793


"""
パッケージ
  モジュールと__init__.pyを含むディレクトリをパッケージという
  __init__.pyには初期化コード記述するが、空のファイルでも問題ない
"""
# 作成したpyファイルをインポート 別ファイルのpyファイルをインポート
import package.func1 
from package import func2

package.func1.hello_world()       # Hello World.
package.func1.show_name("Taro")   # My name is Taro.
func2.show_text("Yes, we can.")   # Yes, we can.
