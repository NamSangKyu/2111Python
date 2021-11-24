score = int(input('국어 점수 입력하세요>>>'))
score += int(input('영어 점수 입력하세요>>>'))
score += int(input('수학 점수 입력하세요>>>'))
score /= 3
result = '합격' if score >= 80 else '불합격'
print(f'평균은 {score}점이고, 결과는 {result}입니다.')