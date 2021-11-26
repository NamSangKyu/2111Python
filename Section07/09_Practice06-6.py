n = 1
while n <= 9:
    dan = 2
    str = ''
    while dan <= 9:
        str += f'{dan}*{n}={dan*n}\t'
        dan += 1
    print(str)
    n += 1