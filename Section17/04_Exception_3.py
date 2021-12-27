
try:
    n1 = int(input('숫자 입력 >>> '))
    n2 = int(input('숫자 입력 >>> '))

    print(n1/n2)
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)

print('프로그램 종료')