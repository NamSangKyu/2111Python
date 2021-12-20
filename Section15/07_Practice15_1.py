class Book:
    def set_info(self,title, writer):
        self.title = title
        self.writer = writer

    def print_info(self):
        print('책 제목 : {}'.format(self.title))
        print('책 저자 : {}'.format(self.writer))

book1 = Book()
book2 = Book()

book1.set_info('파이썬','민경태')
book2.set_info('어린왕자','생텍쥐페리')

book1.print_info()
book2.print_info()
