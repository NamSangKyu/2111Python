"""
    리스트(List)
        데이터를 원하는 만큼 여러개 데이터를 저장
        1. 중복된 데이터가 저장
        2. 데이터를 추가한 순서가 보장
        3. 추가, 삭제, 수정이 가능
"""
#리스트 생성
#        0 1  2      3 4   5     6
list1 = [1,2,'Hello',4,5, True, '안녕하세요']
print(list1)
#리스트에 있는 내용을 하나씩 꺼낼때는 인덱스(index)
#index는 번호가 0부터 시작
#list1은 인덱스 번호가 0부터 6까지 있음
print(list1[0])
print(list1[2])
print(list1[6])
print(list1[-1])
print(list1[-2])
#print(list1[-8]) 범위 벗어났기 때문에 에러
#리스트 슬라이스를 이용하여 부분 추출
print('-----------------')
print(list1[1:])#1번 인덱스부터 끝까지 추출
print(list1[:4])#처음부터 4번 인덱스 전까지 추출
#1번 인덱스부터 5번 인덱스까지 추출
print(list1[1:6])
#리스트를 추출해서 새로 리스트를 생성하는 방법
list2 = list1[1:6]
print(list1)
print(list2)

#리스트 요소에 대한 추가, 삭제, 수정
#리스트에 요소 추가, 추가시 맨 뒤에서 부터 순서대로 추가
list1.append("추가")
list1.append(100)
print(list1)
#원하는 인덱스 위치에 추가 --> 1번 인덱스부터 한칸씩 밀림
list1.insert(1,"추가")
print(list1)
list1.insert(4,False)
print(list1)
#리스트 요소 수정
list1[3] = 777 #원하는 인덱스 번호, 값을 새로 저장
print(list1)
#6번 요소를 3.1415로 수정
list1[6] = 3.1415
print(list1)
#리스트 요소 삭제 --- 인덱스 번호로 삭제
list1.pop() #맨 마지막 요소 삭제
print(list1)
list1.pop(3)#3번 인덱스에 대한 요소 삭제
print(list1)
#리스트 요소삭제 --- 값으로 검색해서 삭제
list1.remove(3.1415);
print(list1)
#안녕하세요 값 삭제
list1.append("안녕하세요")
print(list1)
list1.remove("안녕하세요") #최초 검색된 데이터가 먼저 삭제 1건만 삭제 됨
print(list1)
#전체 데이터 삭제
list1.clear()
print(list1)





