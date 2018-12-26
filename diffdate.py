#!/usr/bin/python
# coding:utf-8
##/from datetime import datetime,timedelta

import sys
import datetime
##import pytz

## Check Command Parameter
##
if( len(sys.argv) <= 2 ):
    print(" Usage:: diffdate.py <Start Day> <Last Day> ")
    print("")
    print("   Exp.) >diffdate.py 20170101 20170201")
    print("          [Start Day] 2017-01-01")
    print("          [End   Day] 2017-02-01")
    print("")
    print("          日差 31日 (この期間の日数：32日)")
    quit()

## Get Start Day, End Day
##
s_year  = int(sys.argv[1][0:4])
s_month = int(sys.argv[1][4:6])
s_day   = int(sys.argv[1][6:8])

l_year  = int(sys.argv[2][0:4])
l_month = int(sys.argv[2][4:6])
l_day   = int(sys.argv[2][6:8])

## Calculate Difference
##
##timezone = pytz.timezone('Asia/Tokyo')
# delta     = datetime.timedelta(days=+1)
#last_day       = datetime.last_day(tz=timezone)
#tomorrow   = now + delta
first_day  = datetime.date(year=s_year, month=s_month, day=s_day) ### 開始日
last_day   = datetime.date(year=l_year, month=l_month, day=l_day) ### 終了日
print("[Start Day] {0}".format(first_day))
print("[End   Day] {0}".format(last_day))

## Output Result
##
## ２つの日付の差を算出する 
delta   = last_day - first_day 
period  = last_day - first_day + datetime.timedelta(days=1) 
print("")
print("  日差 {0}日 (この期間の日数：{1}日)".format(delta.days, period.days))

