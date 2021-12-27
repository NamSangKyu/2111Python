class Car:
    max_oil = 50

    def __init__(self, oil):
        self.oil = oil

    def add_oil(self,oil):
        if oil <= 0:
            return;
        self.oil += oil
        if self.oil > Car.max_oil:
            self.oil = Car.max_oil

    def car_info(self):
        print('현재 주유 상태 : {}'.format(self.oil))

class Hybrid(Car):
    max_battery = 30

    def __init__(self,oil,battery):
        super().__init__(oil)
        self.battery = battery

    def charge(self,charge):
        self.battery += charge
        if self.battery > Hybrid.max_battery:
            self.battery = Hybrid.max_battery

    def hybrid_info(self):
        super().car_info()
        print('현재 충전상태 : {}'.format(self.battery))

car = Hybrid(0,0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()









