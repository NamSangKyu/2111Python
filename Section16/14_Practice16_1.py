class Person:
    population = 0

    def __init__(self,name):
        self.name = name
        Person.population += 1
        print('{} is born'.format(name))

    def __del__(self):
        Person.population -= 1
        print('{} is dead'.format(self.name))

    @classmethod
    def get_population(cls):
        return cls.population

man = Person('James')
woman = Person('emily')

print('전체 인구수 : {}명'.format(Person.get_population()))
del man
print('전체 인구수 : {}명'.format(Person.get_population()))
