count = 0
total = 0
while count < 5:
    n = int(input('{}번째 정수를 입력하세요>>> '.format(count+1)))
    if n <= 0:
        print('0 이하의 정수는 처리할 수 없습니다.')
        continue
    total += n
    count += 1
print('입력된 5개 양수의 총 합은 {}입니다.'.format(total))