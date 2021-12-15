import json

with open('test.json','rt', encoding='utf-8') as file:
    json_reader = file.read()
    dict_list = json.loads(json_reader)

print(dict_list)
for data in dict_list:
    print(data['name'],data['age'],data['score'])