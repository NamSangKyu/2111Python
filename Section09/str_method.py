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







