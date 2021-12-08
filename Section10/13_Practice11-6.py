"""
    매개변수로 숫자 두개를 받아서
    두 숫자의 최대 공약수를 리턴하는 함수
"""
def get_gcd(n1, n2):
    n = min(n1,n2)
    gcd = 1
    for i in range(1,n+1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd

n1 = int(input('숫자 입력 >>> '))
n2 = int(input('숫자 입력 >>> '))
print(get_gcd(n1,n2))








