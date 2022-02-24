import json

with open('cctv.json','rt', encoding='utf-8') as file:
    json_reader = file.read()
    dict_list = json.loads(json_reader)

print(dict_list)
kind = set()
for data in dict_list:
    kind.add(data['단속구분'])
print(kind)