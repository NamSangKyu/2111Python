exam = []
while True:
    score = int(input('점수 입력 >>> '))
    if score < 0:
        break
    exam.append(score)

print(f'평균={sum(exam)/len(exam)},최대={max(exam)},최소={min(exam)}')
