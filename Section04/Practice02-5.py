# dict = {키: 값, 키: 값, 키: 값}
# 저장하고자 하는 것은 키? 값?  값을 저장하는 것이 목적임!
menu = {
    '금요일': '탕수육',
    '토요일': '유산슬'
}
print('금요일 :', menu['금요일'])
print('토요일 :', menu['토요일'])

# ''는 ""와 같다.  문자열 앞 뒤에 붙이는 기호
# word = 'maple'

week = ['금요일', '토요일']
menu = {
    week[0]: '탕수육',
    week[1]: '유산슬'
}
print(week[0], ':', menu[week[0]])
print(week[1], ':', menu[week[1]])
