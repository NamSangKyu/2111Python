def get_average(marks):
    total = 0
    for item in marks:
        total += marks[item]
    return total / len(marks)

marks = {'국어':90,'영어':80,'수학':85}
average = get_average(marks)
print('평균은 {}점 입니다.'.format(average))