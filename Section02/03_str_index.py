# 인덱스
# 1. 문자마다 부여된 번호이다.
# 2. 앞에서부터 0을 부여한다.
# 3. 뒤에서부터 -1을 부여한다.
# 4. [] 안에 인덱스를 작성하면 해당 문자를 사용할 수 있다.

city = 'seoul'
print(city[0], city[-5])  # s
print(city[1], city[-4])  # e
print(city[2], city[-3])  # o
print(city[3], city[-2])  # u
print(city[4], city[-1])  # l

age = 44
print(str(age)[0])
print(str(age)[1])
