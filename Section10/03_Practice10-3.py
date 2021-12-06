data = '"홍길동",85'
data_list = data.split(",")
#print(data_list[0].strip('"'),data_list[1])
print('이름은 {}이고, 점수는 {}점입니다.'.
      format(data_list[0].strip('"'),data_list[1]))