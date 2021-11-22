# input() 함수
# 1. 모든 입력을 str 취급한다.
# 2. 입력을 저장할 변수가 필요하다.

# 문자열 str 입력
name = input('이름이 뭐에요??')
print(f'아~ 이름이 {name}이구나~ 촌스럽네')

# 정수 int 입력
age = int(input('나이는요???'))  # input() 결과가 int() 처리된다. (입력값이 정수로 바뀐다.)
print(f'아~ 나이는 {age}살이구나 내년에는 {age + 1}살이네~')

# 실수 float 입력
eye = float(input('시력은요????'))
print(f'시력이 {eye}네요~')
