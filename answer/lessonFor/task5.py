"""
課題 for文
"""

size = int(input("size -> "))
result = ""
for i in range(size):
  for j in range(size):
    if (j < size - i - 1):
      result += " "
    else:
      result += "*"
  else:
    if (i != size - 1):
      result += "\n"
else:
  print(result)