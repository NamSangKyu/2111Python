count = 5

while count > 0:
    passwd = input('비밀번호를 입력하세요 >>> ')
    if passwd == 'qwerty':
        print('비밀번호를 맞췄습니다.')
        break
    else:
        count-=1
if count == 0:
    print('비밀번호 입력 횟수를 초과했습니다.')