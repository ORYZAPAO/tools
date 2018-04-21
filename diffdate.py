#!/usr/bin/python
# coding:utf-8
##/from datetime import datetime,timedelta
import datetime
import pytz

# 現在時刻を元に加減算する
timezone = pytz.timezone('Asia/Tokyo')
delta     = datetime.timedelta(days=+1)
#last_day       = datetime.last_day(tz=timezone)
#tomorrow   = now + delta
first_day  = datetime.date(year=2017, month=9, day=29) ### 開始日
last_day   = datetime.date(year=2018, month=3, day=31) ### 終了日
##last_day   = datetime.date(year=2017, month=9, day=30)
print("開始日 {0}".format(first_day))
print("終了日 {0}".format(last_day))

# ２つの日付の差を算出する 
delta = last_day - first_day + datetime.timedelta(days=1)
print("差は{0}日".format(delta.days))

## 検算
print(2+31+30+31+31+28+31)
