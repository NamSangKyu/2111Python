class Song:
    def set_song(self, song, type):
        self.song = song
        self.type = type
    def print_song(self):
        print('노래제목 : {}({})'.format(self.song,self.type))

class Singer:
    def set_singer(self,singer):
        self.singer = singer
    def hit_song(self,song):
        self.song = song
    def print_singer(self):
        print(f'가수 이름 : {self.singer}')
        self.song.print_song()

song = Song()
song.set_song('취중진당','발라드')

singer = Singer()
singer.set_singer('김동률')

singer.hit_song(song)
singer.print_singer()