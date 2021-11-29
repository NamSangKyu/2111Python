
for dan in range(2,10):
    if dan % 2 == 0:
        continue
    for n in range(1,10):
        print(f'{dan}*{n}={dan*n}')
        if dan == n:
            break
    print()#아무것도 출력안하면, 줄바꿈 효과