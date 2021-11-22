# len() 함수 : 글자 수를 구한다.
print(len('maple'))

# 글자 수가 홀수인 경우만 따져 보겠습니다.
# 가운데 글자의 인덱스 따져보기
# 3글자 : 1
# 5글자 : 2
# 7글자 : 3
# N글자 : (N - 1) / 2


word = 'maple'
n = len(word)
index = (n - 1) / 2
print(word, '의 가운데 글자는', word[int(index)], '입니다.')

# N글자 : n // 2 (몫 구하기)
word = 'maple'
n = len(word)
index = n // 2
print(word, '의 가운데 글자는', word[index], '입니다.')
