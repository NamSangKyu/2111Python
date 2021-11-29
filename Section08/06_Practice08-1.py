money = 10000

while True:
    m = int(input('사용할 금액 입력 >>> '))
    if m <= 0:
        print('0 이하의 금액은 사용할 수 없습니다.')
        continue
    elif money - m < 0:
        print(f'{m-money}원이 부족합니다.')
        continue
    money -= m
    print(f'현재 {money}원이 있습니다.')
    if money == 0:
        break