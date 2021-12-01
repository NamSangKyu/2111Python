s1 = {'A','B','C','D'}
s2 = {'C','D','G','H'}
#교집합
s3 = s1 & s2
s3 = s1.intersection(s2)
print(s3)
#합집합
s3 = s1 | s2
s3 = s1.union(s2)
print(s3)
#차집합
s3 = s1 - s2
s3 = s1.difference(s2)
print(s3)


