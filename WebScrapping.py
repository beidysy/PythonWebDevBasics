import requests
from bs4 import BeautifulSoup

res = requests.get("https://onepiece.fandom.com/wiki/Devil_Fruit")

soup = BeautifulSoup(res.content, 'html.parser')

s = soup.find_all('p')

for data in s:
    print(data.text)
