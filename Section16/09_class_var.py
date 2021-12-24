class Count:
    class_count = 0

    @classmethod
    def add_count(cls):
        cls.class_count += 1

    @staticmethod
    def static_method():
        print('인스턴스 생성 없이 사용 가능한 메서드')

c1 = Count()
c2 = Count()

c1.add_count()
c2.add_count()
print(c1.class_count)
print(c2.class_count)
c1.static_method()
Count.static_method()
