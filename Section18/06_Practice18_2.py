import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'

response = requests.get(url)
html = response.text
count = 0
soup = BeautifulSoup(html,'html.parser')
movie_list = soup.find_all('td',class_='title')

for movie in movie_list:
    count += 1
    print(count,'위 : ',movie.find('a').text.strip())
