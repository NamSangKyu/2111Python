import csv

with open('차량관리.csv','wt',newline='') as file:
    csv_maker = csv.writer(file,delimiter=',',quotechar='"')
    csv_maker.writerow([1,'08러1234','2020-10-20,14:00'])
    csv_maker.writerow([2,'25다1234','2020-10-20,14:10'])
    csv_maker.writerow([3,'28하1234','2020-10-20,14:20'])
print('csv 파일이 생성되었습니다.')

with open('차량관리.csv','rt',newline='') as file:
    csv_reader = csv.reader(file,delimiter=',',quotechar='"')
    for line in csv_reader:
        print(line)