from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://www.iomfsa.im/enforcement/disqualified-directors/').text
soup = BeautifulSoup(html_text, 'lxml')
def function1():
    directors = soup.find_all('section', class_='accordion-item')
    for director in directors:
        director_list = director.find('div', class_='rte').text
        print(f'{director_list}')

function1()
