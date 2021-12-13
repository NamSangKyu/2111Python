#파일 열기 - 추가 모드도 파일이 없으면 생성
file = open('text.txt','at')
#내용 추가
file.write('추가 테스트\n')
#파일 닫기
file.close()