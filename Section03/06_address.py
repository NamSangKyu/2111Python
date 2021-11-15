#메모리 주소 안바뀌는 형태
#mutable --> list, set, dict
lst = [1,2,3,4]
print(id(lst))
lst.append(10)
print(id(lst))
lst.pop(3)
print(id(lst))
newLst = lst
print(id(lst),id(newLst))
lst[0] = 999
print(lst,newLst)
#메모리 주소가 바뀌는 형태
#immutable --> int, str, float, tuple
num = 10
print(num,id(num))#현재 값, num이 저장된 메모리 주소값
num = 20
print(num,id(num))
num += 20
print(num,id(num))
newNum = num #동일한 메모리 주소는 저장
print(id(num), id(newNum))
newNum = 30 # 새로운 값이 저장되면 새롭게 메모리를 할당
print(id(num), id(newNum))
print(num, newNum)


