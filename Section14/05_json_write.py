import json

dict_list=[
    {
        'menu_no' : 1,
        'menu_name' : '김밥',
        'price' : 2500
    },
    {
        'menu_no' : 2,
        'menu_name' : '제육덮밥',
        'price' : 6500
    },
    {
        'menu_no' : 3,
        'menu_name' : '치즈라면',
        'price' : 4500
    }
]
json_str = json.dumps(dict_list)
with open('menu.json','wt',encoding='utf-8') as file:
    file.write(json_str)
print('json 파일이 정상적으로 생성되었습니다.')

with open('menu.json','rt') as file:
    json_reader = file.read()
    read_list = json.loads(json_reader)
print(read_list)






