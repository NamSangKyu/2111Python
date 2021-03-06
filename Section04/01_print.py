# 이스케이프 : 특수문자 표현 방식, 역슬래시(\)로 시작
print('민\n경\n태')  # \n : 줄 바꿈

print('번호\t이름\t\t번호')  # \t : 탭
print('1\t민경태\t12345')
print('2\t민서방\t567')

print("나는 \"자연인\"이다.")  # C/Java
print('나는 "자연인"이다.')  # Python


# 키워드 속성
# 1. sep : 콤마(,) 사이에 무엇을 넣을 것인가? 생략하면 공백이 들어감.
# 2. end : 출력이 끝나고 무엇을 넣을 것인가? 생략하면 줄 바꿈이 들어감.

print(2021, 11, 17)
print(2021, 11, 17, sep='-')
print(2021, 11, 17, sep=',')

print('민', end='')  # 출력하고 줄 바꾸지 않는다.
print('경', end='')
print('태')
