"""
    이 함수는 매개변수로 받은 값이 완전수 인지 판단하는 함수
    매개변수로 받은 값이 완전수 이면 true 리턴
    매개변수로 받은 값이 완전수 아니면 false 리턴

    완전수 : 자기자신의 약수를 제외한 약수들 전체 합이 자기자신 숫자
            약수들의 합이 숫자랑 같은경우
            6 == 1 + 2 + 3

    숫자 하나 입력 받아서 만든 함수 실행
"""
def check_perfect_number(n):
    lst = []
    for i in range(1,n):
        if n % i == 0:
            lst.append(i)
    if sum(lst) == n:
        return True
    else:
        return False

n = int(input('숫자 입력 >>> '))
if check_perfect_number(n) :
    print('입력하신 숫자는 완전수 입니다.')
else:
    print('입력하신 숫자는 완전수가 아닙니다.')

for i in range(1,101):
    if check_perfect_number(i):
        print(i)










