#목록 한건당 인덱스와 값을 튜플로 꺼냄
list1 = ['서울','대전','대구','부산']
for item in enumerate(list1):
    print(item)

for idx, item in enumerate(list1):
    print(idx,item)
print("--------------")
#range
print(list(range(10))) #0~9 0~종료값
print(list(range(0,10)))#0~9 시작값 종료값
print(list(range(0,10,2)))#시작값 종료값 증감값
print("--------------")
#len  -->  개수 구하는 함수
print(len(list1))
print(len(range(5)))
print(len([1,4,23,51,11]))
print("--------------")
#정렬
list1 = [1,4,2,25,31,67,52,56,11]
print(sorted(list1))
print(sorted(list1,reverse=True))#내림차순
print(sorted(list1,reverse=False))#오름차순
print("--------------")
#zip
list1 = ['A','B','C','D']
list2 = [1,2,3,4,5]
for n in zip(list1,list2):
    print(n)
print("--------------")
#159p 기본예제



