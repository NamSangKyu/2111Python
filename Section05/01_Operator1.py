'''
    변수 두개에 각각 숫자 입력
'''
n1 = int(input('숫자 입력 : '))
n2 = int(input('숫자 입력 : '))
'''
    산술 연산자
    + 덧셈    - 뺄셈    * 곱셈    / 나눗셈   % 나눗셈(나머지)
    // 나눗셈(몫)   n ** a   n의 a승 -->  2 ** 10 --> 1024
'''
print(f'{n1}+{n2}={n1+n2}')
result = n1 - n2#n1 - n2 결과값이 저장됨
print(f'{n1}-{n2}={result}')
print(f'{n1}*{n2}={n1*n2}')
print(f'{n1}/{n2}={n1/n2}')
print(f'{n1}//{n2}={n1//n2}') #몫을 구함
print(f'{n1}%{n2}={n1%n2}') #나머지를 구함
# (n1 + n2) * (n2 - 4) --> 해당 식 결과값 출력
print((n1+n2)*(n2-4))
# 2의 10승
print(2 ** 10)
