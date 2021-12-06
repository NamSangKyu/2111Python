#다중 반환
#, <-- 데이터 및 변수를 구분
def return_multi(*args):
    return sum(args),sum(args)/len(args),max(args),min(args)

s, a, m, n = return_multi(1,2,3,4,5,6,7,8)
print(s)
print(a)
print(m)
print(n)
