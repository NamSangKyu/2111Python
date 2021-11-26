money = int(input('자판기에 얼마를 넣을까요?>>> '))
count = 0
while money >= 300:
    count += 1
    money -= 300
    print(f'커피 {count}잔, 잔돈{money}')