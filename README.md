# Python-Training

> 初学者向け Python入門トレーニング

## 目次
- [Hello Worldを表示](#環境構築)
- [print文](#print文)
- [変数と定数](#変数と定数)
- [データ型](#データ型)
- [演算子](#演算子)
- [関数_スコープ](#関数_スコープ)
- [リスト型_タプル型](#リスト型_タプル型)
- [集合型](#集合型)
- [辞書型](#辞書型)
- [if文](#if文)
- [for文](#for文)
- [while文](#while文)
- [イテレータ_ジェネレータ](#イテレータ_ジェネレータ)
- [Lambda](#Lambda)
- [リスト操作](#リスト操作)
- [クラス](#クラス)
- [継承](#継承)
- [型判定](#型判定)
- [モジュール分割_パッケージ分割](#モジュール分割_パッケージ分割)
- [日付関数](#日付関数)
- [数学関数](#数学関数)
- [例外処理](#例外処理)
- [ファイルの入出力](#ファイルの入出力)
- [with文](#with文)
- [TypeAliases](#TypeAliases)
- [Generics](#Generics)
- [文字列操作_正規表現](#文字列操作_正規表現)
- [Webスクレイピング](#Webスクレイピング)

## 開発環境
- Python 3.6.5 以上

## 手順
### 環境構築
・Pycharm<br>
[https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/)

### Hello worldを表示する
任意のディレクトリ作成し、その中にmain.pyを作成して以下のコードを実装してください。

```python
print('Hello World')
```

プログラムの実行方法は以下の通りです。

```sh
# 実行
# python3 <実行したいpyファイルのパス>
$ python3 lesson/lessonHelloWorld/main.py 

# 実行結果が表示される
Hello World
```

これで環境構築は完了です。

## トレーニング
pythonの文法を学びます。サンプルコードを写経し実行した後、課題を進めてください。

### print文

```sh
# 実行
$ python3 lesson/lessonPrint/main.py 
```

[ソースコード](./lesson/lessonPrint/main.py)

#### 課題
##### 課題 1
「Good Job!」を表示してください。

```sh
# 実行
$ python3 answer/lessonPrint/task1.py 

# 出力
Good Job!
```

### 変数と定数
```sh
# 実行
$ python3 lesson/lessonVarConst/main.py
```

[ソースコード](./lesson/lessonVarConst/main.py)

#### 課題
##### 課題 1
二つの文字列（HelloとWorld）を連結して表示してください。

```sh
# 実行
$ python3 answer/lessonVarConst/task1.py 

# 出力
Hello World
```

##### 課題 2
二つの数字を足し算した結果を表示してください。

```sh
# 実行
$ python3 answer/lessonVarConst/task2.py 

# 出力
7
```

### データ型

```sh
# 実行
$ python3 lesson/lessonDataType/main.py 
```

[ソースコード](./lesson/lessonDataType/main.py)


#### 課題
##### 課題 1
20.123をfloat型で表示してください。またfloat型であることを証明してください。

```sh
# 実行
$ python3 answer/lessonDataType/task1.py 

# 出力
20.123 <class 'float'> True
```

##### 課題 2
float型の20.123をstr型で表示してください。またstr型であることを証明してください。

```sh
# 実行
$ python3 answer/lessonDataType/task2.py 

# 出力
20.123 <class 'str'> True
```

### 演算子

```sh
# 実行
$ python3 lesson/lessonOperator/main.py 
```

[ソースコード](./lesson/lessonOperator/main.py)


#### 課題
##### 課題 1
20と7の二つの数字をそれぞれ計算した結果を表示してください。<br>
足し算、掛け算、割り算、除算、余り、べき乗。

```sh
# 実行
$ python3 answer/lessonOperator/task1.py 

# 出力
23 60 6.666666666666667 6 2 8000
```

##### 課題 2
以下の文字列からマッチする単語を見つけてin演算子で単語が含まれていることを証明してください。

文字列：Attention: Mr. John Smith Human Resources Department AAA Company

```sh
# 実行
$ python3 answer/lessonOperator/task2.py 

# 出力
Attention: Mr. John Smith Human Resources Department AAA Company
Attention True
Resources True
Company True

```

### 関数_スコープ

```sh
# 実行
$ python3 lesson/lessonFunctionScope/main.py 
```

[ソースコード](./lesson/lessonFunctionScope/main.py)


#### 課題
##### 課題 1
「こんにちは」と返す関数を実装してください。

```sh
# 実行
$ python3 answer/lessonFunctionScope/task1.py 

# 出力
こんにちは
```

##### 課題 2
デフォルト引数を使って変数の指定有無に関わらず文字列を表示する関数を実装してください。

```sh
# 実行
$ python3 answer/lessonFunctionScope/task2.py 

# 出力
# func1()
Hello

# func1("Good Morning")
Good Morning
```

##### 課題 3
「足し算」「引き算」「掛け算」「割り算」するそれぞれ４つの関数を実装してください。

```sh
# 実行
$ python3 answer/lessonFunctionScope/task3.py 

# 出力
10 + 2 = 12
10 - 2 = 8
10 * 2 = 20
10 / 2 = 5
```

### リスト型_タプル型

```sh
# 実行
$ python3 lesson/lessonListTuple/main.py 
```

[ソースコード](./lesson/lessonListTuple/main.py)


#### 課題
##### 課題 1
文字列のリスト型を作り、全ての要素を表示してください。

```sh
# 実行
$ python3 answer/lessonListTuple/task1.py 

# 出力
['a', 'i', 'u', 'e', 'o']
```

##### 課題 2
文字列のリスト型を２つを連結して新しいリスト型を作り、全ての要素を表示してください。


```sh
# 実行
$ python3 answer/lessonListTuple/task2.py 

# 出力
values1 ['a', 'i', 'u', 'e', 'o']
values2 ['ka', 'ki', 'ku', 'ke', 'ko']
values3 ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko']
```

##### 課題 3
文字列のリスト型を作り、「リストの長さ」「先頭の要素」「末端の要素」を表示してください。

```sh
# 実行
$ python3 answer/lessonListTuple/task3.py 

# 出力
values1 ['a', 'i', 'u', 'e', 'o']
length 5
first a
last o
```

##### 課題 4
以下のリスト型から "World" が格納されている位置と "!" の個数を表示してください。

```
["Hello", "World", "!", "Good", "Morning", "!"]
["World", "Wide", ".", "!", "Morning", "!"]
```

```sh
# 実行
$ python3 answer/lessonListTuple/task4.py 

# 出力
values1 ['Hello', 'World', '!', 'Good', 'Morning', '!']
values1 index:1 count:2
values2 ['World', 'Wide', '.', '!', 'Morning', '!']
values2 index:0 count:2
```

##### 課題 5
タプル型を作り、全ての要素を表示してください。

```sh
# 実行
$ python3 answer/lessonListTuple/task5.py 

# 出力
('Hello', 100, 'World', 0.123)
```

### 集合型

```sh
# 実行
$ python3 lesson/lessonSet/main.py 
```

[ソースコード](./lesson/lessonSet/main.py)


#### 課題
##### 課題 1
以下の集合型データから "Hello" が含まれていることを証明してください。

```python
values = {0, "H", "e", "Good", "Hello", "Morning", 100} 
```

```sh
# 実行
$ python3 answer/lessonSet/task1.py 

# 出力
{0, 'Morning', 100, 'Good', 'e', 'H', 'Hello'}: Hello is True
```

##### 課題 2
以下の二つの集合型データの和集合・積集合・差集合した結果を表示してください。

```python
values1 = {0, 10, 200, 1000, 2, 100} 
values2 = {0, 0.01, 2, 600, 10, 100}
```

```sh
# 実行
$ python3 answer/lessonSet/task2.py 

# 出力
OR: {0, 2, 100, 1000, 200, 10, 0.01, 600}
AND: {0, 2, 10, 100}
DIFF: {1000, 200}
```

### 辞書型

```sh
# 実行
$ python3 lesson/lessonDictionary/main.py
```

[ソースコード](./lesson/lessonDictionary/main.py)


#### 課題
##### 課題 1
以下の情報の辞書型データを作成してください。

```
name: Sakurai
age: 20
hobby: eating
like: music
girlfriend: nothing
```

```sh
# 実行
$ python3 answer/lessonDictionary/task1.py 

# 出力
{'name': 'Sasuke', 'age': 20, 'hobby': 'eating', 'like': 'music', 'girlFriend': 'nothing'}
```

##### 課題 2
以下の辞書型データから"hobby"と"isHasGirldFriend"の値を表示してください

```python
values = {"name": "Sasuke", "age": 20, "hobby": "running", "like": "music", "isHasGirlFriend": False}
```

```sh
# 実行
$ python3 answer/lessonDictionary/task1.py 

# 出力
hobby is running
isHasGirlFriend is 0
```

### if文

```sh
# 実行
$ python3 lesson/lessonIf/main.py 
```

[ソースコード](./lesson/lessonIf/main.py)


#### 課題
##### 課題 1
valueの値に応じて以下の文字列を返す関数を実装してください。

```
範囲: 1 <= value <= 10  文字列: "Top Ranker"
範囲: 10 < value < 50   文字列: "Ranker"
範囲: 50 < value <= 100 文字列: "Normal Ranker"
範囲: else              文字列: "Unknow"
```

```sh
# 実行
$ python3 answer/lessonIf/task1.py 

# 出力
value 1: Top Ranker
value 13: Ranker
value 90: Normal Ranker
value 200: Unknow
```

##### 課題 2
足し算、引き算、掛け算、割り算する関数を実装してください。<br>
ただし計算の種別の引数を指定して条件判断を行い計算するようにしてください。


```sh
# 実行
$ python3 answer/lessonIf/task2.py 

# 出力
10 + 3: 13
10 - 3: 7
10 * 3: 30
10 / 3: 3.333333
```

##### 課題 3
コンソール上から Hello を入力すると Nice to meet you. と返し、それ以外の文字列の場合は Unknow　と表示する条件判断式を実装してください。

コンソールからの入力は input 構文を使います。

```sh
# 実行
$ python3 answer/lessonIf/task3.py 

# 出力
Please input text > Hello
Nice to meet you.

Please input text > Good
Unknow
```

### for文

```sh
# 実行
$ python3 lesson/lessonFor/main.py 
```

[ソースコード](./lesson/lessonFor/main.py)


#### 課題
##### 課題 1
range(5)をforループで実装してください。

```sh
# 実行
$ python3 answer/lessonFor/task1.py 

# 出力
0
1
2
3
4
```

##### 課題 2
forループを使って以下のリストの全ての要素を2倍にして表示してください。

```python
values = [2, 4, 5, 7, 8, 12]
```
```sh
# 実行
$ python3 answer/lessonFor/task2.py 

# 出力
4
8
10
14
16
24
```

##### 課題 3
for文を2つ使ってrange(size)を表示してください。<br>
sizeは任意の数字が入ります。

```sh
# 実行
$ python3 answer/lessonFor/task3.py 

# 出力
size: 3
i: 0 j: 0
i: 0 j: 1
i: 0 j: 2
i: 1 j: 0
i: 1 j: 1
i: 1 j: 2
i: 2 j: 0
i: 2 j: 1
i: 2 j: 2
```

##### 課題 4
forループとif文を使って*を以下のように表示してください。<br>
但し inputでsizeを入力し、size分表示するようにしてください。

```
*
**
***
****
*****
```

```sh
# 実行
$ python3 answer/lessonFor/task4.py 

# 出力
Please input size > 3
*
**
***

Please input size > 5
*
**
***
****
*****
```


##### 課題 5
forループとif文を使って*を以下のように表示してください。<br>
但し inputでsizeを入力し、size分表示するようにしてください。
```
    *
   **
  ***
 ****
*****
```

```sh
# 実行
$ python3 answer/lessonFor/task5.py 

# 出力
Please input size > 3
  *
 **
***

Please input size > 5
    *
   **
  ***
 ****
*****
```

### while文

```sh
# 実行
$ python3 lesson/lessonWhile/main.py 
```

[ソースコード](./lesson/lessonWhile/main.py)


#### 課題
##### 課題 1
5回ループするwhile文を実装し、5回ループ後に Good を表示してください。

```sh
# 実行
$ python3 answer/lessonWhile/task1.py 

# 出力
loop i 0
loop i 1
loop i 2
loop i 3
loop i 4
Good
```

##### 課題 2
5回ループするwhile文を実装し、1回目はDog、2回目はCatを表示して3回目でbreakしてループを抜けてください。

```sh
# 実行
$ python3 answer/lessonWhile/task2.py 

# 出力
loop i 0
Dog
loop i 1
Cat
loop i 2
Break
```

### イテレータ_ジェネレータ

```sh
# 実行
$ python3 lesson/lessonIterGene/main.py 
```

[ソースコード](./lesson/lessonIterGene/main.py)


#### 課題
##### 課題 1
以下のリストをイテレータ化して全て取り出してください。

```python
values = ["Hello", "world", "Good", "morning"]
```

```sh
# 実行
$ python3 answer/lessonIterGene/task1.py 

# 出力
Hello
world
Good
morning
```

##### 課題 2
以下のリストをジェネレータ化して全て取り出してください。

```python
values = ["Hello", "world", "Good", "morning"]
```

```sh
# 実行
$ python3 answer/lessonIterGene/task2.py 

# 出力
Hello
world
Good
morning
```

### Lambda
```sh
# 実行
$ python3 lesson/lessonLambda/main.py 
```

[ソースコード](./lesson/lessonLambda/main.py)

#### 課題
##### 課題 1
値を10倍にするLambda関数を実装してください。

```sh
# 実行
$ python3 answer/lessonLambda/task1.py 

# 出力
5 => 50
```

##### 課題 2
以下の関数をLambda関数で実装してください。

```python
def func1(a, b):
  return a - b
```

```sh
# 実行
$ python3 answer/lessonLambda/task2.py 

# 出力
5 - 2 = 3
```


### リスト操作
```sh
# 実行
$ python3 lesson/lessonListOperate/main.py 
```

[ソースコード](./lesson/lessonListOperate/main.py)

#### 課題
##### 課題 1
sortを使って以下のリストを昇順・降順に並べ替えてください。

```python
values = [10, 2, 300, 1, 0, 6, 9]
```

```sh
# 実行
$ python3 answer/lessonListOperate/task1.py 

# 出力
asc [0, 1, 2, 6, 9, 10, 300]
desc [300, 10, 9, 6, 2, 1, 0]
```

##### 課題 2
mapを使って以下のリストの要素を全て10倍にしてください。

```python
values = [10, 2, 300, 1, 0, 6, 9]
```

```sh
# 実行
$ python3 answer/lessonListOperate/task1.py 

# 出力
[100, 20, 3000, 10, 0, 60, 90]
```


##### 課題 3
filterを使って以下のリストを10以上の要素だけをフィルタリングしてください。

```python
values = [12, 2, 300, 1, 0, 6, 9]
```

```sh
# 実行
$ python3 answer/lessonListOperate/task3.py 

# 出力
filter [12, 300]
```

##### 課題 4
sortedを使って以下のリストのageの値で昇順・降順に並べ替えてください。

```python
values = [
  {"name": "taro",   "age": 20},
  {"name": "ueno",   "age": 32},
  {"name": "tanaka", "age": 10},
]
```

```sh
# 実行
$ python3 answer/lessonListOperate/task4.py 

# 出力
asc [{'name': 'tanaka', 'age': 10}, {'name': 'taro', 'age': 20}, {'name': 'ueno', 'age': 32}]
desc [{'name': 'ueno', 'age': 32}, {'name': 'taro', 'age': 20}, {'name': 'tanaka', 'age': 10}]
```

##### 課題 5
mapを使って以下のリストのscoreの値を全て10倍にしてください。

```python
values = [
  {"name": "taro",   "score": 1},
  {"name": "ueno",   "score": 4},
  {"name": "tanaka", "score": 8},
]
```

```sh
# 実行
$ python3 answer/lessonListOperate/task5.py 

# 出力
map [{'name': 'taro', 'score': 10}, {'name': 'ueno', 'score': 40}, {'name': 'tanaka', 'score': 80}]
```

##### 課題 6
filterを使って以下のリストのscoreを100以上の要素だけをフィルタリングしてください。

```python
values = [
  {"name": "taro",   "score": 10},
  {"name": "ueno",   "score": 40},
  {"name": "tanaka", "score": 200},
  {"name": "hanako", "score": 90},
  {"name": "baba",   "score": 120},
]
```

```sh
# 実行
$ python3 answer/lessonListOperate/task6.py 

# 出力
filter [{'name': 'tanaka', 'score': 200}, {'name': 'baba', 'score': 120}]
```

### クラス

```sh
# 実行
$ python3 lesson/lessonClass/main.py 
```

[ソースコード](./lesson/lessonClass/main.py)

#### 課題
##### 課題 1
以下のクラス変数をもったクラスを作成してください。クラス変数に値を設定した後に、クラス関数でクラス変数の内容を表示してください。

```python
name = "Taro"
score = 100
```

```sh
# 実行
$ python3 answer/lessonClass/task1.py 

# 出力
My name is Taro. My score is 100.
```


##### 課題 2
「足し算」「引き算」「掛け算」「割り算」するそれぞれ４つの関数をもったクラスを実装してください。


```sh
# 実行
$ python3 answer/lessonClass/task2.py 

# 出力
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.333333
```

### 継承

```sh
# 実行
$ python3 lesson/lessonInheritance/main.py 
```

[ソースコード](./lesson/lessonInheritance/main.py)

#### 課題
##### 課題 1
Bossクラスを継承したクラスでBossクラスのshow_otakaraを実行してotakaraを表示してください。

Bossクラス

```python
class Boss:
  def __init__(self):
    self.otakara = "Otakara is shinsaibashi."
  def show_otakara(self):
    print(self.otakara)
```

```sh
# 実行
$ python3 answer/lessonInheritance/task1.py 

# 出力
Otakara is shinsaibashi.
```

##### 課題 2
Bossクラスを継承したKobunクラスのshow_my_salaryを実行してBossクラスのkobun_salaryを表示してください。

BossクラスとKobunクラス

```python
class Boss:
  def __init__(self):
    self.kobun_salary = 200000
  def get_salary(self):
    return self.kobun_salary

class Kobun(Boss):
  def __init__(self):
    super().__init__()
  def show_my_salary(self):
    """
      ここでget_salaryを呼んでkobun_salaryを表示してください
    """
```

```sh
# 実行
$ python3 answer/lessonInheritance/task2.py 

# 出力
My salary is 200000.
```

### 型判定

```sh
# 実行
$ python3 lesson/lessonType/main.py 
```

[ソースコード](./lesson/lessonType/main.py)

#### 課題
##### 課題 1
str, int, float, bool型の値に応じて任意の文字列を返す関数を実装してください。

型の判定は type() を使ってください。

```sh
# 実行
$ python3 answer/lessonType/task1.py 

# 出力
value -> This is str.
100 -> This is int.
1.230000 -> This is float.
True -> This is bool.
```

##### 課題 2
str, int, float, bool型の値に応じて任意の文字列を返す関数を実装してください。

型の判定は isinstance() を使ってください。

```sh
# 実行
$ python3 answer/lessonType/task2.py 

# 出力
value -> This is str.
100 -> This is int.
1.230000 -> This is float.
True -> This is bool.
```


### モジュール分割_パッケージ分割

```sh
# 実行
$ python3 lesson/lessonModulePackage/main.py 
```

[ソースコード](./lesson/lessonModulePackage/)

#### 課題
##### 課題 1
「Hello World」と表示する hello_world.py を作成し、main.pyから呼び出してください。

また「足し算」「引き算」「掛け算」「割り算」するそれぞれ４つの関数を実装した calc.py を作成し、main.pyでcalc.pyをimportしてそれぞれの計算結果を表示してください。

ディレクトリ構成は以下の通りです
```
.
└── lessonModulePackage
    ├── hello_world.py
    ├── main.py
    └── util
        ├── __init__.py
        └── calc.py
```

```sh
# 実行
$ python3 answer/lessonModulePackage/main.py 

# 出力
Hello world
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.333333
```

### 日付関数

```sh
# 実行
$ python3 lesson/lessonDate/main.py 
```

[ソースコード](./lesson/lessonDate/main.py)

#### 課題
##### 課題 1
日付型で現在日時を表示してください。さらに "2019/1/1 18:20:30" のフォーマットで現在日時を文字列へ変換して表示してください。

```sh
# 実行
$ python3 answer/lessonDate/task1.py 

# 出力
2019-04-26 06:58:56.406846
2019/04/26 06:58:56
```

##### 課題 2
"2019/1/1 18:20:30"の文字列を日付型へ変換して表示してください。

```sh
# 実行
$ python3 answer/lessonDate/task2.py 

# 出力
2019-01-01 18:20:30
```

##### 課題 3
時間によって挨拶を表示する関数を実装してください。

-  5時 - 11時： おはようございます
- 12時 - 18時： こんにちは
- 18時 - 0時：  こんばんは
-  1時 - 4時：  夜更かしさん

```sh
# 実行
$ python3 answer/lessonDate/task3.py 

# 出力
5時 -> おはようございます
13時 -> こんにちは
20時 -> こんばんは
0時 -> 夜更かしさん
```

### 数学関数

```sh
# 実行
$ python3 lesson/lessonMath/main.py 
```

[ソースコード](./lesson/lessonMath/main.py)

#### 課題
##### 課題 1
-20.310 の「2乗して四捨五入した整数」「絶対値」「切り上げ」「小数点以下を切り捨た最大整数」を表示してください。

```sh
# 実行
$ python3 answer/lessonMath/task1.py 

# 出力
412
20.31
-20
-21
```

### 例外処理

```sh
# 実行
$ python3 lesson/lessonExcept/main.py 
```

[ソースコード](./lesson/lessonExcept/main.py)

#### 課題
##### 課題 1
100 / 0 を行いエラーを発生させて例外処理でエラー要因を表示させてください。 

```sh
# 実行
$ python3 answer/lessonExcept/task1.py 

# 出力
except division by zero
```

##### 課題 2
forループを利用して「0から5までカウントする処理」を実装し、3の段階で例外処理を発生させるよう実装してください。

```sh
# 実行
$ python3 answer/lessonExcept/task2.py 

# 出力
0
1
2
3
except error by raise
```

### ファイルの入出力
```sh
# 実行
$ python3 lesson/lessonFile/main.py 
```

[ソースコード](./lesson/lessonFile/main.py)

#### 課題
##### 課題 1
コードからディレクトリとファイルを作成してください。

ディレクトリ構成は以下の通りです。
```
.
└── Dir
    ├── file.py
    └── Child
        ├── __init__.py
        └── file.py
```

また ファイルの内容は以下の通りです。


file.py
```python
print("Hello world")
```

\__init__.py

```python
# none
```

作成後、コードからtreeを呼び出しディレクトリ構成をコンソール上に表示してください。

コードからtreeを呼び出す際は subprocess をimportして利用してください。<br>
[https://docs.python.org/ja/3/library/subprocess.html](https://docs.python.org/ja/3/library/subprocess.html)


```sh
# 実行
$ python3 answer/lessonFile/task1.py

# 出力
├── Dir
│   ├── Child
│   │   ├── __init__.py
│   │   └── file.py
│   └── file.py
└── task1.py

2 directories, 4 files
```

### with文

```sh
# 実行
$ python3 lesson/lessonWith/main.py 
```

[ソースコード](./lesson/lessonWith/main.py)

#### 課題
##### 課題 1
```__enter__, __exit__, __del__``` を実装したクラスを作成し、with文で実行されることを確認してください。

```sh
# 実行
$ python3 answer/lessonWith/task1.py

# 出力
enter <__main__.Model object at 0x10e3f2be0>
exit <__main__.Model object at 0x10e3f2be0>
del <__main__.Model object at 0x10e3f2be0>
```


### TypeAliases
```sh
# 実行
$ python3 lesson/lessonTypeAliases/main.py 
```

[ソースコード](./lesson/lessonTypeAliases/main.py)

#### 課題
##### 課題 1
str型とstrのList型を別名で定義してそれぞれの型のデータを表示する関数を実装してください。

```sh
# 実行
$ python3 answer/lessonTypeAliases/task1.py

# 出力
show_value: a
show_values: ['a', 'b', 'c']
```

### Generics

```sh
# 実行
$ python3 lesson/lessonGenerics/main.py 
```

[ソースコード](./lesson/lessonGenerics/main.py)


#### 課題
##### 課題 1
何も制約されていないGenericsを作成し、Genericsのデータリストを表示する関数を実装してください。

```sh
# 実行
$ python3 answer/lessonGenerics/task1.py

# 出力
[1, 2, 3]
['a', 'b', 'c']
```


##### 課題 2
Genericsをクラス内部で扱えるよう定義し、そのGenericsのsetとget関数を持ったクラスを作成してください。<br>
作成したクラスの使い方は以下の通りです。

```python
model1 = Model[int]()
model1.set_value(123)
print(model1.get_value())

model2 = Model[str]()
model2.set_value('aiueo')
print(model2.get_value())
```

```sh
# 実行
$ python3 answer/lessonGenerics/task2.py

# 出力
123
aiueo
```



### 文字列操作_正規表現
文字列の置換、分割、検索操作を行い、正規表現を利用して操作できることを確認する。

正規表現とは様々な文字列を一つの文字列で表現する。文字列の検索、置換、分割する際に利用される

[基本的な正規表現一覧](https://murashun.jp/blog/20190215-01.html)

```sh
# 実行
$ python3 lesson/lessonRegx/main.py 
```

[ソースコード](./lesson/lessonRegx/main.py)

#### 課題
課題で利用する文字列です。

```python
content: str = 'abcdefg:-:12345678:ABCD:abc:efg:?:123efg456'
```

##### 課題 1
正規表現を用いて、文字列の数字を全て"!"に置換してください。

```sh
# 実行
$ python3 answer/lessonRegx/task1.py

# 出力
abcdefg:-:!:ABCD:abc:efg:?:!efg!
```

##### 課題 2
正規表現を用いて、文字列の「数字」と「大文字の英語」を全て"!"に置換してください。

複数の正規表現のパターンを用いる場合はパイプか文字クラスを使ってOR、ANDを表現します。

[正規表現での、OR（いずれか、または）の表現方法](http://www-creators.com/archives/5039)

```sh
# 実行
$ python3 answer/lessonRegx/task2.py

# 出力
abcdefg:-:!:!:abc:efg:?:!efg!
```

##### 課題 3
splitを用いて":"区切りで文字列を分割し、正規表現を用いて分割した文字列の「数字」と「大文字の英語」を全て"!"に置換した文字列を表示してください。

```sh
# 実行
$ python3 answer/lessonRegx/task3.py

# 出力
abcdefg-!!abcefg?!efg!
```

##### 課題 4
正規表現を用いて、以下の文字列がメールアドレスかどうか判定できるよう実装してください。

```python
content1: str = 'test@test.com'
content2: str = 'dummy'
content3: str = 'https://google.com'
```

メールアドレスの正規表現は以下の通りです。

```python
pattern: str = r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'
```

```sh
# 実行
$ python3 answer/lessonRegx/task4.py

# 出力
test@test.com -> True
dummy -> False
https://google.com -> False
```

### Webスクレイピング


beautifulsoup4 ライブラリをインストール。

```sh
$ pip3 install beautifulsoup4
```

#### HTML要素を操作して、CSVファイルへ出力する

```sh
# 実行
$ python3 lesson/lessonScraping/main1.py 
```

[ソースコード](./lesson/lessonScraping/main1.py)


#### 外部URLの要素を取得、操作してCSVファイルへ出力する

```sh
# 実行
$ python3 lesson/lessonScraping/main2.py 
```

[ソースコード](./lesson/lessonScraping/main2.py)

#### 課題
##### 課題 1
以下のHTML要素からcontent内のtitleとhrefを取得してCSVファイルへ出力し、CSVファイルが正常に出力されていることを確認してください。

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Webスクレイピング</title>
  </head>
  <body>
    <div id="wrapper">
      <h1>タイトル</h1>
      <div class="content">
        <a href="https://newspicks.com/">NewsPicks</a>
        <a href="https://www.yahoo.co.jp/">Yahoo Japan</a>
        <a href="https://www.nikkei.com/">日本経済新聞</a>
      </div>
    </div>
  </body>
</html>
```

```sh
# 実行
$ python3 answer/lessonScraping/task1.py

# 出力
['0', 'NewsPicks', 'https://newspicks.com/']
['1', 'Yahoo Japan', 'https://www.yahoo.co.jp/']
['2', '日本経済新聞', 'https://www.nikkei.com/']
```

##### 課題 2
任意のWebサイトをスクレイピングした情報をCSVへ出力し、CSVファイルが正常に出力されていることを確認してください。

```sh
# 実行
$ python3 answer/lessonScraping/task2.py

# 出力
url is https://www.nikkei.com 2019/05/03 15:19:17
['0', '5G特許出願、中国が最大\u3000世界シェア3分の1', 'https://www.nikkei.com/article/DGXMZO44412620T00C19A5MM8000/']
['1', '幼少から深めた自覚\u3000歴代の姿も探求', 'https://www.nikkei.com/article/DGXMZO44412580S9A500C1CZ8000/']
['2', ' 「大きな道しるべ」\u3000象徴天皇のバトン', 'https://www.nikkei.com/article/DGXMZO44407820S9A500C1EA1000/']
['3', '訪日客が招く「観光公害」\u3000川越・京都…住民に影響も', 'https://www.nikkei.com/article/DGXMZO44266480W9A420C1SHA000/']
['4', '中国、AIで7つの優位(FT)', 'https://www.nikkei.com/article/DGXMZO44244690W9A420C1TCR000/']
['5', '「変化受け止め、次の革新へ」\u3000経団連・中西宏明会長', 'https://www.nikkei.com/article/DGXMZO44277290W9A420C1SHA000/']
['6', '中国対抗へ「官民学で連携強化を」\u3000前米大統領補佐官', 'https://www.nikkei.com/article/DGXMZO44415700T00C19A5000000/']
```


## 備考
[Pythonの基本的なエラー一覧とその原因の確認方法](https://note.nkmk.me/python-error-message/)

[Pycharm：import文で「Unresolved reference」と警告されてしまう](http://virgo.hatenadiary.jp/entry/2015/08/23/023717)

[正規表現での、OR（いずれか、または）の表現方法](http://www-creators.com/archives/5039)

[正規表現：AND（かつ）の表現方法](http://www-creators.com/archives/5332)
