import requests
from bs4 import BeautifulSoup

r = requests.get('https://sneakernews.com/category/adidas')
html = r.text
print(html)

soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.post-content > h4 > a')

for title in titles:
    print(title.text)