# Python-Training

> 初学者向け Python構文理解のためのソースコード

## 目次
- [Hello Worldを表示](#環境構築)
- [変数と定数](#変数と定数)
- [データ型](#データ型)
- [演算子](#演算子)
- [関数・スコープ](#関数・スコープ)
- [リスト型・タプル型](#リスト型・タプル型])
- スライス
- 条件判断
- 集合型
- 辞書型
- イテレーター
- リスト操作
- Map
- Lambda
- クラス
- アクセス制限・継承
- 型判定
- モジュール分割・パッケージ分割
- 例外処理
- ファイルの入出力
- 正規表現
- Type aliases
- Callable
- Generics
- Webスクレイピング

## 開発環境
- Python 3.6.5 以上

## 手順

### 環境構築


### Hello worldを表示する
```python
"""
コメントアウトです。
複数行のコメントを書く特に利用します。
"""

print("Hello World") # Hello World
```

```sh
# 実行
$ python3 lesson/lessonHelloWorld/main.py 
Hello World
```
#### 課題
##### 課題 1
「Good Job!」を表示してください。

```sh
# 実行
$ python3 answer/lessonHelloWorld/task1.py 

# 出力
Good Job!
```
## トレーニング

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

### 関数・スコープ

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

### リスト型・タプル型

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
$ python3 lesson/lessonListTuple/task1.py 

# 出力
['a', 'i', 'u', 'e', 'o']
```

##### 課題 2
文字列のリスト型を２つを連結して新しいリスト型を作り、全ての要素を表示してください。


```sh
# 実行
$ python3 lesson/lessonListTuple/task2.py 

# 出力
values1 ['a', 'i', 'u', 'e', 'o']
values2 ['ka', 'ki', 'ku', 'ke', 'ko']
values3 ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko']
```

##### 課題 3
文字列のリスト型を作り、「リストの長さ」「先頭の要素」「末端の要素」を表示してください。

```sh
# 実行
$ python3 lesson/lessonListTuple/task3.py 

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
$ python3 lesson/lessonListTuple/task4.py 

# 出力
values1 index:1 count:2
values2 index:0 count:2
```

##### 課題 5
タプル型を作り、全ての要素を表示してください。

```sh
# 実行
$ python3 lesson/lessonListTuple/task5.py 

# 出力
('Hello', 100, 'World', 0.123)
```