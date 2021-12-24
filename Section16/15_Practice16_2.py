class Shop:
    total = 0
    menu_list = {'떡볶이':3000,'순대':3000,'튀김':500,'김밥':2000}

    @classmethod
    def sales(cls,menu,ea):
        cls.total += cls.menu_list[menu] * ea

Shop.sales('떡볶이',1)
Shop.sales('김밥',2)
Shop.sales('튀김',5)
print('매출 : {}원'.format(Shop.total))
