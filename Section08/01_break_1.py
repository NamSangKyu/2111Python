total = 0
for i in range(1000):
    total += i
    if total >= 5050:
        break#break를 감싸고 있는 반복문을 강제 종료
print(total)