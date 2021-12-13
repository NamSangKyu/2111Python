file = open('엄마돼지아기돼지.txt','rt')

line_list = file.readlines()
count = 0
for line in line_list:
    for ch in line:
        if ch == '꿀':
            count += 1
print('꿀은 전체{}번 나타납니다.'.format(count))

#돼지 단어 개수 구하기
print('--------------------------')
file = open('엄마돼지아기돼지.txt','rt')

line_list = file.readlines()
count = 0
for line in line_list:
    count += line.count('돼지')
print('돼지는 전체{}번 나타납니다.'.format(count))
