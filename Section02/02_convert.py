# 타입 종류, 타입 변환 함수
# 1. str : 문자열로 변환 ★
# 2. int : 정수로 변환 ★
# 3. float : 실수로 변환 ★
# 4. bool : 논리값으로 변환


# 1. 정수로 변환
#    1) 내장 함수 : int()
#    2) 동작
#       (1) int(1.9) : 1  (소수 이하 버림)
#       (2) int('100') : 100
#       (3) int('1.9') : 오류 발생 (정수형 문자열만 처리 가능)
#       (4) int(True) : 1
#       (5) int(False) : 0
print(int(1.9))
print(int('100'))
print(int(True))
print(int(False))
# print(int('1.9'))

# 원 단위 절사
money = 35999
print(money / 10)
print(int(money / 10))
print(int(money / 10) * 10)


# 2. 실수로 변환
#    1) 내장 함수 : float()
#    2) 동작
#       (1) float(20) : 20.0
#       (2) float('1.9') : 1.9
#       (3) float('100') : 100.0
#       (4) float(True) : 1.0


# 3. 문자열로 변환
#    1) 내장 함수 : str()
#    2) 동작 : 전달된 모든 것이 문자열로 변환된다.
print(str(100))  # '100'
print(str(1.9))  # '1.9'

# 굳이 int를 안써도 바로 3599로 실행이 되는데 잘못된건가요? 이럴리가 없다.
# c에서 %몫 구하는 것이라고 알고 있는데, python에서는 //인 건가요?
# C에서는 정수 / 정수 : 몫, 실수 / 실수 : 나누기, 정수 / 실수 : 나누기
# C에서는 정수 % 정수 : 나머지 (파이썬도 % 연산)

a = int(float('1.9'))
print(a)


# def f1():
#     pass
#
#
# def f2():
#     pass
#
#
# f2()
