class Person:

    def __init__(self):
        print('생성자 호출')

    def __del__(self):
        print('소멸자 호출')

    def print_info(self):
        print('print_info')

p = Person()
p.print_info()