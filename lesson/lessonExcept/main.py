"""
例外処理
  実行中に何らかのエラーが発生することを例外と言う
  例外が発生した時の処理を実装することができる
"""

"""
try: except 例外の種類 as e: で例外処理を実装できる
"""
try:
  value = 10 / 0
  print(value)
except ZeroDivisionError as e:
  print('except Error!', e)


"""
else/finally
  else: 例外発生せずに正常に処理が進んだ場合に実行される
  finally: 例外発生に関係なく最後に実行される
"""
try:
  value = 10 / 0
  print(value)
except ZeroDivisionError as e:
  print('except Error!', e)
else:
  print('else')
finally:
  print('finally')

"""
raise
  故意に例外発生させることができる
"""
try:
  raise NameError('name error by raise')
except NameError as e:
  print(e)