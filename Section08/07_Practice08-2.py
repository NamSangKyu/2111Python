while True:
    score = int(input('이번 영화의 평점을 입력하세요 >>> '))
    if score < 1 or score > 5:
        print('평점은 1~5 사이만 입력할 수 있습니다.')
        continue
    print(f'평점 : {"★"*score}')
    break