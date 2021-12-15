import csv
cctv_set = set()
with open('cctv.csv','rt',newline='') as file:
    count = 0
    csv_reader = csv.reader(file)
    for line in csv_reader:
        cctv_set.add(line[6])

print(cctv_set)
