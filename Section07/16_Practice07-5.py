lst = []
for i in range(1,101):
    msg = ''
    if i // 10 >= 1 and ((i // 10) % 3 == 0 or (i // 10) % 6 == 0 or (i // 10) % 9 == 0) :
        msg += '짝'
    if i % 10 != 0 and ((i % 10) % 3 == 0 or (i % 10) % 6 == 0 or (i % 10) % 9 == 0):
        msg += '짝'
    if msg == '':
        lst.append(i)
    else:
        lst.append(msg)
msg = ''
count = 1
for i in range(len(lst)):
    msg += str(lst[i]) + '\t\t'
    if count % 10 == 0:
        msg += '\n';
    count+=1
print(msg)