file = open('연락처.txt','rt')
line_list = file.readlines()
count = 0
idx = 0
for line in line_list:
    arr = line.split(",")
    tel = arr[2]
    if tel[:3].count('751') == 1:
        tel = tel.replace('751','010')
        count += 1
        arr[2] = tel
        line_list[idx] = ",".join(arr)
    idx += 1
file.close()
file = open('연락처.txt','wt')
for line in line_list:
    file.write(line)
file.close()
print('총 {}건의 751 데이터를 찾았습니다.'.format(count))
print('모든 데이터를 수정했습니다.')


