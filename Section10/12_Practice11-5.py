"""
    섭씨를 화씨로 바꾸는 함수 - CelToFah
        섭씨 -> 화씨 : 온도 * 1.8 + 32
    화씨를 섭씨로 바꾸는 함수 - FahToCel
        화씨 -> 섭씨 : (온도 - 32) / 1.8
"""
def CelToFah(cel):
    return cel * 1.8 + 32

def FahToCel(fah):
    return (fah - 32) / 1.8

cel = float(input('섭씨 온도를 입력하세요 >>> '))
print(f'섭씨 {cel} --> 화씨 {CelToFah(cel)}')
fah = float(input('화씨 온도를 입력하세요 >>> '))
print(f'화씨 {fah} --> 화씨 {FahToCel(fah)}')







