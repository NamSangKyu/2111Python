"""
    딕셔너리(dict)
        단어 - 단어 대한 해설
        Key - Data
        키와 데이터 한쌍으로 데이터를 저장
        키를 이용해서 데이터를 읽기, 저장, 삭제, 수정
"""
#딕셔너리 생성
dict1 = {'홍길동':20, '김철수':44, '이영희':35}
print(dict1)
print(dict1['홍길동']) #홍길동에 해당하는 값을 가져옴
print(dict1['김철수'])
#print(dict1['김'])#키값에 해당하는 데이터가 없으면 에러 처리
dict2 = dict(A = 'TEST', B = False)
print(dict2['A'])
print(dict2['B'])
#추가
dict1['박영수'] = 77
print(dict1)
dict1.setdefault('곽용',90)
print(dict1)

