no = int(input('숫자 입력 : '))
#조건 True면 실행하는 영역
#해당 영역은 if 문 다음 줄부터 똑같은 여백을 두어서 실행문 작성
# if 조건식 :
if no > 0:
    print('입력하신 숫자는 양수 입니다.')

if no < 0:
    print('입력하신 숫자는 음수 입니다.')

if no == 0:
    print('입력하신 숫자는 0 입니다.')
print('프로그램 종료')