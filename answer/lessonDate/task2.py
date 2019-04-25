"""
課題 日付関数
"""

from datetime import datetime

date_str = "2019/1/1 18:20:30"
print(datetime.strptime(date_str, "%Y/%m/%d %H:%M:%S"))