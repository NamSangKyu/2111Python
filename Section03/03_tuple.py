"""
    튜플(Tuple)
        데이터를 리스트 처럼 가지고 있어서
        데이터를 읽어오는 형태는 리스트와 동일
        하지만 최초에 저장한 데이터를 수정, 삭제, 추가 X
"""
#튜플 생성
tup1 = (1,45,23,21,55,True,'안녕하세요')
print(tup1)
tup2 = 1, 4, '안녕하세요', False
print(tup2)
lst = [4,2,6,False,'테스트']
tup3 = tuple(lst) #기존 리스트를 튜플에 복사해서 저장
print(lst)
print(tup3)
#추가 삭제 수정 X
#tup1[0] = 'TEST' #데이터 수정 X
print(tup1[0]) #리스트와 동일한 형태로 데이터 조회는 가능





