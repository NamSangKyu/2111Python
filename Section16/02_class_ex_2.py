'''
    총 클래스
        field
            총알 - 정수 --> 12
        method
            발사 : 1발씩 총알이 감소 - BBang! 출력
                  총알이 없으면 -> reload! 출력

            재장전 : 총알을 12발 리필
'''
class Gun:
    def init(self):
        self.bullet = 12

    def shot(self):
        if self.bullet > 0:
            self.bullet -= 1
            print(f'BBang! - {self.bullet}')
        else:
            print('Reload!')

    def reload(self):
        self.bullet = 12

gun = Gun()
gun.init()
for i in range(0,14):
    gun.shot()
gun.reload()
for i in range(0,14):
    gun.shot()





