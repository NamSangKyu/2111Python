# 주석 (comment) : 파이참 단축키 Ctrl + /
'''
    주석용
    주석용
'''

# 변수
# 1. 대, 소문자 구분
# 2. 밑줄 사용
# 3. 한글 가능 (추천 X)
# 4. 동적 타입 (저장하는 값에 따라서 스스로 타입을 결정)

my_name = '민경태'  # my_name = "민경태"
my_age = 44
my_height = 177.5
is_adult = True
my_hobby = None

print(my_name)
print(my_age)
print(my_height)
print(is_adult)
print(my_hobby)

# 변수들의 타입(자료형) 확인
print(type(my_name))    # str   (string, 문자열)
print(type(my_age))     # int   (integer, 정수)
print(type(my_height))  # float (floating point, 실수)
print(type(is_adult))   # bool  (boolean, 논리)
print(type(my_hobby))

# 결정된 타입을 변경할 수 있는가? Yes
# 값을 바꾸면 타입도 변경된다.
my_hobby = '여행'
print(type(my_hobby))


# 방금 alt 하고 어떤거 눌러야되는지 알수 있을까요?? Alt + Shift + F10
# 재실행은 Shift + F10
# 문제는 아닌데 혹시 오늘 수업한 것도 나중에 볼 수 있어요? 현재 녹화 중.
# 혹시 코딩 줄을 밑으로 똑같이 복사할 수 있는 단축키 있나요? Ctrl + d
# 파이참 오른쪽 위에 indexing... 이 뜨는데 왜그런건가요?? 캡쳐 보내주세요.
