import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn'
param = {'code' : 10016}

response = requests.get(url,params=param)
html = response.text
#print(html)
soup = BeautifulSoup(html,'html.parser')
review_list = soup.find_all('div',class_='score_reple')
#print(review_list)
for review in review_list:
    print(review.find('p').text.strip())
print('---------------------------------')
review_list = soup.find_all('div',class_='tx_top')
for review in review_list:
    print(review.find('strong').text.strip())