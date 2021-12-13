#파일 열기
#파일을 쓰기 모드로 열면 해당 파일을 매번 새로 생성
"""
    파일 모드
        읽기 - r, 쓰기 - w, 추가 - a, 베타적 추가 - x
    파일 종류
        텍스트 파일 - t,  바이너리 파일 - b

    wt ---> 쓰기전용 텍스트 파일
    rt ---> 읽기전용 텍스트 파일일
"""
file = open('firstFile.txt','wt')
print('파일 오픈 완료')
print(file)
#파일 닫기
file.close()

with open('secondFile.txt','wt') as file:
    print('파일 오픈 완료')
    print(file)
    #with 자동으로 close 처리







