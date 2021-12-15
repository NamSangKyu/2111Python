buffer_size = 1024 # 1024 byte --> 1 kb
with open('img.jpg','rb') as source:
    with open('copy.jpg','wb') as copy:
        while True:
            buffer = source.read(buffer_size)
            if not buffer:
                break
            copy.write(buffer)
print('파일 복사가 끝났습니다.')