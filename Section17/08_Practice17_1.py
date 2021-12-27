class Quiz:
    answer = ['경기도','강원도','충청남도','충청북도','전라남도','전라북도','경상남도','경상북도','제주특별자치도']

    @classmethod
    def challenge(cls):
        try:
            do = input('정답은? >>> ')
            cls.answer.remove(do)
            print('정답입니다.')
        except:
            print('틀렸습니다.')

        if len(cls.answer) != 0:
            cls.challenge()
        else:
            raise Exception('모든 도를 맞혔습니다. 성공입니다.')

try:
    print('우리나라의 9개의 모든 도를 맞히는 퀴즈 입니다. 하나씩 대답하세요')
    Quiz.challenge()
except Exception as e:
    print(e)


