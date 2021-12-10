"""
 가위 바위 보 게임
 총 PC와 5판을 하여 승무패 를 출력

 바위 - 1, 가위 - 2, 보 - 3

 컴퓨터도 사용자가 가위 바위 보 번호중 하나 입력하면
 랜덤 1~3 숫자를 뽑음, 그 후에 승무패를 출력

 예시>
 바위 - 1, 가위 - 2, 보 - 3 입력 >>> 3
 당신은 보 선택, 컴퓨터는 가위 선택, 당신이 졌습니다.
    사용자 % 3 + 1 == 컴퓨터  ---> 사용자 승
    사용자         컴퓨터
      1             2
      2             3
      3             1
"""
import random as r
win = 0
draw = 0
lose = 0
lst = ['바위','가위','보']
for i in range(5):
    player = int(input('바위-1,가위-2,보-3 입력 >>>'))
    computer = r.randrange(1,4)
    msg = ''
    if player == computer:
        draw+=1
        msg = '비겼습니다.'
    elif player % 3 + 1 == computer:
        win+=1
        msg = '당신이 이겼습니다.'
    else:
        lose+=1
        msg = '당신이 졌습니다.'
    print(f'당신은 {lst[player-1]}선택, 컴퓨터는 {computer-1}선택, {msg}')
print(f'당신의 전적은 승 : {win}, 무 : {draw}, 패 : {lose}')














