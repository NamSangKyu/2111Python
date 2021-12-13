#파일 열기
file = open('text.txt','wt')
#입출력
file.write('Hello World')
file.write('\n')
file.write('안녕하세요')
#파일 닫기
file.close()