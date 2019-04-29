"""
課題 型判定
"""

def func1(value) -> str:
  if type(value) is str:
    return 'This is str.'
  elif type(value) is int:
    return 'This is int.'
  elif type(value) is float:
    return 'This is float.'
  elif type(value) is bool:
    return 'This is bool.'
  else:
    return 'Unknow.'

str_value = 'value'
int_value = 100
float_value = 1.23
is_value = True

print('%s -> %s' % (str_value, func1(str_value)))
print('%d -> %s' % (int_value, func1(int_value)))
print('%f -> %s' % (float_value, func1(float_value)))
print('%s -> %s' % (is_value, func1(is_value)))
