import requests
url = 'https://www.naver.com'
response = requests.get(url)
print('응답코드 : {}'.format(response.status_code))
print(response.text)