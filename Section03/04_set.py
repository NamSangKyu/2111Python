"""
    셋트(set)
        집합 형태의 자료형
        1. 중복된 데이터가 X ---> 고유값만 저장됨
        2. 데이터가 자동으로 정렬 ---> 저장되는 순서가 없음
"""
#set 생성
set1 = {53,24,55,123,534,1}
print(set1)
set2 = {'C','Z','A','E'}
print(set2)
lst = [2,2,4,'A','C',4]
set3 = set(lst) #리스트를 세트로 저장, 기존 리스트가 세트로 바뀌지 않음
print(set3)
sLst = list(set3)#세트를 리스트로 저장
print(sLst)
#세트 데이터 추가
set1.add(10)
print(set1)
#데이터 삭제
set1.remove(123)
print(set1)
#이미 데이터 123삭제되서 없기 떄문에 없는 데이터로 삭제 하면 에러 발생
#set1.remove(123)
set1.discard(10)
set1.discard(10)#discard는 삭제할 데이터가 없어도 에러 발생을 하지 않음
print(set1)
