import datetime as dt
print(dt.datetime.now())

birthday = dt.date(2020,11,5)
print(birthday)

wake = dt.time(19,29,32)
print(wake)

date = dt.datetime.now()
print(date.year)
print(date.month)
#date.day = 30 수정 X
print(date.day)
print(date.hour)
print(date.minute)
print(date.second)
print(date.microsecond)
#날짜 바꾸기
date = date.replace(2021,12,31,0,0,0,0)
print(date)

today = dt.datetime.now()
tomorrow = today + dt.timedelta(days=1)
print(tomorrow)
#다음주 금요일 날짜 계산
next_week = today + dt.timedelta(weeks=1)
print(next_week)

date1 = dt.date(2021,12,10)
date2 = dt.date(2021,12,11)
print(date2 - date1)
print((date2-date1).total_seconds()/(60*60*24))

#D-Day 오늘부터 연말까지 몇 일?
date1 = dt.date(2021,12,10)
date2 = dt.date(2021,12,31)
print((date2-date1).total_seconds()/(60*60*24))






