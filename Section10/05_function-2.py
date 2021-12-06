#가변 매개변수, 받아온 데이터들을 튜플로 관리
def printItems(*args):
    print(args)
    for item in args:
        print(item)

printItems('Hello','Python','Wellcome','Test')
printItems('홍길동')
printItems('홍길동','김철수',20)