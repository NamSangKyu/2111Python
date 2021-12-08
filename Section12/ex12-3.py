import random as r

#1이상 10이하 정수를 랜덤하게 뽑음
print(r.randint(1,10))
#0~9 정수를 랜덤하게 뽑음
print(r.randrange(10))
#1~9 정수를 랜덤하게 뽑음
print(r.randrange(1,10))
#1~9 정수 중 홀수만 뽑음
print(r.randrange(1,10,2))
#0이상 1미만
print(r.random())
#리스트 내용중 하나 뽑음
list = ['A','B','C','D']
print(r.choice(list))
#중복 없이 5개 숫자 랜덤하게 뽑음 1~100
print(r.sample(range(1,101),5))
#리스트 내용을 랜덤하게 섞음
r.shuffle(list)
print(list)






