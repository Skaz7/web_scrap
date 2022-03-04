from bs4 import BeautifulSoup
import requests
import os

os.system('cls')

source = requests.get('https://www.dobreprogramy.pl/').text
soup = BeautifulSoup(source, 'lxml')

href = soup.find('h2', class_='Pbf')
headline = href
print(headline.prettify())