import random as r
import time as t

pot = []
i = 0
while len(pot) < 6:
    n = r.randrange(1,46)
    if pot.count(n) != 0:
        continue
    pot.append(n)
    print(f'{i+1}번째 당첨번호는 {n}입니다.')
    i+=1
    t.sleep(2)
pot.sort()
print(f'이번 당첨번호는 {pot}입니다.')