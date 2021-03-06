from bs4 import BeautifulSoup
import requests
import os
from selenium import webdriver
from urllib.request import urlopen

os.system('cls')

# with open('D:\\Users\\sebas\\OneDrive\\Repositories\\web_scrap\\simple.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

# match = soup.find('div', class_='footer').text
# print(match)

# print()

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article'):

    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    vid_src = article.find('iframe', class_='youtube-player')['src']


    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]
    print(vid_id)

    yt_link = f'https://youtube.com/watch?v={vid_id}'
    print(yt_link)