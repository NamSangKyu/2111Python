'''
숫자하나 입력 받은 뒤
입력받은 숫자가 짝수이면 '짝수' 출력
입력받은 숫자가 홀수이면 '홀수' 출력
'''
no = int(input('숫자 입력 >>>'))
if no % 2 == 0:
    print('짝수')
else:
    print('홀수')
    