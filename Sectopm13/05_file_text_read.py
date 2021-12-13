#파일 열기 - 읽기 모드에서는 파일이 있어야됨 없으면 에러발생
file = open('text.txt','rt')
#파일 읽기
str = file.read()
print(str)
#파일 닫기
file.close()

print('----------------')
file = open('text.txt','rt')
while True:
    str = file.read(5)
    if not str:
        break
    #print(str)
    print(str, end='')
file.close()
print('\n----------------')
file = open('text.txt','rt')
while True:
    #한줄 단위로 읽어들임
    str = file.readline()
    if str == '':
        break
    print(str,end='')

file.close()
print('\n----------------')
file = open('text.txt','rt')

#파일 내용을 한줄씩 읽어와서 리스트로 생성
line_list = file.readlines()
print(line_list)

for line in line_list:
    print(line,end='')

file.close()




