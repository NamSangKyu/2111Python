class Watch:
    def input_time(self):
        time = input('시간을 입력하세요 >> ')
        time_list = time.split(":")
        self.hour = 0
        self.add_hour(int(time_list[0]))
        self.minute = 0
        self.add_minute(int(time_list[1]))
        self.seconde = 0
        self.add_seconde(int(time_list[2]) % 60)

    def add_hour(self,hour):
        self.hour += hour
        self.hour %= 24

    def add_minute(self,minute):
        self.minute += minute
        self.add_hour(self.minute // 60)
        self.minute %= 60

    def add_seconde(self,seconde):
        self.seconde += seconde
        self.add_minute(self.seconde // 60)
        self.seconde %= 60

    def print_watch(self):
        print('계산된 시간은 {}시 {}분 {}초 입니다.'.format(self.hour,self.minute,self.seconde))

watch = Watch()
watch.input_time()
watch.add_hour(int(input('계산할 시간을 입력하세요 >> ')))
watch.add_minute(int(input('계산할 분을 입력하세요 >> ')))
watch.add_seconde(int(input('계산할 초를 입력하세요 >> ')))
watch.print_watch()
