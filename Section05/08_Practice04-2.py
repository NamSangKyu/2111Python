second = int(input('초를 입력하세요>>>'))
hour = second // 3600 #시간 구함
second %= 3600 #분까지의 데이터만 남음
minute = second // 60 #분 구함
second %= 60 #초까지만 데이터가 남음
print(f'변환 결과는 {hour}시간 {minute}분 {second}초입니다.')
