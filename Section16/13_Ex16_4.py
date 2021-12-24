class Coffee:
    def __init__(self,bean):
        self.bean = bean

    def coffee_info(self):
        print('원두 : {}'.format(self.bean))

class Espresso(Coffee):
    def __init__(self,bean,water):
        super().__init__(bean)
        self.water = water
    def espresso_info(self):
        super().coffee_info()
        print('물 : {}ml'.format(self.water))

coffee = Espresso('콜롬비아',50)
coffee.espresso_info()