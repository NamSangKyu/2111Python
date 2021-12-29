import requests

url = 'https://search.naver.com/search.naver'
param = {'query':'파이썬'}
response = requests.get(url,param)
print(response.text)