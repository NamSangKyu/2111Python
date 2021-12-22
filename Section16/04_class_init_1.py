class Person:
    def __init__(self):
        print("Person 생성자")
        self.name = '홍길동'
        self.age = 20

    def print_info(self):
        print(f'{self.name} - {self.age}')

person = Person()
person.print_info()

class Animal:
    def __init__(self,age):
        self.age = age

    def print_info(self):
        print(f'이 동물의 나이 : {self.age}')

animal = Animal(20)
#animal = Animal() 생성자에 매개변수가 있으면 반드시 데이터를 넣어야됨
animal.print_info()











