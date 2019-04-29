"""
課題 while文
"""

i = 0
while i < 5:
  print('loop i %d' % (i))
  if i == 0:
    print('Dog')
  elif i == 1:
    print('Cat')
  elif i == 2:
    print('Break')
    break
  i += 1