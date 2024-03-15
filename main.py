import json

from bs4 import BeautifulSoup
import requests

data = []

r = requests.get('https://scipost.org/atom/publications/comp-ai')
soup = BeautifulSoup(r.text, 'lxml')

news = soup.findAll('entry')

for news in news:
    title = news.find('title').text
    link = news.find('link').get('href')
    try:
        page = requests.get(link).text
        soup_page = BeautifulSoup(page, 'lxml')
        text = soup_page.find('p', class_='abstract').text.strip()
    except AttributeError:
        text = "No text found"
    data.append({'Title': title, 'Link': link, 'Text': text})

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
