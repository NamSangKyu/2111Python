# 교재에 소개된 % 연산자는 old함.

name = '민경태'
age = 44

# 1. format() 메소드
msg1 = '나는 {}이고 나이는 {}살입니다'.format(name, age)
msg2 = '나는 {0}이고 나이는 {1}살입니다'.format(name, age)
msg3 = '나는 {1}이고 나이는 {0}살입니다'.format(age, name)
print(msg1)
print(msg2)
print(msg3)

# 2. f-strings
#    v3.6 이상
msg4 = f'나는 {name}이고 나이는 {age}살이다 내년에는 {age + 1}살이다'
print(msg4)
