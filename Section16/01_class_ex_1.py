'''
    TV
        field
            전원 - true/false
            채널 - 정수 --> 1 ~ 567
            음량 - 정수 --> 0 ~ 50
        method
            전원OnOff --> 실행 할때마다 전원값이 true <-> false
            채널Up --> 실행 할때마다 채널값이 증가, 마지막 채널값에서 증가하면 처음 채널로 이동
            채널Down --> 실행 할때마다 채널값이 감소, 첫 채널에서 감소하면 마지막 채널로 이동
            음량Up --> 실행할때마다 음량 값이 증가, 최대 음량에서 증가해도 더 이상 증가되지 X
            음량Down --> 실행할때마다 음량 값이 감소, 최소 음량에서 감소해도 더 이상 감소되지 X
            init --> 전원, 채널, 음량 필드를 선언하고 초기화하는 메서드
'''
class TV:
    def init(self):
        self.power = False
        self.ch = 8
        self.vol = 15

    def power_onoff(self):
        self.power = not self.power
        if self.power:
            print('TV 전원 On')
        else:
            print('TV 전원 Off')

tv = TV()
tv.init()
tv.power_onoff()
tv.power_onoff()
tv.power_onoff()
tv.power_onoff()
