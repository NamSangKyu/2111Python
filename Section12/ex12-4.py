import time as t
print(t.time())
print(t.ctime())
print(t.strftime("%Y-%m-%d(%a) %H:%M:%S"))
print(t.strftime("%Y-%m-%d %A %p %I:%M:%S"))
print(t.strftime("%B/%d/%Y %H:%M:%S"))
print(t.strftime("%m/%d/%y"))
print(t.strftime("시작시간 : %Y-%m-%d(%a) %H:%M:%S"))
t.sleep(5) #입력 초 동안 멈춤
print(t.strftime("종료시간 : %Y-%m-%d(%a) %H:%M:%S"))
