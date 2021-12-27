import random as r
class UpDown:
    answer = r.randint(1,100)
    count = 0
    @classmethod
    def play(cls):
        try:
            no = int(input('입력(1~100) >>> '))
            if no > 100 or no < 1:
                raise Exception('1~100사이만 입력하세요')
            cls.count += 1
            if no < cls.answer:
                raise Exception('Up')
            elif no > cls.answer:
                raise Exception('Down')
            else:
                print('{}번만에 정답입니다.'.format(cls.count))

        except Exception as e:
            print(e)
            cls.play()


game = UpDown()
game.play()

