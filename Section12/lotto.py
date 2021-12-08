import random as r
#로또번호 5셋트
#한셋트 숫자 6, 1~45
for i in range(5):
    print(r.sample(range(1, 46), 6))

