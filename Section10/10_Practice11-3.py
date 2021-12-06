total = 0
def gift(dic,who,money):
    global total
    dic[who] = money
    total += money
wedding = {}
gift(wedding,'영희',5)
gift(wedding,'철수',3)
gift(wedding,'이모',10)
print('축의금 명단 {}'.format(wedding))
print('전체 축의금 : {}'.format(total))
