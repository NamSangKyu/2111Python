"""
    함수 (Function)
        자주 사용하는 기능을 내장함수처럼 미리 만들어 놓는 코드
        필요할 때마다 가져다가 쓰겠다.

    함수 문법
    def 함수명([매개변수]):
        실행할 코드
        [return 반환값]
"""
#반환 X, 매개변수 X
def printWelcome():
    print('Hello Python')
    print('Nice to meet you')

#반환 O, 매개변수 X
def inputNumber():
    no = int(input('숫자 하나 입력하세요 >>> '))
    return no

#반환 X, 매개변수 O
def printResult(name,age):
    print(f"{name}님은 나이가 {age}살 입니다.")

#반환 O, 매개변수 O
def sum(n1,n2):
    result = n1 + n2
    return result

print("-----------------")
printWelcome()
print(inputNumber() * 2)
printResult("홍길동",20)#홍길동, 20 값은 인자값, 인수
print(sum(20,30))




