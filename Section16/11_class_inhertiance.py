class Animal:
    def __init__(self):
        print('Animal 생성자')

    def eat(self):
        print('동물이 먹이를 먹습니다.')

class Person(Animal):
    def __init__(self):
        print('Person 생성자')

    def eat(self):
        print('사람이 밥을 먹습니다.')

p = Person()
p.eat()