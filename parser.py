from HTML_maker import html
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')
cars = soup.findAll('div', {"class": "ListingItem__description"})

print(len(cars))