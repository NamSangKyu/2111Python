m = int(input('1~12 사이의 월을 입력하세요 >>> '))

# 월(m)을 인덱스와 같은 값으로 보자.
last = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(last[0])
print(last[1])
print(last[2])
print(last[3])

print(f'{m}월은 {last[m]}일까지 있습니다.')
