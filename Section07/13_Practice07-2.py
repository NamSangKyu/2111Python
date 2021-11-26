n = int(input('임의의 양수를 입력하세요 >>> '))
total = 0
for i in range(1,n+1):
    total += i
print(f'1부터 {n}사이 모든 정수의 합계는 {total}입니다.')