'''
Person 클래스에서 이름, 나이를 저장하고
이름과 나이를 출력하는 print_person_info 메서드를 작성
'''
class Person:
    #self 현재 생성된 객체
    def setting_data(self,name,age):
        #현재 객체에 name이라는 변수를 선언하고 매개변수에서 받아온 name을 저장
        self.name = name
        self.age = age

    def print_person_info(self):
        #self.name 현재 객체에 저장된 name 변수 값을 읽어옴
        print(f'{self.name} - {self.age}')

person1 = Person()
person1.setting_data('홍길동',20)
person1.print_person_info()

#person2로 Person 객체 생성 후 임의 데이터 넣은 후 출력