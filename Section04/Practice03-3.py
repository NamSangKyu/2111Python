english_dic = {"flower":"꽃","fly":"날다",
               "floor":"바닥"}

dic = input('영어 단어를 입력하세요>>>')
print(f'{dic}:{english_dic[dic]}')
print('{}:{}'.format(dic,english_dic[dic]))
