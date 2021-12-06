"""
    전역 변수 : 위치에 상관 없이 어떤 함수에서도 동일하게
               접근이 가능한 변수
    지역 변수 : 특정 영역에서만 접근이 가능한 변수
               함수 및 실행 영역이 끝나면 바로 메모리에서 해제됨
"""
age = 100
def printA():
    print(age)

def printB():
    print(age)

printA()
printB()

def printC():
    msg = 'Hello Python'
    print('printC',msg)
printC()
print(msg)#msg는 printC가 끝나면 바로 메모리에서 해제됨