#알파벳 A B C D, a b c d
print(chr(65)) #유니코드에 해당하는 글자가 나옴
print(chr(66))
print(chr(67))
print(chr(68))
print(chr(97))
print(chr(98))
print(chr(99))
print(chr(100))
print("----------")
#알파벳 A~Z까지 반복문으로 출력
for a in range(65,91):
    print(chr(a),chr(a+32))
print("----------")
print(ord('A'),ord('a'))#문자 -> 문자 코드값(유니코드)
print("----------")
#eval : 연산식을 넣으면 해당 연산식 계산해서 결과값을 리턴하는 함수
print(eval('100+200'))
a=6
print(eval('a*5'))
print(eval('min(100,200,300)'))
print("----------")
print(format(1000000))
print(format(1000000,'_'))
print(format(1000000,','))
print("----------")
print(str(100) + 100)



