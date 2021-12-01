print('왼쪽 정렬 : {:<10d}'.format(123))
print('오른쪽 정렬 : {:>10d}'.format(123))
print('가운데 정렬 : {:^10d}'.format(123))

# 빈공간에 *로 채움
print('왼쪽 정렬 : {:*<10d}'.format(123))
print('오른쪽 정렬 : {:*>10d}'.format(123))
print('가운데 정렬 : {:*^10d}'.format(123))

print("-------------")
#      01234567890
str = 'Hello World Test World In Python'
print(str.count('World'))#World 개수
print(str.count('World',11))#인덱스 11부터 World 개수
print("-------------")
print(str.find('World'))#World가 있는 인덱스 시작값
print(str.find('Java'))#찾는 단어가 없으면 -1
print(str.find('World',11))#인덱스 11부터 World가 있는 인덱스 시작값
print(str.rfind('World'))#World를 끝에서부터 찾음
print("-------------")
print(str.index('World'))#World가 있는 인덱스 시작값
#print(str.index('Java'))#찾는 단어가 없으면 에러
print("-------------")
print(str.upper())#전부 대문자로 변경
print(str.lower())#전부 소문자로 변경
print(str.capitalize())#첫글자만 대문자, 나머지 전부 소문자로 변경
print("-------------")
list1 = ['A','B','C','D']
print('+'.join(list1))#+ 로 하나의 문자열로 합쳐줌
str = '+'.join(list1)
print(str.split('+')) #+ 로 문자열을 쪼개서 리스트로 생성
print("-------------")
str = 'Hello World Test World In Python'
print(str.replace('World','Hell')) #World를 전부 Hell로 바꿈
print("-------------")
s1 = '             A'
s2 = 'A             '
s3 = '      A       '
print(s1.lstrip()) #왼쪽에 있는 불필요한 문자 제거
print(s2.rstrip()) #오른쪽에 있는 불필요한 문자 제거
print(s3.strip()) #양쪽에 있는 불필요한 문자 제거

s1 = '............A'
print(s1.lstrip('.')) #왼쪽에 있는 불필요한 문자 제거










