# 슬라이스
# 형식
# 문자열[begin:end:step]
#    1) begin : 시작 인덱스, 포함, 생략하면 0부터 시작
#    2) end   : 종료 인덱스, 불포함, 생략하면 끝까지
#    3) step  : 증가/감소, 생략하면 1씩 증가

city = 'seoul'

print(city[0:3])  # 0 <=  < 3
print(city[::])   # seoul
print(city[:3])   # seo (자주 사용되는 형태)
print(city[2:])   # oul (자주 사용되는 형태)
print(city[-3:])  # oul (뒤에서부터 3글자)

# 문제 풀이를 위한 내장 함수
# len('seoul') : 5  -- 글자 수 구해주는 함수

money = 100000
print(len(str(money)))


tel1 = '02-543-1234'
tel2 = '010-1234-5678'

# 뒷 번호 4자리 빼 보자.
print(tel1[-4:])
print(tel2[-4:])

# 뒷 번호 4자리 빼고 나머지 전부 빼 보자.
print(tel1[:-4])
print(tel2[:-4])

# 마이너스 인덱스를 사용하지 않는 경우
print(tel1[:len(tel1)-4])
print(tel2[:len(tel2)-4])
