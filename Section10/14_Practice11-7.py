"""
    매개변수로 문자열하나를 받아서
    해당 문자열이 회문인지 체크하는 함수
    회문이면 true 리턴, 회문이 아니면 false 리턴

    회문 >>> lol , 스위스

     0   1   2   3   4
     H   e   l   l   o
    -5  -4  -3  -2  -1
"""
def check_palindrome(str):
    for i in range(0,len(str)//2):
        if str[i] != str[-(i+1)]:
            return False
    return True

str = input('문자열 입력 >>> ')
print(check_palindrome(str))








