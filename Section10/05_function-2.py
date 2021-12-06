#가변 매개변수, 받아온 데이터들을 튜플로 관리
def printItems(*args):
    print(args)
    for item in args:
        print(item)

printItems('Hello','Python','Wellcome','Test')
printItems('홍길동')
printItems('홍길동','김철수',20)

#매개변수에 기본값을 설정하는 디폴트 매개변수
def printMessage(msg='안녕하세요'):
    print(msg)
printMessage()
printMessage('만나서 반갑습니다.')

#디폴트 값은 반드시 오른쪽 끝에서부터
#전부 채우면서 왼쪽으로 디폴트값 설정
def printNumbers(n1,n2=10):
    print(n1,n2)
#n2에 20이 전달될 것으로 예상?
printNumbers(20)






