'''
    논리 연산자      n1 > 10 and n1 < 20
        and     양쪽의 조건식이 둘다 True일때 True가 되는 연산자
        or      양쪽의 조건식 중 하나라도 True면 True가 되는 연산자
        not     오른쪽에 있는 조건식의 결과를 뒤집는 연산
                True면 False로 False면 True로 바꾸는 연산
'''
n1, n2 = 10, 7
print(n1 > 5 and n2 < 7)
print(n1 > 5 and n2 < 10)
print(n1 > 20 or n2 < 7)
print(n1 > 5 or n2 < 10)
result = n1 < 10
print(not result)