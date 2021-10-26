from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://www.iomfsa.im/enforcement/disqualified-directors/').text
soup = BeautifulSoup(html_text, 'lxml')
def function1():
    directors = soup.find_all('section', class_='accordion-item')       # To pull each director from the list under the class 'accordion-item'
    for director in directors:                                          # For each director in the list pulled before
        director_list = director.find('div', class_='rte').text         # To remove all the html tags and place only the strings from their sections
        print(f'{director_list}')                                       # Print each director in its format inside the loop

function1()
