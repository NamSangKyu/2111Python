n = set()

while len(n) != 5:
    num = int(input('0~9 사이 정수를 입력하세요 >>> '))
    if 0 <= num <= 9:
        n.add(num)
print('모두 입력되었습니다.')
print(f'입력된 값은 {n}입니다.')