'''
    에어컨 클래스
        field
            전원 : True - On, False - Off
            온도 - 18 ~ 32
            바람세기 - 1 - 약풍, 2 - 중풍, 3 - 강풍, 4 - 자율
            모드 - 냉방 - 1, 송풍 - 2, 제습 - 3
        method
            전원OnOff - True <--> False
            온도Up - 온도 1씩 증가, 최대값 벗어날수 없음
            온도Down - 온도 1씩 감소, 최소값 벗어날수 없음
            바람세기 - 실행 할때마다 1 -> 4 순환
            모드 -> 실행 할때마다 1 -> 3 순환
'''
class Aircon:
    def init(self):
        self.power = False
        self.temp = 24
        self.wind = 1
        self.mode = 1

    def power_onoff(self):
        self.power = not self.power
        if self.power:
            print('에어컨 전원 On')
        else:
            print('에어컨 전원 Off')

    def temp_up(self):
        if self.temp < 32:
            self.temp += 1
        print(f'현재 온도 : {self.temp}')

    def temp_down(self):
        if self.temp > 18:
            self.temp -= 1
        print(f'현재 온도 : {self.temp}')

    def wind_power(self):
        self.wind = self.wind % 4 + 1
        if self.wind == 1:
            print('약풍')
        elif self.wind == 2:
            print('중풍')
        elif self.wind == 3:
            print('강풍')
        else:
            print('자동 모드')

    def change_mode(self):
        self.mode = self.mode % 3 + 1
        if self.mode == 1:
            print('냉방')
        elif self.mode == 2:
            print('송풍')
        else:
            print('제습')


air = Aircon()
air.init()
air.wind_power()
air.wind_power()
air.wind_power()
air.wind_power()
air.wind_power()
air.wind_power()
air.change_mode()
air.change_mode()
air.change_mode()
air.change_mode()
air.change_mode()
air.change_mode()




