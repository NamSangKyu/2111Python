# 연습. 리스트에 딕셔너리 저장하기
schedule = [
    {
        'date': '2021-11-17',
        'place': 'seoul'
    },
    {
        'date': '2021-11-18',
        'place': 'incheon',
        'people': [
            '배수지',
            '이정재'
        ]
    }
]

print(schedule[0])
print(schedule[1])

print()  # 빈 줄 삽입

print(schedule[0]['date'])
print(schedule[0]['place'])

print(schedule[1]['date'])
print(schedule[1]['place'])
print(schedule[1]['people'][0])
print(schedule[1]['people'][1])
