tel = input('전화번호를 입력하세요 >>> ')
# 0    1    2
#010-1111-2222  ---> 1111 뽑기
tel_list = tel.split("-")
if len(tel_list) == 3:
    print(tel_list[1])
else:
    print('전화번호 형식이 아닙니다.')