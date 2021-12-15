import csv

with open('cctv.csv','rt',newline='') as file:
    count = 0
    csv_reader = csv.reader(file)
    for line in csv_reader:
        if line[4].isdecimal():
            count += int(line[4])
    print('서울특별시 마포구에 설치된 CCTV는 총 {}대 입니다.'.format(count))
