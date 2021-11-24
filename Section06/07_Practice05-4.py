car_no = input('차량번호를 입력하세요 >>>')
if int(car_no[-1]) % 2 == 0:
    print(f'차량번호 {car_no}는 오늘 운행이 가능합니다.')
else:
    print(f'차량번호 {car_no}는 오늘 운행이 불가능합니다.')