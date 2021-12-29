import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rpeople.nhn'

response = requests.get(url)
html = response.text
#print(html)
soup = BeautifulSoup(html,'html.parser')
movie_in_list = soup.find_all('td',class_='title')
#print(movie_in_list)
for movie in movie_in_list:
    print(movie.find('a').text.strip())
