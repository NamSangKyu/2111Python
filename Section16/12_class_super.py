class Animal:
    def __init__(self, age):
        self.age = age
        print('Animal 생성자 호출')

    def print_info(self):
        print('이 동물의 나이 : {}'.format(self.age))

class Person(Animal):
    def __init__(self, age):
        #부모 생성자에서 필요한 데이터를 자식이 받아서 보내줌
        super().__init__(age)
        print('Person 생성자 호출')

p = Person(20)
p.print_info()