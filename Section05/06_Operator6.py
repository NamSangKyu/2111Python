#시퀸스 연산자
#리스트, 튜플 문자열 등에서 서로 연결할때 사용하는 연산자
lst1 = [1,2,3,4]
lst2 = [5,6,7,8]
lst3 = lst1 + lst2
print(lst3)
str1 = 'Hello'
str2 = 'World'
print(str1 + str2)
#in, not in
#컬렉션, 문자열에서 해당 데이터가 있는지 없는지 판단
print(10 in lst3) #lst3에 숫자 10이 있냐?
print(10 not in lst3)#lst3에 숫자 10이 없냐?
print('e' in str1) #str1 문자열에 'e'가 있냐?
print('e' not in str1)#str1 문자열에 'e'가 없냐?

#삼항 연산자
#조건식의 결과에 따라서 True일때 나타낼 식, False 일때 나타낼 식을 표현
n = 10
#          참         조건식         거짓
message = "짝수" if n % 2 == 0 else "홀수";
print(message)

#반복연산자
print("★" * 5)
print("★" * 4)
print("★" * 3)