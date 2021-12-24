class Number:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def sum(self):
        return self.n1 + self.n2

    #인스턴스 끼리 비교할때 사용되는 메서드
    # ==
    def __eq__(self, other):
        print('__eq__ 실행')
        return self.n1 == other.n1 and self.n2==other.n2
    # !=
    def __ne__(self, other):
        print('__ne__ 실행')
        #return self.n1 != other.n1 or self.n2 != other.n2
        return not self == other
    # <
    def __lt__(self, other):
        print('__lt__ 실행')
        return self.sum() < other.sum()

    # <=
    def __le__(self, other):
        print('__le__ 실행')
        return self.sum() <= other.sum()

    # >
    def __gt__(self, other):
        print('__gt__ 실행')
        return self.sum() > other.sum()

    # >=
    def __ge__(self, other):
        print('__ge__ 실행')
        return self.sum() >= other.sum()


n1 = Number(10,20)
n2 = Number(10,20)
n3 = n1
print(n1,n2,n3)
print(n1 == n2) #일반적으로는 메모리 주소값으로 비교
print(n1 == n3)
n1.n1 = 5
print(n1 != n2)
print(n1 < n2)
print(n1 <= n2)
print(n1 > n2)
print(n1 >= n2)