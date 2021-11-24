n1 = int(input('정수1 입력 >>>'))
n2 = int(input('정수2 입력 >>>'))
n3 = int(input('정수3 입력 >>>'))

max = n1 if n1 > n2 else n2
max = max if max > n3 else n3

print(f'가장 큰수는 {max}입니다.')