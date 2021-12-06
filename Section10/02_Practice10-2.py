no = input('사업자등록번호를 입력하세요(예:123-45-67890) >>>')
no_list = no.split('-')
check = 0
for n in no_list:
    if n.isdecimal() == True:
        check += 1

if check == 3:
    print('올바른 형식입니다.')
else:
    print('올바른 형식이 아닙니다.')