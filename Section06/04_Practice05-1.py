score = int(input('점수를 입력하세요>>>'))
grade = 'F'
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f'점수는 {score}점이고, 학점음 {grade}학점입니다.')