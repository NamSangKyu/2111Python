n = 1
i = 0
while i < 10:
    j = 0
    str = ''
    while j < 10:
        str += f'{n}\t\t'
        n+=1
        j+=1
    print(str)
    i+=1
#----------------------------------------------
i = 1
str = ''
while i <= 100:
    str += f'{i}\t\t'
    if i%10 == 0:
        str += '\n'
    i+=1
print(str)
