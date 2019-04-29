"""
課題 日付関数
"""

from datetime import datetime

def show_aisatu(date: datetime):
  if (5 <= date.hour and date.hour < 12):
    print('%d時 -> おはようございます' % (date.hour))
  elif (12 <= date.hour and date.hour < 18):
    print('%d時 -> こんにちは' % (date.hour))
  elif (18 <= date.hour and date.hour < 24):
    print('%d時 -> こんばんは' % (date.hour))
  else:
    print('%d時 -> 夜更かしさん' % (date.hour))

datetime1 = datetime(2019, 1, 1, 5, 10, 20)
show_aisatu(datetime1)

datetime1 = datetime1.replace(hour=13)
show_aisatu(datetime1)

datetime1 = datetime1.replace(hour=20)
show_aisatu(datetime1)

datetime1 = datetime1.replace(hour=0)
show_aisatu(datetime1)