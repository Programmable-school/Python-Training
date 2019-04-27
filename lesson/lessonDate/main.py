"""
日付関数
    datetimeパッケージを利用する
"""
import datetime


"""
現在の日時を取得
"""
print(datetime.date.today())        # 2019-04-26
print(datetime.datetime.today())    # 2019-04-26 06:40:43.120633
print(datetime.datetime.now())      # 2019-04-26 06:40:43.120650


"""
文字列から日付を取得
    %d : 0埋めした10進数で表記した月中の日にち
    %m : 0埋めした10進数で表記した月
    %y : 0埋めした10進数で表記した西暦の下2桁
    %Y : 0埋めした10進数で表記した西暦4桁
    %H : 0埋めした10進数で表記した時 （24時間表記）
    %I : 0埋めした10進数で表記した時 （12時間表記）
    %M : 0埋めした10進数で表記した分
    %S : 0埋めした10進数で表記した秒
    %f : 0埋めした10進数で表記したマイクロ秒（6桁）
    %A : ロケールの曜日名
    %a : ロケールの曜日名（短縮形）
    %B : ロケールの月名
    %b : ロケールの月名（短縮形）
    %j : 0埋めした10進数で表記した年中の日にち（正月が'001'）
    %U : 0埋めした10進数で表記した年中の週番号 （週の始まりは日曜日）
    %W : 0埋めした10進数で表記した年中の週番号 （週の始まりは月曜日）
"""
date_str1 = '2019/1/10 10:20:30'
datetime1 = datetime.datetime.strptime(date_str1, '%Y/%m/%d %H:%M:%S')
print(datetime1)            # 2019-01-10 10:20:30
print(datetime1.year)       # 2019
print(datetime1.month)      # 1
print(datetime1.day)        # 10
print(datetime1.hour)       # 10
print(datetime1.minute)     # 20
print(datetime1.second)     # 30
print(datetime1.date())     # 2019-01-10
print(datetime1.weekday())  # 3
day_of_week_str = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][datetime1.weekday()]
print(day_of_week_str)      # Thu
print('%d/%d/%d (%s) %d:%d:%d' % (datetime1.year, datetime1.month, datetime1.day, day_of_week_str, datetime1.hour, datetime1.minute, datetime1.second))
# 2019/1/10 (Thu) 10:20:30


"""
日付から文字列を取得
"""
datetime2 = datetime.datetime(2019, 1, 10, 10, 20, 30)
date_str2 = datetime2.strftime('%Y/%m/%d %H:%M:%S')
print(date_str2)    # 2019/01/10 10:20:30


"""
日付の計算
"""
datetime3 = datetime.datetime(2019, 1, 10, 10, 20, 30)
print(datetime3 + datetime.timedelta(weeks=1))          # 2019-01-17 10:20:30
print(datetime3 + datetime.timedelta(days=3))           # 2019-01-13 10:20:30
print(datetime3 + datetime.timedelta(hours=2))          # 2019-01-10 12:20:30
print(datetime3 + datetime.timedelta(minutes=30))       # 2019-01-10 10:50:30
print(datetime3 + datetime.timedelta(seconds=20))       # 2019-01-10 10:20:50
print(datetime3 + datetime.timedelta(days=3, hours=2, minutes=30, seconds=20))  # 2019-01-13 12:50:50


"""
日付の比較
"""
datetime4 = datetime.datetime(2018, 10, 7, 16, 30, 0)
datetime5 = datetime.datetime(2019, 8, 1, 10, 50, 20)
print(datetime4 > datetime5)    # False
print(datetime4 < datetime5)    # True
print(datetime4 == datetime5)   # False
